# Source: https://docs.getdbt.com/docs/core/connect-data-platform/materialize-setup

Materialize setup | dbt Developer Hub

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

* About
* [What is dbt?](/docs/introduction)
* [dbt Fusion engine](/docs/fusion)
* [About the dbt platform](/docs/cloud/about-cloud/dbt-cloud-features)
* [Supported data platforms](/docs/supported-data-platforms)
* Get started
* [Get started with dbt](/docs/get-started-dbt)
* [Set up dbt](/docs/about-setup)

  + [About dbt setup](/docs/about-setup)
  + [About environments](/docs/environments-in-dbt)
  + [dbt platform](/docs/cloud/about-cloud-setup)
  + [dbt Core and Fusion](/docs/about-dbt-install)

    - [About dbt installation](/docs/about-dbt-install)
    - [dbt environments](/docs/core/dbt-core-environments)
    - [Install dbt Fusion engine](/docs/fusion/about-fusion-install)
    - [Connect Fusion to your data platform](/docs/fusion/connect-data-platform-fusion/profiles.yml)
    - [Install dbt Core](/docs/core/installation-overview)
    - [Connect dbt Core to your data platform](/docs/core/connect-data-platform/about-core-connections)

      * [About data platform connections in dbt Core](/docs/core/connect-data-platform/about-core-connections)
      * [About profiles.yml](/docs/core/connect-data-platform/profiles.yml)
      * [Connection profiles](/docs/core/connect-data-platform/connection-profiles)
      * [Apache Spark setup](/docs/core/connect-data-platform/spark-setup)
      * [BigQuery setup](/docs/core/connect-data-platform/bigquery-setup)
      * [Databricks setup](/docs/core/connect-data-platform/databricks-setup)
      * [DeltaStream setup](/docs/core/connect-data-platform/deltastream-setup)
      * [Microsoft Fabric Data Warehouse setup](/docs/core/connect-data-platform/fabric-setup)
      * [Microsoft Fabric Lakehouse setup](/docs/core/connect-data-platform/fabricspark-setup)
      * [Postgres setup](/docs/core/connect-data-platform/postgres-setup)
      * [AlloyDB setup](/docs/core/connect-data-platform/alloydb-setup)
      * [Databricks Lakebase setup](/docs/core/connect-data-platform/lakebase-setup)
      * [Redshift setup](/docs/core/connect-data-platform/redshift-setup)
      * [Snowflake setup](/docs/core/connect-data-platform/snowflake-setup)
      * [Starburst/Trino setup](/docs/core/connect-data-platform/trino-setup)
      * [Cloudera Hive setup](/docs/core/connect-data-platform/hive-setup)
      * [Cloudera Impala setup](/docs/core/connect-data-platform/impala-setup)
      * [Athena setup](/docs/core/connect-data-platform/athena-setup)
      * [AWS Glue setup](/docs/core/connect-data-platform/glue-setup)
      * [ClickHouse setup](/docs/core/connect-data-platform/clickhouse-setup)
      * [CrateDB setup](/docs/core/connect-data-platform/cratedb-setup)
      * [Databend Cloud setup](/docs/core/connect-data-platform/databend-setup)
      * [Decodable setup](/docs/core/connect-data-platform/decodable-setup)
      * [Doris setup](/docs/core/connect-data-platform/doris-setup)
      * [Dremio setup](/docs/core/connect-data-platform/dremio-setup)
      * [DuckDB setup](/docs/core/connect-data-platform/duckdb-setup)
      * [Exasol setup](/docs/core/connect-data-platform/exasol-setup)
      * [Extrica Setup](/docs/core/connect-data-platform/extrica-setup)
      * [Firebolt setup](/docs/core/connect-data-platform/firebolt-setup)
      * [Greenplum setup](/docs/core/connect-data-platform/greenplum-setup)
      * [IBM DB2 setup](/docs/core/connect-data-platform/ibmdb2-setup)
      * [IBM Netezza setup](/docs/core/connect-data-platform/ibmnetezza-setup)
      * [Infer setup](/docs/core/connect-data-platform/infer-setup)
      * [iomete setup](/docs/core/connect-data-platform/iomete-setup)
      * [Layer setup](/docs/core/connect-data-platform/layer-setup)
      * [Materialize setup](/docs/core/connect-data-platform/materialize-setup)
      * [Microsoft Azure Synapse Analytics setup](/docs/core/connect-data-platform/azuresynapse-setup)
      * [Microsoft SQL Server setup](/docs/core/connect-data-platform/mssql-setup)
      * [MindsDB setup](/docs/core/connect-data-platform/mindsdb-setup)
      * [MySQL setup](/docs/core/connect-data-platform/mysql-setup)
      * [Oracle setup](/docs/core/connect-data-platform/oracle-setup)
      * [RisingWave setup](/docs/core/connect-data-platform/risingwave-setup)
      * [Rockset setup](/docs/core/connect-data-platform/rockset-setup)
      * [SingleStore setup](/docs/core/connect-data-platform/singlestore-setup)
      * [SQLite setup](/docs/core/connect-data-platform/sqlite-setup)
      * [Starrocks setup](/docs/core/connect-data-platform/starrocks-setup)
      * [Teradata setup](/docs/core/connect-data-platform/teradata-setup)
      * [TiDB setup](/docs/core/connect-data-platform/tidb-setup)
      * [Upsolver setup](/docs/core/connect-data-platform/upsolver-setup)
      * [Vertica setup](/docs/core/connect-data-platform/vertica-setup)
      * [IBM watsonx.data Presto setup](/docs/core/connect-data-platform/watsonx-presto-setup)
      * [IBM watsonx.data Spark setup](/docs/core/connect-data-platform/watsonx-spark-setup)
      * [Yellowbrick setup](/docs/core/connect-data-platform/yellowbrick-setup)
      * [YDB setup](/docs/core/connect-data-platform/ydb-setup)
      * [MaxCompute setup](/docs/core/connect-data-platform/maxcompute-setup)
  + [Run your dbt projects](/docs/running-a-dbt-project/run-your-dbt-projects)
  + [Use threads](/docs/running-a-dbt-project/using-threads)
