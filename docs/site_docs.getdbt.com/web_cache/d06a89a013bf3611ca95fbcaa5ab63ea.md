# Source: https://docs.getdbt.com/reference/artifacts/sources-json

Sources JSON file | dbt Developer Hub

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
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)

  + [About dbt artifacts](/reference/artifacts/dbt-artifacts)
  + [Catalog](/reference/artifacts/catalog-json)
  + [Manifest](/reference/artifacts/manifest-json)
  + [Run results](/reference/artifacts/run-results-json)
  + [Sources](/reference/artifacts/sources-json)
  + [Semantic manifest](/reference/artifacts/sl-manifest)
  + [Other artifacts](/reference/artifacts/other-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* Sources

Copy page

On this page

Sources JSON file
=================

**Current schema:** [`v3`](https://schemas.getdbt.com/dbt/sources/v3/index.html)

**Produced by:** [`source freshness`](/reference/commands/source)

This file contains information about [sources with freshness checks](/docs/build/sources#checking-source-freshness). Today, dbt uses this file to power its [Source Freshness visualization](/docs/build/sources#source-data-freshness).

### Top-level keys[​](#top-level-keys "Direct link to Top-level keys")

* [`metadata`](/reference/artifacts/dbt-artifacts#common-metadata)
* `elapsed_time`: Total invocation time in seconds.
* `results`: Array of freshness-check execution details.

Each entry in `results` is a dictionary with the following keys:

* `unique_id`: Unique source node identifier, which map results to `sources` in the [manifest](/reference/artifacts/manifest-json)
* `max_loaded_at`: Max value of `loaded_at_field` timestamp in the source table when queried.
* `snapshotted_at`: Current timestamp when querying.
* `max_loaded_at_time_ago_in_s`: Interval between `max_loaded_at` and `snapshotted_at`, calculated in python to handle timezone complexity.
* `criteria`: The freshness threshold(s) for this source, defined in the project.
* `status`: The freshness status of this source, based on `max_loaded_at_time_ago_in_s` + `criteria`, reported on the CLI. One of `pass`, `warn`, or `error` if the query succeeds, `runtime error` if the query fails.
* `execution_time`: Total time spent checking freshness for this source
* `timing`: Array that breaks down execution time into steps (`compile` + `execute`)

* `adapter_response`: Dictionary of metadata returned from the database, which varies by adapter. For example, success `code`, number of `rows_affected`, total `bytes_processed`, and so on. Not applicable for [data tests](/docs/build/data-tests).
  + `rows_affected` returns the number of rows modified by the last statement executed. In cases where the query's row count can't be determined or isn't applicable (such as when creating a view), a [standard value](https://peps.python.org/pep-0249/#rowcount) of `-1` is returned for `rowcount`.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/artifacts/sources-json.md)

Last updated on **Nov 19, 2025**

[Previous

Run results](/reference/artifacts/run-results-json)[Next

Semantic manifest](/reference/artifacts/sl-manifest)

* [Top-level keys](#top-level-keys)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/artifacts/sources-json.md)

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