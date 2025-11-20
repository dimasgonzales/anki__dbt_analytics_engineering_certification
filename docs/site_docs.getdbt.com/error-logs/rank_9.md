# Source: https://docs.getdbt.com/reference/global-configs/warnings

Warnings | dbt Developer Hub

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
* [Commands](/reference/dbt-commands)

  + [dbt Command reference](/reference/dbt-commands)
  + [List of commands](/category/list-of-commands)
  + [Node selection](/reference/node-selection/syntax)
  + [Flags (global configs)](/reference/global-configs/about-global-configs)

    - [About flags (global configs)](/reference/global-configs/about-global-configs)
    - [Behavior changes](/reference/global-configs/behavior-changes)
    - [Adapter behavior changes](/reference/global-configs/adapter-behavior-changes)
    - [Setting flags](/category/setting-flags)
    - [Available flags](/category/available-flags)

      * [Anonymous usage stats](/reference/global-configs/usage-stats)
      * [Checking version compatibility](/reference/global-configs/version-compatibility)
      * [Logs](/reference/global-configs/logs)
      * [Cache](/reference/global-configs/cache)
      * [Failing fast](/reference/global-configs/failing-fast)
      * [Indirect selection](/reference/global-configs/indirect-selection)
      * [JSON artifacts](/reference/global-configs/json-artifacts)
      * [Parsing](/reference/global-configs/parsing)
      * [Print output](/reference/global-configs/print-output)
      * [Record timing info](/reference/global-configs/record-timing-info)
      * [Resource type](/reference/global-configs/resource-type)
      * [Static analysis](/reference/global-configs/static-analysis-flag)
      * [Warnings](/reference/global-configs/warnings)
  + [Events and logs](/reference/events-logging)
  + [Exit codes](/reference/exit-codes)
  + [Deprecations](/reference/deprecations)
  + [Project Parsing](/reference/parsing)
  + [Programmatic invocations](/reference/programmatic-invocations)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Commands](/reference/dbt-commands)
* [Flags (global configs)](/reference/global-configs/about-global-configs)
* [Available flags](/category/available-flags)
* Warnings

Copy page

On this page

Warnings
========

Use the --warn-error flag to promote all warnings to errors or --warn-error-options for granular control through options.