* Build and develop
* [Develop with dbt](/docs/cloud/about-develop-dbt)
* [Build dbt projects](/docs/build/projects)
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

* [Set up dbt](/docs/about-setup)
* [dbt Core and Fusion](/docs/about-dbt-install)
* [Connect dbt Core to your data platform](/docs/core/connect-data-platform/about-core-connections)
* Materialize setup

Copy page

On this page

Materialize setup
=================

Vendor-supported plugin

Certain core functionality may vary. If you would like to report a bug, request a feature, or contribute, you can check out the linked repository and open an issue.

* **Maintained by**: Materialize Inc.
* **Authors**: Materialize team
* **GitHub repo**: [MaterializeInc/materialize](https://github.com/MaterializeInc/materialize) [![](https://img.shields.io/github/stars/MaterializeInc/materialize?style=for-the-badge)](https://github.com/MaterializeInc/materialize)
* **PyPI package**: `dbt-materialize` [![](https://badge.fury.io/py/dbt-materialize.svg)](https://badge.fury.io/py/dbt-materialize)
* **Slack channel**: [#db-materialize](https://getdbt.slack.com/archives/C01PWAH41A5)
* **Supported dbt Core version**: v0.18.1 and newer
* **dbt support**: Not Supported
* **Minimum data platform version**: v0.28.0

Installing dbt-materialize
--------------------------

Use `pip` to install the adapter. Before 1.8, installing the adapter would automatically install `dbt-core` and any additional dependencies. Beginning in 1.8, installing an adapter does not automatically install `dbt-core`. This is because adapters and dbt Core versions have been decoupled from each other so we no longer want to overwrite existing dbt-core installations.
Use the following command for installation:

`python -m pip install dbt-core dbt-materialize`

Configuring dbt-materialize
---------------------------

For Materialize-specific configuration, please refer to [Materialize configs.](/reference/resource-configs/materialize-configs)

Connecting to Materialize[​](#connecting-to-materialize "Direct link to Connecting to Materialize")
---------------------------------------------------------------------------------------------------

Once you have set up a [Materialize account](https://materialize.com/register/), adapt your `profiles.yml` to connect to your instance using the following reference profile configuration:

~/.dbt/profiles.yml

```
materialize:  
  target: dev  
  outputs:  
    dev:  
      type: materialize  
      host: [host]  
      port: [port]  
      user: [user@domain.com]  
      pass: [password]  
      dbname: [database]  
      cluster: [cluster] # default 'default'  
      schema: [dbt schema]  
      sslmode: require  
      keepalives_idle: 0 # default: 0, indicating the system default  
      connect_timeout: 10 # default: 10 seconds  
      retries: 1 # default: 1, retry on error/timeout when opening connections
```

### Configurations[​](#configurations "Direct link to Configurations")

`cluster`: The default [cluster](https://materialize.com/docs/overview/key-concepts/#clusters) is used to maintain materialized views or indexes. A [`default` cluster](https://materialize.com/docs/sql/show-clusters/#default-cluster) is pre-installed in every environment, but we recommend creating dedicated clusters to isolate the workloads in your dbt project (for example, `staging` and `data_mart`).

`keepalives_idle`: The number of seconds before sending a ping to keep the Materialize connection active. If you are encountering `SSL SYSCALL error: EOF detected`, you may want to lower the [keepalives\_idle](/docs/core/connect-data-platform/postgres-setup#keepalives_idle) value to prevent the database from closing its connection.

To test the connection to Materialize, run:

```
dbt debug
```

If the output reads "All checks passed!", you’re good to go! Check the [dbt and Materialize guide](https://materialize.com/docs/guides/dbt/) to learn more and get started.

Supported Features[​](#supported-features "Direct link to Supported Features")
------------------------------------------------------------------------------

### Materializations[​](#materializations "Direct link to Materializations")

Because Materialize is optimized for transformations on streaming data and the core of dbt is built around batch, the `dbt-materialize` adapter implements a few custom materialization types:

| Type | Supported? | Details |
| --- | --- | --- |
| `source` | YES | Creates a [source](https://materialize.com/docs/sql/create-source/). |
| `view` | YES | Creates a [view](https://materialize.com/docs/sql/create-view/#main). |
| `materializedview` | YES | Creates a [materialized view](https://materialize.com/docs/sql/create-materialized-view/#main). |
| `table` | YES | Creates a [materialized view](https://materialize.com/docs/sql/create-materialized-view/#main). (Actual table support pending [#5266](https://github.com/MaterializeInc/materialize/issues/5266)) |
| `sink` | YES | Creates a [sink](https://materialize.com/docs/sql/create-sink/#main). |
| `ephemeral` | YES | Executes queries using CTEs. |
| `incremental` | NO | Use the `materializedview` materialization instead. Materialized views will always return up-to-date results without manual or configured refreshes. For more information, check out [Materialize documentation](https://materialize.com/docs/). |

### Indexes[​](#indexes "Direct link to Indexes")

Materialized views (`materializedview`), views (`view`) and sources (`source`) may have a list of [`indexes`](/reference/resource-configs/materialize-configs#indexes) defined.

### Seeds[​](#seeds "Direct link to Seeds")

Running [`dbt seed`](/reference/commands/seed) will create a static materialized view from a CSV file. You will not be able to add to or update this view after it has been created.

### Tests[​](#tests "Direct link to Tests")

Running [`dbt test`](/reference/commands/test) with the optional `--store-failures` flag or [`store_failures` config](/reference/resource-configs/store_failures) will create a materialized view for each configured test that can keep track of failures over time.

Resources[​](#resources "Direct link to Resources")
---------------------------------------------------

* [dbt and Materialize guide](https://materialize.com/docs/guides/dbt/)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/core/connect-data-platform/materialize-setup.md)

Last updated on **Nov 19, 2025**

[Previous

Layer setup](/docs/core/connect-data-platform/layer-setup)[Next

Microsoft Azure Synapse Analytics setup](/docs/core/connect-data-platform/azuresynapse-setup)

* [Connecting to Materialize](#connecting-to-materialize)
  + [Configurations](#configurations)
* [Supported Features](#supported-features)
  + [Materializations](#materializations)
  + [Indexes](#indexes)
  + [Seeds](#seeds)
  + [Tests](#tests)
* [Resources](#resources)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/core/connect-data-platform/materialize-setup.md)

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