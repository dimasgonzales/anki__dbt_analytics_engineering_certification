# Source: https://docs.getdbt.com/docs/build/materializations

Materializations | dbt Developer Hub

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

* About
* [What is dbt?](/docs/introduction)
* [dbt Fusion engine](/docs/fusion)
* [About the dbt platform](/docs/cloud/about-cloud/dbt-cloud-features)
* [Supported data platforms](/docs/supported-data-platforms)
* Get started
* [Get started with dbt](/docs/get-started-dbt)
* [Set up dbt](/docs/about-setup)
* Build and develop
* [Develop with dbt](/docs/cloud/about-develop-dbt)
* [Build dbt projects](/docs/build/projects)

  + [About dbt projects](/docs/build/projects)
  + [dbt tips and tricks](/docs/build/dbt-tips)
  + [Build your DAG](/docs/build/models)
  + [Build your metrics](/docs/build/build-metrics-intro)
  + [Enhance your models](/docs/build/enhance-your-models)

    - [Enhance your models](/docs/build/enhance-your-models)
    - [Materializations](/docs/build/materializations)
    - [Incremental models](/docs/build/incremental-models-overview)
  + [Enhance your code](/docs/build/enhance-your-code)
  + [Organize your outputs](/docs/build/organize-your-outputs)
  + [Optimize development](/docs/build/empty-flag)
* [Build dbt Mesh](/docs/mesh/about-mesh)
* Deploy and explore
* [Deploy dbt](/docs/deploy/deployments)
* [Explore your data](/docs/explore/explore-your-data)
* [Use the dbt Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl)
* dbt AI
* [Copilot](/docs/cloud/dbt-copilot)
* [dbt MCP](/docs/dbt-ai/about-mcp)
* Additional tools
* [dbt integrations](/docs/cloud-integrations/overview)
* [Cost management](/docs/cloud/cost-management)
* Release information
* [Available dbt versions](/docs/dbt-versions/about-versions)
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [Build dbt projects](/docs/build/projects)
* [Enhance your models](/docs/build/enhance-your-models)
* Materializations

Copy page

On this page

Materializations
================

