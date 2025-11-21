# Source: https://docs.getdbt.com/reference/snapshot-configs

Snapshot configurations | dbt Developer Hub

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
  + [For models](/reference/model-properties)
  + [For seeds](/reference/seed-properties)
  + [For snapshots](/reference/snapshot-properties)

    - [Snapshot properties](/reference/snapshot-properties)
    - [Snapshot configurations](/reference/snapshot-configs)
    - [Legacy snapshot configurations](/reference/resource-configs/snapshots-jinja-legacy)
    - [check\_cols](/reference/resource-configs/check_cols)
    - [dbt\_valid\_to\_current](/reference/resource-configs/dbt_valid_to_current)
    - [hard\_deletes](/reference/resource-configs/hard-deletes)
    - [invalidate\_hard\_deletes](/reference/resource-configs/invalidate_hard_deletes)
    - [snapshot\_meta\_column\_names](/reference/resource-configs/snapshot_meta_column_names)
    - [snapshot\_name](/reference/resource-configs/snapshot_name)
    - [strategy](/reference/resource-configs/strategy)
    - [updated\_at](/reference/resource-configs/updated_at)
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
* [For snapshots](/reference/snapshot-properties)
* Snapshot configurations

Copy page

On this page

Snapshot configurations
=======================

Learn about using snapshot configurations in dbt, including snapshot-specific configurations and general configurations.

