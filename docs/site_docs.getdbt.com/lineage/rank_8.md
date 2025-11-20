# Source: https://docs.getdbt.com/docs/build/view-documentation

View documentation | dbt Developer Hub

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

    - [Models](/docs/build/models)
    - [Tests](/docs/build/data-tests)
    - [Documentation](/docs/build/documentation)

      * [About documentation](/docs/build/documentation)
      * [View documentation](/docs/build/view-documentation)
    - [Snapshots](/docs/build/snapshots)
    - [Seeds](/docs/build/seeds)
    - [Jinja and macros](/docs/build/jinja-macros)
    - [User-defined functions](/docs/build/udfs)
    - [Sources](/docs/build/sources)
    - [Exposures](/docs/build/exposures)
    - [Groups](/docs/build/groups)
    - [Analyses](/docs/build/analyses)
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

* [Build dbt projects](/docs/build/projects)
* [Build your DAG](/docs/build/models)
* [Documentation](/docs/build/documentation)
* View documentation

Copy page

On this page

View documentation
==================

dbt provides intuitive and scalable tools for viewing your dbt documentation. Detailed documentation is essential for your developers and other stakeholders to gain shared context for your dbt project.

You can view documentation in two complementary ways, depending on your needs:

| Option | Description | Availability |
| --- | --- | --- |
| [**dbt Docs**](#dbt-docs) | Generates a static website with model lineage, metadata, and documentation that can be hosted on your web server (like S3 or Netlify). | dbt Core or dbt Developer plans |
| [**Catalog**](/docs/explore/explore-projects) | The premier documentation experience in dbt. Builds on dbt Docs to provide a dynamic, real-time interface with rich [metadata](/docs/explore/explore-projects#generate-metadata), customizable views, deep insight into your project and resources, and collaborative tools. | dbt Starter, Enterprise, or Enterprise+ plans |

Navigating your documentation[​](#navigating-your-documentation "Direct link to Navigating your documentation")
---------------------------------------------------------------------------------------------------------------

The following sections describe how to navigate your documentation in Catalog and dbt Docs.

### Catalog [Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[​](#catalog- "Direct link to catalog-")

[Catalog](/docs/explore/explore-projects) offers a dynamic, interactive way to explore your models, sources, and lineage.
To access Catalog, navigate to the **Explore** option in the dbt navigation menu.

[![Example of Catalog's resource details page and its lineage.](/img/docs/collaborate/dbt-explorer/example-model-details.png?v=2 "Example of Catalog's resource details page and its lineage.")](#)Example of Catalog's resource details page and its lineage.

[![Navigate Catalog to discover your project's resources and lineage.](/img/docs/collaborate/dbt-explorer/explorer-main-page.gif?v=2 "Navigate Catalog to discover your project's resources and lineage.")](#)Navigate Catalog to discover your project's resources and lineage.

Catalog offers users a comprehensive suite of features to enhance data project navigation and understanding, like:

* Interactive lineage visualization for your project's DAG to understand relationships between resources.
* Resource search bar with comprehensive filters to help find project resources efficiently and quickly.
* Model performance insights to access metadata on dbt runs for in-depth analysis of model performance and quality.
* Project recommendations with suggestions to improve test coverage and documentation across your data estate.
* Data health signals to monitor the health and performance of each resource through data health indicators.
* Model query history to track consumption queries on your models to gain deeper insights into data usage.
* Downstream exposures to automatically expose relevant data models from tools like Tableau to enhance visibility.

For additional details and instructions on how to explore your lineage, navigate your resources, view model query history and data health signals, feature availability, and more — refer to [Discover data with Catalog](/docs/explore/explore-projects).

### dbt Docs[​](#dbt-docs "Direct link to dbt Docs")

dbt Docs provides valuable insights into your dbt Core or dbt Developer plan projects. The interface enables you to navigate to the documentation for specific models. That might look something like this:

[![Auto-generated documentation for a dbt model](/img/docs/building-a-dbt-project/testing-and-documentation/f2221dc-Screen_Shot_2018-08-14_at_6.29.55_PM.png?v=2 "Auto-generated documentation for a dbt model")](#)Auto-generated documentation for a dbt model

Here, you can see a representation of the project structure, a markdown description for a model, and a list of all of the columns (with documentation) in the model.

From the dbt Docs page, click the green button in the bottom-right corner of the webpage to expand a "mini-map" of your DAG. This pane displays the immediate parents and children of the model that you're exploring.

[![Opening the DAG mini-map](/img/docs/building-a-dbt-project/testing-and-documentation/ec77c45-Screen_Shot_2018-08-14_at_6.31.56_PM.png?v=2 "Opening the DAG mini-map")](#)Opening the DAG mini-map

In this example, the `fct_subscription_transactions` model only has one direct parent. By clicking the "Expand" button in the top-right corner of the window, we can pivot the graph horizontally and view the full lineage for our model. This lineage is filterable using the `--select` and `--exclude` flags, which are consistent with the semantics of [model selection syntax](/reference/node-selection/syntax). Further, you can right-click to interact with the DAG, jump to documentation, or share links to your graph visualization with your coworkers.

[![The full lineage for a dbt model](/img/docs/building-a-dbt-project/testing-and-documentation/ac97fba-Screen_Shot_2018-08-14_at_6.35.14_PM.png?v=2 "The full lineage for a dbt model")](#)The full lineage for a dbt model

Deploy the documentation site[​](#deploy-the-documentation-site "Direct link to Deploy the documentation site")
---------------------------------------------------------------------------------------------------------------

Effortlessly deploy documentation in Catalog or dbt Docs to make it available to your teams.

Security

The `dbt docs serve` command is only intended for local/development hosting of the documentation site. Please use one of the methods listed in the next section (or similar) to ensure that your documentation site is hosted securely!

### Catalog [Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[​](#catalog--1 "Direct link to catalog--1")

Catalog automatically updates documentation after each production or staging job run using the metadata generated. This means it always has the latest results for your project with no manual deployment required. For details on how Catalog uses metadata to automatically update documentation, refer to [Generate metadata](/docs/explore/explore-projects#generate-metadata).

To learn how to deploy your documentation site, see [Build and view your docs with dbt](/docs/explore/build-and-view-your-docs).

### dbt Docs[​](#dbt-docs-1 "Direct link to dbt Docs")

dbt Docs was built to make it easy to host on the web. The site is "static," meaning you don't need any "dynamic" servers to serve the docs. You can host your documentation in several ways:

* Host on [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) (optionally [with IP access restrictions](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-3))
* Publish with [Netlify](https://discourse.getdbt.com/t/publishing-dbt-docs-to-netlify/121)
* Use your own web server like Apache/Nginx
* If you're on a dbt Developer plan, see [Build and view your docs with dbt](/docs/explore/build-and-view-your-docs#dbt-docs) to learn how to deploy your documentation site.

Interested in using Catalog for the complete dbt documentation experience, sign up for a free [dbt trial](https://www.getdbt.com/signup) or [contact us](https://www.getdbt.com/contact).

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/view-documentation.md)

Last updated on **Nov 19, 2025**

[Previous

About documentation](/docs/build/documentation)[Next

Snapshots](/docs/build/snapshots)

* [Navigating your documentation](#navigating-your-documentation)
  + [Catalog](#catalog-)
  + [dbt Docs](#dbt-docs)
* [Deploy the documentation site](#deploy-the-documentation-site)
  + [Catalog](#catalog--1)
  + [dbt Docs](#dbt-docs-1)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/view-documentation.md)

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