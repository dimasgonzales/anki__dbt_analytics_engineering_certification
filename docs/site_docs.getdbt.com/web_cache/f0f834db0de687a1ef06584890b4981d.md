# Source: https://docs.getdbt.com/docs/explore/view-downstream-exposures

Visualize downstream exposures | dbt Developer Hub

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

  + [Explore your data](/docs/explore/explore-your-data)
  + [Discover data with dbt Catalog](/docs/explore/explore-projects)

    - [Discover data with Catalog](/docs/explore/explore-projects)
    - [Access from dbt platform](/docs/explore/access-from-dbt-cloud)
    - [Column-level lineage](/docs/explore/column-level-lineage)
    - [Data health signals](/docs/explore/data-health-signals)
    - [Explore multiple projects](/docs/explore/explore-multiple-projects)
    - [External metadata ingestion](/docs/explore/external-metadata-ingestion)
    - [Global navigation](/docs/explore/global-navigation)
    - [Model performance](/docs/explore/model-performance)
    - [Project recommendations](/docs/explore/project-recommendations)
    - [dbt Catalog FAQs](/docs/explore/dbt-explorer-faqs)
    - [Model consumption](/docs/explore/view-downstream-exposures)

      * [Visualize downstream exposures](/docs/explore/view-downstream-exposures)
      * [Data health tile](/docs/explore/data-tile)
      * [Model query history](/docs/explore/model-query-history)
  + [Analyze with dbt Insights](/docs/explore/dbt-insights)
  + [Document your projects](/docs/explore/build-and-view-your-docs)
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

* [Explore your data](/docs/explore/explore-your-data)
* [Discover data with dbt Catalog](/docs/explore/explore-projects)
* Model consumption

Copy page

On this page

Visualize downstream exposures [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
=======================================================================================================================================================================================================

Downstream exposures integrate natively with Tableau (Power BI coming soon) and auto-generate downstream lineage in Catalog for a richer experience.

As a data team, it’s critical that you have context into the downstream use cases and users of your data products. By leveraging downstream [exposures](/docs/build/exposures) automatically, data teams can:

* Gain a better understanding of how models are used in downstream analytics, improving governance and decision-making.
* Reduce incidents and optimize workflows by linking upstream models to downstream dependencies.
* Automate exposure tracking for supported BI tools, ensuring lineage is always up to date.
* [Orchestrate exposures](/docs/cloud-integrations/orchestrate-exposures) to refresh the underlying data sources during scheduled dbt jobs, improving timeliness and reducing costs. Orchestrating exposures is essentially a way to ensure that your BI tools are updated regularly by using the [dbt job scheduler](/docs/deploy/deployments).
  + For more info on the differences between visualizing and orchestrating exposures, see [Visualize and orchestrate downstream exposures](/docs/cloud-integrations/downstream-exposures).

To configure downstream exposures automatically from dashboards in Tableau, prerequisites, and more — refer to [Configure downstream exposures](/docs/cloud-integrations/downstream-exposures-tableau).

### Supported plans[​](#supported-plans "Direct link to Supported plans")

Downstream exposures is available on all dbt [Enterprise-tier plans](https://www.getdbt.com/pricing/). Currently, you can only connect to a single Tableau site on the same server.

Tableau Server

If you're using Tableau Server, you need to [allowlist dbt's IP addresses](/docs/cloud/about-cloud/access-regions-ip-addresses) for your dbt region.

View downstream exposures[​](#view-downstream-exposures "Direct link to View downstream exposures")
---------------------------------------------------------------------------------------------------

After setting up downstream exposures in dbt, you can view them in [Catalog](/docs/explore/explore-projects) for a richer experience.

Navigate to Catalog by clicking on the **Explore** link in the navigation. From the **Overview** page, you can view downstream exposures from a couple of places:

* [Exposures menu](#exposures-menu)
* [File tree](#file-tree)
* [Project lineage](#project-lineage)

### Exposures menu[​](#exposures-menu "Direct link to Exposures menu")

View downstream exposures from the **Exposures** menu item under **Resources**. This menu provides a comprehensive list of all the exposures so you can quickly access and manage them. The menu displays the following information:

* **Name**: The name of the exposure.
* **Health**: The [data health signal](/docs/explore/data-health-signals) of the exposure.
* **Type**: The type of exposure, such as `dashboard` or `notebook`.
* **Owner**: The owner of the exposure.
* **Owner email**: The email address of the owner of the exposure.
* **Integration**: The BI tool that the exposure is integrated with.
* **Exposure mode**: The type of exposure defined: **Auto** or **Manual**.

[![View from the dbt Catalog under the 'Resources' menu.](/img/docs/cloud-integrations/auto-exposures/explorer-view-resources.jpg?v=2 "View from the dbt Catalog under the 'Resources' menu.")](#)View from the dbt Catalog under the 'Resources' menu.

### File tree[​](#file-tree "Direct link to File tree")

Locate directly from within the **File tree** under the **imported\_from\_tableau** sub-folder. This view integrates exposures seamlessly with your project files, making it easy to find and reference them from your project's structure.

[![View from the dbt Catalog under the 'File tree' menu.](/img/docs/cloud-integrations/auto-exposures/explorer-view-file-tree.jpg?v=2 "View from the dbt Catalog under the 'File tree' menu.")](#)View from the dbt Catalog under the 'File tree' menu.

### Project lineage[​](#project-lineage "Direct link to Project lineage")

From the **Project lineage** view, which visualizes the dependencies and relationships in your project. Exposures are represented with the Tableau icon, offering an intuitive way to see how they fit into your project's overall data flow.

[![View from the dbt Catalog in your Project lineage view, displayed with the Tableau icon.](/img/docs/cloud-integrations/auto-exposures/explorer-lineage2.jpg?v=2 "View from the dbt Catalog in your Project lineage view, displayed with the Tableau icon.")](#)View from the dbt Catalog in your Project lineage view, displayed with the Tableau icon.

[![View from the dbt Catalog in your Project lineage view, displayed with the Tableau icon.](/img/docs/cloud-integrations/auto-exposures/explorer-lineage.jpg?v=2 "View from the dbt Catalog in your Project lineage view, displayed with the Tableau icon.")](#)View from the dbt Catalog in your Project lineage view, displayed with the Tableau icon.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/explore/view-downstream-exposures.md)

Last updated on **Nov 19, 2025**

[Next

Data health tile](/docs/explore/data-tile)

* [Supported plans](#supported-plans)
* [View downstream exposures](#view-downstream-exposures)
  + [Exposures menu](#exposures-menu)
  + [File tree](#file-tree)
  + [Project lineage](#project-lineage)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/explore/view-downstream-exposures.md)

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