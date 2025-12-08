About flags variable | dbt Developer Hub

[Skip to main content](#__docusaurus_skipToContent_fallback)

[Join our virtual event on Dec 16 & 17: Delivering reliable AI with the dbt Semantic Layer and dbt MCP Server](https://www.getdbt.com/resources/webinars/delivering-reliable-ai-with-the-dbt-semantic-layer-and-dbt-mcp-server)

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

  + [dbt Jinja functions](/reference/dbt-jinja-functions)

    - [adapter](/reference/dbt-jinja-functions/adapter)
    - [as\_bool](/reference/dbt-jinja-functions/as_bool)
    - [as\_native](/reference/dbt-jinja-functions/as_native)
    - [as\_number](/reference/dbt-jinja-functions/as_number)
    - [builtins](/reference/dbt-jinja-functions/builtins)
    - [config](/reference/dbt-jinja-functions/config)
    - [cross-database macros](/reference/dbt-jinja-functions/cross-database-macros)
    - [dbt\_project.yml context](/reference/dbt-jinja-functions/dbt-project-yml-context)
    - [dbt\_version](/reference/dbt-jinja-functions/dbt_version)
    - [debug](/reference/dbt-jinja-functions/debug-method)
    - [dispatch](/reference/dbt-jinja-functions/dispatch)
    - [doc](/reference/dbt-jinja-functions/doc)
    - [env\_var](/reference/dbt-jinja-functions/env_var)
    - [exceptions](/reference/dbt-jinja-functions/exceptions)
    - [execute](/reference/dbt-jinja-functions/execute)
    - [flags](/reference/dbt-jinja-functions/flags)
    - [fromjson](/reference/dbt-jinja-functions/fromjson)
    - [fromyaml](/reference/dbt-jinja-functions/fromyaml)
    - [graph](/reference/dbt-jinja-functions/graph)
    - [invocation\_id](/reference/dbt-jinja-functions/invocation_id)
    - [local\_md5](/reference/dbt-jinja-functions/local_md5)
    - [log](/reference/dbt-jinja-functions/log)
    - [model](/reference/dbt-jinja-functions/model)
    - [modules](/reference/dbt-jinja-functions/modules)
    - [on-run-end context](/reference/dbt-jinja-functions/on-run-end-context)
    - [print](/reference/dbt-jinja-functions/print)
    - [profiles.yml context](/reference/dbt-jinja-functions/profiles-yml-context)
    - [project\_name](/reference/dbt-jinja-functions/project_name)
    - [properties.yml context](/reference/dbt-jinja-functions/dbt-properties-yml-context)
    - [ref](/reference/dbt-jinja-functions/ref)
    - [return](/reference/dbt-jinja-functions/return)
    - [run\_query](/reference/dbt-jinja-functions/run_query)
    - [run\_started\_at](/reference/dbt-jinja-functions/run_started_at)
    - [schema](/reference/dbt-jinja-functions/schema)
    - [schemas](/reference/dbt-jinja-functions/schemas)
    - [selected\_resources](/reference/dbt-jinja-functions/selected_resources)
    - [set](/reference/dbt-jinja-functions/set)
    - [source](/reference/dbt-jinja-functions/source)
    - [statement blocks](/reference/dbt-jinja-functions/statement-blocks)
    - [target](/reference/dbt-jinja-functions/target)
    - [this](/reference/dbt-jinja-functions/this)
    - [thread\_id](/reference/dbt-jinja-functions/thread_id)
    - [tojson](/reference/dbt-jinja-functions/tojson)
    - [toyaml](/reference/dbt-jinja-functions/toyaml)
    - [var](/reference/dbt-jinja-functions/var)
    - [zip](/reference/dbt-jinja-functions/zip)
  + [dbt Classes](/reference/dbt-classes)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Jinja reference](/category/jinja-reference)
* [dbt Jinja functions](/reference/dbt-jinja-functions)
* flags

Copy page

Copy page

Copy page as Markdown for LLMs

[Open in ChatGPT

Ask questions about this page](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fflags+so+I+can+ask+questions+about+it.)[Open in Claude

Ask questions about this page](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fflags+so+I+can+ask+questions+about+it.)[Open in Perplexity

Ask questions about this page](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fflags+so+I+can+ask+questions+about+it.)

On this page

About flags variable
====================

The `flags` variable contains values of flags provided on the command line.

**Example usage:**

flags.sql

```
{% if flags.FULL_REFRESH %}  
drop table ...  
{% else %}  
-- no-op  
{% endif %}
```

The list of available flags is defined in the [`flags` module](https://github.com/dbt-labs/dbt-core/blob/HEAD/core/dbt/flags.py) within `dbt-core`.

Recommended use cases include:

* different materialization logic based on "run modes," such as `flags.FULL_REFRESH` and `flags.STORE_FAILURES`
* running hooks conditionally based on the current command / task type, via `flags.WHICH`

**Note:** It is *not* recommended to use flags as an input to parse-time configurations, properties, or dependencies (`ref` + `source`). Flags are likely to change in every invocation of dbt, and their parsed values will become stale (and yield incorrect results) in subsequent invocations that have partial parsing enabled. For more details, see [the docs on parsing](/reference/parsing).

### invocation\_args\_dict[​](#invocation_args_dict "Direct link to invocation_args_dict")

For the full set of information passed from the CLI—subcommand, flags, arguments—you can use `invocation_args_dict`. This is equivalent to the `args` dictionary in [`run_results.json`](/reference/artifacts/run-results-json).

models/my\_model.sql

```
-- invocation_args_dict:  
-- {{ invocation_args_dict }}  
  
-- dbt_metadata_envs:  
-- {{ dbt_metadata_envs }}  
  
select 1 as id
```

The `invocation_command` key within `invocation_args_dict` includes the entire subcommand when it compiles:

```
$ DBT_ENV_CUSTOM_ENV_MYVAR=myvalue dbt compile -s my_model  
  
12:10:22  Running with dbt=1.6.0-b8  
12:10:22  Registered adapter: postgres=1.6.0-b8  
12:10:22  Found 1 seed, 1 model, 349 macros  
12:10:22  
12:10:22  Concurrency: 5 threads (target='dev')  
12:10:22  
12:10:22  Compiled node 'my_model' is:  
-- invocation_args_dict:  
-- {'log_format_file': 'debug', 'log_level': 'info', 'exclude': (), 'send_anonymous_usage_stats': True, 'which': 'compile', 'defer': False, 'output': 'text', 'log_format': 'default', 'macro_debugging': False, 'populate_cache': True, 'static_parser': True, 'vars': {}, 'warn_error_options': WarnErrorOptions(include=[], exclude=[]), 'quiet': False, 'select': ('my_model',), 'indirect_selection': 'eager', 'strict_mode': False, 'version_check': False, 'enable_legacy_logger': False, 'log_path': '/Users/jerco/dev/scratch/testy/logs', 'profiles_dir': '/Users/jerco/.dbt', 'invocation_command': 'dbt compile -s my_model', 'log_level_file': 'debug', 'project_dir': '/Users/jerco/dev/scratch/testy', 'favor_state': False, 'use_colors_file': True, 'write_json': True, 'partial_parse': True, 'printer_width': 80, 'print': True, 'cache_selected_only': False, 'use_colors': True, 'introspect': True}  
  
-- dbt_metadata_envs:  
-- {'MYVAR': 'myvalue'}  
  
select 1 as id
```

flags.WHICH[​](#flagswhich "Direct link to flags.WHICH")
--------------------------------------------------------

`flags.WHICH` is a global variable that gets set when you run a dbt command. If used in a macro, it allows you to conditionally change behavior depending on the command currently being executed. For example, conditionally modifying SQL:

```
{% macro conditional_filter(table_name) %}  
    {# Add a WHERE clause only during `dbt run`, not during `dbt test` or `dbt compile` #}  
  
    select *  
    from {{ table_name }}  
    {% if flags.WHICH == "run" %}  
        where is_active = true  
    {% elif flags.WHICH == "test" %}  
        -- In test runs, restrict rows to keep tests fast  
        limit 10  
    {% elif flags.WHICH == "compile" %}  
        -- During compile, just add a harmless comment  
        -- compile mode detected  
    {% endif %}  
{% endmacro %}
```

The following commands are supported:

| `flags.WHICH` value | Description |
| --- | --- |
| `"build"` | Build and test all selected resources. |
| `"clean"` | Remove artifacts like target directory and packages. |
| `"clone"` | Clone models and other resources. |
| `"compile"` | Compile SQL, but do not execute. |
| `"debug"` | Test connections and validate configs. |
| `"deps"` | Download package dependencies. |
| `"docs"` | Generate and serve documentation. |
| `"environment"` | Workspace environment commands (cloud CLI). |
| `"help"` | Show help for commands and subcommands. |
| `"init"` | Bootstrap a new project. |
| `"invocation"` | For interacting with or inspecting current invocation (cloud CLI). |
| `"list"` | List resources. |
| `"parse"` | Parse project and report errors, but don’t build/test. |
| `"retry"` | Retry the last invocation from the point of failure. |
| `"run"` | Execute models. |
| `"run-operation"` | Invoke arbitrary macros or SQL ops. |
| `"seed"` | Load CSV(s) into the database. |
| `"show"` | Inspect resource definitions or materializations. |
| `"snapshot"` | Execute snapshots. |
| `"source"` | Validate freshness and inspect source definitions. |
| `"test"` | Schema and data tests. |
| `"version"` | Display dbt version. |

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt-jinja-functions/flags.md)

Last updated on **Dec 4, 2025**

[Previous

execute](/reference/dbt-jinja-functions/execute)[Next

fromjson](/reference/dbt-jinja-functions/fromjson)

* [invocation\_args\_dict](#invocation_args_dict)
* [flags.WHICH](#flagswhich)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt-jinja-functions/flags.md)

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