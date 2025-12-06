# Source: https://docs.getdbt.com/docs/build/projects

About dbt projects | dbt Developer Hub

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

  + [About dbt projects](/docs/build/projects)
  + [dbt tips and tricks](/docs/build/dbt-tips)
  + [Build your DAG](/docs/build/models)
  + [Build your metrics](/docs/build/build-metrics-intro)
  + [Enhance your models](/docs/build/enhance-your-models)
  + [Enhance your code](/docs/build/enhance-your-code)
  + [Organize your outputs](/docs/build/organize-your-outputs)
  + [Optimize development](/docs/build/empty-flag)
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

* Build dbt projects

Copy page

On this page

About dbt projects
==================

A dbt project informs dbt about the context of your project and how to transform your data (build your data sets). By design, dbt enforces the top-level structure of a dbt project such as the `dbt_project.yml` file, the `models` directory, the `snapshots` directory, and so on. Within the directories of the top-level, you can organize your project in any way that meets the needs of your organization and data pipeline.

At a minimum, all a project needs is the `dbt_project.yml` project configuration file. dbt supports a number of different resources, so a project may also include:

| Resource | Description |
| --- | --- |
| [models](/docs/build/models) | Each model lives in a single file and contains logic that either transforms raw data into a dataset that is ready for analytics or, more often, is an intermediate step in such a transformation. |
| [snapshots](/docs/build/snapshots) | A way to capture the state of your mutable tables so you can refer to it later. |
| [seeds](/docs/build/seeds) | CSV files with static data that you can load into your data platform with dbt. |
| [data tests](/docs/build/data-tests) | SQL queries that you can write to test the models and resources in your project. |
| [macros](/docs/build/jinja-macros) | Blocks of code that you can reuse multiple times. |
| [docs](/docs/build/documentation) | Docs for your project that you can build. |
| [sources](/docs/build/sources) | A way to name and describe the data loaded into your warehouse by your Extract and Load tools. |
| [exposures](/docs/build/exposures) | A way to define and describe a downstream use of your project. |
| [metrics](/docs/build/build-metrics-intro) | A way for you to define metrics for your project. |
| [groups](/docs/build/groups) | Groups enable collaborative node organization in restricted collections. |
| [analysis](/docs/build/analyses) | A way to organize analytical SQL queries in your project such as the general ledger from your QuickBooks. |
| [semantic models](/docs/build/semantic-models) | Semantic models define the foundational data relationships in [MetricFlow](/docs/build/about-metricflow) and the [Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl), enabling you to query metrics using a semantic graph. |
| [saved queries](/docs/build/saved-queries) | Saved queries organize reusable queries by grouping metrics, dimensions, and filters into nodes visible in the dbt DAG. |
| [user-defined functions](/docs/build/udfs) | User-defined functions (UDFs) let you create reusable custom functions in your warehouse, shareable across dbt, BI tools, data science workflows, and more. |

When building out the structure of your project, you should consider these impacts on your organization's workflow:

* **How would people run dbt commands** — Selecting a path
* **How would people navigate within the project** — Whether as developers in the Studio IDE or stakeholders from the docs
* **How would people configure the models** — Some bulk configurations are easier done at the directory level so people don’t have to remember to do everything in a config block with each new model

