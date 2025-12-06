# Source: https://docs.getdbt.com/reference/commands/build

About dbt build command | dbt Developer Hub

[Skip to main content](#__docusaurus_skipToContent_fallback)

[✨ Live virtual event - Smarter pipelines, 29% more efficient: How the dbt Fusion engine optimizes data work on December 3rd!](https://www.getdbt.com/resources/webinars/how-the-dbt-fusion-engine-optimizes-data-work)

[![dbt Logo](/img/dbt-logo.svg?v=2)](/)

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

[dbt platform (Latest)](#)

* dbt platform (Latest)
* dbt Fusion engine
* Core v1.11 Beta
* Core v1.10 (Compatible)
* Core v1.9 (Extended)

Search`⌘``K`

[![dbt Logo](/img/dbt-logo.svg?v=2)](/)

* [About References](/reference/references-overview)
* [Project configs](/category/project-configs)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)
* [Commands](/reference/dbt-commands)

  + [dbt Command reference](/reference/dbt-commands)
  + [List of commands](/category/list-of-commands)

    - [build](/reference/commands/build)
    - [clean](/reference/commands/clean)
    - [clone](/reference/commands/clone)
    - [docs](/reference/commands/cmd-docs)
    - [compile](/reference/commands/compile)
    - [debug](/reference/commands/debug)
    - [deps](/reference/commands/deps)
    - [environment](/reference/commands/dbt-environment)
    - [init](/reference/commands/init)
    - [invocation](/reference/commands/invocation)
    - [ls (list)](/reference/commands/list)
    - [parse](/reference/commands/parse)
    - [retry](/reference/commands/retry)
    - [rpc](/reference/commands/rpc)
    - [run](/reference/commands/run)
    - [run-operation](/reference/commands/run-operation)
    - [seed](/reference/commands/seed)
    - [show](/reference/commands/show)
    - [snapshot](/reference/commands/snapshot)
    - [source](/reference/commands/source)
    - [test](/reference/commands/test)
    - [version](/reference/commands/version)
  + [Node selection](/reference/node-selection/syntax)
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
* [List of commands](/category/list-of-commands)
* build

Copy page

On this page

About dbt build command
=======================

The `dbt build` command will:

* run [models](/docs/build/models)
* test [tests](/docs/build/data-tests)
* snapshot [snapshots](/docs/build/snapshots)
* seed [seeds](/docs/build/seeds)
* build [user-defined functions](/docs/build/udfs) (available from dbt Core v1.11 and in the dbt Fusion Engine)

In DAG order, for selected resources or an entire project.

Details[​](#details "Direct link to Details")
---------------------------------------------

**Artifacts:** The `build` task will write a single [manifest](/reference/artifacts/manifest-json) and a single [run results artifact](/reference/artifacts/run-results-json). The run results will include information about all models, tests, seeds, and snapshots that were selected to build, combined into one file.

**Skipping on failures:** Tests on upstream resources will block downstream resources from running, and a test failure will cause those downstream resources to skip entirely. E.g. If `model_b` depends on `model_a`, and a `unique` test on `model_a` fails, then `model_b` will `SKIP`.

* Don't want a test to cause skipping? Adjust its [severity or thresholds](/reference/resource-configs/severity) to `warn` instead of `error`
* In the case of a test with multiple parents, where one parent depends on the other (e.g. a `relationships` test between `model_a` + `model_b`), that test will block-and-skip children of the most-downstream parent only (`model_b`).
* If you have a test with multiple parents that are independent of each other, dbt [skips](https://github.com/dbt-labs/dbt-core/blob/d5071fa13502be273596a0b7c8b13d14b6c68655/core/dbt/compilation.py#L224-L257) the downstream node only if that node depends on all of those parents.

**Selecting resources:** The `build` task supports standard selection syntax (`--select`, `--exclude`, `--selector`), as well as a `--resource-type` flag that offers a final filter (just like `list`). Whichever resources are selected, those are the ones that `build` will run/test/snapshot/seed.

* Remember that tests support indirect selection, so `dbt build -s model_a` will both run *and* test `model_a`. What does that mean? Any tests that directly depend on `model_a` will be included, so long as those tests don't also depend on other unselected parents. See [test selection](/reference/node-selection/test-selection-examples) for details and examples.

**Flags:** The `build` task supports all the same flags as `run`, `test`, `snapshot`, and `seed`. For flags that are shared between multiple tasks (e.g. `--full-refresh`), `build` will use the same value for all selected resource types (e.g. both models and seeds will be full refreshed).

### The `--empty` flag[​](#the---empty-flag "Direct link to the---empty-flag")

The `build` command supports the `--empty` flag for building schema-only dry runs. The `--empty` flag limits the refs and sources to zero rows. dbt will still execute the model SQL against the target data warehouse but will avoid expensive reads of input data. This validates dependencies and ensures your models will build properly.

#### The render method[​](#the-render-method "Direct link to The render method")

The `.render()` method is generally used to resolve or evaluate Jinja expressions (such as `{{ source(...) }}`) during runtime.

When using the `--empty flag`, dbt may skip processing `ref()` or `source()` for optimization. To avoid compilation errors and to explicitly tell dbt to process a specific relation (`ref()` or `source()`), use the `.render()` method in your model file. For example:

models.sql

```
{{ config(  
    pre_hook = [  
        "alter external table {{ source('sys', 'customers').render() }} refresh"  
    ]  
) }}  
  
select ...
```

Tests[​](#tests "Direct link to Tests")
---------------------------------------

When `dbt build` is executed with unit tests applied, the models will be processed according to their lineage and dependencies. The tests will be executed as follows:

* [Unit tests](/docs/build/unit-tests) are run on a SQL model.
* The model is materialized.
* [Data tests](/docs/build/data-tests) are run on the model.

This saves on warehouse spend as the model will only be materialized if the unit tests pass successfully.

Unit tests and data tests can be selected using `--select test_type:unit` or `--select test_type:data` for `dbt build` (same for the `--exclude` flag).

### Examples[​](#examples "Direct link to Examples")

```
$ dbt build  
Running with dbt=1.9.0-b2  
Found 1 model, 4 tests, 1 snapshot, 1 analysis, 341 macros, 0 operations, 1 seed file, 2 sources, 2 exposures  
  
18:49:43 | Concurrency: 1 threads (target='dev')  
18:49:43 |  
18:49:43 | 1 of 7 START seed file dbt_jcohen.my_seed............................ [RUN]  
18:49:43 | 1 of 7 OK loaded seed file dbt_jcohen.my_seed........................ [INSERT 2 in 0.09s]  
18:49:43 | 2 of 7 START view model dbt_jcohen.my_model.......................... [RUN]  
18:49:43 | 2 of 7 OK created view model dbt_jcohen.my_model..................... [CREATE VIEW in 0.12s]  
18:49:43 | 3 of 7 START test not_null_my_seed_id................................ [RUN]  
18:49:43 | 3 of 7 PASS not_null_my_seed_id...................................... [PASS in 0.05s]  
18:49:43 | 4 of 7 START test unique_my_seed_id.................................. [RUN]  
18:49:43 | 4 of 7 PASS unique_my_seed_id........................................ [PASS in 0.03s]  
18:49:43 | 5 of 7 START snapshot snapshots.my_snapshot.......................... [RUN]  
18:49:43 | 5 of 7 OK snapshotted snapshots.my_snapshot.......................... [INSERT 0 5 in 0.27s]  
18:49:43 | 6 of 7 START test not_null_my_model_id............................... [RUN]  
18:49:43 | 6 of 7 PASS not_null_my_model_id..................................... [PASS in 0.03s]  
18:49:43 | 7 of 7 START test unique_my_model_id................................. [RUN]  
18:49:43 | 7 of 7 PASS unique_my_model_id....................................... [PASS in 0.02s]  
18:49:43 |  
18:49:43 | Finished running 1 seed, 1 view model, 4 tests, 1 snapshot in 1.01s.  
  
Completed successfully  
  
Done. PASS=7 WARN=0 ERROR=0 SKIP=0 TOTAL=7
```

Functions[​](#functions "Direct link to Functions")
---------------------------------------------------

*Available from dbt Core v1.11 and in the dbt Fusion Engine*

The `build` command builds [user-defined functions](/docs/build/udfs) as part of the DAG execution. To build or rebuild only `functions` in your project, run `dbt build --select "resource_type:function"`. For example:

```
dbt build --select "resource_type:function"  
dbt-fusion 2.0.0-preview.45  
 Succeeded [  0.98s] function dbt_schema.whoami (function)  
 Succeeded [  1.12s] function dbt_schema.area_of_circle (function)
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/build.md)

Last updated on **Nov 19, 2025**

[Previous

List of commands](/category/list-of-commands)[Next

clean](/reference/commands/clean)

* [Details[​](#details "Direct link to Details")](#details)
  + [The `--empty` flag[​](#the---empty-flag "Direct link to the---empty-flag")](#the---empty-flag)
* [Tests[​](#tests "Direct link to Tests")](#tests)
  + [Examples[​](#examples "Direct link to Examples")](#examples)
* [Functions[​](#functions "Direct link to Functions")](#functions)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/build.md)

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