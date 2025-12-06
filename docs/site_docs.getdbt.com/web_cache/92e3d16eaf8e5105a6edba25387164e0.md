# Source: https://docs.getdbt.com/reference/commands/run

About dbt run command | dbt Developer Hub

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
* run

Copy page

On this page

About dbt run command
=====================

Overview[​](#overview "Direct link to Overview")
------------------------------------------------

The `dbt run` command only applies to models. It doesn't run tests, snapshots, seeds, or other resource types. To run those commands, use the appropriate dbt commands found in the [dbt commands](/reference/dbt-commands) section — such as `dbt test`, `dbt snapshot`, or `dbt seed`. Alternatively, use `dbt build` with a [resource type selector](/reference/node-selection/methods#resource_type).

You can use the `dbt run` command when you want to build or rebuild models in your project.

### How does `dbt run` work?[​](#how-does-dbt-run-work "Direct link to how-does-dbt-run-work")

* `dbt run` executes compiled SQL model files against the current `target` database.
* dbt connects to the target database and runs the relevant SQL required to materialize all data models using the specified materializationThe exact Data Definition Language (DDL) that dbt will use when creating the model’s equivalent in a data warehouse. strategies.
* Models are run in the order defined by the dependency graph generated during compilation. Intelligent multi-threading is used to minimize execution time without violating dependencies.
* Deploying new models frequently involves destroying prior versions of these models. In these cases, `dbt run` minimizes downtime by first building each model with a temporary name, then dropping and renaming within a single transaction (for adapters that support transactions).

Refresh incremental models[​](#refresh-incremental-models "Direct link to Refresh incremental models")
------------------------------------------------------------------------------------------------------

If you provide the `--full-refresh` flag to `dbt run`, dbt will treat incremental models as tableIn simplest terms, a table is the direct storage of data in rows and columns. Think excel sheet with raw values in each of the cells. models. This is useful when

1. The schema of an incremental model changes and you need to recreate it.
2. You want to reprocess the entirety of the incremental model because of new logic in the model code.

bash

```
dbt run --full-refresh
```

You can also supply the flag by its short name: `dbt run -f`.

In the dbt compilation context, this flag will be available as [flags.FULL\_REFRESH](/reference/dbt-jinja-functions/flags). Further, the `is_incremental()` macro will return `false` for *all* models in response when the `--full-refresh` flag is specified.

models/example.sql

```
select * from all_events  
  
-- if the table already exists and `--full-refresh` is  
-- not set, then only add new records. otherwise, select  
-- all records.  
{% if is_incremental() %}  
   where collector_tstamp > (  
     select coalesce(max(max_tstamp), '0001-01-01') from {{ this }}  
   )  
{% endif %}
```

Running specific models[​](#running-specific-models "Direct link to Running specific models")
---------------------------------------------------------------------------------------------

dbt will also allow you select which specific models you'd like to materialize. This can be useful during special scenarios where you may prefer running a different set of models at various intervals. This can also be helpful when you may want to limit the tables materialized while you develop and test new models.

For more information, see the [Model Selection Syntax Documentation](/reference/node-selection/syntax).

For more information on running parents or children of specific models, see the [Graph Operators Documentation](/reference/node-selection/graph-operators).

Treat warnings as errors[​](#treat-warnings-as-errors "Direct link to Treat warnings as errors")
------------------------------------------------------------------------------------------------

See [global configs](/reference/global-configs/warnings)

Failing fast[​](#failing-fast "Direct link to Failing fast")
------------------------------------------------------------

See [global configs](/reference/global-configs/failing-fast)

Enable or Disable Colorized Logs[​](#enable-or-disable-colorized-logs "Direct link to Enable or Disable Colorized Logs")
------------------------------------------------------------------------------------------------------------------------

See [global configs](/reference/global-configs/print-output#print-color)

The `--empty` flag[​](#the---empty-flag "Direct link to the---empty-flag")
--------------------------------------------------------------------------

The `run` command supports the `--empty` flag for building schema-only dry runs. The `--empty` flag limits the refs and sources to zero rows. dbt will still execute the model SQL against the target data warehouse but will avoid expensive reads of input data. This validates dependencies and ensures your models will build properly.

Status codes[​](#status-codes "Direct link to Status codes")
------------------------------------------------------------

When calling the [list\_runs api](/dbt-cloud/api-v2#/operations/List%20Runs), you will get a status code for each run returned. The available run status codes are as follows:

* Queued = 1
* Starting = 2
* Running = 3
* Success = 10
* Error = 20
* Canceled = 30
* Skipped = 40

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/run.md)

Last updated on **Nov 19, 2025**

[Previous

rpc](/reference/commands/rpc)[Next

run-operation](/reference/commands/run-operation)

![Loading](/img/loader-icon.svg "Loading")

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