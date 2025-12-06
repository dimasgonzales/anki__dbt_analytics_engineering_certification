# Source: https://docs.getdbt.com/reference/resource-configs/contract

contract | dbt Developer Hub

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

  + [About resource paths](/reference/resource-configs/resource-path)
  + [Configs and properties](/reference/configs-and-properties)
  + [General properties](/category/general-properties)
  + [General configs](/category/general-configs)
  + [For models](/reference/model-properties)

    - [Model properties](/reference/model-properties)
    - [Model configurations](/reference/model-configs)
    - [freshness](/reference/resource-configs/freshness)
    - [batch\_size](/reference/resource-configs/batch-size)
    - [begin](/reference/resource-configs/begin)
    - [concurrent\_batches](/reference/resource-properties/concurrent_batches)
    - [contract](/reference/resource-configs/contract)
    - [lookback](/reference/resource-configs/lookback)
    - [materialized](/reference/resource-configs/materialized)
    - [model\_name](/reference/resource-properties/model_name)
    - [on\_configuration\_change](/reference/resource-configs/on_configuration_change)
    - [sql\_header](/reference/resource-configs/sql_header)
  + [For seeds](/reference/seed-properties)
  + [For snapshots](/reference/snapshot-properties)
  + [For data tests](/reference/data-test-configs)
  + [For unit tests](/reference/resource-properties/unit-tests)
  + [For sources](/reference/source-properties)
  + [For analyses](/reference/analysis-properties)
  + [For exposures](/reference/exposure-properties)
  + [For macros](/reference/macro-properties)
  + [For functions](/reference/function-properties)
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Resource configs and properties](/reference/resource-configs/resource-path)
* [For models](/reference/model-properties)
* contract

Copy page

On this page

contract
========

When the `contract` configuration is enforced, dbt will ensure that your model's returned dataset exactly matches the attributes you have defined in yaml:

* `name` and `data_type` for every column
* Additional [`constraints`](/reference/resource-properties/constraints), as supported for this materialization and data platform

This is to ensure that the people querying your model downstream—both inside and outside dbt—have a predictable and consistent set of columns to use in their analyses. Even a subtle change in data type, such as from `boolean` (`true`/`false`) to `integer` (`0`/`1`), could cause queries to fail in surprising ways.

Support[​](#support "Direct link to Support")
---------------------------------------------

At present, model contracts are supported for:

* SQL models (not yet Python)
* Models materialized as `table`, `view`, and `incremental` (with `on_schema_change: append_new_columns` or `on_schema_change: fail`)
* The most popular data platforms — though support and enforcement of different [constraint types](/reference/resource-properties/constraints) vary by platform

Data type aliasing[​](#data-type-aliasing "Direct link to Data type aliasing")
------------------------------------------------------------------------------

dbt uses built-in type aliasing for the `data_type` defined in your YAML. For example, you can specify `string` in your contract, and on Postgres/Redshift, dbt will convert it to `text`. If dbt doesn't recognize the `data_type` name among its known aliases, it will pass it through as-is. This is enabled by default, but you can opt-out by setting `alias_types` to `false`.

Example for disabling:

FOLDER\_NAME/FILE\_NAME.yml

```
models:  
  - name: my_model  
    config:  
      contract:  
        enforced: true  
        alias_types: false  # true by default
```

Size, precision, and scale[​](#size-precision-and-scale "Direct link to Size, precision, and scale")
----------------------------------------------------------------------------------------------------

When dbt compares data types, it will not compare granular details such as size, precision, or scale. We don't think you should sweat the difference between `varchar(256)` and `varchar(257)`, because it doesn't really affect the experience of downstream queriers. You can accomplish a more-precise assertion by [writing or using a custom test](/best-practices/writing-custom-generic-tests).

Note that you need to specify a varchar size or numeric scale, otherwise dbt relies on default values. For example, if a `numeric` type defaults to a precision of 38 and a scale of 0, then the numeric column stores 0 digits to the right of the decimal (it only stores whole numbers), which might cause it to fail contract enforcement. To avoid this implicit coercion, specify your `data_type` with a nonzero scale, like `numeric(38, 6)`. dbt Core 1.7 and higher provides a warning if you don't specify precision and scale when providing a numeric data type.

### Example[​](#example "Direct link to Example")

models/dim\_customers.yml

```
models:  
  - name: dim_customers  
    config:  
      materialized: table  
      contract:  
        enforced: true  
    columns:  
      - name: customer_id  
        data_type: int  
        constraints:  
          - type: not_null  
      - name: customer_name  
        data_type: string  
      - name: non_integer  
        data_type: numeric(38,3)
```

Let's say your model is defined as:

models/dim\_customers.sql

```
select  
  'abc123' as customer_id,  
  'My Best Customer' as customer_name
```

When you `dbt run` your model, *before* dbt has materialized it as a table in the database, you will see this error:

```
20:53:45  Compilation Error in model dim_customers (models/dim_customers.sql)  
20:53:45    This model has an enforced contract that failed.  
20:53:45    Please ensure the name, data_type, and number of columns in your contract match the columns in your model's definition.  
20:53:45  
20:53:45    | column_name | definition_type | contract_type | mismatch_reason    |  
20:53:45    | ----------- | --------------- | ------------- | ------------------ |  
20:53:45    | customer_id | TEXT            | INT           | data type mismatch |  
20:53:45  
20:53:45  
20:53:45    > in macro assert_columns_equivalent (macros/materializations/models/table/columns_spec_ddl.sql)
```

### Incremental models and `on_schema_change`[​](#incremental-models-and-on_schema_change "Direct link to incremental-models-and-on_schema_change")

Why require that incremental models also set [`on_schema_change`](/docs/build/incremental-models#what-if-the-columns-of-my-incremental-model-change), and why to `append_new_columns` or `fail`?

Imagine:

* You add a new column to both the SQL and the YAML spec
* You don't set `on_schema_change`, or you set `on_schema_change: 'ignore'`
* dbt doesn't actually add that new column to the existing table — and the upsert/merge still succeeds, because it does that upsert/merge on the basis of the already-existing "destination" columns only (this is long-established behavior)
* The result is a delta between the yaml-defined contract, and the actual table in the database - which means the contract is now incorrect!

Why `append_new_columns` (or `fail`) rather than `sync_all_columns`? Because removing existing columns is a breaking change for contracted models! `sync_all_columns` works like `append_new_columns` but also removes deleted columns, which you're not suppose to do with contracted models unless you upgrade the version.

Related documentation[​](#related-documentation "Direct link to Related documentation")
---------------------------------------------------------------------------------------

* [What is a model contract?](/docs/mesh/govern/model-contracts)
* [Defining `columns`](/reference/resource-properties/columns)
* [Defining `constraints`](/reference/resource-properties/constraints)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/contract.md)

Last updated on **Nov 19, 2025**

[Previous

concurrent\_batches](/reference/resource-properties/concurrent_batches)[Next

lookback](/reference/resource-configs/lookback)

* [Support](#support)
* [Data type aliasing](#data-type-aliasing)
* [Size, precision, and scale](#size-precision-and-scale)
  + [Example](#example)
  + [Incremental models and `on_schema_change`](#incremental-models-and-on_schema_change)
* [Related documentation](#related-documentation)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/contract.md)

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