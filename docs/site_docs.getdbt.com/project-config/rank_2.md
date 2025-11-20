# Source: https://docs.getdbt.com/reference/model-configs

Model configurations | dbt Developer Hub

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
* Model configurations

Copy page

On this page

Model configurations
====================

Related documentation[​](#related-documentation "Direct link to Related documentation")
---------------------------------------------------------------------------------------

* [Models](/docs/build/models)
* [`run` command](/reference/commands/run)

Available configurations[​](#available-configurations "Direct link to Available configurations")
------------------------------------------------------------------------------------------------

### Model-specific configurations[​](#model-specific-configurations "Direct link to Model-specific configurations")

Resource-specific configurations are applicable to only one dbt resource type rather than multiple resource types. You can define these settings in the project file (`dbt_project.yml`), a property file (`models/properties.yml` for models, similarly for other resources), or within the resource’s file using the `{{ config() }}` macro.

The following resource-specific configurations are only available to Models:

* Project file
* Property file
* Config block

dbt\_project.yml

models/<model\_name>.sql

### General configurations[​](#general-configurations "Direct link to General configurations")

General configurations provide broader operational settings applicable across multiple resource types. Like resource-specific configurations, these can also be set in the project file, property files, or within resource-specific files.

* Project file
* Property file
* Config block

dbt\_project.yml

models/properties.yml

models/<model\_name>.sql

### Warehouse-specific configurations[​](#warehouse-specific-configurations "Direct link to Warehouse-specific configurations")

* [BigQuery configurations](/reference/resource-configs/bigquery-configs)
* [Redshift configurations](/reference/resource-configs/redshift-configs)
* [Snowflake configurations](/reference/resource-configs/snowflake-configs)
* [Databricks configurations](/reference/resource-configs/databricks-configs)
* [Spark configurations](/reference/resource-configs/spark-configs)

Configuring models[​](#configuring-models "Direct link to Configuring models")
------------------------------------------------------------------------------

Model configurations are applied hierarchically. You can configure models from within an installed package and also from within your dbt project in the following ways, listed in order of precedence:

1. Using a `config()` Jinja macro within a model.
2. Using a `config` [resource property](/reference/model-properties) in a `.yml` file.
3. From the `dbt_project.yml` project file, under the `models:` key. In this case, the model that's nested the deepest will have the highest priority.

The most specific configuration always takes precedence. In the project file, for example, configurations applied to a `marketing` subdirectory will take precedence over configurations applied to the entire `jaffle_shop` project. To apply a configuration to a model or directory of models, define the [resource path](/reference/resource-configs/resource-path) as nested dictionary keys.

Model configurations in your root dbt project have *higher* precedence than configurations in installed packages. This enables you to override the configurations of installed packages, providing more control over your dbt runs.

Example[​](#example "Direct link to Example")
---------------------------------------------

### Configuring directories of models in `dbt_project.yml`[​](#configuring-directories-of-models-in-dbt_projectyml "Direct link to configuring-directories-of-models-in-dbt_projectyml")

To configure models in your `dbt_project.yml` file, use the `models:` configuration option. Be sure to namespace your configurations to your project (shown below):

dbt\_project.yml

```
name: dbt_labs  
  
models:  
  # Be sure to namespace your model configs to your project name  
  dbt_labs:  
  
    # This configures models found in models/events/  
    events:  
      +enabled: true  
      +materialized: view  
  
      # This configures models found in models/events/base  
      # These models will be ephemeral, as the config above is overridden  
      base:  
        +materialized: ephemeral  
  
      ...
```

### Apply configurations to one model only[​](#apply-configurations-to-one-model-only "Direct link to Apply configurations to one model only")

Some types of configurations are specific to a particular model. In these cases, placing configurations in the `dbt_project.yml` file can be unwieldy. Instead, you can specify these configurations at the top of a model `.sql` file, or in its individual YAML properties.

models/events/base/base\_events.sql

```
{{  
  config(  
    materialized = "table",  
    tags = ["core", "events"]  
  )  
}}  
  
  
select * from {{ ref('raw_events') }}
```

models/events/base/properties.yml

```
models:  
  - name: base_events  
    description: "Standardized event data from raw sources"  
    columns:  
      - name: user_id  
        description: "Unique identifier for a user"  
        data_tests:  
          - not_null  
          - unique  
      - name: event_type  
        description: "Type of event recorded (click, purchase, etc.)"
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/model-configs.md)

Last updated on **Nov 19, 2025**

[Previous

Model properties](/reference/model-properties)[Next

freshness](/reference/resource-configs/freshness)

* [Related documentation](#related-documentation)
* [Available configurations](#available-configurations)
  + [Model-specific configurations](#model-specific-configurations)
  + [General configurations](#general-configurations)
  + [Warehouse-specific configurations](#warehouse-specific-configurations)
* [Configuring models](#configuring-models)
* [Example](#example)
  + [Configuring directories of models in `dbt_project.yml`](#configuring-directories-of-models-in-dbt_projectyml)
  + [Apply configurations to one model only](#apply-configurations-to-one-model-only)
  + [Configuring source freshness](#configuring-source-freshness)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/model-configs.md)

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