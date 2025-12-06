# Source: https://docs.getdbt.com/docs/cloud/git/version-control-basics

Version control basics | dbt Developer Hub

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

* About
* [What is dbt?](/docs/introduction)
* [dbt Fusion engine](/docs/fusion)
* [About the dbt platform](/docs/cloud/about-cloud/dbt-cloud-features)
* [Supported data platforms](/docs/supported-data-platforms)
* Get started
* [Get started with dbt](/docs/get-started-dbt)
* [Set up dbt](/docs/about-setup)

  + [About dbt setup](/docs/about-setup)
  + [About environments](/docs/environments-in-dbt)
  + [dbt platform](/docs/cloud/about-cloud-setup)

    - [About dbt setup](/docs/cloud/about-cloud-setup)
    - [Account settings](/docs/cloud/account-settings)
    - [Account integrations](/docs/cloud/account-integrations)
    - [dbt environments](/docs/dbt-cloud-environments)
    - [Multi-cell migration checklist](/docs/cloud/migration)
    - [Connect your data platforms](/docs/cloud/connect-data-platform/about-connections)
    - [Manage access](/docs/cloud/manage-access/about-user-access)
    - [Configure Git](/docs/cloud/git/git-configuration-in-dbt-cloud)

      * [Configure Git in dbt](/docs/cloud/git/git-configuration-in-dbt-cloud)
      * [Connect with managed repository](/docs/cloud/git/managed-repository)
      * [Connect with Git clone](/docs/cloud/git/import-a-project-by-git-url)
      * [Connect to GitHub](/docs/cloud/git/connect-github)
      * [Connect to GitLab](/docs/cloud/git/connect-gitlab)
      * [Azure DevOps](/docs/cloud/git/connect-azure-devops)
      * [Git version control](/docs/cloud/git/git-version-control)

        + [About git](/docs/cloud/git/git-version-control)
        + [Version control basics](/docs/cloud/git/version-control-basics)
        + [PR template](/docs/cloud/git/pr-template)
        + [Merge conflicts](/docs/cloud/git/merge-conflicts)
    - [Secure your tenant](/docs/cloud/secure/secure-your-tenant)
  + [dbt Core and Fusion](/docs/about-dbt-install)
  + [Run your dbt projects](/docs/running-a-dbt-project/run-your-dbt-projects)
  + [Use threads](/docs/running-a-dbt-project/using-threads)
* Build and develop
* [Develop with dbt](/docs/cloud/about-develop-dbt)
* [Build dbt projects](/docs/build/projects)
* [Build dbt Mesh](/docs/mesh/about-mesh)
* Deploy and explore
* [Deploy dbt](/docs/deploy/deployments)
* [Explore your data](/docs/explore/explore-your-data)
* [Use the dbt Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl)
* dbt AI
* [Copilot](/docs/cloud/dbt-copilot)
* [dbt MCP](/docs/dbt-ai/about-mcp)
* Additional tools
* [dbt integrations](/docs/cloud-integrations/overview)
* [Cost management](/docs/cloud/cost-management)
* Release information
* [Available dbt versions](/docs/dbt-versions/about-versions)
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [Set up dbt](/docs/about-setup)
* [dbt platform](/docs/cloud/about-cloud-setup)
* [Configure Git](/docs/cloud/git/git-configuration-in-dbt-cloud)
* [Git version control](/docs/cloud/git/git-version-control)
* Version control basics

Copy page

On this page

Version control basics
======================

When you develop in the command line interface (CLI) or Cloud integrated development environment (Studio IDE), you can leverage Git directly to version control your code. To use version control, make sure you are connected to a Git repository in the CLI or Studio IDE.

You can create a separate branch to develop and make changes. The changes you make aren’t merged into the default branch in your connected repository (typically named the `main` branch) unless it successfully passes tests. This helps keep the code organized and improves productivity by making the development process smooth.