Use `--warn-error` to promote all warnings to errors[​](#use---warn-error-to-promote-all-warnings-to-errors "Direct link to use---warn-error-to-promote-all-warnings-to-errors")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Enabling `WARN_ERROR` config or setting the `--warn-error` flag will convert *all* dbt warnings into errors. Any time dbt would normally warn, it will instead raise an error. Examples include `--select` criteria that selects no resources, deprecations, configurations with no associated models, invalid test configurations, or tests and freshness checks that are configured to return warnings.

Usage

```
dbt run --warn-error
```

Proceed with caution in production environments

Using the `--warn-error` flag or `--warn-error-options '{"error": "all"}'` will treat *all* current and future warnings as errors.

This means that if a new warning is introduced in a future version of dbt Core, your production job may start failing unexpectedly. We recommend proceeding with caution when doing this in production environments, and explicitly listing only the warnings you want to treat as errors in production.

Use `--warn-error-options` for targeted warnings[​](#use---warn-error-options-for-targeted-warnings "Direct link to use---warn-error-options-for-targeted-warnings")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

In some cases, you may want to convert *all* warnings to errors. However, when you want *some* warnings to stay as warnings and only promote or silence specific warnings you can instead use `--warn-error-options`. The `WARN_ERROR_OPTIONS` config or `--warn-error-options` flag gives you more granular control over *exactly which types of warnings* are treated as errors.

`WARN_ERROR` and `WARN_ERROR_OPTIONS` are mutually exclusive

`WARN_ERROR` and `WARN_ERROR_OPTIONS` are mutually exclusive. You can only specify one, even when you're specifying the config in multiple places (like env var or a flag), otherwise, you'll see a usage error.

Warnings that should be treated as errors can be specified through `error` parameter. Warning names can be found in:

* [dbt-core's types.py file](https://github.com/dbt-labs/dbt-core/blob/main/core/dbt/events/types.py), where each class name that inherits from `WarnLevel` corresponds to a warning name (e.g. `AdapterDeprecationWarning`, `NoNodesForSelectionCriteria`).
* Using the `--log-format json` flag.

The `error` parameter can be set to `"all"` or `"*"` to treat all warnings as errors (this behavior is the same as using the `--warn-error` flag), or to a list of specific warning names to treat as exceptions.

* When `error` is set to `"all"` or `"*"`, the optional `warn` parameter can be set to exclude specific warnings from being treated as exceptions.
* Use the `silence` parameter to ignore warnings. To silence certain warnings you want to ignore, you can specify them in the `silence` parameter. This is useful in large projects where certain warnings aren't critical and can be ignored to keep the noise low and logs clean.

Here's how you can use the [`--warn-error-options`](#use---warn-error-options-for-targeted-warnings) flag to promote *specific* warnings to errors:

* [Test warnings](/reference/resource-configs/severity) with the `--warn-error-options '{"error": ["LogTestResult"]}'` flag.
* Jinja [exception warnings](/reference/dbt-jinja-functions/exceptions#warn) with `--warn-error-options '{"error": ["JinjaLogWarning"]}'`.
* No nodes selected with `--warn-error-options '{"error": ["NoNodesForSelectionCriteria"]}'`.
* Deprecation warnings with `--warn-error-options '{"error": ["Deprecations"]}'` (new in v1.10).

### Configuration[​](#configuration "Direct link to Configuration")

You can configure warnings as errors or which warnings to silence, by warn error options through command flag, environment variable, or `dbt_project.yml`.

You can choose to:

* Promote all warnings to errors using `{"error": "all"}` or `--warn-error` flag.
* Promote specific warnings to errors using `error` and optionally exclude others from being treated as errors with `--warn-error-options` flag. `warn` tells dbt to continue treating the warnings as warnings.
* Ignore warnings using `silence` with `--warn-error-options` flag.

In the following example, we're silencing the [`NoNodesForSelectionCriteria` warning](https://github.com/dbt-labs/dbt-core/blob/main/core/dbt/events/types.py#L1227) in the `dbt_project.yml` file by adding it to the `silence` parameter:

dbt\_project.yml

```
...  
flags:  
  warn_error_options:  
    error: # Previously called "include"  
    warn: # Previously called "exclude"  
    silence: # To silence or ignore warnings  
      - NoNodesForSelectionCriteria
```

### Examples[​](#examples "Direct link to Examples")

Here are some examples that show you how to configure `warn_error_options` using flags or file-based configuration.

#### Target specific warnings[​](#target-specific-warnings "Direct link to Target specific warnings")

Some of the examples use `NoNodesForSelectionCriteria`, which is a specific warning that occurs when your `--select` flag doesn't match any nodes/resources in your dbt project:

* This command promotes all warnings to errors, except for `NoNodesForSelectionCriteria`:

  ```
  dbt run --warn-error-options '{"error": "all", "warn": ["NoNodesForSelectionCriteria"]}'
  ```
* This command promotes all warnings to errors, except for deprecation warnings:

  ```
  dbt run --warn-error-options '{"error": "all", "warn": ["Deprecations"]}'
  ```
* This command promotes only `NoNodesForSelectionCriteria` as an error:

  ```
  dbt run --warn-error-options '{"error": ["NoNodesForSelectionCriteria"]}'
  ```
* This promotes only `NoNodesForSelectionCriteria` as an error, using an environment variable:

  ```
  DBT_WARN_ERROR_OPTIONS='{"error": ["NoNodesForSelectionCriteria"]}' dbt run
  ```

Values for `error`, `warn`, and/or `silence` should be passed on as arrays. For example, `dbt run --warn-error-options '{"error": "all", "warn": ["NoNodesForSelectionCriteria"]}'` not `dbt run --warn-error-options '{"error": "all", "warn": "NoNodesForSelectionCriteria"}'`.

The following example shows how to promote all warnings to errors, except for the `NoNodesForSelectionCriteria` warning using the `silence` and `warn` parameters in the `dbt_project.yml` file:

dbt\_project.yml

```
...  
flags:  
  warn_error_options:  
    error: all # Previously called "include"  
    warn:      # Previously called "exclude"  
      - NoNodesForSelectionCriteria  
    silence:   # To silence or ignore warnings  
      - NoNodesForSelectionCriteria
```

#### Promote all warnings to errors[​](#promote-all-warnings-to-errors "Direct link to Promote all warnings to errors")

Some examples of how to promote all warnings to errors:

##### using dbt command flags[​](#using-dbt-command-flags "Direct link to using dbt command flags")

```
dbt run --warn-error  
dbt run --warn-error-options '{"error": "all"}'  
dbt run --warn-error-options '{"error": "*"}'
```

##### using environment variables[​](#using-environment-variables "Direct link to using environment variables")

```
WARN_ERROR=true dbt run   
DBT_WARN_ERROR_OPTIONS='{"error": "all"}' dbt run   
DBT_WARN_ERROR_OPTIONS='{"error": "*"}' dbt run
```

caution

Note, using `warn_error_options: error: "all"` will treat all current and future warnings as errors.

This means that if a new warning is introduced in a future version of dbt Core, your production job may start failing unexpectedly. We recommend proceeding with caution when doing this in production environments, and explicitly listing only the warnings you want to treat as errors in production.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/global-configs/warnings.md)

Last updated on **Nov 19, 2025**

[Previous

Static analysis](/reference/global-configs/static-analysis-flag)[Next

Events and logs](/reference/events-logging)

* [Use `--warn-error` to promote all warnings to errors[​](#use---warn-error-to-promote-all-warnings-to-errors "Direct link to use---warn-error-to-promote-all-warnings-to-errors")](#use---warn-error-to-promote-all-warnings-to-errors)
* [Use `--warn-error-options` for targeted warnings[​](#use---warn-error-options-for-targeted-warnings "Direct link to use---warn-error-options-for-targeted-warnings")](#use---warn-error-options-for-targeted-warnings)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/global-configs/warnings.md)

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