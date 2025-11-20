# Source: https://docs.getdbt.com/reference/resource-configs/snapshot_meta_column_names

snapshot\_meta\_column\_names | dbt Developer Hub

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
    - [target\_database](/reference/resource-configs/target_database)
    - [target\_schema](/reference/resource-configs/target_schema)
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
* snapshot\_meta\_column\_names

Copy page

On this page

snapshot\_meta\_column\_names
=============================

💡Did you know...

Available from dbt v1.9 or with the [dbt "Latest" release track](/docs/dbt-versions/cloud-release-tracks).

snapshots/schema.yml

```
snapshots:  
  - name: <snapshot_name>  
    config:  
      snapshot_meta_column_names:  
        dbt_valid_from: <string>  
        dbt_valid_to: <string>  
        dbt_scd_id: <string>  
        dbt_updated_at: <string>  
        dbt_is_deleted: <string>
```

snapshots/<filename>.sql

```
{{  
    config(  
      snapshot_meta_column_names={  
        "dbt_valid_from": "<string>",  
        "dbt_valid_to": "<string>",  
        "dbt_scd_id": "<string>",  
        "dbt_updated_at": "<string>",  
        "dbt_is_deleted": "<string>",  
      }  
    )  
}}
```

dbt\_project.yml

```
snapshots:  
  <resource-path>:  
    +snapshot_meta_column_names:  
      dbt_valid_from: <string>  
      dbt_valid_to: <string>  
      dbt_scd_id: <string>  
      dbt_updated_at: <string>  
      dbt_is_deleted: <string>
```

Description[​](#description "Direct link to Description")
---------------------------------------------------------

In order to align with an organization's naming conventions, the `snapshot_meta_column_names` config can be used to customize the names of the [metadata columns](/docs/build/snapshots#snapshot-meta-fields) within each snapshot.

Default[​](#default "Direct link to Default")
---------------------------------------------

By default, dbt snapshots use the following column names to track change history using [Type 2 slowly changing dimension](https://en.wikipedia.org/wiki/Slowly_changing_dimension#Type_2:_add_new_row) records:

| Field | Meaning | Notes | Example |
| --- | --- | --- | --- |
| `dbt_valid_from` | The timestamp when this snapshot row was first inserted and became valid. | The value is affected by the [`strategy`](/reference/resource-configs/strategy). | `snapshot_meta_column_names: {dbt_valid_from: start_date}` |
| `dbt_valid_to` | The timestamp when this row is no longer valid. |  | `snapshot_meta_column_names: {dbt_valid_to: end_date}` |
| `dbt_scd_id` | A unique key generated for each snapshot row. | This is used internally by dbt. | `snapshot_meta_column_names: {dbt_scd_id: scd_id}` |
| `dbt_updated_at` | The `updated_at` timestamp of the source record when this snapshot row was inserted. | This is used internally by dbt. | `snapshot_meta_column_names: {dbt_updated_at: modified_date}` |
| `dbt_is_deleted` | A string value indicating if the record has been deleted. (`True` if deleted, `False` if not deleted). | Added when `hard_deletes='new_record'` is configured. | `snapshot_meta_column_names: {dbt_is_deleted: is_deleted}` |

All of these column names can be customized using the `snapshot_meta_column_names` config. Refer to the [Example](#example) for more details.

warning

To avoid any unintentional data modification, dbt will **not** automatically apply any column renames. So if a user applies `snapshot_meta_column_names` config for a snapshot without updating the pre-existing table, they will get an error. We recommend either only using these settings for net-new snapshots, or arranging an update of pre-existing tables prior to committing a column name change.

How [`dbt_scd_id`](/reference/resource-configs/snapshot_meta_column_names#default) is calculated[​](#how-dbt_scd_id-is-calculated "Direct link to how-dbt_scd_id-is-calculated")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`dbt_scd_id` is a unique identifier generated for each row in a snapshot. dbt uses this identifier to detect changes in source records and manage versioning in slowly changing dimension (SCD) snapshots.

dbt's snapshot macro handles `dbt_scd_id` in [the dbt-adapters repository](https://github.com/dbt-labs/dbt-adapters/blob/b12c9870d6134905ab09bfda609ce8f81bc4b40a/dbt/include/global_project/macros/materializations/snapshots/strategies.sql#L38).

The hash is computed by concatenating values of the snapshot's [`unique_key`](/reference/resource-configs/unique_key) and either the `updated_at` timestamp (for the timestamp strategy) or the values in `check_cols` (for the check strategy), and then hashing the resulting string using the `md5` function. This enables dbt to track whether the contents of a row have changed between runs.

Here's an example of a custom hash calculation that combines multiple fields into a single string and hashes the result using `md5`.

```
md5(  
 coalesce(cast(unique_key1 as string), '') || '|' ||  
 coalesce(cast(unique_key2 as string), '') || '|' ||  
 coalesce(cast(updated_at as string), '')  
)
```

The exact fields included in the hash depend on the snapshot strategy:

* [`timestamp` strategy](/reference/resource-configs/strategy#use-the-timestamp-strategy): The hash typically combines the [`unique_key`](/reference/resource-configs/unique_key) columns and the `updated_at` value.
* [`check` strategy](/reference/resource-configs/strategy#use-the-check-strategy): The hash combines the `unique_key` columns and the values of the columns listed in [`check_cols`](/reference/resource-configs/check_cols).

If you don’t want to use `md5`, you can customize the [dispatched macro](https://github.com/dbt-labs/dbt-adapters/blob/4b3966efc50b1d013907a88bee4ab8ebd022d17a/dbt-adapters/src/dbt/include/global_project/macros/materializations/snapshots/strategies.sql#L42-L47).

Example[​](#example "Direct link to Example")
---------------------------------------------

snapshots/schema.yml

```
snapshots:  
  - name: orders_snapshot  
    relation: ref("orders")  
    config:  
      unique_key: id  
      strategy: check  
      check_cols: all  
      hard_deletes: new_record  
      snapshot_meta_column_names:  
        dbt_valid_from: start_date  
        dbt_valid_to: end_date  
        dbt_scd_id: scd_id  
        dbt_updated_at: modified_date  
        dbt_is_deleted: is_deleted
```

The resulting snapshot table contains the configured meta column names:

| id | scd\_id | modified\_date | start\_date | end\_date | is\_deleted |
| --- | --- | --- | --- | --- | --- |
| 1 | 60a1f1dbdf899a4dd... | 2024-10-02 ... | 2024-10-02 ... | 2024-10-03 ... | False |
| 1 | 60a1f1dbdf899a4dd... | 2024-10-03 ... | 2024-10-03 ... |  | True |
| 2 | b1885d098f8bcff51... | 2024-10-02 ... | 2024-10-02 ... |  | False |

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/snapshot_meta_column_names.md)

Last updated on **Nov 19, 2025**

[Previous

invalidate\_hard\_deletes](/reference/resource-configs/invalidate_hard_deletes)[Next

snapshot\_name](/reference/resource-configs/snapshot_name)

* [Description](#description)
* [Default](#default)
* [How `dbt_scd_id` is calculated](#how-dbt_scd_id-is-calculated)
* [Example](#example)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/snapshot_meta_column_names.md)

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