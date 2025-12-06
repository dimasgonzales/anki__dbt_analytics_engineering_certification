# Source: https://docs.getdbt.com/reference/resource-configs/grants

grants | dbt Developer Hub

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
* grants

Copy page

On this page

grants
======

You can manage access to the datasets you're producing with dbt by using grants. To implement these permissions, define grants as resource configs on each model, seed, or snapshot. Define the default grants that apply to the entire project in your `dbt_project.yml`, and define model-specific grants within each model's SQL or YAML file.

The grant resource configs enable you to apply permissions at build time to a specific set of recipients and model, seed, or snapshot. When your model, seed, or snapshot finishes building, dbt ensures that the grants on its view or table match exactly the grants you have configured.

dbt aims to use the most efficient approach when updating grants, which varies based on the adapter you're using, and whether dbt is replacing or updating an object that already exists. You can always check the debug logs for the full set of grant and revoke statements that dbt runs.

You should define grants as resource configs whenever possible, but you might occasionally need to write grants statements manually and run them using [hooks](/docs/build/hooks-operations). For example, hooks may be appropriate if you want to:

* Apply grants on other database objects besides views and tables.
* Create more granular row- and column-level access, use masking policies, or apply future grants.
* Take advantage of more advanced permission capabilities offered by your data platform, for which dbt does not offer out-of-the-box support using resource configuration.
* Apply grants in a more complex or custom manner, beyond what the built-in grants capability can provide.

For more information on hooks, see [Hooks & operations](/docs/build/hooks-operations).

