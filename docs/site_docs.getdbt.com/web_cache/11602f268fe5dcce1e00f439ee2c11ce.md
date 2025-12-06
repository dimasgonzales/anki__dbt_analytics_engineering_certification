# Source: https://docs.getdbt.com/reference/resource-configs/postgres-configs

Postgres configurations | dbt Developer Hub

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

  + [Microsoft Azure Synapse DWH configurations](/reference/resource-configs/azuresynapse-configs)
  + [Amazon Athena configurations](/reference/resource-configs/athena-configs)
  + [Cloudera Impala configurations](/reference/resource-configs/impala-configs)
  + [Apache Spark configurations](/reference/resource-configs/spark-configs)
  + [BigQuery configurations](/reference/resource-configs/bigquery-configs)
  + [ClickHouse configurations](/reference/resource-configs/clickhouse-configs)
  + [Databricks configurations](/reference/resource-configs/databricks-configs)
  + [DeltaStream configurations](/reference/resource-configs/deltastream-configs)
  + [Doris/SelectDB configurations](/reference/resource-configs/doris-configs)
  + [DuckDB configurations](/reference/resource-configs/duckdb-configs)
  + [Microsoft Fabric Data Warehouse configurations](/reference/resource-configs/fabric-configs)
  + [Microsoft Fabric Spark configurations](/reference/resource-configs/fabricspark-configs)
  + [Firebolt configurations](/reference/resource-configs/firebolt-configs)
  + [Greenplum configurations](/reference/resource-configs/greenplum-configs)
  + [Infer configurations](/reference/resource-configs/infer-configs)
  + [IBM Netezza configurations](/reference/resource-configs/ibm-netezza-config)
  + [Materialize configurations](/reference/resource-configs/materialize-configs)
  + [Microsoft SQL Server configurations](/reference/resource-configs/mssql-configs)
  + [MindsDB configurations](/reference/resource-configs/mindsdb-configs)
  + [Oracle configurations](/reference/resource-configs/oracle-configs)
  + [Postgres configurations](/reference/resource-configs/postgres-configs)
  + [Redshift configurations](/reference/resource-configs/redshift-configs)
  + [SingleStore configurations](/reference/resource-configs/singlestore-configs)
  + [Snowflake configurations](/reference/resource-configs/snowflake-configs)
  + [Starburst/Trino configurations](/reference/resource-configs/trino-configs)
  + [Starrocks configurations](/reference/resource-configs/starrocks-configs)
  + [Salesforce Data Cloud configurations](/reference/resource-configs/data-cloud-configs)
  + [Teradata configurations](/reference/resource-configs/teradata-configs)
  + [Upsolver configurations](/reference/resource-configs/upsolver-configs)
  + [Vertica configurations](/reference/resource-configs/vertica-configs)
  + [IBM watsonx.data Presto configurations](/reference/resource-configs/watsonx-presto-config)
  + [IBM watsonx.data Spark configurations](/reference/resource-configs/watsonx-spark-config)
  + [Yellowbrick configurations](/reference/resource-configs/yellowbrick-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Platform-specific configs](/reference/resource-configs/resource-configs)
* Postgres configurations

Copy page

On this page

Postgres configurations
=======================

