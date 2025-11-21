List of commands
================

The list of commands available in dbt.

[📄️ build
--------

The dbt build command will:](/reference/commands/build)

[📄️ clean
--------

dbt clean is a utility function that deletes the paths specified within the clean-targets list in the dbt\_project.yml file. It helps by removing unnecessary files or directories generated during the execution of other dbt commands, ensuring a clean state for the project.](/reference/commands/clean)

[📄️ clone
--------

The dbt clone command clones selected nodes from the specified state to the target schema(s). This command makes use of the clone materialization:](/reference/commands/clone)

[📄️ docs
-------

Generate and serve the docs for your dbt project.](/reference/commands/cmd-docs)

[📄️ compile
----------

The dbt compile command creates executable SQL from model, test, and analysis files.](/reference/commands/compile)

[📄️ debug
--------

Use dbt debug to test database connections and check system setup.](/reference/commands/debug)

[📄️ deps
-------

dbt deps pulls the most recent version of the dependencies listed in your packages.yml from git. See Package-Management for more information.](/reference/commands/deps)

[📄️ environment
--------------

The dbt environment command enables you to interact with your environment. Use the command for:](/reference/commands/dbt-environment)

[📄️ init
-------

dbt init helps get you started using !](/reference/commands/init)

[📄️ invocation
-------------

The dbt invocation command is available in the and allows you to:](/reference/commands/invocation)

[📄️ ls (list)
------------

Read this guide on how dbt's ls (list) command can be used to list resources in your dbt project.](/reference/commands/list)

[📄️ parse
--------

Read this guide on how dbt's parse command can be used to parse your dbt project and write detailed timing information.](/reference/commands/parse)

[📄️ retry
--------

dbt retry re-executes the last dbt command from the node point of failure.](/reference/commands/retry)

[📄️ rpc
------

Remote Procedure Call (rpc) dbt server compiles and runs queries, and provides methods that enable you to list and terminate running processes.](/reference/commands/rpc)

[📄️ run
------

The dbt run command executes your compiled SQL models against a target database.](/reference/commands/run)

[📄️ run-operation
----------------

Read this guide on how dbt's run-operation command can be used to invoke a macro.](/reference/commands/run-operation)

[📄️ seed
-------

The dbt seed command will load csv files located in the seed-paths directory of your dbt project into your .](/reference/commands/seed)

[📄️ show
-------

Use dbt show to:](/reference/commands/show)

[📄️ snapshot
-----------

The dbt snapshot command executes the Snapshots defined in your project.](/reference/commands/snapshot)

[📄️ source
---------

The dbt source command provides subcommands that are useful when working with source data. This command provides one subcommand, dbt source freshness.](/reference/commands/source)

[📄️ test
-------

dbt test runs data tests defined on models, sources, snapshots, and seeds and unit tests defined on SQL models. It expects that you have already created those resources through the appropriate commands.](/reference/commands/test)

[📄️ version
----------

The --version command-line flag returns information about the currently installed version of or the . This flag is not supported when invoking dbt in other runtimes (for example, the IDE or scheduled runs).](/reference/commands/version)