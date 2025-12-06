# Source: https://docs.getdbt.com/docs/introduction

What is dbt? | dbt Developer Hub

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

* What is dbt?

Copy page

On this page

What is dbt?
============

dbt is the industry standard for data transformation. Learn how it can help you transform data and deploy analytics code following software engineering best practices like version control, modularity, portability, CI/CD, and documentation.

dbt is a transformation workflow that helps you get more work done while producing higher quality results. You can use dbt to modularize and centralize your analytics code, while also providing your data team with guardrails typically found in software engineering workflows. Collaborate on data models, version them, and test and document your queries before safely deploying them to production, with monitoring and visibility.

dbt compiles and runs your analytics code against your data platform, enabling you and your team to collaborate on a single source of truth for metrics, insights, and business definitions. This single source of truth, combined with the ability to define tests for your data, reduces errors when logic changes, and alerts you when issues arise.

[![dbt works alongside your ingestion, visualization, and other data tools, so you can transform data directly in your cloud data platform.](/img/docs/cloud-overview.jpg?v=2 "dbt works alongside your ingestion, visualization, and other data tools, so you can transform data directly in your cloud data platform.")](#)dbt works alongside your ingestion, visualization, and other data tools, so you can transform data directly in your cloud data platform.

Read more about why we want to enable analysts to work more like software engineers in [The dbt Viewpoint](/community/resources/viewpoint). Learn how other data practitioners around the world are using dbt by [joining the dbt Community](https://www.getdbt.com/community/join-the-community).

dbt[​](#dbt "Direct link to dbt")
---------------------------------

Use dbt to quickly and collaboratively transform data and deploy analytics code following software engineering best practices like version control, modularity, portability, CI/CD, and documentation. This means anyone on the data team comfortable with SQL can safely contribute to production-grade data pipelines.

### The dbt platform (formerly dbt Cloud)[​](#the-dbt-platform-formerly-dbt-cloud "Direct link to The dbt platform (formerly dbt Cloud)")

The dbt platform offers the fastest, most reliable, and scalable way to deploy dbt. Allowing data teams to optimize their data transformation by developing, testing, scheduling, and investigating data models using a single, fully managed service through a web-based user interface (UI).

You can learn about plans and pricing on [www.getdbt.com](https://www.getdbt.com/pricing/). Learn more about the [dbt platform features](/docs/cloud/about-cloud/dbt-cloud-features) and try one of the [dbt quickstarts](/docs/get-started-dbt).

### The dbt Fusion engine[​](#the-dbt-fusion-engine "Direct link to The dbt Fusion engine")

The dbt Fusion Engine is the next-generation dbt engine, designed to deliver data teams a lightning-fast development experience, intelligent cost savings, and improved governance.

For more information, refer to [the dbt Fusion Engine](/docs/fusion), [supported features](/docs/fusion/supported-features), and the [installation instructions](/docs/fusion/install-fusion) pages.

### dbt Core[​](#dbt-core "Direct link to dbt Core")

[dbt Core](/docs/about-setup) is an open-source tool that enables data practitioners to transform data and is suitable for users who prefer to manually set up dbt and locally maintain it. You can [install dbt Core](/docs/core/installation-overview) through the command line. Learn more with the [quickstart for dbt Core](/guides/duckdb?step=1).

dbt optimizes your workflow[​](#dbt-optimizes-your-workflow "Direct link to dbt optimizes your workflow")
---------------------------------------------------------------------------------------------------------

* Avoid writing boilerplate DML and DDL by managing transactions, dropping tables, and managing schema changes. Write business logic with just a SQL `select` statement, or a Python DataFrame, that returns the dataset you need, and dbt takes care of materialization.
* Build up reusable, or modular, data models that can be referenced in subsequent work instead of starting at the raw data with every analysis.
* Dramatically reduce the time your queries take to run: Leverage metadata to find long-running models that you want to optimize and use [incremental models](/docs/build/incremental-models) which dbt makes easy to configure and use.
* Write DRYer code by leveraging [macros](/docs/build/jinja-macros), [hooks](/docs/build/hooks-operations), and [package management](/docs/build/packages).

dbt provides more reliable analysis[​](#dbt-provides-more-reliable-analysis "Direct link to dbt provides more reliable analysis")
---------------------------------------------------------------------------------------------------------------------------------

* No longer copy and paste SQL, which can lead to errors when logic changes. Instead, build reusable data models that get pulled into subsequent models and analysis. Change a model once and that change will propagate to all its dependencies.
* Publish the canonical version of a particular data model, encapsulating all complex business logic. All analysis on top of this model will incorporate the same business logic without needing to reimplement it.
* Use mature source control processes like branching, pull requests, and code reviews.
* Write data quality tests quickly and easily on the underlying data. Many analytic errors are caused by edge cases in the data: testing helps analysts find and handle those edge cases.

The power of dbt[​](#the-power-of-dbt "Direct link to The power of dbt")
------------------------------------------------------------------------

As a dbt user, your main focus will be on writing models (select queries) that reflect core business logic – there’s no need to write boilerplate code to create tables and views, or to define the order of execution of your models. Instead, dbt handles turning these models into objects in your warehouse for you.

| Feature | Description |
| --- | --- |
| Handle boilerplate code to materialize queries as relations | For each model you create, you can easily configure a *materialization*. A materialization represents a build strategy for your select query – the code behind a materialization is robust, boilerplate SQL that wraps your select query in a statement to create a new, or update an existing, relation. Read more about [Materializations](/docs/build/materializations). |
| Use a code compiler | SQL files can contain Jinja, a lightweight templating language. Using Jinja in SQL provides a way to use control structures in your queries. For example, `if` statements and `for` loops. It also enables repeated SQL to be shared through `macros`. Read more about [Macros](/docs/build/jinja-macros). |
| Determine the order of model execution | Often, when transforming data, it makes sense to do so in a staged approach. dbt provides a mechanism to implement transformations in stages through the [ref function](/reference/dbt-jinja-functions/ref). Rather than selecting from existing tables and views in your warehouse, you can select from another model. |
| Document your dbt project | In the dbt platform, you can auto-generate the documentation when your dbt project runs. dbt provides a mechanism to write, version-control, and share documentation for your dbt models. You can write descriptions (in plain text or markdown) for each model and field. Read more about the [Documentation](/docs/build/documentation). |
| Test your models | Tests provide a way to improve the integrity of the SQL in each model by making assertions about the results generated by a model. Build, test, and run your project with a button click or by using the [Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud) command bar. Read more about writing tests for your models [Testing](/docs/build/data-tests) |
| Manage packages | dbt ships with a package manager, which allows analysts to use and publish both public and private repositories of dbt code which can then be referenced by others. Read more about [Package Management](/docs/build/packages). |
| Load seed files | Often in analytics, raw values need to be mapped to a more readable value (for example, converting a country-code to a country name) or enriched with static or infrequently changing data. These data sources, known as seed files, can be saved as a CSV file in your `project` and loaded into your data warehouse using the `seed` command. Read more about [Seeds](/docs/build/seeds). |
| Snapshot data | Often, records in a data source are mutable, in that they change over time. This can be difficult to handle in analytics if you want to reconstruct historic values. dbt provides a mechanism to snapshot raw data for a point in time, through use of [snapshots](/docs/build/snapshots). |

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Quickstarts for dbt](/guides)
* [Best practice guides](/best-practices)
* [What is a dbt Project?](/docs/build/projects)
* [dbt run](/docs/running-a-dbt-project/run-your-dbt-projects)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/introduction.md)

Last updated on **Nov 19, 2025**

* [dbt](#dbt)
  + [The dbt platform (formerly dbt Cloud)](#the-dbt-platform-formerly-dbt-cloud)
  + [The dbt Fusion engine](#the-dbt-fusion-engine)
  + [dbt Core](#dbt-core)
* [dbt optimizes your workflow](#dbt-optimizes-your-workflow)
* [dbt provides more reliable analysis](#dbt-provides-more-reliable-analysis)
* [The power of dbt](#the-power-of-dbt)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/introduction.md)

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