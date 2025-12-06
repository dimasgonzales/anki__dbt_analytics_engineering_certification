# Source: https://docs.getdbt.com/reference/node-selection/defer

Defer | dbt Developer Hub

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

* [About References](/reference/references-overview)
* [Project configs](/category/project-configs)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)
* [Commands](/reference/dbt-commands)

  + [dbt Command reference](/reference/dbt-commands)
  + [List of commands](/category/list-of-commands)
  + [Node selection](/reference/node-selection/syntax)

    - [Syntax overview](/reference/node-selection/syntax)
    - [Exclude](/reference/node-selection/exclude)
    - [Defer](/reference/node-selection/defer)
    - [Graph operators](/reference/node-selection/graph-operators)
    - [Set operators](/reference/node-selection/set-operators)
    - [Node selector methods](/reference/node-selection/methods)
    - [Putting it together](/reference/node-selection/putting-it-together)
    - [YAML Selectors](/reference/node-selection/yaml-selectors)
    - [Test selection examples](/reference/node-selection/test-selection-examples)
    - [About state selection](/reference/node-selection/state-selection)
  + [Flags (global configs)](/reference/global-configs/about-global-configs)
  + [Events and logs](/reference/events-logging)
  + [Exit codes](/reference/exit-codes)
  + [Deprecations](/reference/deprecations)
  + [Project Parsing](/reference/parsing)
  + [Programmatic invocations](/reference/programmatic-invocations)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Commands](/reference/dbt-commands)
* [Node selection](/reference/node-selection/syntax)
* Defer

Copy page

On this page

Defer
=====

Defer is a powerful feature that makes it possible to run a subset of models or tests in a [sandbox environment](/docs/environments-in-dbt) without having to first build their upstream parents. This can save time and computational resources when you want to test a small number of models in a large project.

