Copy page

On this page

dbt Command reference
=====================

You can run dbt using the following tools:

A key distinction with the tools mentioned, is that Cloud CLI and Studio IDE are designed to support safe parallel execution of dbt commands, leveraging dbt's infrastructure and its comprehensive [features](/docs/cloud/about-cloud/dbt-cloud-features). In contrast, dbt Core *doesn't support* safe parallel execution for multiple invocations in the same process. Learn more in the [parallel execution](#parallel-execution) section.

Parallel execution[​](#parallel-execution "Direct link to Parallel execution")
------------------------------------------------------------------------------

dbt allows for concurrent execution of commands, enhancing efficiency without compromising data integrity. This enables you to run multiple commands at the same time. However, it's important to understand which commands can be run in parallel and which can't.

In contrast, [`dbt-core` *doesn't* support](/reference/programmatic-invocations#parallel-execution-not-supported) safe parallel execution for multiple invocations in the same process, and requires users to manage concurrency manually to ensure data integrity and system stability.

To ensure your dbt workflows are both efficient and safe, you can run different types of dbt commands at the same time (in parallel) — for example, `dbt build` (write operation) can safely run alongside `dbt parse` (read operation) at the same time. However, you can't run `dbt build` and `dbt run` (both write operations) at the same time.

dbt commands can be `read` or `write` commands:

| Command type | Description | Example |
| --- | --- | --- |
| **Write** | These commands perform actions that change data or metadata in your data platform.   Limited to one invocation at any given time, which prevents any potential conflicts, such as overwriting the same table in your data platform at the same time. | `dbt build` `dbt run` |
| **Read** | These commands involve operations that fetch or read data without making any changes to your data platform.   Can have multiple invocations in parallel and aren't limited to one invocation at any given time. This means read commands can run in parallel with other read commands and a single write command. | `dbt parse` `dbt compile` |

Available commands[​](#available-commands "Direct link to Available commands")
------------------------------------------------------------------------------

The following sections outline the commands supported by dbt and their relevant flags. They are available in all tools and all [supported versions](/docs/dbt-versions/core) unless noted otherwise. You can run these commands in your specific tool by prefixing them with `dbt` — for example, to run the `test` command, type `dbt test`.

For information about selecting models on the command line, refer to [Model selection syntax](/reference/node-selection/syntax).

Commands with a ('❌') indicate write commands, commands with a ('✅') indicate read commands, and commands with a (N/A) indicate it's not relevant to the parallelization of dbt commands.

info

Some commands are not yet supported in the dbt Fusion Engine or have limited functionality. See the [Fusion supported features](/docs/fusion/supported-features) page for details.

| Command | Description | Parallel execution | Caveats |
| --- | --- | --- | --- |
| [build](/reference/commands/build) | Builds and tests all selected resources (models, seeds, tests, and more) | ❌ | All tools   All [supported versions](/docs/dbt-versions/core) |
| cancel | Cancels the most recent invocation. | N/A | Cloud CLI   Requires [dbt v1.6 or higher](/docs/dbt-versions/core) |
| [clean](/reference/commands/clean) | Deletes artifacts present in the dbt project | ✅ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [clone](/reference/commands/clone) | Clones selected models from the specified state | ❌ | All tools   Requires [dbt v1.6 or higher](/docs/dbt-versions/core) |
| [compile](/reference/commands/compile) | Compiles (but does not run) the models in a project | ✅ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [debug](/reference/commands/debug) | Debugs dbt connections and projects | ✅ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [deps](/reference/commands/deps) | Downloads dependencies for a project | ✅ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [docs](/reference/commands/cmd-docs) | Generates documentation for a project | ✅ | All tools   All [supported versions](/docs/dbt-versions/core)   Not yet supported in Fusion |
| [environment](/reference/commands/dbt-environment) | Enables you to interact with your dbt environment. | N/A | Cloud CLI   Requires [dbt v1.5 or higher](/docs/dbt-versions/core) |
| help | Displays help information for any command | N/A | dbt Core, Cloud CLI   All [supported versions](/docs/dbt-versions/core) |
| [init](/reference/commands/init) | Initializes a new dbt project | ✅ | Fusion   dbt Core  All [supported versions](/docs/dbt-versions/core) |
| [invocation](/reference/commands/invocation) | Enables users to debug long-running sessions by interacting with active invocations. | N/A | Cloud CLI   Requires [dbt v1.5 or higher](/docs/dbt-versions/core) |
| [list](/reference/commands/list) | Lists resources defined in a dbt project | ✅ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [parse](/reference/commands/parse) | Parses a project and writes detailed timing info | ✅ | All tools   All [supported versions](/docs/dbt-versions/core) |
| reattach | Reattaches to the most recent invocation to retrieve logs and artifacts. | N/A | Cloud CLI   Requires [dbt v1.6 or higher](/docs/dbt-versions/core) |
| [retry](/reference/commands/retry) | Retry the last run `dbt` command from the point of failure | ❌ | All tools   Requires [dbt v1.6 or higher](/docs/dbt-versions/core)  Not yet supported in Fusion |
| [run](/reference/commands/run) | Runs the models in a project | ❌ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [run-operation](/reference/commands/run-operation) | Invokes a macro, including running arbitrary maintenance SQL against the database | ❌ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [seed](/reference/commands/seed) | Loads CSV files into the database | ❌ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [show](/reference/commands/show) | Previews table rows post-transformation | ✅ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [snapshot](/reference/commands/snapshot) | Executes "snapshot" jobs defined in a project | ❌ | All tools   All [supported versions](/docs/dbt-versions/core) |
| [source](/reference/commands/source) | Provides tools for working with source data (including validating that sources are "fresh") | ✅ | All tools  All [supported versions](/docs/dbt-versions/core) |
| [test](/reference/commands/test) | Executes tests defined in a project | ✅ | All tools   All [supported versions](/docs/dbt-versions/core)   Fusion flags `--store-failures`, `--fail-fast`, `--warn-error` not yet supported |

Note, use the [`--version`](/reference/commands/version) flag to display the installed dbt Core or Cloud CLI version. (Not applicable for the Studio IDE). Available on all [supported versions](/docs/dbt-versions/core).