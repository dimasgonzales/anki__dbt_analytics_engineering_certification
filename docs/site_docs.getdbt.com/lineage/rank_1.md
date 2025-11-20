# Source: https://docs.getdbt.com/docs/explore/column-level-lineage

Column-level lineage | dbt Developer Hub

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
* Column-level lineage

Copy page

On this page

Column-level lineage [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
=============================================================================================================================================================================================

Catalog now offers column-level lineage (CLL) for the resources in your dbt project. Analytics engineers can quickly and easily gain insight into the provenance of their data products at a more granular level. For each column in a resource (model, source, or snapshot) in a dbt project, Catalog provides end-to-end lineage for the data in that column given how it's used.

CLL is available to all dbt Enterprise plans that can use Catalog.

[![Overview of column level lineage](/img/docs/collaborate/dbt-explorer/example-overview-cll.png?v=2 "Overview of column level lineage")](#)Overview of column level lineage

On-demand learning

If you enjoy video courses, check out our [dbt Catalog on-demand course](https://learn.getdbt.com/courses/dbt-catalog) and learn how to best explore your dbt project(s)!

Access the column-level lineage[​](#access-the-column-level-lineage "Direct link to Access the column-level lineage")
---------------------------------------------------------------------------------------------------------------------

There is no additional setup required for CLL if your account is on an Enterprise plan that can use Catalog. You can access the CLL by expanding the column card in the **Columns** tab of an Catalog [resource details page](/docs/explore/explore-projects#view-resource-details) for a model, source, or snapshot.

dbt updates the lineage in Explorer after each run that's executed in the production or staging environment. At least one job in the production or staging environment must run `dbt docs generate`. Refer to [Generating metadata](/docs/explore/explore-projects#generate-metadata) for more details.

[![Example of the Columns tab and where to expand for the CLL](/img/docs/collaborate/dbt-explorer/example-cll.png?v=2 "Example of the Columns tab and where to expand for the CLL")](#)Example of the Columns tab and where to expand for the CLL

Column evolution lens[​](#column-lens "Direct link to Column evolution lens")
-----------------------------------------------------------------------------

You can use the column evolution lineage lens to determine when a column is transformed vs. reused (passthrough or rename). The lens helps you distinguish when and how a column is actually changed as it flows through your dbt lineage, informing debugging workflows in particular.

[![Example of the Column evolution lens](/img/docs/collaborate/dbt-explorer/example-evolution-lens.png?v=2 "Example of the Column evolution lens")](#)Example of the Column evolution lens

### Inherited column descriptions[​](#inherited-column-descriptions "Direct link to Inherited column descriptions")

A reused column, labeled as **Passthrough** or **Rename** in the lineage, automatically inherits its description from the source and upstream model columns. The inheritance goes as far back as possible. As long as the column isn't transformed, you don't need to manually define the description; it'll automatically propagate downstream.

Passthrough and rename columns are clearly labeled and color-coded in the lineage.

In the following `dim_salesforce_accounts` model example (located at the end of the lineage), the description for a column inherited from the `stg_salesforce__accounts` model (located second to the left) indicates its origin. This helps developers quickly identify the original source of the column, making it easier to know where to make documentation changes.

[![Example of lineage with propagated and inherited column descriptions.](/img/docs/collaborate/dbt-explorer/example-prop-inherit.jpg?v=2 "Example of lineage with propagated and inherited column descriptions.")](#)Example of lineage with propagated and inherited column descriptions.

Column-level lineage use cases[​](#use-cases "Direct link to Column-level lineage use cases")
---------------------------------------------------------------------------------------------

Learn more about why and how you can use CLL in the following sections.

### Root cause analysis[​](#root-cause-analysis "Direct link to Root cause analysis")

When there is an unexpected breakage in a data pipeline, column-level lineage can be a valuable tool to understand the exact point where the error occurred in the pipeline. For example, a failing data test on a particular column in your dbt model might've stemmed from an untested column upstream. Using CLL can help quickly identify and fix breakages when they happen.

### Impact analysis[​](#impact-analysis "Direct link to Impact analysis")

During development, analytics engineers can use column-level lineage to understand the full scope of the impact of their proposed changes. This knowledge empowers them to create higher-quality pull requests that require fewer edits, as they can anticipate and preempt issues that would've been unchecked without column-level insights.

### Collaboration and efficiency[​](#collaboration-and-efficiency "Direct link to Collaboration and efficiency")

When exploring your data products, navigating column lineage allows analytics engineers and data analysts to more easily navigate and understand the origin and usage of their data, enabling them to make better decisions with higher confidence.

Caveats[​](#caveats "Direct link to Caveats")
---------------------------------------------

Refer to the following CLL caveats or limitations as you navigate Catalog.

### Column usage[​](#column-usage "Direct link to Column usage")

Column-level lineage reflects the lineage from `select` statements in your models' SQL code. It doesn't reflect other usage like joins and filters.

### SQL parsing[​](#sql-parsing "Direct link to SQL parsing")

Column-level lineage relies on SQL parsing. Errors can occur when parsing fails or a column's origin is unknown (like with JSON unpacking, lateral joins, and so on). In these cases, lineage may be incomplete and dbt will provide a warning about it in the column lineage.

[![Example of warning in the full lineage graph](/img/docs/collaborate/dbt-explorer/example-parsing-error-pill.png?v=2 "Example of warning in the full lineage graph")](#)Example of warning in the full lineage graph

To review the error details:

1. Click the **Expand** icon in the upper right corner to open the column's lineage graph
2. Select the node to open the column’s details panel

Possible error cases are:

* **Parsing error** — Error occurs when the SQL is ambiguous or too complex for parsing. An example of ambiguous parsing scenarios are *complex* lateral joins.
* **Python error** — Error occurs when a Python model is used within the lineage. Due to the nature of Python models, it's not possible to parse and determine the lineage.
* **Unknown error** — Error occurs when the lineage can't be determined for an unknown reason. An example of this would be if a dbt best practice is not being followed, like using hardcoded table names instead of `ref` statements.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/explore/column-level-lineage.md)

Last updated on **Nov 19, 2025**

[Previous

Access from dbt platform](/docs/explore/access-from-dbt-cloud)[Next

Data health signals](/docs/explore/data-health-signals)

* [Access the column-level lineage](#access-the-column-level-lineage)
* [Column evolution lens](#column-lens)
  + [Inherited column descriptions](#inherited-column-descriptions)
* [Column-level lineage use cases](#use-cases)
  + [Root cause analysis](#root-cause-analysis)
  + [Impact analysis](#impact-analysis)
  + [Collaboration and efficiency](#collaboration-and-efficiency)
* [Caveats](#caveats)
  + [Column usage](#column-usage)
  + [SQL parsing](#sql-parsing)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/explore/column-level-lineage.md)

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