Related documentation[​](#related-documentation "Direct link to Related documentation")
---------------------------------------------------------------------------------------

* [Snapshots](/docs/build/snapshots)
* The `dbt snapshot` [command](/reference/commands/snapshot)

Learn by video!

For video tutorials on Snapshots, go to dbt Learn and check out the [Snapshots course](https://learn.getdbt.com/courses/snapshots).

Available configurations[​](#available-configurations "Direct link to Available configurations")
------------------------------------------------------------------------------------------------

### Snapshot-specific configurations[​](#snapshot-specific-configurations "Direct link to Snapshot-specific configurations")

Resource-specific configurations are applicable to only one dbt resource type rather than multiple resource types. You can define these settings in the project file (`dbt_project.yml`), a property file (`models/properties.yml` for models, similarly for other resources), or within the resource’s file using the `{{ config() }}` macro.

The following resource-specific configurations are only available to Snapshots:

* Project file
* YAML file
* Config block

dbt\_project.yml

```
snapshots:  
  <resource-path>:  
    +schema: <string>  
    +database: <string>  
    +alias: <string>  
    +unique_key: <column_name_or_expression>  
    +strategy: timestamp | check  
    +updated_at: <column_name>  
    +check_cols: [<column_name>] | all  
    +snapshot_meta_column_names: {<dictionary>}  
    +dbt_valid_to_current: <string>   
    +hard_deletes: string
```

Refer to [configuring snapshots](/docs/build/snapshots#configuring-snapshots) for the available configurations.

snapshots/schema.yml

```
snapshots:  
  - name: <string>  
    relation: ref() | source()  
    config:  
      database: <string>  
      schema: <string>  
      unique_key: <column_name_or_expression>  
      strategy: timestamp | check  
      updated_at: <column_name>  
      check_cols: [<column_name>] | all  
      snapshot_meta_column_names: {<dictionary>}  
      hard_deletes: string  
      dbt_valid_to_current: <string>
```

info

Starting from [the dbt "Latest" release track](/docs/dbt-versions/cloud-release-tracks) and dbt Core v1.9, defining snapshots in a `.sql` file using a config block is a legacy method. You can define snapshots in YAML format using the latest [snapshot-specific configurations](/docs/build/snapshots#configuring-snapshots). For new snapshots, we recommend using these latest configs. If applying them to existing snapshots, you'll need to [migrate](#snapshot-configuration-migration) over.

### Snapshot configuration migration[​](#snapshot-configuration-migration "Direct link to Snapshot configuration migration")

The latest snapshot configurations introduced in dbt Core v1.9 (such as [`snapshot_meta_column_names`](/reference/resource-configs/snapshot_meta_column_names), [`dbt_valid_to_current`](/reference/resource-configs/dbt_valid_to_current), and `hard_deletes`) are best suited for new snapshots, but you can also adopt them in existing snapshots by migrating your table schema and configs carefully to avoid any inconsistencies in your snapshots.

Here's how you can do it:

1. In your data platform, create a backup snapshot table. You can copy it to a new table:

   ```
   create table my_snapshot_table_backup as  
   select * from my_snapshot_table;
   ```

   This allows you to restore your snapshot if anything goes wrong during migration.
2. If you want to use the new configs, add required columns to your existing snapshot table using `alter` statements as needed. Here's an example of what to add if you're going to use `dbt_valid_to_current` and `snapshot_meta_column_names`:

   ```
   alter table my_snapshot_table  
   add column dbt_valid_from timestamp,  
   add column dbt_valid_to timestamp;
   ```
3. Then update your snapshot config:

   ```
   snapshots:  
     - name: orders_snapshot  
       relation: source('something','orders')  
       config:  
         strategy: timestamp  
         updated_at: updated_at  
         unique_key: id  
         dbt_valid_to_current: "to_date('9999-12-31')"  
         snapshot_meta_column_names:  
           dbt_valid_from: start_date  
           dbt_valid_to: end_date
   ```
4. Test each change before adopting multiple new configs by running `dbt snapshot` in development or staging.
5. Confirm if the snapshot run completes without errors, the new columns are created, and historical logic behaves as you’d expect. The table should look like this:

   | `id` | `start_date` | `end_date` | `updated_at` |
   | --- | --- | --- | --- |
   | 1 | 2024-10-01 09:00:00 | 2024-10-03 08:00:00 | 2024-10-01 09:00:00 |
   | 2 | 2024-10-03 08:00:00 | 9999-12-31 00:00:00 | 2024-10-03 08:00:00 |
   | 3 | 2024-10-02 11:15:00 | 9999-12-31 00:00:00 | 2024-10-02 11:15:00 |

Note: The `end_date` column (defined by `snapshot_meta_column_names`) uses the configured value from `dbt_valid_to_current` (9999-12-31) for newly inserted records, instead of the default `NULL`. Existing records will have `NULL` for `end_date`.

warning

If you use one of the latest configs, such as `dbt_valid_to_current`, without migrating your data, you may have mixed old and new data, leading to an incorrect downstream result.

### General configurations[​](#general-configurations "Direct link to General configurations")

General configurations provide broader operational settings applicable across multiple resource types. Like resource-specific configurations, these can also be set in the project file, property files, or within resource-specific files.

* Project file
* YAML file
* Config block

dbt\_project.yml

```
snapshots:  
  <resource-path>:  
    +enabled: true | false  
    +tags: <string> | [<string>]  
    +alias: <string>  
    +pre-hook: <sql-statement> | [<sql-statement>]  
    +post-hook: <sql-statement> | [<sql-statement>]  
    +persist_docs: {<dict>}  
    +grants: {<dict>}  
    +event_time: my_time_field
```

snapshots/properties.yml

```
snapshots:  
  - name: [<snapshot-name>]  
    relation: source('my_source', 'my_table')  
    config:  
      enabled: true | false  
      tags: <string> | [<string>]  
      alias: <string>  
      pre_hook: <sql-statement> | [<sql-statement>]  
      post_hook: <sql-statement> | [<sql-statement>]  
      persist_docs: {<dict>}  
      grants: {<dictionary>}  
      event_time: my_time_field
```

info

Starting from [the dbt "Latest" release track](/docs/dbt-versions/cloud-release-tracks) and dbt Core v1.9, defining snapshots in a `.sql` file using a config block is a legacy method. You can define snapshots in YAML format using the latest [snapshot-specific configurations](/docs/build/snapshots#configuring-snapshots). For new snapshots, we recommend using these latest configs. If applying them to existing snapshots, you'll need to [migrate](#snapshot-configuration-migration) over.

Configuring snapshots[​](#configuring-snapshots "Direct link to Configuring snapshots")
---------------------------------------------------------------------------------------

Snapshots can be configured in multiple ways:

1. Defined in YAML files using the `config` [resource property](/reference/model-properties), typically in your [snapshots directory](/reference/project-configs/snapshot-paths) or whichever folder you pefer. Available in [the dbt release track](/docs/dbt-versions/cloud-release-tracks), dbt v1.9 and higher.
2. From the `dbt_project.yml` file, under the `snapshots:` key. To apply a configuration to a snapshot, or directory of snapshots, define the resource path as nested dictionary keys.

Snapshot configurations are applied hierarchically in the order above with higher taking precedence. You can also apply [data tests](/reference/snapshot-properties) to snapshots using the [`tests` property](/reference/resource-properties/data-tests).

### Examples[​](#examples "Direct link to Examples")

The following examples demonstrate how to configure snapshots using the `dbt_project.yml` file and a `.yml` file.

* #### Apply configurations to all snapshots[​](#apply-configurations-to-all-snapshots "Direct link to Apply configurations to all snapshots")

  To apply a configuration to all snapshots, including those in any installed [packages](/docs/build/packages), nest the configuration directly under the `snapshots` key:

  dbt\_project.yml

  ```
  snapshots:  
    +unique_key: id
  ```
* #### Apply configurations to all snapshots in your project[​](#apply-configurations-to-all-snapshots-in-your-project "Direct link to Apply configurations to all snapshots in your project")

  To apply a configuration to all snapshots in your project only (for example, *excluding* any snapshots in installed packages), provide your project name as part of the resource path.

  For a project named `jaffle_shop`:

  dbt\_project.yml

  ```
  snapshots:  
    jaffle_shop:  
      +unique_key: id
  ```

  Similarly, you can use the name of an installed package to configure snapshots in that package.
* #### Apply configurations to one snapshot only[​](#apply-configurations-to-one-snapshot-only "Direct link to Apply configurations to one snapshot only")

  snapshots/postgres\_app/order\_snapshot.yml

  ```
  snapshots:  
   - name: orders_snapshot  
     relation: source('jaffle_shop', 'orders')  
     config:  
       unique_key: id  
       strategy: timestamp  
       updated_at: updated_at  
       persist_docs:  
         relation: true  
         columns: true
  ```

  Pro-tip: Use sources in snapshots: `select * from {{ source('jaffle_shop', 'orders') }}`

  You can also use the full resource path (including the project name, and subdirectories) to configure an individual snapshot from your `dbt_project.yml` file.

  For a project named `jaffle_shop`, with a snapshot file within the `snapshots/postgres_app/` directory, where the snapshot is named `orders_snapshot` (as above), this would look like:

  dbt\_project.yml

  ```
  snapshots:  
    jaffle_shop:  
      postgres_app:  
        orders_snapshot:  
          +unique_key: id  
          +strategy: timestamp  
          +updated_at: updated_at
  ```

  You can also define some common configs in a snapshot's `config` block. However, we don't recommend this for a snapshot's required configuration.

  dbt\_project.yml

  ```
  snapshots:  
    - name: orders_snapshot  
      +persist_docs:  
        relation: true  
        columns: true
  ```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/snapshot-configs.md)

Last updated on **Nov 19, 2025**

[Previous

Snapshot properties](/reference/snapshot-properties)[Next

Legacy snapshot configurations](/reference/resource-configs/snapshots-jinja-legacy)

* [Related documentation[​](#related-documentation "Direct link to Related documentation")](#related-documentation)
* [Available configurations[​](#available-configurations "Direct link to Available configurations")](#available-configurations)
  + [Snapshot-specific configurations[​](#snapshot-specific-configurations "Direct link to Snapshot-specific configurations")](#snapshot-specific-configurations)
  + [Snapshot configuration migration[​](#snapshot-configuration-migration "Direct link to Snapshot configuration migration")](#snapshot-configuration-migration)
  + [General configurations[​](#general-configurations "Direct link to General configurations")](#general-configurations)
* [Configuring snapshots[​](#configuring-snapshots "Direct link to Configuring snapshots")](#configuring-snapshots)
  + [Examples[​](#examples "Direct link to Examples")](#examples)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/snapshot-configs.md)

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