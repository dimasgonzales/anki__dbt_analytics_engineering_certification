# Source: https://docs.getdbt.com/docs/deploy/job-commands

Job commands | dbt Developer Hub

[Skip to main content](#__docusaurus_skipToContent_fallback)

[✨ Live virtual event - Smarter pipelines, 29% more efficient: How the dbt Fusion engine optimizes data work on December 3rd!](https://www.getdbt.com/resources/webinars/how-the-dbt-fusion-engine-optimizes-data-work)

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

* About
* [What is dbt?](/docs/introduction)
* [dbt Fusion engine](/docs/fusion)
* [About the dbt platform](/docs/cloud/about-cloud/dbt-cloud-features)
* [Supported data platforms](/docs/supported-data-platforms)
* Get started
* [Get started with dbt](/docs/get-started-dbt)
* [Set up dbt](/docs/about-setup)
* Build and develop
* [Develop with dbt](/docs/cloud/about-develop-dbt)
* [Build dbt projects](/docs/build/projects)
* [Build dbt Mesh](/docs/mesh/about-mesh)
* Deploy and explore
* [Deploy dbt](/docs/deploy/deployments)

  + [Deploy dbt](/docs/deploy/deployments)
  + [Job scheduler](/docs/deploy/job-scheduler)
  + [Deployment environments](/docs/deploy/deploy-environments)
  + [Continuous integration](/docs/deploy/about-ci)
  + [Continuous deployment](/docs/deploy/continuous-deployment)
  + [State aware](/docs/deploy/state-aware-about)
  + [Jobs](/docs/deploy/jobs)

    - [About jobs](/docs/deploy/jobs)
    - [Deploy jobs](/docs/deploy/deploy-jobs)
    - [CI jobs](/docs/deploy/ci-jobs)
    - [Merge jobs](/docs/deploy/merge-jobs)
    - [Job commands](/docs/deploy/job-commands)
  + [Monitor jobs and alerts](/docs/deploy/monitor-jobs)
  + [Hybrid projects](/docs/deploy/hybrid-projects)
  + [Integrate with other tools](/docs/deploy/deployment-tools)
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

* [Deploy dbt](/docs/deploy/deployments)
* [Jobs](/docs/deploy/jobs)
* Job commands

Copy page

On this page

Job commands
============

A dbt production job allows you to set up a system to run a dbt job and job commands on a schedule, rather than running dbt commands manually from the command line or [Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud). A job consists of commands that are "chained" together and executed as run steps. Each run step can succeed or fail, which may determine the job's run status (Success, Cancel, or Error).

Each job allows you to:

* Configure job commands
* View job run details, including timing, artifacts, and detailed run steps
* Access logs to view or help debug issues and historical invocations of dbt
* Set up notifications, and [more](/docs/deploy/deployments#dbt-cloud)

Job command types[​](#job-command-types "Direct link to Job command types")
---------------------------------------------------------------------------

Job commands are specific tasks executed by the job, and you can configure them seamlessly by either adding [dbt commands](/reference/dbt-commands) or using the checkbox option in the **Commands** section.

During a job run, the commands are "chained" together and executed as run steps. When you add a dbt command in the **Commands** section, you can expect different outcomes compared to the checkbox option.

[![Configuring checkbox and commands list](/img/docs/dbt-cloud/using-dbt-cloud/job-commands.gif?v=2 "Configuring checkbox and commands list")](#)Configuring checkbox and commands list

### Built-in commands[​](#built-in-commands "Direct link to Built-in commands")

Every job invocation automatically includes the [`dbt deps`](/reference/commands/deps) command, meaning you don't need to add it to the **Commands** list in your job settings. You will also notice every job will include a run step to reclone your repository and connect to your data platform, which can affect your job status if these run steps aren't successful.

**Job outcome** — During a job run, the built-in commands are "chained" together. This means if one of the run steps in the chain fails, then the next commands aren't executed, and the entire job fails with an "Error" job status.

[![A failed job that had an error during the dbt deps run step.](/img/docs/dbt-cloud/using-dbt-cloud/fail-dbtdeps.png?v=2 "A failed job that had an error during the dbt deps run step.")](#)A failed job that had an error during the dbt deps run step.

### Checkbox commands[​](#checkbox-commands "Direct link to Checkbox commands")

For every job, you have the option to select the [Generate docs on run](/docs/explore/build-and-view-your-docs) or [Run source freshness](/docs/deploy/source-freshness) checkboxes, enabling you to run the commands automatically.

**Job outcome Generate docs on run checkbox** — dbt executes the `dbt docs generate` command, *after* the listed commands. If that particular run step in your job fails, the job can still succeed if all subsequent run steps are successful. Read [Set up documentation job](/docs/explore/build-and-view-your-docs) for more info.

**Job outcome Source freshness checkbox** — dbt executes the `dbt source freshness` command as the first run step in your job. If that particular run step in your job fails, the job can still succeed if all subsequent run steps are successful. Read [Source freshness](/docs/deploy/source-freshness) for more info.

### Command list[​](#command-list "Direct link to Command list")

You can add or remove as many dbt commands as necessary for every job. However, you need to have at least one dbt command. There are few commands listed as "dbt CLI" or "dbt Core" in the [dbt Command reference page](/reference/dbt-commands) page. This means they are meant for use in dbt Core or dbt CLI, and not in Studio IDE.

Using selectors

Use [selectors](/reference/node-selection/syntax) as a powerful way to select and execute portions of your project in a job run. For example, to run tests for `one_specific_model`, use the selector: `dbt test --select one_specific_model`. The job will still run if a selector doesn't match any models.

#### Compare changes custom commands[​](#compare-changes-custom-commands "Direct link to Compare changes custom commands")

For users that have Advanced CI's [compare changes](/docs/deploy/advanced-ci#compare-changes) feature enabled and selected the **dbt compare** checkbox, you can add custom dbt commands to optimize running the comparison (for example, to exclude specific large models, or groups of models with tags). Running comparisons on large models can significantly increase the time it takes for CI jobs to complete.

[![Add custom dbt commands to when using dbt compare.](/img/docs/deploy/dbt-compare.jpg?v=2 "Add custom dbt commands to when using dbt compare.")](#)Add custom dbt commands to when using dbt compare.

The following examples highlight how you can customize the dbt compare command box:

* Exclude the large `fct_orders` model from the comparison to run a CI job on fewer or smaller models and reduce job time/resource consumption. Use the following command:

  ```
  --select state:modified --exclude fct_orders
  ```
* Exclude models based on tags for scenarios like when models share a common feature or function. Use the following command:

  ```
     --select state modified --exclude tag:tagname_a tag:tagname_b
  ```
* Include models that were directly modified and also those one step downstream using the `modified+1` selector. Use the following command:

  ```
  --select state:modified+1
  ```

#### Job outcome[​](#job-outcome "Direct link to Job outcome")

During a job run, the commands are "chained" together and executed as run steps. If one of the run steps in the chain fails, then the subsequent steps aren't executed, and the job will fail.

In the following example image, the first four run steps are successful. However, if the fifth run step (`dbt run --select state:modified+ --full-refresh --fail-fast`) fails, then the next run steps aren't executed, and the entire job fails. The failed job returns a non-zero [exit code](/reference/exit-codes) and "Error" job status:

[![A failed job run that had an error during a run step](/img/docs/dbt-cloud/using-dbt-cloud/skipped-jobs.png?v=2 "A failed job run that had an error during a run step")](#)A failed job run that had an error during a run step

Job command failures[​](#job-command-failures "Direct link to Job command failures")
------------------------------------------------------------------------------------

Job command failures can mean different things for different commands. Some common reasons why a job command may fail:

* **Failure at`dbt run`** — [`dbt run`](/reference/commands/run) executes compiled SQL model files against the current target database. It will fail if there is an error in any of the built models. Tests on upstream resources prevent downstream resources from running and a failed test will skip them.
* **Failure at `dbt test`** — [`dbt test`](/reference/commands/test) runs tests defined on models, sources, snapshots, and seeds. A test can pass, fail, or warn depending on its [severity](/reference/resource-configs/severity). Unless you set [warnings as errors](/reference/global-configs/warnings), only an error stops the next step.
* **Failure at `dbt build`** — [`dbt build`](/reference/commands/build) runs models, tests, snapshots, and seeds. This command executes resources in the DAG-specified order. If any upstream resource fails, all downstream resources are skipped, and the command exits with an error code of 1.
* **Selector failures**

  + If a [`select`](/reference/node-selection/set-operators) matches multiple nodes and one of the nodes fails, then the job will have an exit code `1` and the subsequent command will fail. If you specified the [`—fail-fast`](/reference/global-configs/failing-fast) flag, then the first failure will stop the entire connection for any models that are in progress.
  + If a selector doesn't match any nodes, it's not considered a failure.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Job creation best practices](https://discourse.getdbt.com/t/job-creation-best-practices-in-dbt-cloud-feat-my-moms-lasagna/2980)
* [dbt Command reference](/reference/dbt-commands)
* [Job notifications](/docs/deploy/job-notifications)
* [Source freshness](/docs/deploy/source-freshness)
* [Build and view your docs](/docs/explore/build-and-view-your-docs)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/deploy/job-commands.md)

Last updated on **Nov 19, 2025**

[Previous

Merge jobs](/docs/deploy/merge-jobs)[Next

Monitor jobs and alerts](/docs/deploy/monitor-jobs)

* [Job command types](#job-command-types)
  + [Built-in commands](#built-in-commands)
  + [Checkbox commands](#checkbox-commands)
  + [Command list](#command-list)
* [Job command failures](#job-command-failures)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/deploy/job-commands.md)

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




![dbt Labs](https://cdn.cookielaw.org/logos/4a2cde9e-5f84-44b2-bdbb-6a93354d1c72/e1199e19-1935-49fa-a4e2-bf7f9d08cee6/783d7c83-af8c-4032-901b-b3ec48982078/dbt-logo.png)

Privacy Preference Center
-------------------------

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.
  
[More information](https://www.getdbt.com/cloud/privacy-policy/)

Allow All

### Manage Consent Preferences

#### Strictly Necessary Cookies

Always Active

Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.

#### Performance Cookies

Always Active

Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.

#### Targeting Cookies

Always Active

Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Always Active

Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox label label

Apply Cancel

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

Confirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg "Powered by OneTrust Opens in a new Tab")](https://www.onetrust.com/products/cookie-consent/)