Copy page

On this page

About the Studio IDE
====================

The dbt integrated development environment (Studio IDE) is a single web-based interface for building, testing, running, and version-controlling dbt projects. It compiles dbt code into SQL and executes it directly on your database.

The Studio IDE offers several [keyboard shortcuts](/docs/cloud/dbt-cloud-ide/keyboard-shortcuts) and [editing features](/docs/cloud/dbt-cloud-ide/ide-user-interface#editing-features) for faster and efficient development and governance:

* Syntax highlighting for SQL — Makes it easy to distinguish different parts of your code, reducing syntax errors and enhancing readability.
* AI copilot — Use [Copilot](/docs/cloud/dbt-copilot), an AI-powered assistant that can [generate code](/docs/cloud/dbt-cloud-ide/develop-copilot#generate-and-edit-code) using natural language, and [generate resources](/docs/cloud/dbt-cloud-ide/develop-copilot#generate-resources) (like documentation, tests, and semantic models) for you — with the click of a button. Check out [Develop with Copilot](/docs/cloud/dbt-cloud-ide/develop-copilot) for more details.
* Auto-completion — Suggests table names, arguments, and column names as you type, saving time and reducing typos.
* Code [formatting and linting](/docs/cloud/dbt-cloud-ide/lint-format) — Helps standardize and fix your SQL code effortlessly.
* Navigation tools — Easily move around your code, jump to specific lines, find and replace text, and navigate between project files.
* Version control — Manage code versions with a few clicks.
* Project documentation — Generate and view your [project documentation](#build-and-document-your-projects) for your dbt project in real-time.
* Build, test, and run button — Build, test, and run your project with a button click or by using the Studio IDE command bar.

These [features](#dbt-cloud-ide-features) create a powerful editing environment for efficient SQL coding, suitable for both experienced and beginner developers.

[![The Studio IDE includes version control, files/folders, an editor, a command/console, and more.](/img/docs/dbt-cloud/cloud-ide/ide-basic-layout.png?v=2 "The Studio IDE includes version control, files/folders, an editor, a command/console, and more.")](#)The Studio IDE includes version control, files/folders, an editor, a command/console, and more.

[![Enable dark mode for a great viewing experience in low-light environments.](/img/docs/dbt-cloud/cloud-ide/cloud-ide-v2.png?v=2 "Enable dark mode for a great viewing experience in low-light environments.")](#)Enable dark mode for a great viewing experience in low-light environments.

Disable ad blockers

To improve your experience using dbt, we suggest that you turn off ad blockers. This is because some project file names, such as `google_adwords.sql`, might resemble ad traffic and trigger ad blockers.

Prerequisites[​](#prerequisites "Direct link to Prerequisites")
---------------------------------------------------------------

* A [dbt account](https://www.getdbt.com/signup) and [Developer seat license](/docs/cloud/manage-access/seats-and-users)
* A git repository set up and git provider must have `write` access enabled. See [Connecting your GitHub Account](/docs/cloud/git/connect-github) or [Importing a project by git URL](/docs/cloud/git/import-a-project-by-git-url) for detailed setup instructions
* A dbt project connected to a [data platform](/docs/cloud/connect-data-platform/about-connections)
* A [development environment and development credentials](#get-started-with-the-cloud-ide) set up
* The environment must be on dbt version 1.0 or higher

Studio IDE features[​](#studio-ide-features "Direct link to Studio IDE features")
---------------------------------------------------------------------------------

The Studio IDE comes with features that make it easier for you to develop, build, compile, run, and test data models.

To understand how to navigate the Studio IDE and its user interface elements, refer to the [Studio IDE user interface](/docs/cloud/dbt-cloud-ide/ide-user-interface) page.

| Feature | Description |
| --- | --- |
| [**Studio IDE shortcuts**](/docs/cloud/dbt-cloud-ide/keyboard-shortcuts) | You can access a variety of [commands and actions](/docs/cloud/dbt-cloud-ide/keyboard-shortcuts) in the Studio IDE by choosing the appropriate keyboard shortcut. Use the shortcuts for common tasks like building modified models or resuming builds from the last failure. |
| **IDE version control** | The Studio IDE version control section and git button allow you to apply the concept of [version control](/docs/cloud/git/version-control-basics) to your project directly into the Studio IDE.    - Create or change branches, execute git commands using the git button.  - Commit or revert individual files by right-clicking the edited file  - [Resolve merge conflicts](/docs/cloud/git/merge-conflicts)  - Link to the repo directly by clicking the branch name   - Edit, format, or lint files and execute dbt commands in your primary protected branch, and commit to a new branch.  - Use Git diff view to view what has been changed in a file before you make a pull request.  - Use the **Prune branches** [button](/docs/cloud/dbt-cloud-ide/ide-user-interface#prune-branches-modal) to delete local branches that have been deleted from the remote repository, keeping your branch management tidy.  - Sign your [git commits](/docs/cloud/dbt-cloud-ide/git-commit-signing) to mark them as 'Verified'. [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing") |
| **Preview and Compile button** | You can [compile or preview](/docs/cloud/dbt-cloud-ide/ide-user-interface#console-section) code, a snippet of dbt code, or one of your dbt models after editing and saving. |
| [**Copilot**](/docs/cloud/dbt-cloud-ide/develop-copilot) | A powerful AI-powered assistant that can [generate code](/docs/cloud/dbt-cloud-ide/develop-copilot#generate-and-edit-code) using natural language, and [generate resources](/docs/cloud/dbt-cloud-ide/develop-copilot#generate-resources) (like documentation, tests, metrics, and semantic models) for you — with the click of a button. [Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing"). |
| **Build, test, and run button** | Build, test, and run your project with the click of a button or by using the command bar. |
| **Command bar** | You can enter and run commands from the command bar at the bottom of the Studio IDE. Use the [rich model selection syntax](/reference/node-selection/syntax) to execute [dbt commands](/reference/dbt-commands) directly within dbt. You can also view the history, status, and logs of previous runs by clicking History on the left of the bar. |
| **Drag and drop** | Drag and drop files located in the file explorer, and use the file breadcrumb on the top of the Studio IDE for quick, linear navigation. Access adjacent files in the same file by right-clicking on the breadcrumb file. |
| **Organize tabs and files** | - Move your tabs around to reorganize your work in the IDE   - Right-click on a tab to view and select a list of actions, including duplicate files   - Close multiple, unsaved tabs to batch save your work   - Double click files to rename files |
| **Find and replace** | - Press Command-F or Control-F to open the find-and-replace bar in the upper right corner of the current file in the IDE. The IDE highlights your search results in the current file and code outline  - You can use the up and down arrows to see the match highlighted in the current file when there are multiple matches  - Use the left arrow to replace the text with something else |
| **Multiple selections** | You can make multiple selections for small and simultaneous edits. The below commands are a common way to add more cursors and allow you to insert cursors below or above with ease.   - Option-Command-Down arrow or Ctrl-Alt-Down arrow  - Option-Command-Up arrow or Ctrl-Alt-Up arrow  - Press Option and click on an area or Press Ctrl-Alt and click on an area |
| **Lint and Format** | [Lint and format](/docs/cloud/dbt-cloud-ide/lint-format) your files with a click of a button, powered by SQLFluff, sqlfmt, Prettier, and Black. |
| **dbt autocomplete** | Autocomplete features to help you develop faster:   - Use `ref` to autocomplete your model names  - Use `source` to autocomplete your source name + table name  - Use `macro` to autocomplete your arguments  - Use `env var` to autocomplete env var  - Start typing a hyphen (-) to use in-line autocomplete in a YAML file  - Automatically create models from dbt sources with a click of a button. |
| **DAGA DAG is a Directed Acyclic Graph, a type of graph whose nodes are directionally related to each other and don’t form a directional closed loop. in the IDE** | You can see how models are used as building blocks from left to right to transform your data from raw sources into cleaned-up modular derived pieces and final outputs on the far right of the DAG. The default view is 2+model+2 (defaults to display 2 nodes away), however, you can change it to +model+ (full DAGA DAG is a Directed Acyclic Graph, a type of graph whose nodes are directionally related to each other and don’t form a directional closed loop.). Note the `--exclude` flag isn't supported. |
| **Status bar** | This area provides you with useful information about your Studio IDE and project status. You also have additional options like enabling light or dark mode, restarting the Studio IDE, or [recloning your repo](/docs/cloud/git/version-control-basics). |
| **Dark mode** | From the status bar in the Studio IDE, enable dark mode for a great viewing experience in low-light environments. |

### Code generation[​](#code-generation "Direct link to Code generation")

The Studio IDE comes with **CodeGenCodeLens**, a powerful feature that simplifies creating models from your sources with a click of a button. To use this feature, click on the **Generate model** action next to each table in the source YAML file(s). It automatically creates a basic starting staging model for you to expand on. This feature helps streamline your workflow by automating the first steps of model generation.

### dbt YAML validation[​](#dbt-yaml-validation "Direct link to dbt YAML validation")

Use dbt-jsonschema to validate dbt YAML files, helping you leverage the autocomplete and assistance capabilities of the Studio IDE. This also provides immediate feedback on YAML file structure and syntax, helping you make sure your project configurations meet the required standards.