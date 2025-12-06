# Source: https://docs.getdbt.com/best-practices/clone-incremental-models

Clone incremental models as the first step of your CI job | dbt Developer Hub

[Skip to main content](#__docusaurus_skipToContent_fallback)

[✨ Live virtual event - Smarter pipelines, 29% more efficient: How the dbt Fusion engine optimizes data work on December 3rd!](https://www.getdbt.com/resources/webinars/how-the-dbt-fusion-engine-optimizes-data-work)

[![dbt Logo](/img/dbt-logo.svg?v=2)![dbt Logo](/img/dbt-logo-light.svg?v=2)](/)

[Docs](#)

* [Product docs](/docs/introduction)
* [References](/reference/references-overview)
* [Best practices](/best-practices)
* [Developer blog](/blog)

[Guides](/guides)[APIs](/docs/dbt-cloud-apis/overview)

[Help](#)

* [Release notes](/docs/dbt-versions/dbt-cloud-release-notes)
* [FAQs](/docs/faqs)
* [Support and billing](/docs/dbt-support)
* [Fusion Diaries](https://github.com/dbt-labs/dbt-fusion/discussions/categories/announcements)
* [Courses](https://learn.getdbt.com)

[Community](#)

* [Join the dbt Community](/community/join)
* [Become a contributor](/community/contribute)
* [Community forum](/community/forum)
* [Events](/community/events)
* [Spotlight](/community/spotlight)

[Account](#)

* [Log in to dbt](https://cloud.getdbt.com/)
* [Create a free account](https://www.getdbt.com/signup)

[Install VS Code extension](https://marketplace.visualstudio.com/items?itemName=dbtLabsInc.dbt)

[v](#) 

* dbt platform (Latest)
* dbt Fusion engine
* Core v1.11 Beta
* Core v1.10 (Compatible)
* Core v1.9 (Extended)

Search

[![dbt Logo](/img/dbt-logo.svg?v=2)![dbt Logo](/img/dbt-logo-light.svg?v=2)](/)

* [Best practices](/best-practices)

  + [How we structure our dbt projects](/best-practices/how-we-structure/1-guide-overview)
  + [How we style our dbt projects](/best-practices/how-we-style/0-how-we-style-our-dbt-projects)
  + [How we build our metrics](/best-practices/how-we-build-our-metrics/semantic-layer-1-intro)
  + [How we build our dbt Mesh projects](/best-practices/how-we-mesh/mesh-1-intro)
  + [Materialization best practices](/best-practices/materializations/1-guide-overview)
  + [Don't nest your curlies](/best-practices/dont-nest-your-curlies)
  + [Clone incremental models as the first step of your CI job](/best-practices/clone-incremental-models)
  + [Writing custom generic data tests](/best-practices/writing-custom-generic-tests)
  + [Best practices for workflows](/best-practices/best-practice-workflows)
  + [Best practices for dbt and Unity Catalog](/best-practices/dbt-unity-catalog-best-practices)

* [Best practices](/best-practices)
* Clone incremental models as the first step of your CI job

Copy page

On this page

Clone incremental models as the first step of your CI job
=========================================================

Before you begin, you must be aware of a few conditions:

* `dbt clone` is only available with dbt version 1.6 and newer. Refer to our [upgrade guide](/docs/dbt-versions/upgrade-dbt-version-in-cloud) for help enabling newer versions in dbt.
* This strategy only works for warehouse that support zero copy cloning (otherwise `dbt clone` will just create pointer views).
* Some teams may want to test that their incremental models run in both incremental mode and full-refresh mode.

Imagine you've created a [Slim CI job](/docs/deploy/continuous-integration) in dbt and it is configured to:

* Defer to your production environment.
* Run the command `dbt build --select state:modified+` to run and test all of the models you've modified and their downstream dependencies.
* Trigger whenever a developer on your team opens a PR against the main branch.

[![Example of a slim CI job with the above configurations](/img/best-practices/slim-ci-job.png?v=2 "Example of a slim CI job with the above configurations")](#)Example of a slim CI job with the above configurations

Now imagine your dbt project looks something like this in the DAG:

[![Sample project DAG](/img/best-practices/dag-example.png?v=2 "Sample project DAG")](#)Sample project DAG

When you open a pull request (PR) that modifies `dim_wizards`, your CI job will kickoff and build *only the modified models and their downstream dependencies* (in this case, `dim_wizards` and `fct_orders`) into a temporary schema that's unique to your PR.

This build mimics the behavior of what will happen once the PR is merged into the main branch. It ensures you're not introducing breaking changes, without needing to build your entire dbt project.

What happens when one of the modified models (or one of their downstream dependencies) is an incremental model?[​](#what-happens-when-one-of-the-modified-models-or-one-of-their-downstream-dependencies-is-an-incremental-model "Direct link to What happens when one of the modified models (or one of their downstream dependencies) is an incremental model?")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Because your CI job is building modified models into a PR-specific schema, on the first execution of `dbt build --select state:modified+`, the modified incremental model will be built in its entirety *because it does not yet exist in the PR-specific schema* and [is\_incremental will be false](/docs/build/incremental-models#understand-the-is_incremental-macro). You're running in `full-refresh` mode.

This can be suboptimal because:

* Typically incremental models are your largest datasets, so they take a long time to build in their entirety which can slow down development time and incur high warehouse costs.
* There are situations where a `full-refresh` of the incremental model passes successfully in your CI job but an *incremental* build of that same table in prod would fail when the PR is merged into main (think schema drift where [on\_schema\_change](/docs/build/incremental-models#what-if-the-columns-of-my-incremental-model-change) config is set to `fail`)

You can alleviate these problems by zero copy cloning the relevant, pre-existing incremental models into your PR-specific schema as the first step of the CI job using the `dbt clone` command. This way, the incremental models already exist in the PR-specific schema when you first execute the command `dbt build --select state:modified+` so the `is_incremental` flag will be `true`.

You'll have two commands for your dbt CI check to execute:

1. Clone all of the pre-existing incremental models that have been modified or are downstream of another model that has been modified:

```
dbt clone --select state:modified+,config.materialized:incremental,state:old
```

2. Build all of the models that have been modified and their downstream dependencies:

```
dbt build --select state:modified+
```

Because of your first clone step, the incremental models selected in your `dbt build` on the second step will run in incremental mode.

[![Clone command in the CI config](/img/best-practices/clone-command.png?v=2 "Clone command in the CI config")](#)Clone command in the CI config

Your CI jobs will run faster, and you're more accurately mimicking the behavior of what will happen once the PR has been merged into main.

### Expansion on "think schema drift" where [on\_schema\_change](/docs/build/incremental-models#what-if-the-columns-of-my-incremental-model-change) config is set to `fail`" from above[​](#expansion-on-think-schema-drift-where-on_schema_change-config-is-set-to-fail-from-above "Direct link to expansion-on-think-schema-drift-where-on_schema_change-config-is-set-to-fail-from-above")

Imagine you have an incremental model `my_incremental_model` with the following config:

```
{{  
    config(  
        materialized='incremental',  
        unique_key='unique_id',  
        on_schema_change='fail'  
    )  
}}
```

Now, let’s say you open up a PR that adds a new column to `my_incremental_model`. In this case:

* An incremental build will fail.
* A `full-refresh` will succeed.

If you have a daily production job that just executes `dbt build` without a `--full-refresh` flag, once the PR is merged into main and the job kicks off, you will get a failure. So the question is - what do you want to happen in CI?

* Do you want to also get a failure in CI, so that you know that once this PR is merged into main you need to immediately execute a `dbt build --full-refresh --select my_incremental_model` in production in order to avoid a failure in prod? This will block your CI check from passing.
* Do you want your CI check to succeed, because once you do run a `full-refresh` for this model in prod you will be in a successful state? This may lead unpleasant surprises if your production job is suddenly failing when you merge this PR into main if you don’t remember you need to execute a `dbt build --full-refresh --select my_incremental_model` in production.

There’s probably no perfect solution here; it’s all just tradeoffs! Our preference would be to have the failing CI job and have to manually override the blocking branch protection rule so that there are no surprises and we can proactively run the appropriate command in production once the PR is merged.

### Expansion on "why `state:old`"[​](#expansion-on-why-stateold "Direct link to expansion-on-why-stateold")

For brand new incremental models, you want them to run in `full-refresh` mode in CI, because they will run in `full-refresh` mode in production when the PR is merged into `main`. They also don't exist yet in the production environment... they're brand new!
If you don't specify this, you won't get an error just a “No relation found in state manifest for…”. So, it technically works without specifying `state:old` but adding `state:old` is more explicit and means it won't even try to clone the brand new incremental models.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/clone-incremental-models.md)

Last updated on **Nov 19, 2025**

[Previous

Don't nest your curlies](/best-practices/dont-nest-your-curlies)[Next

Writing custom generic data tests](/best-practices/writing-custom-generic-tests)

* [What happens when one of the modified models (or one of their downstream dependencies) is an incremental model?](#what-happens-when-one-of-the-modified-models-or-one-of-their-downstream-dependencies-is-an-incremental-model)
  + [Expansion on "think schema drift" where on\_schema\_change config is set to `fail`" from above](#expansion-on-think-schema-drift-where-on_schema_change-config-is-set-to-fail-from-above)
  + [Expansion on "why `state:old`"](#expansion-on-why-stateold)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/clone-incremental-models.md)

Get started

Start building with dbt.
------------------------

The free dbt VS Code extension is the best way to develop locally with the dbt Fusion Engine.

[Install free extension](https://marketplace.visualstudio.com/items?itemName=dbtLabsInc.dbt)
[Request your demo](https://www.getdbt.com/contact)

[![dbt Labs](/img/dbt-logo-light.svg?v=2)](/)

##### Resources

[VS Code Extension](/docs/about-dbt-extension)
[Resource Hub](https://www.getdbt.com/resources)
[dbt Learn](https://www.getdbt.com/dbt-learn)
[Certification](https://www.getdbt.com/dbt-certification)
[Developer Blog](/blog)

##### Community

[Join the Community](/community/join)
[Become a Contributor](/community/contribute)
[Open Source dbt Packages](https://hub.getdbt.com/)
[Community Forum](/community/forum)

##### Support

[Contact Support](/docs/dbt-support)
[Professional Services](https://www.getdbt.com/services)
[Find a Partner](https://www.getdbt.com/partner-directory)
[System Status](https://status.getdbt.com/)

##### Connect with Us

© 2025 dbt Labs, Inc. All Rights Reserved.

[Terms of Service](https://www.getdbt.com/terms-of-use/)
[Privacy Policy](https://www.getdbt.com/cloud/privacy-policy/)
[Security](https://www.getdbt.com/security/)
Cookie Settings