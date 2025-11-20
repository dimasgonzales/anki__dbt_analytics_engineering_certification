# Source: https://docs.getdbt.com/faqs/Snapshots/snapshot-target-is-not-a-snapshot-table

Debug Snapshot target is not a snapshot table errors | dbt Developer Hub

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

* [Frequently asked questions](/docs/faqs)

  + [Accounts](/category/accounts)
  + [dbt Core](/category/dbt-core)
  + [Documentation](/category/documentation)
  + [Environments](/category/environments)
  + [Git](/category/git)
  + [Jinja](/category/jinja)
  + [Models](/category/models)
  + [Projects](/category/projects)
  + [Project\_ref](/faqs/Project_ref/define-private-packages)
  + [Runs](/category/runs)
  + [Seeds](/category/seeds)
  + [Snapshots](/category/snapshots)

    - [Use hooks to run with snapshots](/faqs/Snapshots/snapshot-hooks)
    - [Snapshot column changes](/faqs/Snapshots/snapshot-schema-changes)
    - [Snapshot target is not a snapshot table](/faqs/Snapshots/snapshot-target-is-not-a-snapshot-table)
    - [Snapshot freshness for specific sources.](/faqs/Snapshots/snapshotting-freshness-for-one-source)
  + [Tests](/category/tests)
  + [Troubleshooting](/category/troubleshooting)
  + [Warehouse](/category/warehouse)

* [Frequently asked questions](/docs/faqs)
* [Snapshots](/category/snapshots)
* Snapshot target is not a snapshot table

Copy page

Debug Snapshot target is not a snapshot table errors
====================================================

If you see the following error when you try executing the snapshot command:

> Snapshot target is not a snapshot table (missing `dbt_scd_id`, `dbt_valid_from`, `dbt_valid_to`)

Double check that you haven't inadvertently caused your snapshot to behave like table materializations by setting its `materialized` config to be `table`. Prior to dbt version 1.4, it was possible to have a snapshot like this:

```
{% snapshot snappy %}  
  {{ config(materialized = 'table', ...) }}  
  ...  
{% endsnapshot %}
```

dbt is treating snapshots like tables (issuing `create or replace table ...` statements) **silently** instead of actually snapshotting data (SCD2 via `insert` / `merge` statements). When upgrading to dbt versions 1.4 and higher, dbt now raises a Parsing Error (instead of silently treating snapshots like tables) that reads:

```
A snapshot must have a materialized value of 'snapshot'
```

This tells you to change your `materialized` config to `snapshot`. But when you make that change, you might encounter an error message saying that certain fields like `dbt_scd_id` are missing. This error happens because, previously, when dbt treated snapshots as tables, it didn't include the necessary [snapshot meta-fields](/docs/build/snapshots#snapshot-meta-fields) in your target table. Since those meta-fields don't exist, dbt correctly identifies that you're trying to create a snapshot in a table that isn't actually a snapshot.

When this happens, you have to start from scratch — re-snapshotting your source data as if it was the first time by dropping your "snapshot" which isn't a real snapshot table. Then dbt snapshot will create a new snapshot and insert the snapshot meta-fields as expected.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/faqs/Snapshots/snapshot-target-is-not-a-snapshot-table.md)

Last updated on **Nov 19, 2025**

[Previous

Snapshot column changes](/faqs/Snapshots/snapshot-schema-changes)[Next

Snapshot freshness for specific sources.](/faqs/Snapshots/snapshotting-freshness-for-one-source)

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