Overview[​](#overview "Direct link to Overview")
------------------------------------------------

MaterializationsThe exact Data Definition Language (DDL) that dbt will use when creating the model’s equivalent in a data warehouse. are strategies for persisting dbt models in a warehouse. There are five types of materializations built into dbt. They are:

* tableIn simplest terms, a table is the direct storage of data in rows and columns. Think excel sheet with raw values in each of the cells.
* viewA view (as opposed to a table) is a defined passthrough SQL query that can be run against a database (or data warehouse).
* incremental
* ephemeral
* materialized view

You can also configure [custom materializations](/guides/create-new-materializations?step=1) in dbt. Custom materializations are a powerful way to extend dbt's functionality to meet your specific needs.

Learn by video!

For video tutorials on Materializations, go to dbt Learn and check out the [Materializations fundamentals course](https://learn.getdbt.com/courses/materializations-fundamentals).

Configuring materializations[​](#configuring-materializations "Direct link to Configuring materializations")
------------------------------------------------------------------------------------------------------------

By default, dbt models are materialized as "views". Models can be configured with a different materialization by supplying the [`materialized` configuration](/reference/resource-configs/materialized) parameter as shown in the following tabs.

* Project file
* Model file
* Property file

dbt\_project.yml

```
# The following dbt_project.yml configures a project that looks like this:  
# .  
# └── models  
#     ├── csvs  
#     │   ├── employees.sql  
#     │   └── goals.sql  
#     └── events  
#         ├── stg_event_log.sql  
#         └── stg_event_sessions.sql  
  
name: my_project  
version: 1.0.0  
config-version: 2  
  
models:  
  my_project:  
    events:  
      # materialize all models in models/events as tables  
      +materialized: table  
    csvs:  
      # this is redundant, and does not need to be set  
      +materialized: view
```

Alternatively, materializations can be configured directly inside of the model SQL files. This can be useful if you are also setting [Performance Optimization] configs for specific models (for example, [Redshift specific configurations](/reference/resource-configs/redshift-configs) or [BigQuery specific configurations](/reference/resource-configs/bigquery-configs)).

models/events/stg\_event\_log.sql

```
{{ config(materialized='table', sort='timestamp', dist='user_id') }}  
  
select *  
from ...
```

Materializations can also be configured in the model's `properties.yml` file. The following example shows the `table` materialization type. For a complete list of materialization types, refer to [materializations](/docs/build/materializations#materializations).

models/properties.yml

```
models:  
  - name: events  
    config:  
      materialized: table
```

Materializations[​](#materializations "Direct link to Materializations")
------------------------------------------------------------------------

### View[​](#view "Direct link to View")

When using the `view` materialization, your model is rebuilt as a view on each run, via a `create view as` statement.

* **Pros:** No additional data is stored, views on top of source data will always have the latest records in them.
* **Cons:** Views that perform a significant transformation, or are stacked on top of other views, are slow to query.
* **Advice:**
  + Generally start with views for your models, and only change to another materialization when you notice performance problems.
  + Views are best suited for models that do not do significant transformation, for example, renaming, or recasting columns.

### Table[​](#table "Direct link to Table")

When using the `table` materialization, your model is rebuilt as a tableIn simplest terms, a table is the direct storage of data in rows and columns. Think excel sheet with raw values in each of the cells. on each run, via a `create table as` statement.

* **Pros:** Tables are fast to query
* **Cons:**
  + Tables can take a long time to rebuild, especially for complex transformations
  + New records in underlying source data are not automatically added to the table
* **Advice:**
  + Use the table materialization for any models being queried by BI tools, to give your end user a faster experience
  + Also use the table materialization for any slower transformations that are used by many downstream models

### Incremental[​](#incremental "Direct link to Incremental")

`incremental` models allow dbt to insert or update records into a table since the last time that model was run.

* **Pros:** You can significantly reduce the build time by just transforming new records
* **Cons:** Incremental models require extra configuration and are an advanced usage of dbt. Read more about using incremental models [here](/docs/build/incremental-models).
* **Advice:**
  + Incremental models are best for event-style data
  + Use incremental models when your `dbt run`s are becoming too slow (i.e. don't start with incremental models)

### Ephemeral[​](#ephemeral "Direct link to Ephemeral")

`ephemeral` models are not directly built into the database. Instead, dbt will interpolate the code from an ephemeral model into its dependent models using a common table expression (CTEA Common Table Expression (CTE) is a temporary result set that can be used in a SQL query. You can use CTEs to break up complex queries into simpler blocks of code that can connect and build on each other.). You can control the identifier for this CTE using a [model alias](/docs/build/custom-aliases), but dbt will always prefix the model identifier with `__dbt__cte__`.

* **Pros:**
  + You can still write reusable logic
  + Ephemeral models can help keep your data warehouseA data warehouse is a data management system used for data storage and computing that allows for analytics activities such as transforming and sharing data. clean by reducing clutter (also consider splitting your models across multiple schemas by [using custom schemas](/docs/build/custom-schemas)).
* **Cons:**
  + You cannot select directly from this model.
  + [Operations](/docs/build/hooks-operations#about-operations) (for example, macros called using [`dbt run-operation`](/reference/commands/run-operation) cannot `ref()` ephemeral nodes)
  + Overuse of ephemeral materialization can also make queries harder to debug.
  + Ephemeral materialization doesn't support [model contracts](/docs/mesh/govern/model-contracts#where-are-contracts-supported).
* **Advice:** Use the ephemeral materialization for:
  + Very light-weight transformations that are early on in your DAG
  + Are only used in one or two downstream models, and
  + Don't need to be queried directly

### Materialized View[​](#materialized-view "Direct link to Materialized View")

The `materialized_view` materialization allows the creation and maintenance of materialized views in the target database.
Materialized views are a combination of a view and a table, and serve use cases similar to incremental models.

* **Pros:**
  + Materialized views combine the query performance of a table with the data freshness of a view
  + Materialized views operate much like incremental materializations, however they are usually
    able to be refreshed without manual interference on a regular cadence (depending on the database), forgoing the regular dbt batch refresh
    required with incremental materializations
  + `dbt run` on materialized views corresponds to a code deployment, just like views

* **Cons:**
  + Due to the fact that materialized views are more complex database objects, database platforms tend to have
    fewer configuration options available; see your database platform's docs for more details
  + Materialized views may not be supported by every database platform

* **Advice:**
  + Consider materialized views for use cases where incremental models are sufficient, but you would like the data platform to manage the incremental logic and refresh.

#### Configuration Change Monitoring[​](#configuration-change-monitoring "Direct link to Configuration Change Monitoring")

This materialization makes use of the [`on_configuration_change`](/reference/resource-configs/on_configuration_change)
config, which aligns with the incremental nature of the namesake database object. This setting tells dbt to attempt to
make configuration changes directly to the object when possible, as opposed to completely recreating
the object to implement the updated configuration. Using `dbt-postgres` as an example, indexes can
be dropped and created on the materialized view without the need to recreate the materialized view itself.

#### Scheduled Refreshes[​](#scheduled-refreshes "Direct link to Scheduled Refreshes")

In the context of a `dbt run` command, materialized views should be thought of as similar to views.
For example, a `dbt run` command is only needed if there is the potential for a change in configuration or sql;
it's effectively a deploy action.
By contrast, a `dbt run` command is needed for a table in the same scenarios *AND when the data in the table needs to be updated*.
This also holds true for incremental and snapshot models, whose underlying relations are tables.
In the table cases, the scheduling mechanism is either dbt or your local scheduler;
there is no built-in functionality to automatically refresh the data behind a table.
However, most platforms (Postgres excluded) provide functionality to configure automatically refreshing a materialized view.
Hence, materialized views work similarly to incremental models with the benefit of not needing to run dbt to refresh the data.
This assumes, of course, that auto refresh is turned on and configured in the model.

info

`dbt-snowflake` *does not* support materialized views, it uses Dynamic Tables instead. For details, refer to [Snowflake specific configurations](/reference/resource-configs/snowflake-configs#dynamic-tables).

Python materializations[​](#python-materializations "Direct link to Python materializations")
---------------------------------------------------------------------------------------------

Python models support two materializations:

* `table`
* `incremental`

Incremental Python models support all the same [incremental strategies](/docs/build/incremental-strategy) as their SQL counterparts. The specific strategies supported depend on your adapter.

Python models can't be materialized as `view` or `ephemeral`. Python isn't supported for non-model resource types (like tests and snapshots).

For incremental models, like SQL models, you will need to filter incoming tables to only new rows of data:

* Snowpark
* PySpark

models/my\_python\_model.py

```
import snowflake.snowpark.functions as F  
  
def model(dbt, session):  
    dbt.config(materialized = "incremental")  
    df = dbt.ref("upstream_table")  
  
    if dbt.is_incremental:  
  
        # only new rows compared to max in current table  
        max_from_this = f"select max(updated_at) from {dbt.this}"  
        df = df.filter(df.updated_at >= session.sql(max_from_this).collect()[0][0])  
  
        # or only rows from the past 3 days  
        df = df.filter(df.updated_at >= F.dateadd("day", F.lit(-3), F.current_timestamp()))  
  
    ...  
  
    return df
```

models/my\_python\_model.py

```
import pyspark.sql.functions as F  
  
def model(dbt, session):  
    dbt.config(materialized = "incremental")  
    df = dbt.ref("upstream_table")  
  
    if dbt.is_incremental:  
  
        # only new rows compared to max in current table  
        max_from_this = f"select max(updated_at) from {dbt.this}"  
        df = df.filter(df.updated_at >= session.sql(max_from_this).collect()[0][0])  
  
        # or only rows from the past 3 days  
        df = df.filter(df.updated_at >= F.date_add(F.current_timestamp(), F.lit(-3)))  
  
    ...  
  
    return df
```

**Note:** Incremental models are supported on BigQuery/Dataproc for the `merge` incremental strategy. The `insert_overwrite` strategy is not yet supported.

### Questions from the Community[​](#questions-from-the-community "Direct link to Questions from the Community")

![Loading](/img/loader-icon.svg)[Ask the Community](https://discourse.getdbt.com/new-topic?category=help&tags=materialization "Ask the Community")

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/materializations.md)

Last updated on **Nov 19, 2025**

[Previous

Enhance your models](/docs/build/enhance-your-models)[Next

Configure incremental models](/docs/build/incremental-models)

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