You can read more about git terminology below and also check out [GitHub Docs](https://docs.github.com/en) as well.

Git overview[​](#git-overview "Direct link to Git overview")
------------------------------------------------------------

Check out some common git terms below that you might encounter when developing:

| Name | Definition |
| --- | --- |
| Repository or repo | A repository is a directory that stores all the files, folders, and content needed for your project. You can think of this as an object database of the project, storing everything from the files themselves to the versions of those files, commits, and deletions. Repositories are not limited by user and can be shared and copied. |
| Branch | A branch is a parallel version of a repository. It is contained within the repository but does not affect the primary or main branch allowing you to work freely without disrupting the live version. When you've made the changes you want to make, you can merge your branch back into the main branch to publish your changes |
| Checkout | The `checkout` command is used to create a new branch, change your current working branch to a different branch, or switch to a different version of a file from a different branch. |
| Commit | A commit is a user’s change to a file (or set of files). When you make a commit to save your work, Git creates a unique ID that allows you to keep a record of the specific changes committed along with who made them and when. Commits usually contain a commit message which is a brief description of what changes were made. |
| main | The primary, base branch of all repositories. All committed and accepted changes should be on the main branch.   In the Studio IDE, the main branch is protected. This means you can't directly edit, format, or lint files and execute dbt commands in your protected primary git branch. Since the Studio IDE prevents commits to the protected branch, you can commit those changes to a new branch. |
| Merge | Merge takes the changes from one branch and adds them into another (usually main) branch. These commits are usually first requested via pull request before being merged by a maintainer. |
| Pull Request | If someone has changed code on a separate branch of a project and wants it to be reviewed to add to the main branch, they can submit a pull request. Pull requests ask the repo maintainers to review the commits made, and then, if acceptable, merge the changes upstream. A pull happens when adding the changes to the main branch. |
| Push | A `push` updates a remote branch with the commits made to the current branch. You are literally *pushing* your changes into the remote. |
| Remote | This is the version of a repository or branch that is hosted on a server. Remote versions can be connected to local clones so that changes can be synced. |

The git button in the Cloud IDE[​](#the-git-button-in-the-cloud-ide "Direct link to The git button in the Cloud IDE")
---------------------------------------------------------------------------------------------------------------------

You can perform git tasks with the git button in the [Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud). The following are descriptions of each git button command and what they do:

| Name | Actions |
| --- | --- |
| Abort merge | This option allows you to cancel a merge that had conflicts. Be careful with this action because all changes will be reset and this operation can't be reverted, so make sure to commit or save all your changes before you start a merge. |
| Change branch | This option allows you to change between branches (checkout). |
| Commit | A commit is an individual change to a file (or set of files). When you make a commit to save your work, Git creates a unique ID (a.k.a. the "SHA" or "hash") that allows you to keep record of the specific changes committed along with who made them and when. Commits usually contain a commit message which is a brief description of what changes were made. When you make changes to your code in the future, you'll need to commit them as well. |
| Create new branch | This allows you to branch off of your base branch and edit your project. You’ll notice after initializing your project that the main branch is protected.   This means you can directly edit, format, or lint files and execute dbt commands in your protected primary git branch. When ready, you can commit those changes to a new branch. |
| Initialize your project | This is done when first setting up your project. Initializing a project creates all required directories and files within an empty repository by using the dbt starter project.   Note: This option will not display if your repo isn't completely empty (i.e. includes a README file).   Once you click **Initialize your project**, click **Commit** to finish setting up your project. |
| Open pull request | This allows you to open a pull request in Git for peers to review changes before merging into the base branch. |
| Pull changes from main | This option is available if you are on any local branch that is behind the remote version of the base branch or the remote version of the branch that you're currently on. |
| Pull from remote | This option is available if you’re on the local base branch and changes have recently been pushed to the remote version of the branch. Pulling in changes from the remote repo allows you to pull in the most recent version of the base branch. |
| Rollback to remote | Reset changes to your repository directly from the Studio IDE. You can rollback your repository back to an earlier clone from your remote. To do this, click on the three dot ellipsis in the bottom right-hand side of the Studio IDE and select **Rollback to remote**. |
| Refresh git state | This enables you to pull new branches from a different remote branch to your local branch with just one command. |

Merge conflicts[​](#merge-conflicts "Direct link to Merge conflicts")
---------------------------------------------------------------------

Merge conflicts often occur when multiple users are concurrently making edits to the same section in the same file. This makes it difficult for Git to determine which change should be kept.

Refer to [merge conflicts](/docs/cloud/git/merge-conflicts) to learn how to resolve merge conflicts.

The .gitignore file[​](#the-gitignore-file "Direct link to The .gitignore file")
--------------------------------------------------------------------------------

dbt implements a global [`.gitignore file`](https://github.com/dbt-labs/dbt-starter-project/blob/main/.gitignore) that automatically excludes the following sub-folders from your git repository to ensure smooth operation:

```
dbt_packages/  
logs/  
target/
```

This inclusion uses a trailing slash, making these lines in the `.gitignore` file act as 'folder wildcards' that prevent any files or folders within them from being tracked by git. You can also specify additional exclusions as needed for your project.

However, this global `.gitignore` *does not* apply to dbt Core and Cloud CLI users directly. Therefore, if you're working with dbt Core or Cloud CLI, you need to manually add the three lines mentioned previously to your project's `.gitignore` file.

It's worth noting that while some git providers generate a basic `.gitignore` file when the repository is created, these often lack the necessary exclusions for dbt. This means it's important to ensure you add the three lines mentioned previously in your `.gitignore` to ensure dbt operates smoothly.

note

* **dbt projects created after Dec 1, 2022** — If you use the **Initialize dbt Project** button in the Studio IDE to set up a new and empty dbt project, dbt will automatically add a `.gitignore` file with the required entries. If a `.gitignore` file already exists, the necessary folders will be appended to the existing file.
* **Migrating project from dbt Core to dbt** — Make sure you check the `.gitignore` file contains the necessary entries. dbt Core doesn't interact with git so dbt doesn't automatically add or verify entries in the `.gitignore` file. Additionally, if the repository already contains dbt code and doesn't require initialization, dbt won't add any missing entries to the .gitignore file.

For additional info or troubleshooting tips please refer to the [detailed FAQ](/faqs/Git/gitignore).

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud/git/version-control-basics.md)

Last updated on **Nov 19, 2025**

[Previous

About git](/docs/cloud/git/git-version-control)[Next

PR template](/docs/cloud/git/pr-template)

* [Git overview](#git-overview)
* [The git button in the Cloud IDE](#the-git-button-in-the-cloud-ide)
* [Merge conflicts](#merge-conflicts)
* [The .gitignore file](#the-gitignore-file)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud/git/version-control-basics.md)

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