Project configuration[​](#project-configuration "Direct link to Project configuration")
---------------------------------------------------------------------------------------

Every dbt project includes a project configuration file called `dbt_project.yml`. It defines the directory of the dbt project and other project configurations.

Edit `dbt_project.yml` to set up common project configurations such as:

| YAML key | Value description |
| --- | --- |
| [name](/reference/project-configs/name) | Your project’s name in [snake case](https://en.wikipedia.org/wiki/Snake_case) |
| [version](/reference/project-configs/version) | Version of your project |
| [require-dbt-version](/reference/project-configs/require-dbt-version) | Restrict your project to only work with a range of [dbt Core versions](/docs/dbt-versions/core) |
| [profile](/reference/project-configs/profile) | The profile dbt uses to connect to your data platform |
| [model-paths](/reference/project-configs/model-paths) | Directories to where your model and source files live |
| [seed-paths](/reference/project-configs/seed-paths) | Directories to where your seed files live |
| [test-paths](/reference/project-configs/test-paths) | Directories to where your test files live |
| [analysis-paths](/reference/project-configs/analysis-paths) | Directories to where your analyses live |
| [macro-paths](/reference/project-configs/macro-paths) | Directories to where your macros live |
| [snapshot-paths](/reference/project-configs/snapshot-paths) | Directories to where your snapshots live |
| [docs-paths](/reference/project-configs/docs-paths) | Directories to where your docs blocks live |
| [vars](/docs/build/project-variables) | Project variables you want to use for data compilation |

For complete details on project configurations, see [dbt\_project.yml](/reference/dbt_project.yml).

Project subdirectories[​](#project-subdirectories "Direct link to Project subdirectories")
------------------------------------------------------------------------------------------

You can use the Project subdirectory option in dbt to specify a subdirectory in your git repository that dbt should use as the root directory for your project. This is helpful when you have multiple dbt projects in one repository or when you want to organize your dbt project files into subdirectories for easier management.

To use the Project subdirectory option in dbt, follow these steps:

1. Click your account name in the bottom left and select **Your profile**.
2. Under **Projects**, select the project you want to configure as a project subdirectory.
3. Select **Edit** on the lower right-hand corner of the page.
4. In the **Project subdirectory** field, add the name of the subdirectory. For example, if your dbt project files are located in a subdirectory called `<repository>/finance`, you would enter `finance` as the subdirectory.

   * You can also reference nested subdirectories. For example, if your dbt project files are located in `<repository>/teams/finance`, you would enter `teams/finance` as the subdirectory. **Note**: You do not need a leading or trailing `/` in the Project subdirectory field.
5. Click **Save** when you've finished.

After configuring the Project subdirectory option, dbt will use it as the root directory for your dbt project. This means that dbt commands, such as `dbt run` or `dbt test`, will operate on files within the specified subdirectory. If there is no `dbt_project.yml` file in the Project subdirectory, you will be prompted to initialize the dbt project.

Project support in dbt plans

Some [plans](https://www.getdbt.com/pricing) support only one dbt project, while [Enterprise-tier plans](https://www.getdbt.com/contact) allow multiple projects and [cross-project references](/best-practices/how-we-mesh/mesh-1-intro) with Mesh.

New projects[​](#new-projects "Direct link to New projects")
------------------------------------------------------------

You can create new projects and [share them](/docs/cloud/git/git-version-control) with other people by making them available on a hosted git repository like GitHub, GitLab, and BitBucket.

After you set up a connection with your data platform, you can [initialize your new project in dbt](/guides) and start developing. Or, run [dbt init from the command line](/reference/commands/init) to set up your new project.

During project initialization, dbt creates sample model files in your project directory to help you start developing quickly.

Sample projects[​](#sample-projects "Direct link to Sample projects")
---------------------------------------------------------------------

If you want to explore dbt projects more in-depth, you can clone dbt Lab’s [Jaffle shop](https://github.com/dbt-labs/jaffle_shop) on GitHub. It's a runnable project that contains sample configurations and helpful notes.

If you want to see what a mature, production project looks like, check out the [GitLab Data Team public repo](https://gitlab.com/gitlab-data/analytics/-/tree/master/transform/snowflake-dbt).

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Best practices: How we structure our dbt projects](/best-practices/how-we-structure/1-guide-overview)
* [Quickstarts for dbt](/guides)
* [Quickstart for dbt Core](/guides/manual-install)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/projects.md)

Last updated on **Nov 19, 2025**

* [Project configuration](#project-configuration)
* [Project subdirectories](#project-subdirectories)
* [New projects](#new-projects)
* [Sample projects](#sample-projects)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/projects.md)

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