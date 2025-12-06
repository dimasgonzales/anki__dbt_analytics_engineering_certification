# Source: https://docs.getdbt.com/category/project-configs

Project configs | dbt Developer Hub

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

  + [dbt\_project.yml](/reference/dbt_project.yml)
  + [.dbtignore](/reference/dbtignore)
  + [analysis-paths](/reference/project-configs/analysis-paths)
  + [asset-paths](/reference/project-configs/asset-paths)
  + [clean-targets](/reference/project-configs/clean-targets)
  + [config-version](/reference/project-configs/config-version)
  + [dispatch (config)](/reference/project-configs/dispatch-config)
  + [docs-paths](/reference/project-configs/docs-paths)
  + [function-paths](/reference/project-configs/function-paths)
  + [macro-paths](/reference/project-configs/macro-paths)
  + [name](/reference/project-configs/name)
  + [on-run-start & on-run-end](/reference/project-configs/on-run-start-on-run-end)
  + [packages-install-path](/reference/project-configs/packages-install-path)
  + [profile](/reference/project-configs/profile)
  + [query-comment](/reference/project-configs/query-comment)
  + [quoting](/reference/project-configs/quoting)
  + [require-dbt-version](/reference/project-configs/require-dbt-version)
  + [snapshot-paths](/reference/project-configs/snapshot-paths)
  + [seed-paths](/reference/project-configs/seed-paths)
  + [model-paths](/reference/project-configs/model-paths)
  + [test-paths](/reference/project-configs/test-paths)
  + [version](/reference/project-configs/version)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* Project configs

Project configs
===============

The list of project configs available in dbt.

[📄️ dbt\_project.yml
-------------------

Reference guide for configuring the dbt\_project.yml file.](/reference/dbt_project.yml)

[📄️ .dbtignore
-------------

You can create a .dbtignore file in the root of your dbt project to specify files that should be entirely ignored by dbt. The file behaves like a .gitignore file, using the same syntax. Files and subdirectories matching the pattern will not be read, parsed, or otherwise detected by dbt—as if they didn't exist.](/reference/dbtignore)

[📄️ analysis-paths
-----------------

Read this guide to understand the analysis-paths configuration in dbt.](/reference/project-configs/analysis-paths)

[📄️ asset-paths
--------------

Read this guide to understand the asset-paths configuration in dbt.](/reference/project-configs/asset-paths)

[📄️ clean-targets
----------------

Definition](/reference/project-configs/clean-targets)

[📄️ config-version
-----------------

Read this guide to understand the config-version configuration in dbt.](/reference/project-configs/config-version)

[📄️ dispatch (config)
--------------------

Read this guide to understand the dispatch configuration in dbt.](/reference/project-configs/dispatch-config)

[📄️ docs-paths
-------------

Read this guide to understand the docs-paths configuration in dbt.](/reference/project-configs/docs-paths)

[📄️ function-paths
-----------------

Definition](/reference/project-configs/function-paths)

[📄️ macro-paths
--------------

Read this guide to understand the macro-paths configuration in dbt.](/reference/project-configs/macro-paths)

[📄️ name
-------

Read this guide to understand the name configuration in dbt.](/reference/project-configs/name)

[📄️ on-run-start & on-run-end
----------------------------

Read this guide to understand the on-run-start and on-run-end configurations in dbt.](/reference/project-configs/on-run-start-on-run-end)

[📄️ packages-install-path
------------------------

Definition](/reference/project-configs/packages-install-path)

[📄️ profile
----------

Read this guide to understand the profile configuration in dbt.](/reference/project-configs/profile)

[📄️ query-comment
----------------

The query-comment configuration also accepts a dictionary input, like so:](/reference/project-configs/query-comment)

[📄️ quoting
----------

Read this guide to understand the quoting configuration in dbt.](/reference/project-configs/quoting)

[📄️ require-dbt-version
----------------------

Read this guide to understand the require-dbt-version configuration in dbt.](/reference/project-configs/require-dbt-version)

[📄️ snapshot-paths
-----------------

Read this guide to understand the snapshot-paths configuration in dbt.](/reference/project-configs/snapshot-paths)

[📄️ seed-paths
-------------

Definition](/reference/project-configs/seed-paths)

[📄️ model-paths
--------------

Definition](/reference/project-configs/model-paths)

[📄️ test-paths
-------------

Definition](/reference/project-configs/test-paths)

[📄️ version
----------

dbt projects have two distinct types of version tags. This field has a different meaning depending on its location.](/reference/project-configs/version)

[Previous

About References](/reference/references-overview)[Next

dbt\_project.yml](/reference/dbt_project.yml)

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