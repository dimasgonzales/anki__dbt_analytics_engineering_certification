dbt Jinja functions
===================

In addition to the standard Jinja library, we've added additional functions and variables to the Jinja context that are useful when working with a dbt project.

[📄️ adapter
----------

Wrap the internal database adapter with the Jinja object `adapter`.](/reference/dbt-jinja-functions/adapter)

[📄️ as\_bool
-----------

Use this filter to coerce a Jinja output into boolean value.](/reference/dbt-jinja-functions/as_bool)

[📄️ as\_native
-------------

Use this filter to coerce Jinja-compiled output into its native python.](/reference/dbt-jinja-functions/as_native)

[📄️ as\_number
-------------

Use this filter to convert Jinja-compiled output to a numeric value..](/reference/dbt-jinja-functions/as_number)

[📄️ builtins
-----------

Read this guide to understand the builtins Jinja variable in dbt.](/reference/dbt-jinja-functions/builtins)

[📄️ config
---------

Read this guide to understand the config Jinja function in dbt.](/reference/dbt-jinja-functions/config)

[📄️ cross-database macros
------------------------

Read this guide to understand cross-database macros in dbt.](/reference/dbt-jinja-functions/cross-database-macros)

[📄️ dbt\_project.yml context
---------------------------

The context methods and variables available when configuring resources in the dbt\_project.yml file.](/reference/dbt-jinja-functions/dbt-project-yml-context)

[📄️ dbt\_version
---------------

Read this guide to understand the dbt\_version Jinja function in dbt.](/reference/dbt-jinja-functions/dbt_version)

[📄️ debug
--------

The `{{ debug() }}` macro will open an iPython debugger.](/reference/dbt-jinja-functions/debug-method)

[📄️ dispatch
-----------

dbt extends functionality across data platforms using multiple dispatch.](/reference/dbt-jinja-functions/dispatch)

[📄️ doc
------

Use the `doc` to reference docs blocks in description fields.](/reference/dbt-jinja-functions/doc)

[📄️ env\_var
-----------

Incorporate environment variables using `en\_var` function.](/reference/dbt-jinja-functions/env_var)

[📄️ exceptions
-------------

Raise warnings/errors with the `exceptions` namespace.](/reference/dbt-jinja-functions/exceptions)

[📄️ execute
----------

Use `execute` to return True when dbt is in 'execute' mode.](/reference/dbt-jinja-functions/execute)

[📄️ flags
--------

The `flags` variable contains values of flags provided on the cli.](/reference/dbt-jinja-functions/flags)

[📄️ fromjson
-----------

Deserialize a JSON string into python with `fromjson` context method.](/reference/dbt-jinja-functions/fromjson)

[📄️ fromyaml
-----------

Deserialize a YAML string into python with `fromyaml` context method.](/reference/dbt-jinja-functions/fromyaml)

[📄️ graph
--------

The `graph` context variable contains info about nodes in your project.](/reference/dbt-jinja-functions/graph)

[📄️ invocation\_id
-----------------

The `invocation\_id` outputs a UUID generated for this dbt command.](/reference/dbt-jinja-functions/invocation_id)

[📄️ local\_md5
-------------

Calculate an MD5 hash of a string with `local\_md5` context variable.](/reference/dbt-jinja-functions/local_md5)

[📄️ log
------

Learn more about the log Jinja function in dbt.](/reference/dbt-jinja-functions/log)

[📄️ model
--------

`model` is the dbt graph object (or node) for the current model.](/reference/dbt-jinja-functions/model)

[📄️ modules
----------

`modules` Jinja variables has useful Python modules to operate data.](/reference/dbt-jinja-functions/modules)

[📄️ on-run-end context
---------------------

Use these variables in the context for `on-run-end` hooks.](/reference/dbt-jinja-functions/on-run-end-context)

[📄️ print
--------

Use the `print()` to print messages to the log file and stdout.](/reference/dbt-jinja-functions/print)

[📄️ profiles.yml context
-----------------------

Use these context methods to configure resources in `profiles.yml` file.](/reference/dbt-jinja-functions/profiles-yml-context)

[📄️ project\_name
----------------

Read this guide to understand the project\_name Jinja function in dbt.](/reference/dbt-jinja-functions/project_name)

[📄️ properties.yml context
-------------------------

The context methods and variables available when configuring resources in a properties.yml file.](/reference/dbt-jinja-functions/dbt-properties-yml-context)

[📄️ ref
------

Read this guide to understand the ref Jinja function in dbt.](/reference/dbt-jinja-functions/ref)

[📄️ return
---------

Read this guide to understand the return Jinja function in dbt.](/reference/dbt-jinja-functions/return)

[📄️ run\_query
-------------

Use `run\_query` macro to run queries and fetch results.](/reference/dbt-jinja-functions/run_query)

[📄️ run\_started\_at
-------------------

Use `run\_started\_at` to output the timestamp the run started.](/reference/dbt-jinja-functions/run_started_at)

[📄️ schema
---------

The schema that the model is configured to be materialized in.](/reference/dbt-jinja-functions/schema)

[📄️ schemas
----------

A list of schemas where dbt built objects during the current run.](/reference/dbt-jinja-functions/schemas)

[📄️ selected\_resources
----------------------

Contains a list of all the nodes selected by current dbt command.](/reference/dbt-jinja-functions/selected_resources)

[📄️ set
------

Converts any iterable to a sequence of iterable and unique elements.](/reference/dbt-jinja-functions/set)

[📄️ source
---------

Read this guide to understand the source Jinja function in dbt.](/reference/dbt-jinja-functions/source)

[📄️ statement blocks
-------------------

SQL queries that hit database and return results to your Jinja context.](/reference/dbt-jinja-functions/statement-blocks)

[📄️ target
---------

The `target` variable contains information about your connection to the warehouse.](/reference/dbt-jinja-functions/target)

[📄️ this
-------

Represents the current model in the database.](/reference/dbt-jinja-functions/this)

[📄️ thread\_id
-------------

The `thread\_id` outputs an identifier for the current Python thread.](/reference/dbt-jinja-functions/thread_id)

[📄️ tojson
---------

Use this context method to serialize a Python object primitive.](/reference/dbt-jinja-functions/tojson)

[📄️ toyaml
---------

Used to serialize a Python object primitive.](/reference/dbt-jinja-functions/toyaml)

[📄️ var
------

Pass variables from `dbt\_project.yml` file into models.](/reference/dbt-jinja-functions/var)

[📄️ zip
------

Use this context method to return an iterator of tuples.](/reference/dbt-jinja-functions/zip)