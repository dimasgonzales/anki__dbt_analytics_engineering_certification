# Source: https://docs.getdbt.com/docs/deploy/state-aware-interface

Navigating the state-aware interface | dbt Developer Hub

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

    - [About state-aware orchestration](/docs/deploy/state-aware-about)
    - [Setting up state-aware](/docs/deploy/state-aware-setup)
    - [Navigating the interface](/docs/deploy/state-aware-interface)
  + [Jobs](/docs/deploy/jobs)
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
* [State aware](/docs/deploy/state-aware-about)
* Navigating the interface

Copy page

On this page

Navigating the state-aware interface
====================================

Learn how to navigate the state-aware orchestration interface for better visibility into model builds and cost tracking.

Models built and reused chart[​](#models-built-and-reused-chart "Direct link to Models built and reused chart")
---------------------------------------------------------------------------------------------------------------

When you go to your **Account home**, you'll see a chart showing the number of models built and reused, giving you visibility into how state-aware orchestration is optimizing your data builds. This chart helps you to:

* **Track effectiveness of state-aware orchestration** — See how state-aware orchestration reduces unnecessary model rebuilds by only building models when there are changes to the data or code⁠. This chart provides transparency into how the optimization is working across your dbt implementation.
* **Analyze build patterns** — Gain insights into your project's build frequency and identify opportunities for further optimization.

You can also view the number of reused models per project in the **Accounts home** page.

[![Models built and reused chart in Account home](/img/docs/dbt-cloud/using-dbt-cloud/account-home-chart.png?v=2 "Models built and reused chart in Account home")](#)Models built and reused chart in Account home

[![View reused models count per project in the Accounts home page](/img/docs/deploy/sao-model-reuse.png?v=2 "View reused models count per project in the Accounts home page")](#)View reused models count per project in the Accounts home page

Model consumption view in jobs[​](#model-consumption-view-in-jobs "Direct link to Model consumption view in jobs")
------------------------------------------------------------------------------------------------------------------

State-aware jobs provide charts that show information about your job runs, and how many models were built and reused by your job in the past week, in the last 14 days, or in the last 30 days. In the **Overview** section of your job, the following charts are available:

Under the **Runs** tab:

* **Recent runs**
* **Total run duration time**

[![Charts for Recent runs and Total run duration time](/img/docs/dbt-cloud/using-dbt-cloud/sao-runs-chart.png?v=2 "Charts for Recent runs and Total run duration time")](#)Charts for Recent runs and Total run duration time

Under the **Models** tab:

* **Models built**
* **Models reused**

[![Charts for Models built and Models reused](/img/docs/dbt-cloud/using-dbt-cloud/sao-models-chart.png?v=2 "Charts for Models built and Models reused")](#)Charts for Models built and Models reused

Logs view of built models[​](#logs-view-of-built-models "Direct link to Logs view of built models")
---------------------------------------------------------------------------------------------------

When running a job, a structured logs view shows which models were built, skipped, or reused.

[![Logs view of built models](/img/docs/dbt-cloud/using-dbt-cloud/sao-logs-view.png?v=2 "Logs view of built models")](#)Logs view of built models

1. Each model has an icon indicating its status.
2. The **Reused** tab indicates the total number of reused models.
3. You can use the search bar or filter the logs to show **All**, **Success**, **Warning**, **Failed**, **Running**, **Skipped**, **Reused**, or **Debugged** messages.
4. Detailed log messages are provided to get more context on why models were built, reused, or skipped. These messages are highlighted in the logs.

Reused tag in the Latest status lens[​](#reused-tag-in-the-latest-status-lens "Direct link to Reused tag in the Latest status lens")
------------------------------------------------------------------------------------------------------------------------------------

Lineage lenses are interactive visual filters in [dbt Catalog](/docs/explore/explore-projects#lenses) that show additional context on your lineage graph to understand how resources are defined or performing. When you apply a lens, tags become visible on the nodes in the lineage graph, indicating the layer value along with coloration based on that value. If you're significantly zoomed out, only the tags and their colors are visible in the graph.

The **Latest status** lens shows the status from the latest execution of the resource in the current environment. When you use this lens to view your lineage, models that were reused from state-aware orchestration are tagged with **Reused**.

[![Latest status lens showing reused models](/img/docs/dbt-cloud/using-dbt-cloud/sao-latest-status-lens.png?v=2 "Latest status lens showing reused models")](#)Latest status lens showing reused models

To view your lineage with the **Latest status** lens:

1. From the main menu, go to **Orchestration** > **Runs**.
2. Select your run.
3. Go to the **Lineage** tab.
   The lineage of your project appears.
4. In the **Lenses** field, select **Latest status**.

Clear cache button[​](#clear-cache-button "Direct link to Clear cache button")
------------------------------------------------------------------------------

State-aware orchestration uses a cached hash of both code and data state for each model in an environment stored in Redis. When running a job, dbt checks if there are changes in the hash for the model being built between the saved state in Redis and the current state that would be built by the job. If there is a change, dbt builds the model. If there are no changes, dbt reuses the model from the last time it was built.

* To wipe this state clean and start again, clear the cache by going to **Orchestration** > **Environments**. Select your environment and click the **Clear cache** button.
* The **Clear cache** button is only available if you have enabled state-aware orchestration.
* After clearing the cache, the next run rebuilds every model from scratch. Subsequent runs rely on the regenerated cache.

[![Clear cache button](/img/docs/dbt-cloud/using-dbt-cloud/sao-clear-cache.png?v=2 "Clear cache button")](#)Clear cache button

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [scheduler](/tags/scheduler)
* [SAO](/tags/sao)
* [cost savings](/tags/cost-savings)
* [models built](/tags/models-built)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/deploy/state-aware-interface.md)

Last updated on **Nov 19, 2025**

[Previous

Setting up state-aware](/docs/deploy/state-aware-setup)[Next

About jobs](/docs/deploy/jobs)

* [Models built and reused chart[​](#models-built-and-reused-chart "Direct link to Models built and reused chart")](#models-built-and-reused-chart)
* [Model consumption view in jobs[​](#model-consumption-view-in-jobs "Direct link to Model consumption view in jobs")](#model-consumption-view-in-jobs)
* [Logs view of built models[​](#logs-view-of-built-models "Direct link to Logs view of built models")](#logs-view-of-built-models)
* [Reused tag in the Latest status lens[​](#reused-tag-in-the-latest-status-lens "Direct link to Reused tag in the Latest status lens")](#reused-tag-in-the-latest-status-lens)
* [Clear cache button[​](#clear-cache-button "Direct link to Clear cache button")](#clear-cache-button)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/deploy/state-aware-interface.md)

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