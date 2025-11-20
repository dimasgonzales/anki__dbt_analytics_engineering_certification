# Source: https://docs.getdbt.com/reference/commands/show

About dbt show command | dbt Developer Hub

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
* show

Copy page

About dbt show command
======================

Use `dbt show` to:

* Compile the dbt-SQL definition of a single `model`, `test`, `analysis`, or an arbitrary dbt-SQL query passed `--inline`
  + `dbt show` does not support [Python (dbt-py)](/docs/build/python-models) models.
  + Only selecting a single node is supported. [Selector methods](/reference/node-selection/methods), [graph operators](/reference/node-selection/graph-operators), and other methods that select multiple nodes will not be utilized.
* Run that query against the data warehouse
* Preview the results in the terminal

By default, `dbt show` will display the first 5 rows from the query result. This can be customized by passing the flag `--limit n`, where `n` is the number of rows to display.

The results of the preview query are not materialized in the data warehouse, or stored in any dbt file. They are only included in dbt's logs and displayed in the terminal. Note also that, if previewing a model, dbt will always compile and run the compiled query from source. It will not select from the already-materialized database relation, even if you've just run the model. (We may support that in the future; if you're interested, upvote or comment on [dbt-core#7391](https://github.com/dbt-labs/dbt-core/issues/7391).)

Example:

```
dbt show --select "model_name.sql"
```

or

```
dbt show --inline "select * from {{ ref('model_name') }}"
```

The following is an example of `dbt show` output for a model named `stg_orders`:

```
dbt show --select "stg_orders"  
21:17:38 Running with dbt=1.5.0-b5  
21:17:38 Found 5 models, 20 tests, 0 snapshots, 0 analyses, 425 macros, 0 operations, 3 seed files, 0 sources, 0 exposures, 0 metrics, 0 groups  
21:17:38  
21:17:38 Concurrency: 24 threads (target='dev')  
21:17:38  
21:17:38 Previewing node 'stg_orders' :  
| order_id | customer_id | order_date | status    |  
|----------+-------------+------------+--------   |  
| 1        |           1 | 2023-01-01 | returned  |  
| 2        |           3 | 2023-01-02 | completed |  
| 3        |          94 | 2023-01-03 | completed |  
| 4        |          50 | 2023-01-04 | completed |  
| 5        |          64 | 2023-01-05 | completed |
```

For example, if you've just built a model that has a failing test, you can quickly preview the test failures right in the terminal, to find values of `id` that are duplicated:

```
$ dbt build -s "my_model_with_duplicates"  
13:22:47 .0  
...  
13:22:48 Completed with 1 error and 0 warnings:  
13:22:48  
13:22:48 Failure in test unique_my_model_with_duplicates (models/schema.yml)  
13:22:48   Got 1 result, configured to fail if not 0  
13:22:48  
13:22:48   compiled code at target/compiled/my_dbt_project/models/schema.yml/unique_my_model_with_duplicates_id.sql  
13:22:48  
13:22:48 Done. PASS=1 WARN=0 ERROR=1 SKIP=0 TOTAL=2  
  
$ dbt show -s "unique_my_model_with_duplicates_id"  
13:22:53 Running with dbt=1.5.0  
13:22:53 Found 4 models, 2 tests, 0 snapshots, 0 analyses, 309 macros, 0 operations, 0 seed files, 0 sources, 0 exposures, 0 metrics, 0 groups  
13:22:53  
13:22:53 Concurrency: 5 threads (target='dev')  
13:22:53  
13:22:53 Previewing node 'unique_my_model_with_duplicates_id':  
| unique_field | n_records |  
| ------------ | --------- |  
|            1 |         2 |
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/show.md)

Last updated on **Nov 19, 2025**

[Previous

seed](/reference/commands/seed)[Next

snapshot](/reference/commands/snapshot)

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