[![Use 'defer' to modify end-of-pipeline models by pointing to production models, instead of running everything upstream.](/img/docs/reference/defer-diagram.png?v=2 "Use 'defer' to modify end-of-pipeline models by pointing to production models, instead of running everything upstream.")](#)Use 'defer' to modify end-of-pipeline models by pointing to production models, instead of running everything upstream.

Defer requires that a manifest from a previous dbt invocation be passed to the `--state` flag or env var. Together with the `state:` selection method, these features enable "Slim CI". Read more about [state](/reference/node-selection/state-selection).

An alternative command that accomplishes similar functionality for different use cases is `dbt clone` - see the docs for [clone](/reference/commands/clone#when-to-use-dbt-clone-instead-of-deferral) for more information.

It is possible to use separate state for `state:modified` and `--defer`, by passing paths to different manifests to each of the `--state`/`DBT_STATE` and `--defer-state`/`DBT_DEFER_STATE`. This enables more granular control in cases where you want to compare against logical state from one environment or past point in time, and defer to applied state from a different environment or point in time. If `--defer-state` is not specified, deferral will use the manifest supplied to `--state`. In most cases, you will want to use the same state for both: compare logical changes against production, and also "fail over" to the production environment for unbuilt upstream resources.

### Usage[​](#usage "Direct link to Usage")

```
dbt run --select [...] --defer --state path/to/artifacts  
dbt test --select [...] --defer --state path/to/artifacts
```

By default, dbt uses the [`target`](/reference/dbt-jinja-functions/target) namespace to resolve `ref` calls.

When `--defer` is enabled, dbt resolves ref calls using the state manifest instead, but only if:

1. The node isn’t among the selected nodes, *and*
2. It doesn’t exist in the database (or `--favor-state` is used).

Ephemeral models are never deferred, since they serve as "passthroughs" for other `ref` calls.

When using defer, you may be selecting from production datasets, development datasets, or a mix of both. Note that this can yield unexpected results

* if you apply env-specific limits in dev but not prod, as you may end up selecting more data than you expect
* when executing tests that depend on multiple parents (e.g. `relationships`), since you're testing "across" environments

Deferral requires both `--defer` and `--state` to be set, either by passing flags explicitly or by setting environment variables (`DBT_DEFER` and `DBT_STATE`). If you use dbt, read about [how to set up CI jobs](/docs/deploy/continuous-integration).

#### Favor state[​](#favor-state "Direct link to Favor state")

When `--favor-state` is passed, dbt prioritizes node definitions from the `--state directory`. However, this doesn’t apply if the node is also part of the selected nodes.

### Example[​](#example "Direct link to Example")

In my local development environment, I create all models in my target schema, `dev_alice`. In production, the same models are created in a schema named `prod`.

I access the dbt-generated [artifacts](/docs/deploy/artifacts) (namely `manifest.json`) from a production run, and copy them into a local directory called `prod-run-artifacts`.

### run[​](#run "Direct link to run")

I've been working on `model_b`:

models/model\_b.sql

```
select  
  
    id,  
    count(*)  
  
from {{ ref('model_a') }}  
group by 1
```

I want to test my changes. Nothing exists in my development schema, `dev_alice`.

* Standard run
* Deferred run

```
dbt run --select "model_b"
```

target/run/my\_project/model\_b.sql

```
create or replace view dev_me.model_b as (  
  
    select  
  
        id,  
        count(*)  
  
    from dev_alice.model_a  
    group by 1  
  
)
```

Unless I had previously run `model_a` into this development environment, `dev_alice.model_a` will not exist, thereby causing a database error.

```
dbt run --select "model_b" --defer --state prod-run-artifacts
```

target/run/my\_project/model\_b.sql

```
create or replace view dev_me.model_b as (  
  
    select  
  
        id,  
        count(*)  
  
    from prod.model_a  
    group by 1  
  
)
```

Because `model_a` is unselected, dbt will check to see if `dev_alice.model_a` exists. If it doesn't exist, dbt will resolve all instances of `{{ ref('model_a') }}` to `prod.model_a` instead.

### test[​](#test "Direct link to test")

I also have a `relationships` test that establishes referential integrity between `model_a` and `model_b`:

models/resources.yml

```
models:  
  - name: model_b  
    columns:  
      - name: id  
        data_tests:  
          - relationships:  
              arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                to: ref('model_a')  
                field: id
```

(A bit silly, since all the data in `model_b` had to come from `model_a`, but suspend your disbelief.)

* Without defer
* With defer

```
dbt test --select "model_b"
```

target/compiled/.../relationships\_model\_b\_id\_\_id\_\_ref\_model\_a\_.sql

```
select count(*) as validation_errors  
from (  
    select id as id from dev_alice.model_b  
) as child  
left join (  
    select id as id from dev_alice.model_a  
) as parent on parent.id = child.id  
where child.id is not null  
  and parent.id is null
```

The `relationships` test requires both `model_a` and `model_b`. Because I did not build `model_a` in my previous `dbt run`, `dev_alice.model_a` does not exist and this test query fails.

```
dbt test --select "model_b" --defer --state prod-run-artifacts
```

target/compiled/.../relationships\_model\_b\_id\_\_id\_\_ref\_model\_a\_.sql

```
select count(*) as validation_errors  
from (  
    select id as id from dev_alice.model_b  
) as child  
left join (  
    select id as id from prod.model_a  
) as parent on parent.id = child.id  
where child.id is not null  
  and parent.id is null
```

dbt will check to see if `dev_alice.model_a` exists. If it doesn't exist, dbt will resolve all instances of `{{ ref('model_a') }}`, including those in schema tests, to use `prod.model_a` instead. The query succeeds. Whether I really want to test for referential integrity across environments is a different question.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Using defer in dbt](/docs/cloud/about-cloud-develop-defer)
* [on\_configuration\_change](/reference/resource-configs/on_configuration_change)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/defer.md)

Last updated on **Nov 19, 2025**

[Previous

Exclude](/reference/node-selection/exclude)[Next

Graph operators](/reference/node-selection/graph-operators)

* [Usage](#usage)
* [Example](#example)
* [run](#run)
* [test](#test)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/defer.md)

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




![dbt Labs](https://cdn.cookielaw.org/logos/4a2cde9e-5f84-44b2-bdbb-6a93354d1c72/e1199e19-1935-49fa-a4e2-bf7f9d08cee6/783d7c83-af8c-4032-901b-b3ec48982078/dbt-logo.png)

Privacy Preference Center
-------------------------

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.
  
[More information](https://www.getdbt.com/cloud/privacy-policy/)

Allow All

### Manage Consent Preferences

#### Strictly Necessary Cookies

Always Active

Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.

#### Performance Cookies

Always Active

Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.

#### Targeting Cookies

Always Active

Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Always Active

Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox label label

Apply Cancel

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg "Powered by OneTrust Opens in a new Tab")](https://www.onetrust.com/products/cookie-consent/)