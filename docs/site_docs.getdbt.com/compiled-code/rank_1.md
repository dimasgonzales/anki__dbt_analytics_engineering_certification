# Source: https://docs.getdbt.com/reference/commands/compile

About dbt compile command | dbt Developer Hub

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
* compile

Copy page

On this page

About dbt compile command
=========================

`dbt compile` generates executable SQL from source `model`, `test`, and `analysis` files. You can find these compiled SQL files in the `target/` directory of your dbt project.

The `compile` command is useful for:

1. Visually inspecting the compiled output of model files. This is useful for validating complex Jinja logic or macro usage.
2. Manually running compiled SQL. While debugging a model or schema test, it's often useful to execute the underlying `select` statement to find the source of the bug.
3. Compiling `analysis` files. Read more about analysis files [here](/docs/build/analyses).

Some common misconceptions:

* `dbt compile` is *not* a pre-requisite of `dbt run`, or other building commands. Those commands will handle compilation themselves.
* If you just want dbt to read and validate your project code, without connecting to the data warehouse, use `dbt parse` instead.

### Interactive compile[​](#interactive-compile "Direct link to Interactive compile")

Starting in dbt v1.5, `compile` can be "interactive" in the CLI, by displaying the compiled code of a node or arbitrary dbt-SQL query:

* `--select` a specific node *by name*
* `--inline` an arbitrary dbt-SQL query

This will log the compiled SQL to the terminal, in addition to writing to the `target/` directory.

For example:

```
dbt compile --select "stg_orders"                             
dbt compile --inline "select * from {{ ref('raw_orders') }}"
```

returns the following:

```
dbt compile --select "stg_orders"                             
  
21:17:09  Running with dbt=1.7.5  
21:17:09  Registered adapter: postgres=1.7.5  
21:17:09  Found 5 models, 3 seeds, 20 tests, 0 sources, 0 exposures, 0 metrics, 401 macros, 0 groups, 0 semantic models  
21:17:09    
21:17:09 Concurrency: 24 threads (target='dev')  
21:17:09    
21:17:09  Compiled node 'stg_orders' is:  
with source as (  
    select * from "jaffle_shop"."main"."raw_orders"  
  
),  
  
renamed as (  
  
    select  
        id as order_id,  
        user_id as customer_id,  
        order_date,  
        status  
  
    from source  
  
)  
  
select * from renamed
```

```
dbt compile --inline "select * from {{ ref('raw_orders') }}"  
  
18:15:49  Running with dbt=1.7.5  
18:15:50  Registered adapter: postgres=1.7.5  
18:15:50  Found 5 models, 3 seeds, 20 tests, 0 sources, 0 exposures, 0 metrics, 401 macros, 0 groups, 0 semantic models  
18:15:50    
18:15:50  Concurrency: 5 threads (target='postgres')  
18:15:50    
18:15:50  Compiled inline node is:  
select * from "jaffle_shop"."main"."raw_orders"
```

The command accesses the data platform to cache-related metadata, and to run introspective queries. Use the flags:

* `--no-populate-cache` to disable the initial cache population. If metadata is needed, it will be a cache miss, requiring dbt to run the metadata query. This is a `dbt` flag, which means you need to add `dbt` as a prefix. For example: `dbt --no-populate-cache`.
* `--no-introspect` to disable [introspective queries](/faqs/Warehouse/db-connection-dbt-compile#introspective-queries). dbt will raise an error if a model's definition requires running one. This is a `dbt compile` flag, which means you need to add `dbt compile` as a prefix. For example:`dbt compile --no-introspect`.

### FAQs[​](#faqs "Direct link to FAQs")

Why dbt compile needs a data platform connection

`dbt compile` needs a data platform connection in order to gather the info it needs (including from introspective queries) to prepare the SQL for every model in your project.

### dbt compile[​](#dbt-compile "Direct link to dbt compile")

The [`dbt compile` command](/reference/commands/compile) generates executable SQL from `source`, `model`, `test`, and `analysis` files. `dbt compile` is similar to `dbt run` except that it doesn't materialize the model's compiled SQL into an existing table. So, up until the point of materialization, `dbt compile` and `dbt run` are similar because they both require a data platform connection, run queries, and have an [`execute` variable](/reference/dbt-jinja-functions/execute) set to `True`.

However, here are some things to consider:

* You don't need to execute `dbt compile` before `dbt run`
* In dbt, `compile` doesn't mean `parse`. This is because `parse` validates your written `YAML`, configured tags, and so on.

### Introspective queries[​](#introspective-queries "Direct link to Introspective queries")

To generate the compiled SQL for many models, dbt needs to run introspective queries, (which is when dbt needs to run SQL in order to pull data back and do something with it) against the data platform.

These introspective queries include:

* Populating the relation cache. For more information, refer to the [Create new materializations](/guides/create-new-materializations) guide. Caching speeds up the metadata checks, including whether an [incremental model](/docs/build/incremental-models) already exists in the data platform.
* Resolving [macros](/docs/build/jinja-macros#macros), such as `run_query` or `dbt_utils.get_column_values` that you're using to template out your SQL. This is because dbt needs to run those queries during model SQL compilation.

Without a data platform connection, dbt can't perform these introspective queries and won't be able to generate the compiled SQL needed for the next steps in the dbt workflow. You can [`parse`](/reference/commands/parse) a project and use the [`list`](/reference/commands/list) resources in the project, without an internet or data platform connection. Parsing a project is enough to produce a [manifest](/reference/artifacts/manifest-json), however, keep in mind that the written-out manifest won't include compiled SQL.

To configure a project, you do need a [connection profile](/docs/core/connect-data-platform/connection-profiles) (`profiles.yml` if using the CLI). You need this file because the project's configuration depends on its contents. For example, you may need to use [`{{target}}`](/reference/dbt-jinja-functions/target) for conditional configs or know what platform you're running against so that you can choose the right flavor of SQL.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/compile.md)

Last updated on **Nov 19, 2025**

[Previous

docs](/reference/commands/cmd-docs)[Next

debug](/reference/commands/debug)

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