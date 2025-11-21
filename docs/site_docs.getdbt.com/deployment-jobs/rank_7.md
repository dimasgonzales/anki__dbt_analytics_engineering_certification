# Source: https://docs.getdbt.com/docs/environments-in-dbt

About environments | dbt Developer Hub

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

  + [About dbt setup](/docs/about-setup)
  + [About environments](/docs/environments-in-dbt)
  + [dbt platform](/docs/cloud/about-cloud-setup)
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
* About environments

Copy page

About environments
==================

In software engineering, environments are used to enable engineers to develop and test code without impacting the users of their software. Typically, there are two types of environments in dbt:

* **Deployment or Production** (or *prod*) — Refers to the environment that end users interact with.
* **Development** (or *dev*) — Refers to the environment that engineers work in. This means that engineers can work iteratively when writing and testing new code in *development*. Once they are confident in these changes, they can deploy their code to *production*.

In traditional software engineering, different environments often use completely separate architecture. For example, the dev and prod versions of a website may use different servers and databases. Data warehouses can also be designed to have separate environments — the *production* environment refers to the relations (for example, schemas, tables, and views) that your end users query (often through a BI tool).

Configure environments to tell dbt or dbt Core how to build and execute your project in development and production:

[![](/img/icons/dbt-bit.svg)

#### Environments in dbt

Seamlessly configure development and deployment environments in dbt to control how your project runs in both the Studio IDE, dbt CLI, and dbt jobs.](/docs/dbt-cloud-environments)

[![](/img/icons/command-line.svg)

#### Environments in dbt Core

Setup and maintain separate deployment and development environments through the use of targets within a profile file](/docs/core/dbt-core-environments)

  

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [dbt environment best practices](/guides/set-up-ci)
* [Deployment environments](/docs/deploy/deploy-environments)
* [About dbt Core versions](/docs/dbt-versions/core)
* [Set Environment variables in dbt](/docs/build/environment-variables#special-environment-variables)
* [Use Environment variables in jinja](/reference/dbt-jinja-functions/env_var)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/environments-in-dbt.md)

Last updated on **Nov 19, 2025**

[Previous

About dbt setup](/docs/about-setup)

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