Incremental materialization strategies[​](#incremental-materialization-strategies "Direct link to Incremental materialization strategies")
------------------------------------------------------------------------------------------------------------------------------------------

In dbt-postgres, the following incremental materialization strategies are supported:

* `append` (default when `unique_key` is not defined)
* `merge`
* `delete+insert` (default when `unique_key` is defined)
* [`microbatch`](/docs/build/incremental-microbatch)

Performance optimizations[​](#performance-optimizations "Direct link to Performance optimizations")
---------------------------------------------------------------------------------------------------

### Unlogged[​](#unlogged "Direct link to Unlogged")

"Unlogged" tables can be considerably faster than ordinary tables, as they are not written to the write-ahead log nor replicated to read replicas. They are also considerably less safe than ordinary tables. See [Postgres docs](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-UNLOGGED) for details.

my\_table.sql

```
{{ config(materialized='table', unlogged=True) }}  
  
select ...
```

dbt\_project.yml

```
models:  
  +unlogged: true
```

### Indexes[​](#indexes "Direct link to Indexes")

While Postgres works reasonably well for datasets smaller than about 10m rows, database tuning is sometimes required. It's important to create indexes for columns that are commonly used in joins or where clauses.

Table models, incremental models, seeds, snapshots, and materialized views may have a list of `indexes` defined. Each Postgres index can have three components:

* `columns` (list, required): one or more columns on which the index is defined
* `unique` (boolean, optional): whether the index should be [declared unique](https://www.postgresql.org/docs/9.4/indexes-unique.html)
* `type` (string, optional): a supported [index type](https://www.postgresql.org/docs/current/indexes-types.html) (B-tree, Hash, GIN, etc)

my\_table.sql

```
{{ config(  
    materialized = 'table',  
    indexes=[  
      {'columns': ['column_a'], 'type': 'hash'},  
      {'columns': ['column_a', 'column_b'], 'unique': True},  
    ]  
)}}  
  
select ...
```

If one or more indexes are configured on a resource, dbt will run `create index` DDL statement(s) as part of that resource's materialization, within the same transaction as its main `create` statement. For the index's name, dbt uses a hash of its properties and the current timestamp, in order to guarantee uniqueness and avoid namespace conflict with other indexes.

```
create index if not exists  
"3695050e025a7173586579da5b27d275"  
on "my_target_database"."my_target_schema"."indexed_model"   
using hash  
(column_a);  
  
create unique index if not exists  
"1bf5f4a6b48d2fd1a9b0470f754c1b0d"  
on "my_target_database"."my_target_schema"."indexed_model"   
(column_a, column_b);
```

You can also configure indexes for a number of resources at once:

dbt\_project.yml

```
models:  
  project_name:  
    subdirectory:  
      +indexes:  
        - columns: ['column_a']  
          type: hash
```

Materialized views[​](#materialized-views "Direct link to Materialized views")
------------------------------------------------------------------------------

The Postgres adapter supports [materialized views](https://www.postgresql.org/docs/current/rules-materializedviews.html)
with the following configuration parameters:

| Parameter | Type | Required | Default | Change Monitoring Support |
| --- | --- | --- | --- | --- |
| [`on_configuration_change`](/reference/resource-configs/on_configuration_change) | `<string>` | no | `apply` | n/a |
| [`indexes`](#indexes) | `[{<dictionary>}]` | no | `none` | alter |

* Project file
* Property file
* Config block

dbt\_project.yml

```
models:  
  <resource-path>:  
    +materialized: materialized_view  
    +on_configuration_change: apply | continue | fail  
    +indexes:  
      - columns: [<column-name>]  
        unique: true | false  
        type: hash | btree
```

models/properties.yml

```
models:  
  - name: [<model-name>]  
    config:  
      materialized: materialized_view  
      on_configuration_change: apply | continue | fail  
      indexes:  
        - columns: [<column-name>]  
          unique: true | false  
          type: hash | btree
```

models/<model\_name>.sql

```
{{ config(  
    materialized="materialized_view",  
    on_configuration_change="apply" | "continue" | "fail",  
    indexes=[  
        {  
            "columns": ["<column-name>"],  
            "unique": true | false,  
            "type": "hash" | "btree",  
        }  
    ]  
) }}
```

The [`indexes`](#indexes) parameter corresponds to that of a table, as explained above.
It's worth noting that, unlike tables, dbt monitors this parameter for changes and applies the changes without dropping the materialized view.
This happens via a `DROP/CREATE` of the indexes, which can be thought of as an `ALTER` of the materialized view.

Learn more about these parameters in Postgres's [docs](https://www.postgresql.org/docs/current/sql-creatematerializedview.html).

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/postgres-configs.md)

Last updated on **Nov 19, 2025**

[Previous

Oracle configurations](/reference/resource-configs/oracle-configs)[Next

Redshift configurations](/reference/resource-configs/redshift-configs)

* [Incremental materialization strategies](#incremental-materialization-strategies)
* [Performance optimizations](#performance-optimizations)
  + [Unlogged](#unlogged)
  + [Indexes](#indexes)
* [Materialized views](#materialized-views)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/postgres-configs.md)

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