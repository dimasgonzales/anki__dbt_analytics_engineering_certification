Copy page

On this page

Run your dbt projects
=====================

You can run your dbt projects with [dbt](/docs/cloud/about-cloud/dbt-cloud-features) or [dbt Core](https://github.com/dbt-labs/dbt-core):

* **dbt**: A hosted application where you can develop directly from a web browser using the [Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud). It also natively supports developing using a command line interface, [dbt CLI](/docs/cloud/cloud-cli-installation). Among other features, dbt provides:

  + Development environment to help you build, test, run, and [version control](/docs/cloud/git/git-version-control) your project faster.
  + Share your [dbt project's documentation](/docs/build/documentation) with your team.
  + Integrates with the Studio IDE, allowing you to run development tasks and environment in the dbt UI for a seamless experience.
  + The dbt CLI to develop and run dbt commands against your dbt development environment from your local command line.
  + For more details, refer to [Develop dbt](/docs/cloud/about-develop-dbt).
* **dbt Core**: An open source project where you can develop from the [command line](/docs/core/installation-overview).

The dbt CLI and dbt Core are both command line tools that enable you to run dbt commands. The key distinction is the dbt CLI is tailored for dbt's infrastructure and integrates with all its [features](/docs/cloud/about-cloud/dbt-cloud-features).

The command line is available from your computer's terminal application such as Terminal and iTerm. With the command line, you can run commands and do other work from the current working directory on your computer. Before running the dbt project from the command line, make sure you are working in your dbt project directory. Learning terminal commands such as `cd` (change directory), `ls` (list directory contents), and `pwd` (present working directory) can help you navigate the directory structure on your system.

In dbt or dbt Core, the commands you commonly use are:

For information on all dbt commands and their arguments (flags), see the [dbt command reference](/reference/dbt-commands). If you want to list all dbt commands from the command line, run `dbt --help`. To list a dbt command’s specific arguments, run `dbt COMMAND_NAME --help` .

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------