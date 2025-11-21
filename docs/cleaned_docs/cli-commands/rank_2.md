Copy page

On this page

Command line options
====================

For consistency, command-line interface (CLI) flags should come right after the `dbt` prefix and its subcommands. This includes "global" flags (supported for all commands). For a list of all Cloud CLI flags you can set, refer to [Available flags](/reference/global-configs/about-global-configs#available-flags). When set, CLI flags override [environment variables](/reference/global-configs/environment-variable-configs) and [project flags](/reference/global-configs/project-flags).

Environment variables contain a `DBT_` prefix.

For example, instead of using:

```
dbt --no-populate-cache run
```

You should use:

```
dbt run --no-populate-cache
```

Historically, passing flags (such as "global flags") *before* the subcommand is a legacy functionality that dbt Labs can remove at any time. We do not support using the same flag before and after the subcommand.

Using boolean and non-boolean flags[​](#using-boolean-and-non-boolean-flags "Direct link to Using boolean and non-boolean flags")
---------------------------------------------------------------------------------------------------------------------------------

You can construct your commands with boolean flags to enable or disable or with non-boolean flags that use specific values, such as strings.

* Non-boolean config
* Boolean config

Use this non-boolean config structure:

* Replacing `<SUBCOMMAND>` with the command this config applies to.
* `<THIS-CONFIG>` with the config you are enabling or disabling, and
* `<SETTING>` with the new setting for the config.

CLI flags

```
<SUBCOMMAND> --<THIS-CONFIG>=<SETTING>
```

### Example[​](#example "Direct link to Example")

CLI flags

```
dbt run --printer-width=80   
dbt test --indirect-selection=eager
```

To enable or disable boolean configs:

* Use `<SUBCOMMAND>` this config applies to.
* Followed by `--<THIS-CONFIG>` to turn it on, or `--no-<THIS-CONFIG>` to turn it off.
* Replace `<THIS-CONFIG>` with the config you are enabling or disabling

CLI flags

```
dbt <SUBCOMMAND> --<THIS-CONFIG>   
dbt <SUBCOMMAND> --no-<THIS-CONFIG>
```

### Example[​](#example-1 "Direct link to Example")

CLI flags

```
dbt run --version-check  
dbt run --no-version-check
```

Config precedence[​](#config-precedence "Direct link to Config precedence")
---------------------------------------------------------------------------

There are multiple ways of setting flags, which depend on the use case:

* **[Project-level `flags` in `dbt_project.yml`](/reference/global-configs/project-flags):** Define version-controlled defaults for everyone running this project. Also, opt in or opt out of [behavior changes](/reference/global-configs/behavior-changes) to manage your migration off legacy functionality.
* **[Environment variables](/reference/global-configs/environment-variable-configs):** Define different behavior in different runtime environments (development vs. production vs. [continuous integration](/docs/deploy/continuous-integration), or different behavior for different users in development (based on personal preferences).
* **[CLI options](/reference/global-configs/command-line-options):** Define behavior specific to *this invocation*. Supported for all dbt commands.

The most specific setting "wins." If you set the same flag in all three places, the CLI option will take precedence, followed by the environment variable, and finally, the value in `dbt_project.yml`. If you set the flag in none of those places, it will use the default value defined within dbt.

Most flags can be set in all three places:

```
# dbt_project.yml  
flags:  
  # set default for running this project -- anywhere, anytime, by anyone  
  fail_fast: true
```

```
# set this environment variable to 'True' (bash syntax)  
export DBT_FAIL_FAST=1  
dbt run
```

```
dbt run --fail-fast # set to True for this specific invocation  
dbt run --no-fail-fast # set to False
```

There are two categories of exceptions:

1. **Flags setting file paths:** Flags for file paths that are relevant to runtime execution (for example, `--log-path` or `--state`) cannot be set in `dbt_project.yml`. To override defaults, pass CLI options or set environment variables (`DBT_LOG_PATH`, `DBT_STATE`). Flags that tell dbt where to find project resources (for example, `model-paths`) are set in `dbt_project.yml`, but as a top-level key, outside the `flags` dictionary; these configs are expected to be fully static and never vary based on the command or execution environment.
2. **Opt-in flags:** Flags opting in or out of [behavior changes](/reference/global-configs/behavior-changes) can *only* be defined in `dbt_project.yml`. These are intended to be set in version control and migrated via pull/merge request. Their values should not diverge indefinitely across invocations, environments, or users.