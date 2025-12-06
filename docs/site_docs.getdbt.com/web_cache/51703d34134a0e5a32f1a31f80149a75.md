# Source: https://docs.getdbt.com/reference/global-configs/logs

Logs | dbt Developer Hub

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
* Logs

Copy page

On this page

Logs
====

### Log formatting[​](#log-formatting "Direct link to Log formatting")

dbt outputs logs to two different locations: CLI console and the log file.

The `LOG_FORMAT` and `LOG_FORMAT_FILE` configs specify how dbt's logs should be formatted, and they each have the same options: `json`, `text`, and `debug`.

Usage

```
dbt run --log-format json
```

The `text` format is the default for console logs and has plain text messages prefixed with a simple timestamp:

```
23:30:16  Running with dbt=1.8.0  
23:30:17  Registered adapter: postgres=1.8.0
```

The `debug` format is the default for the log file and is the same as the `text` format but with a more detailed timestamp and also includes the [`invocation_id`](/reference/dbt-jinja-functions/invocation_id), [`thread_id`](/reference/dbt-jinja-functions/thread_id), and [log level](/reference/global-configs/logs#log-level) of each message:

```
============================== 16:12:08.555032 | 9089bafa-4010-4f38-9b42-564ec9106e07 ==============================  
16:12:08.555032 [info ] [MainThread]: Running with dbt=1.8.0  
16:12:08.751069 [info ] [MainThread]: Registered adapter: postgres=1.8.0
```

The `json` format outputs fully structured logs in the JSONJSON (JavaScript Object Notation) is a minimal format for semi-structured data used to capture relationships between fields and values. format:

```
{"data": {"log_version": 3, "version": "=1.8.0"}, "info": {"category": "", "code": "A001", "extra": {}, "invocation_id": "82131fa0-d2b4-4a77-9436-019834e22746", "level": "info", "msg": "Running with dbt=1.8.0", "name": "MainReportVersion", "pid": 7875, "thread": "MainThread", "ts": "2024-05-29T23:32:54.993336Z"}}  
{"data": {"adapter_name": "postgres", "adapter_version": "=1.8.0"}, "info": {"category": "", "code": "E034", "extra": {}, "invocation_id": "82131fa0-d2b4-4a77-9436-019834e22746", "level": "info", "msg": "Registered adapter: postgres=1.8.0", "name": "AdapterRegistered", "pid": 7875, "thread": "MainThread", "ts": "2024-05-29T23:32:56.437986Z"}}
```

When the `LOG_FORMAT` is set explicitly, it will take effect in both the console and log files, whereas the `LOG_FORMAT_FILE` only affects the log file.

Usage

```
dbt run --log-format-file json
```

Tip: verbose structured logs

Use `json` formatting value in conjunction with the `DEBUG` config to produce rich log information which can be piped into monitoring tools for analysis:

```
dbt run --debug --log-format json
```

See [structured logging](/reference/events-logging#structured-logging) for more details.

### Log Level[​](#log-level "Direct link to Log Level")

The `LOG_LEVEL` config sets the minimum severity of events captured in the console and file logs. This is a more flexible alternative to the `--debug` flag. The available options for the log levels are `debug`, `info`, `warn`, `error`, or `none`.

* Setting the `--log-level` will configure console and file logs.

  ```
  dbt run --log-level debug
  ```
* Setting the `LOG_LEVEL` to `none` will disable information from being sent to either the console or file logs.

  ```
  dbt run --log-level none
  ```
* To set the file log level as a different value than the console, use the `--log-level-file` flag.

  ```
  dbt run --log-level-file error
  ```
* To only disable writing to the logs file but keep console logs, set `LOG_LEVEL_FILE` config to none.

  ```
  dbt run --log-level-file none
  ```

### Debug-level logging[​](#debug-level-logging "Direct link to Debug-level logging")

The `DEBUG` config redirects dbt's debug logs to standard output. This has the effect of showing debug-level log information in the terminal in addition to the `logs/dbt.log` file. This output is verbose.

The `--debug` flag is also available via shorthand as `-d`.

Usage

```
dbt run --debug
```

### Log and target paths[​](#log-and-target-paths "Direct link to Log and target paths")

By default, dbt will write logs to a directory named `logs/`, and all other artifacts to a directory named `target/`. Both of those directories are located relative to `dbt_project.yml` of the active project.

Just like other global configs, it is possible to override these values for your environment or invocation by using CLI options (`--target-path`, `--log-path`) or environment variables (`DBT_TARGET_PATH`, `DBT_LOG_PATH`).

### Suppress non-error logs in output[​](#suppress-non-error-logs-in-output "Direct link to Suppress non-error logs in output")

By default, dbt shows all logs in standard out (stdout). You can use the `QUIET` config to show only error logs in stdout. Logs will still include the output of anything passed to the [`print()`](/reference/dbt-jinja-functions/print) macro. For example, you might suppress all but error logs to more easily find and debug a Jinja error.

profiles.yml

```
config:  
  quiet: true
```

Supply the `-q` or `--quiet` flag to `dbt run` to show only error logs and suppress non-error logs.

```
dbt run --quiet
```

### dbt list logging[​](#dbt-list-logging "Direct link to dbt list logging")

In [dbt version 1.5](/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.5#behavior-changes), we updated the logging behavior of the [dbt list](/reference/commands/list) command to include `INFO` level logs by default.

You can use either of these parameters to ensure clean output that's compatible with downstream processes, such as piping results to [`jq`](https://jqlang.github.io/jq/manual/), a file, or another process:

* `dbt list --log-level warn` (recommended; equivalent to previous default)
* `dbt list --quiet` (suppresses all logging less than `ERROR` level, except for "printed" messages and list output)

### Logging relational cache events[​](#logging-relational-cache-events "Direct link to Logging relational cache events")

The `LOG_CACHE_EVENTS` config allows detailed logging for [relational cache](https://docs.getdbt.com/reference/global-configs/cache), which are disabled by default.

```
dbt compile --log-cache-events
```

### Color[​](#color "Direct link to Color")

You can set the color preferences for the file logs only within `profiles.yml` or using the `--use-colors-file / --no-use-colors-file` flags.

profiles.yml

```
config:  
  use_colors_file: False
```

```
dbt run --use-colors-file  
dbt run --no-use-colors-file
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/global-configs/logs.md)

Last updated on **Nov 19, 2025**

[Previous

Checking version compatibility](/reference/global-configs/version-compatibility)[Next

Cache](/reference/global-configs/cache)

* [Log formatting[​](#log-formatting "Direct link to Log formatting")](#log-formatting)
* [Log Level[​](#log-level "Direct link to Log Level")](#log-level)
* [Debug-level logging[​](#debug-level-logging "Direct link to Debug-level logging")](#debug-level-logging)
* [Log and target paths[​](#log-and-target-paths "Direct link to Log and target paths")](#log-and-target-paths)
* [Suppress non-error logs in output[​](#suppress-non-error-logs-in-output "Direct link to Suppress non-error logs in output")](#suppress-non-error-logs-in-output)
* [dbt list logging[​](#dbt-list-logging "Direct link to dbt list logging")](#dbt-list-logging)
* [Logging relational cache events[​](#logging-relational-cache-events "Direct link to Logging relational cache events")](#logging-relational-cache-events)
* [Color[​](#color "Direct link to Color")](#color)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/global-configs/logs.md)

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