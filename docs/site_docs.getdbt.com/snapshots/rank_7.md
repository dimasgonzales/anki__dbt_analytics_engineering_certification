# Source: https://docs.getdbt.com/reference/resource-configs/unique_key

unique\_key | dbt Developer Hub

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

  + [About resource paths](/reference/resource-configs/resource-path)
  + [Configs and properties](/reference/configs-and-properties)
  + [General properties](/category/general-properties)
  + [General configs](/category/general-configs)

    - [Advanced usage](/reference/advanced-config-usage)
    - [access](/reference/resource-configs/access)
    - [alias](/reference/resource-configs/alias)
    - [database](/reference/resource-configs/database)
    - [docs](/reference/resource-configs/docs)
    - [enabled](/reference/resource-configs/enabled)
    - [event\_time](/reference/resource-configs/event-time)
    - [full\_refresh](/reference/resource-configs/full_refresh)
    - [grants](/reference/resource-configs/grants)
    - [group](/reference/resource-configs/group)
    - [meta](/reference/resource-configs/meta)
    - [persist\_docs](/reference/resource-configs/persist_docs)
    - [Using the + prefix](/reference/resource-configs/plus-prefix)
    - [pre-hook & post-hook](/reference/resource-configs/pre-hook-post-hook)
    - [schema](/reference/resource-configs/schema)
    - [static\_analysis](/reference/resource-configs/static-analysis)
    - [tags](/reference/resource-configs/tags)
    - [unique\_key](/reference/resource-configs/unique_key)
  + [For models](/reference/model-properties)
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
* [General configs](/category/general-configs)
* unique\_key

Copy page

On this page

unique\_key
===========

unique\_key identifies records for incremental models or snapshots, ensuring changes are captured or updated correctly.

* Models
* Snapshots

Configure the `unique_key` in the `config` block of your [incremental model's](/docs/build/incremental-models) SQL file, in your `models/properties.yml` file, or in your `dbt_project.yml` file.

models/my\_incremental\_model.sql

```
{{  
    config(  
        materialized='incremental',  
        unique_key='id'  
    )  
}}
```

models/properties.yml

```
models:  
  - name: my_incremental_model  
    description: "An incremental model example with a unique key."  
    config:  
      materialized: incremental  
      unique_key: id
```

dbt\_project.yml

```
name: jaffle_shop  
  
models:  
  jaffle_shop:  
    staging:  
      +unique_key: id
```

For [snapshots](/docs/build/snapshots), configure the `unique_key` in the your `snapshot/filename.yml` file or in your `dbt_project.yml` file.

snapshots/<filename>.yml

```
snapshots:  
  - name: orders_snapshot  
    relation: source('my_source', 'my_table')  
    config:  
      unique_key: order_id
```

dbt\_project.yml

```
snapshots:  
  <resource-path>:  
    +unique_key: column_name_or_expression
```

Description[​](#description "Direct link to Description")
---------------------------------------------------------

A column name or expression that uniquely identifies each record in the inputs of a snapshot or incremental model. dbt uses this key to match incoming records to existing records in the target table (either a snapshot or an incremental model) so that changes can be captured or updated correctly:

* In an incremental model, dbt replaces the old row (like a merge key or upsert).
* In a snapshot, dbt keeps history, storing multiple rows for that same `unique_key` as it evolves over time.

In dbt "Latest" release track and from dbt v1.9, [snapshots](/docs/build/snapshots) are defined and configured in YAML files within your `snapshots/` directory. You can specify one or multiple `unique_key` values within your snapshot YAML file's `config` key.

caution

Providing a non-unique key will result in unexpected snapshot results. dbt **will not** test the uniqueness of this key, consider [testing](/blog/primary-key-testing#how-to-test-primary-keys-with-dbt) the source data to ensure that this key is indeed unique.

Default[​](#default "Direct link to Default")
---------------------------------------------

This parameter is optional. If you don't provide a `unique_key`, your adapter will default to using `incremental_strategy: append`.

If you leave out the `unique_key` parameter and use strategies like `merge`, `insert_overwrite`, `delete+insert`, or `microbatch`, the adapter will fall back to using `incremental_strategy: append`.

This is different for BigQuery:

* For `incremental_strategy = merge`, you must provide a `unique_key`; leaving it out leads to ambiguous or failing behavior.
* For `insert_overwrite` or `microbatch`, `unique_key` is not required because they work by partition replacement rather than row-level upserts.

Examples[​](#examples "Direct link to Examples")
------------------------------------------------

### Use an `id` column as a unique key[​](#use-an-id-column-as-a-unique-key "Direct link to use-an-id-column-as-a-unique-key")

* Models
* Snapshots

In this example, the `id` column is the unique key for an incremental model.

models/my\_incremental\_model.sql

```
{{  
    config(  
        materialized='incremental',  
        unique_key='id'  
    )  
}}  
  
select * from ..
```

In this example, the `id` column is used as a unique key for a snapshot.

snapshots/orders\_snapshot.yml

```
snapshots:  
  - name: orders_snapshot  
    relation: source('jaffle_shop', 'orders')  
    config:  
      schema: snapshots  
      unique_key: id  
      strategy: timestamp  
      updated_at: updated_at
```

You can also specify configurations in your `dbt_project.yml` file if multiple snapshots share the same `unique_key`:

dbt\_project.yml

```
snapshots:  
  <resource-path>:  
    +unique_key: id
```

### Use multiple unique keys[​](#use-multiple-unique-keys "Direct link to Use multiple unique keys")

* Models
* Snapshots

Configure multiple unique keys for an incremental model as a string representing a single column or a list of single-quoted column names that can be used together, for example, `['col1', 'col2', …]`.

Columns must not contain null values, otherwise the incremental model will fail to match rows and generate duplicate rows. Refer to [Defining a unique key](/docs/build/incremental-models#defining-a-unique-key-optional) for more information.

models/my\_incremental\_model.sql

```
{{ config(  
    materialized='incremental',  
    unique_key=['order_id', 'location_id']  
) }}  
  
with...
```

You can configure snapshots to use multiple unique keys for `primary_key` columns.

snapshots/transaction\_items\_snapshot.yml

```
snapshots:  
  - name: orders_snapshot  
    relation: source('jaffle_shop', 'orders')  
    config:  
      schema: snapshots  
      unique_key:   
        - order_id  
        - product_id  
      strategy: timestamp  
      updated_at: updated_at
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/unique_key.md)

Last updated on **Nov 19, 2025**

[Previous

tags](/reference/resource-configs/tags)[Next

Model properties](/reference/model-properties)

* [Description[​](#description "Direct link to Description")](#description)
* [Default[​](#default "Direct link to Default")](#default)
* [Examples[​](#examples "Direct link to Examples")](#examples)
  + [Use an `id` column as a unique key[​](#use-an-id-column-as-a-unique-key "Direct link to use-an-id-column-as-a-unique-key")](#use-an-id-column-as-a-unique-key)
  + [Use multiple unique keys[​](#use-multiple-unique-keys "Direct link to Use multiple unique keys")](#use-multiple-unique-keys)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/unique_key.md)

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