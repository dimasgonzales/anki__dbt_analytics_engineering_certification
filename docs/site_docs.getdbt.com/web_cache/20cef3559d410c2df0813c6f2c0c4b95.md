# Source: https://docs.getdbt.com/reference/dbt_project.yml

dbt\_project.yml | dbt Developer Hub

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

* [Project configs](/category/project-configs)
* dbt\_project.yml

Copy page

On this page

dbt\_project.yml
================

The dbt\_project.yml file is a required file for all dbt projects. It contains important information that tells dbt how to operate your project.

Every [dbt project](/docs/build/projects) needs a `dbt_project.yml` file — this is how dbt knows a directory is a dbt project. It also contains important information that tells dbt how to operate your project. It works as follows:

* dbt uses [YAML](https://yaml.org/) in a few different places. If you're new to YAML, it would be worth learning how arrays, dictionaries, and strings are represented.
* By default, dbt looks for the `dbt_project.yml` in your current working directory and its parents, but you can set a different directory using the `--project-dir` flag or the `DBT_PROJECT_DIR` environment variable.
* Specify your dbt project ID in the `dbt_project.yml` file using `project-id` under the `dbt-cloud` config. Find your project ID in your dbt project URL: For example, in `https://YOUR_ACCESS_URL/11/projects/123456`, the project ID is `123456`.
* Note, you can't set up a "property" in the `dbt_project.yml` file if it's not a config (an example is [macros](/reference/macro-properties)). This applies to all types of resources. Refer to [Configs and properties](/reference/configs-and-properties) for more detail.

Example[​](#example "Direct link to Example")
---------------------------------------------

The following example is a list of all available configurations in the `dbt_project.yml` file:

dbt\_project.yml

```
name: string  
  
config-version: 2  
version: version  
  
profile: profilename  
  
model-paths: [directorypath]  
seed-paths: [directorypath]  
test-paths: [directorypath]  
analysis-paths: [directorypath]  
macro-paths: [directorypath]  
snapshot-paths: [directorypath]  
docs-paths: [directorypath]  
asset-paths: [directorypath]  
function-paths: [directorypath]  
  
packages-install-path: directorypath  
  
clean-targets: [directorypath]  
  
query-comment: string  
  
require-dbt-version: version-range | [version-range]  
  
flags:  
  <global-configs>  
  
dbt-cloud:  
  project-id: project_id # Required  
  defer-env-id: environment_id # Optional  
  account-host: account-host # Defaults to 'cloud.getdbt.com'; Required if use a different Access URL  
  
exposures:  
  +enabled: true | false  
  
quoting:  
  database: true | false  
  schema: true | false  
  identifier: true | false  
  snowflake_ignore_case: true | false  # Fusion-only config. Aligns with Snowflake's session parameter QUOTED_IDENTIFIERS_IGNORE_CASE behavior.   
                                       # Ignored by dbt Core and other adapters.  
metrics:  
  <metric-configs>  
  
models:  
  <model-configs>  
  
seeds:  
  <seed-configs>  
  
semantic-models:  
  <semantic-model-configs>  
  
saved-queries:  
  <saved-queries-configs>  
  
snapshots:  
  <snapshot-configs>  
  
sources:  
  <source-configs>  
    
data_tests:  
  <test-configs>  
  
vars:  
  <variables>  
  
on-run-start: sql-statement | [sql-statement]  
on-run-end: sql-statement | [sql-statement]  
  
dispatch:  
  - macro_namespace: packagename  
    search_order: [packagename]  
  
restrict-access: true | false  
  
functions:  
  <function-configs>
```

The `+` prefix[​](#the--prefix "Direct link to the--prefix")
------------------------------------------------------------

dbt demarcates between a folder name and a configuration by using a `+` prefix before the configuration name. The `+` prefix is used for configs *only* and applies to `dbt_project.yml` under the corresponding resource key. It doesn't apply to:

* `config()` Jinja macro within a resource file
* config property in a `.yml` file.

For more info, see the [Using the `+` prefix](/reference/resource-configs/plus-prefix).

Naming convention[​](#naming-convention "Direct link to Naming convention")
---------------------------------------------------------------------------

It's important to follow the correct YAML naming conventions for the configs in your `dbt_project.yml` file to ensure dbt can process them properly. This is especially true for resource types with more than one word.

* Use dashes (`-`) when configuring resource types with multiple words in your `dbt_project.yml` file. Here's an example for [saved queries](/docs/build/saved-queries#configure-saved-query):

  dbt\_project.yml

  ```
  saved-queries:  # Use dashes for resource types in the dbt_project.yml file.  
    my_saved_query:  
      +cache:  
        enabled: true
  ```
* Use underscore (`_`) when configuring resource types with multiple words for YAML files other than the `dbt_project.yml` file. For example, here's the same saved queries resource in the `semantic_models.yml` file:

  models/semantic\_models.yml

  ```
  saved_queries:  # Use underscores everywhere outside the dbt_project.yml file.  
    - name: saved_query_name  
      ... # Rest of the saved queries configuration.  
      config:  
        cache:  
          enabled: true
  ```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt_project.yml.md)

Last updated on **Nov 19, 2025**

[Previous

Project configs](/category/project-configs)[Next

.dbtignore](/reference/dbtignore)

* [Example[​](#example "Direct link to Example")](#example)
* [The `+` prefix[​](#the--prefix "Direct link to the--prefix")](#the--prefix)
* [Naming convention[​](#naming-convention "Direct link to Naming convention")](#naming-convention)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt_project.yml.md)

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