Definition[​](#definition "Direct link to Definition")
------------------------------------------------------

You can use the `grants` field to set permissions or grants for a resource. When you `run` a model, `seed` data, or `snapshot` a dataset, dbt will run `grant` and/or `revoke` statements to ensure that the permissions on the database object match the `grants` you have configured on the resource.

Like all configurations, `grants` will be included in dbt project metadata, including [the manifest artifact](/reference/artifacts/manifest-json).

### Common syntax[​](#common-syntax "Direct link to Common syntax")

Grants have two key components:

* **Privilege:** A right to perform a specific action or set of actions on an object in the database, such as selecting data from a table.
* **Grantees:** One or more recipients of granted privileges. Some platforms also call these "principals." For example, a grantee could be a user, a group of users, a role held by one or more users (Snowflake), or a service account (BigQuery/GCP).

Configuring grants[​](#configuring-grants "Direct link to Configuring grants")
------------------------------------------------------------------------------

You can configure `grants` in `dbt_project.yml` to apply grants to many resources at once—all models in your project, a package, or a subfolder—and you can also configure `grants` one-by-one for specific resources, in YAML `config:` blocks or right within their `.sql` files.

* Models
* Seeds
* Snapshots

models/schema.yml

```
models:  
  - name: specific_model  
    config:  
      grants:  
        select: ['reporter', 'bi']
```

The `grants` config can also be defined:

* under the `models` config block in `dbt_project.yml`
* in a `config()` Jinja macro within a model's SQL file

See [configs and properties](/reference/configs-and-properties) for details.

seeds/schema.yml

```
seeds:  
  - name: seed_name  
    config:  
      grants:  
        select: ['reporter', 'bi']
```

The `grants` config can also be defined under the `seeds` config block in `dbt_project.yml`. See [configs and properties](/reference/configs-and-properties) for details.

snapshots/schema.yml

```
snapshots:  
  - name: snapshot_name  
    config:    
      grants:  
        select: ['reporter', 'bi']
```

The `grants` config can also be defined:

* under the `snapshots` config block in `dbt_project.yml`
* in a `config()` Jinja macro within a snapshot's SQL block

See [configs and properties](/reference/configs-and-properties) for details.

### Grant config inheritance[​](#grant-config-inheritance "Direct link to Grant config inheritance")

When you set `grants` for the same model in multiple places, such as in `dbt_project.yml` and in a more-specific `.sql` or `.yml` file, dbt's default behavior replaces the less-specific set of grantees with the more-specific set of grantees. This "merge and clobber" behavior updates each privilege when dbt parses your project.

For example:

dbt\_project.yml

```
models:  
  +grants:  # In this case the + is not optional, you must include it for your project to parse.  
    select: ['user_a', 'user_b']
```

models/specific\_model.sql

```
{{ config(grants = {'select': ['user_c']}) }}
```

As a result of this configuration, `specific_model` will be configured to grant the `select` privilege to `user_c` *only*. After you run `specific_model`, that is the only granted privilege you would see in the database, and the only `grant` statement you would find in dbt's logs.

Let's say we wanted to *add* `user_c` to the existing list of grantees receiving the `select` privilege on `specific_model`, rather than *replacing* that list entirely. To accomplish that, we can use the `+` ("addition") symbol, prefixing the name of the privilege:

models/specific\_model.sql

```
{{ config(grants = {'+select': ['user_c']}) }}
```

Now, the model will grant select to `user_a`, `user_b`, AND `user_c`!

**Notes:**

* This will only take effect for privileges which include the `+` prefix. Each privilege controls that behavior separately. If we were granting other privileges, in addition to `select`, and those privilege names lacked the `+` prefix, they would continue to "clobber" rather than "add" new grantees.
* This use of `+`, controlling clobber vs. add merge behavior, is distinct from the use of `+` in `dbt_project.yml` (shown in the example above) for defining configs with dictionary values. For more information, see [the plus prefix](/reference/resource-configs/plus-prefix).
* `grants` is the first config to support a `+` prefix for controlling config merge behavior. Currently, it's the only one. If it proves useful, we may extend this capability to new and existing configs in the future.

### Conditional grants[​](#conditional-grants "Direct link to Conditional grants")

Like any other config, you can use Jinja to vary the grants in different contexts. For example, you might grant different permissions in prod than dev:

dbt\_project.yml

```
models:  
  +grants:  
    select: "{{ ['user_a', 'user_b'] if target.name == 'prod' else ['user_c'] }}"
```

Revoking grants[​](#revoking-grants "Direct link to Revoking grants")
---------------------------------------------------------------------

dbt only modifies grants on a node (including revocation) when a `grants` configuration is attached to that node. For example, imagine you had originally specified the following grants in `dbt_project.yml`:

dbt\_project.yml

```
models:  
  +grants:  
    select: ['user_a', 'user_b']
```

If you delete the entire `+grants` section, dbt assumes you no longer want it to manage grants and doesn't change anything. To have dbt revoke all existing grants from a node, provide an empty list of grantees.

* Revoke from one user
* Revoke from all users
* Stop dbt from managing grants

dbt\_project.yml

```
models:  
  +grants:  
    select: ['user_b']
```

dbt\_project.yml

```
models:  
  +grants:  
    select: []
```

dbt\_project.yml

```
models:  
  
  # this section intentionally left blank
```

General examples[​](#general-examples "Direct link to General examples")
------------------------------------------------------------------------

You can grant each permission to a single grantee, or a set of multiple grantees. In this example, we're granting `select` on this model to just `bi_user`, so that it can be queried in our Business Intelligence (BI) tool.

models/table\_model.sql

```
{{ config(materialized = 'table', grants = {  
    'select': 'bi_user'  
}) }}
```

When dbt runs this model for the first time, it will create the table, and then run code like:

```
grant select on schema_name.table_model to bi_user;
```

In this case, we're creating an incremental model, and granting the `select` privilege to two recipients: `bi_user` and `reporter`.

models/incremental\_model.sql

```
{{ config(materialized = 'incremental', grants = {  
    'select': ['bi_user', 'reporter']  
}) }}
```

When dbt runs this model for the first time, it will create the table, and then run code like:

```
grant select on schema_name.incremental_model to bi_user, reporter;
```

In subsequent runs, dbt will use database-specific SQL to show the grants already on `incremental_model`, and then determine if any `revoke` or `grant` statements are needed.

Database-specific requirements and notes[​](#database-specific-requirements-and-notes "Direct link to Database-specific requirements and notes")
------------------------------------------------------------------------------------------------------------------------------------------------

While we try to standardize the terms we use to describe different features, you will always find nuances in different databases. This section outlines some of those database-specific requirements and notes.

In our examples above and below, you will find us referring to a privilege named `select`, and a grantee named `another_user`. Many databases use these or similar terms. Be aware that your database may require different syntax for privileges and grantees; you must configure `grants` in dbt with the appropriate names for both.

* BigQuery
* Databricks
* Redshift
* Snowflake

On BigQuery, "privileges" are called "roles," and they take the form `roles/service.roleName`. For instance, instead of granting `select` on a model, you would grant `roles/bigquery.dataViewer`.

Grantees can be users, groups, service accounts, domains—and each needs to be clearly demarcated as such with a prefix. For instance, to grant access on a model to `someone@yourcompany.com`, you need to specify them as `user:someone@yourcompany.com`.

We encourage you to read Google's documentation for more context:

* [Understanding GCP roles](https://cloud.google.com/iam/docs/understanding-roles)
* [How to format grantees](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-control-language#user_list)

Note

The `grants` config and the `grant_access_to` config are distinct.

* **`grant_access_to`:** Enables you to set up authorized views. When configured, dbt provides an authorized view access to show partial information from other datasets, without providing end users with full access to those underlying datasets. For more information, see ["BigQuery configurations: Authorized views"](/reference/resource-configs/bigquery-configs#authorized-views)
* **`grants`:** Provides specific permissions to users, groups, or service accounts for managing access to datasets you're producing with dbt. For more information, see ["Resource configs: grants"](/reference/resource-configs/grants)

You can use the two features together: "authorize" a view model with the `grants_access_to` configuration, and then add `grants` to that view model to share its query results (and *only* its query results) with other users, groups, or service accounts.

### BigQuery examples[​](#bigquery-examples "Direct link to BigQuery examples")

Granting permission using SQL and BigQuery:

```
{{ config(grants = {'roles/bigquery.dataViewer': ['user:someone@yourcompany.com']}) }}
```

Granting permission in a model schema using BigQuery:

models/schema.yml

```
models:  
  - name: specific_model  
    config:  
      grants:  
        roles/bigquery.dataViewer: ['user:someone@yourcompany.com']
```

* OSS Apache Spark / Delta Lake do not support `grants`.
* Databricks automatically enables `grants` on SQL endpoints. For interactive clusters, admins should enable grant functionality using these two setup steps in the Databricks documentation:
  + [Enable table access control for your workspace](https://docs.databricks.com/administration-guide/access-control/table-acl.html)
  + [Enable table access control for a cluster](https://docs.databricks.com/security/access-control/table-acls/table-acl.html)
* In order to grant `READ_METADATA` or `USAGE`, use [post-hooks](/reference/resource-configs/pre-hook-post-hook)

* Granting to / revoking from is only fully supported for Redshift users (not [groups](https://docs.aws.amazon.com/redshift/latest/dg/r_Groups.html) or [roles](https://docs.aws.amazon.com/redshift/latest/dg/r_roles-managing.html)). See [dbt-redshift#415](https://github.com/dbt-labs/dbt-redshift/issues/415) for the corresponding issue.

* dbt accounts for the [`copy_grants` configuration](/reference/resource-configs/snowflake-configs#copying-grants) when calculating which grants need to be added or removed.
* Granting to / revoking from is only fully supported for Snowflake roles (not [database roles](https://docs.snowflake.com/user-guide/security-access-control-overview#types-of-roles)).

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/grants.md)

Last updated on **Nov 19, 2025**

[Previous

full\_refresh](/reference/resource-configs/full_refresh)[Next

group](/reference/resource-configs/group)

* [Definition](#definition)
  + [Common syntax](#common-syntax)
* [Configuring grants](#configuring-grants)
  + [Grant config inheritance](#grant-config-inheritance)
  + [Conditional grants](#conditional-grants)
* [Revoking grants](#revoking-grants)
* [General examples](#general-examples)
* [Database-specific requirements and notes](#database-specific-requirements-and-notes)
  + [BigQuery examples](#bigquery-examples)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/grants.md)

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