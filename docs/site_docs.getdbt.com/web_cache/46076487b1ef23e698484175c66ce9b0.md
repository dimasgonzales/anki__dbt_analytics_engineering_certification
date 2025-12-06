# Source: https://docs.getdbt.com/docs/explore/explore-multiple-projects

Explore multiple projects | dbt Developer Hub

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
* Explore multiple projects

Copy page

On this page

Explore multiple projects
=========================

View all the projects and public models in your account (where public models are defined) and gain a better understanding of your cross-project resources and how they're used.

On-demand learning

If you enjoy video courses, check out our [dbt Catalog on-demand course](https://learn.getdbt.com/courses/dbt-catalog) and learn how to best explore your dbt project(s)!

The resource-level lineage graph for a project displays the cross-project relationships in the DAG, with a **PRJ** icon indicating whether or not it's a project resource. That icon is located to the left side of the node name.

To view the project-level lineage graph, click the **View lineage** icon in the upper right corner from the main overview page:

* This view displays all the projects in your account and their relationships.
* Viewing an upstream (parent) project displays the downstream (child) projects that depend on it.
* Selecting a model reveals its dependent projects in the lineage.
* Click on an upstream (parent) project to view the other projects that reference it in the **Relationships** tab, showing the number of downstream (child) projects that depend on them.
  + This includes all projects listing the upstream one as a dependency in its `dependencies.yml` file, even without a direct `{{ ref() }}`.
* Selecting a project node from a public model opens its detailed lineage graph if you have the [permissions](/docs/cloud/manage-access/enterprise-permissions) to do so.

Indirect dependencies

When viewing a project's lineage, Catalog shows only *directly* [referenced](/docs/mesh/govern/project-dependencies) public models. It doesn't show [indirect dependencies](/faqs/Project_ref/indirectly-reference-upstream-model). If a referenced model in your project depends on another upstream public model, the second-level model won't appear in Catalog, however it will appear in the [Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud) lineage view.

[![View your cross-project lineage in a parent project and the other projects that reference it by clicking the 'Relationships' tab.](/img/docs/collaborate/dbt-explorer/cross-project-lineage-parent.png?v=2 "View your cross-project lineage in a parent project and the other projects that reference it by clicking the 'Relationships' tab.")](#)View your cross-project lineage in a parent project and the other projects that reference it by clicking the 'Relationships' tab.

When viewing a downstream (child) project that imports and refs public models from upstream (parent) projects:

* Public models will show up in the lineage graph and you can click on them to view the model details.
* Clicking on a model opens a side panel containing general information about the model, such as the specific dbt project that produces that model, description, package, and more.
* Double-clicking on a model from another project opens the resource-level lineage graph of the parent project, if you have the permissions to do so.

[![View a downstream (child) project that imports and refs public models from the upstream (parent) project.](/img/docs/collaborate/dbt-explorer/cross-project-child.png?v=2 "View a downstream (child) project that imports and refs public models from the upstream (parent) project.")](#)View a downstream (child) project that imports and refs public models from the upstream (parent) project.

Explore the project-level lineage graph[​](#explore-the-project-level-lineage-graph "Direct link to Explore the project-level lineage graph")
---------------------------------------------------------------------------------------------------------------------------------------------

For cross-project collaboration, you can interact with the DAG in all the same ways as described in [Explore your project's lineage](/docs/explore/explore-projects#project-lineage) but you can also interact with it at the project level and view the details.

If you have permissions for a project in the account, you can view all public models used across the entire account. However, you can only view full public model details and private models if you have permissions for the specific project where those models are defined.

To view all the projects in your account (displayed as a lineage graph or list view):

* Navigate to the top left section of the **Explore** page, near the navigation bar.
* Hover over the project name and select the account name. This takes you to a account-level lineage graph page, where you can view all the projects in the account, including dependencies and relationships between different projects.
* Click the **List view** icon in the page's upper right corner to see a list view of all the projects in the account.
* The list view page displays a public model list, project list, and a search bar for project searches.
* Click the **Lineage view** icon in the page's upper right corner to view the account-level lineage graph.

[![View a downstream (child) project, which imports and refs public models from upstream (parent) projects.](/img/docs/collaborate/dbt-explorer/account-level-lineage.gif?v=2 "View a downstream (child) project, which imports and refs public models from upstream (parent) projects.")](#)View a downstream (child) project, which imports and refs public models from upstream (parent) projects.

From the account-level lineage graph, you can:

* Click the **Lineage view** icon (in the graph’s upper right corner) to view the cross-project lineage graph.
* Click the **List view** icon (in the graph’s upper right corner) to view the project list.
  + Select a project from the **Projects** tab to switch to that project’s main **Explore** page.
  + Select a model from the **Public Models** tab to view the [model’s details page](/docs/explore/explore-projects#view-resource-details).
  + Perform searches on your projects with the search bar.
* Select a project node in the graph (double-clicking) to switch to that particular project’s lineage graph.

When you select a project node in the graph, a project details panel opens on the graph’s right-hand side where you can:

* View counts of the resources defined in the project.
* View a list of its public models, if any.
* View a list of other projects that uses the project, if any.
* Click **Open Project Lineage** to switch to the project’s lineage graph.
* Click the **Share** icon to copy the project panel link to your clipboard so you can share the graph with someone.

[![Select a downstream (child) project to open the project details panel for resource counts, public models associated, and more. ](/img/docs/collaborate/dbt-explorer/multi-project-overview.gif?v=2 "Select a downstream (child) project to open the project details panel for resource counts, public models associated, and more. ")](#)Select a downstream (child) project to open the project details panel for resource counts, public models associated, and more.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/explore/explore-multiple-projects.md)

Last updated on **Nov 19, 2025**

[Previous

Data health signals](/docs/explore/data-health-signals)[Next

External metadata ingestion](/docs/explore/external-metadata-ingestion)

* [Explore the project-level lineage graph](#explore-the-project-level-lineage-graph)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/explore/explore-multiple-projects.md)

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