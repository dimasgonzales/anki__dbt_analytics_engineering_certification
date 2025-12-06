# Source: https://docs.getdbt.com/docs/deploy/run-visibility

Run visibility | dbt Developer Hub

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
  + [Monitor jobs and alerts](/docs/deploy/monitor-jobs)

    - [Monitor jobs and alerts](/docs/deploy/monitor-jobs)
    - [Visualize and orchestrate exposures](/docs/deploy/orchestrate-exposures)
    - [Artifacts](/docs/deploy/artifacts)
    - [Job notifications](/docs/deploy/job-notifications)
    - [Model notifications](/docs/deploy/model-notifications)
    - [Run visibility](/docs/deploy/run-visibility)
    - [Retry jobs](/docs/deploy/retry-jobs)
    - [Source freshness](/docs/deploy/source-freshness)
    - [Webhooks](/docs/deploy/webhooks)
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
* [Monitor jobs and alerts](/docs/deploy/monitor-jobs)
* Run visibility

Copy page

On this page

Run visibility
==============

You can view the history of your runs and the model timing dashboard to help identify where improvements can be made to jobs.

Run history[​](#run-history "Direct link to Run history")
---------------------------------------------------------

The **Run history** dashboard in dbt helps you monitor the health of your dbt project. It provides a detailed overview of all your project's job runs and empowers you with a variety of filters that enable you to focus on specific aspects. You can also use it to review recent runs, find errored runs, and track the progress of runs in progress. You can access it from the top navigation menu by clicking **Deploy** and then **Run history**.

The dashboard displays your full run history, including job name, status, associated environment, job trigger, commit SHA, schema, and timing info.

dbt developers can access their run history for the last 365 days through the dbt user interface (UI) and API.

dbt Labs limits self-service retrieval of run history metadata to 365 days to improve dbt's performance.

[![Run history dashboard allows you to monitor the health of your dbt project and displays jobs, job status, environment, timing, and more.](/img/docs/dbt-cloud/deployment/run-history.png?v=2 "Run history dashboard allows you to monitor the health of your dbt project and displays jobs, job status, environment, timing, and more.")](#)Run history dashboard allows you to monitor the health of your dbt project and displays jobs, job status, environment, timing, and more.

Job run details[​](#job-run-details "Direct link to Job run details")
---------------------------------------------------------------------

From the **Run history** dashboard, select a run to view complete details about it. The job run details page displays job trigger, commit SHA, time spent in the scheduler queue, all the run steps and their [logs](#access-logs), [model timing](#model-timing), and more.

Click **Rerun now** to rerun the job immediately.

An example of a completed run with a configuration for a [job completion trigger](/docs/deploy/deploy-jobs#trigger-on-job-completion):

[![Example of run details](/img/docs/dbt-cloud/deployment/example-job-details.png?v=2 "Example of run details")](#)Example of run details

### Run summary tab[​](#run-summary-tab "Direct link to Run summary tab")

You can view or download in-progress and historical logs for your dbt runs. This makes it easier for the team to debug errors more efficiently.

[![Access logs for run steps](/img/docs/dbt-cloud/deployment/access-logs.png?v=2 "Access logs for run steps")](#)Access logs for run steps

### Lineage tab[​](#lineage-tab "Direct link to Lineage tab")

View the lineage graph associated with the job run so you can better understand the dependencies and relationships of the resources in your project. To view a node's metadata directly in [Catalog](/docs/explore/explore-projects), select it (double-click) from the graph.

[![Example of accessing dbt Catalog from the Lineage tab](/img/docs/collaborate/dbt-explorer/explorer-from-lineage.gif?v=2 "Example of accessing dbt Catalog from the Lineage tab")](#)Example of accessing dbt Catalog from the Lineage tab

### Model timing tab [Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[​](#model-timing-tab- "Direct link to model-timing-tab-")

The **Model timing** tab displays the composition, order, and time each model takes in a job run. The visualization appears for successful jobs and highlights the top 1% of model durations. This helps you identify bottlenecks in your runs so you can investigate them and potentially make changes to improve their performance.

You can find the dashboard on the [job's run details](#job-run-details).

[![The Model timing tab displays the top 1% of model durations and visualizes model bottlenecks](/img/docs/dbt-cloud/model-timing.png?v=2 "The Model timing tab displays the top 1% of model durations and visualizes model bottlenecks")](#)The Model timing tab displays the top 1% of model durations and visualizes model bottlenecks

### Artifacts tab[​](#artifacts-tab "Direct link to Artifacts tab")

This provides a list of the artifacts generated by the job run. The files are saved and available for download.

[![Example of the Artifacts tab](/img/docs/dbt-cloud/example-artifacts-tab.png?v=2 "Example of the Artifacts tab")](#)Example of the Artifacts tab

### Compare tab [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[​](#compare-tab- "Direct link to compare-tab-")

The **Compare** tab is shown for [CI job runs](/docs/deploy/ci-jobs) with the **Run compare changes** setting enabled. It displays details about [the changes from the comparison dbt performed](/docs/deploy/advanced-ci#compare-changes) between what's in your production environment and the pull request. To help you better visualize the differences, dbt highlights changes to your models in red (deletions) and green (inserts).

From the **Modified** section, you can view the following:

* **Overview** — High-level summary about the changes to the models such as the number of primary keys that were added or removed.
* **Primary keys** — Details about the changes to the records.
* **Modified rows** — Details about the modified rows. Click **Show full preview** to display all columns.
* **Columns** — Details about the changes to the columns.

To view the dependencies and relationships of the resources in your project more closely, click **View in Catalog** to launch [Catalog](/docs/explore/explore-projects).

[![Example of the Compare tab](/img/docs/dbt-cloud/example-ci-compare-changes-tab.png?v=2 "Example of the Compare tab")](#)Example of the Compare tab

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [scheduler](/tags/scheduler)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/deploy/run-visibility.md)

Last updated on **Nov 19, 2025**

[Previous

Model notifications](/docs/deploy/model-notifications)[Next

Retry jobs](/docs/deploy/retry-jobs)

* [Run history](#run-history)
* [Job run details](#job-run-details)
  + [Run summary tab](#run-summary-tab)
  + [Lineage tab](#lineage-tab)
  + [Model timing tab](#model-timing-tab-)
  + [Artifacts tab](#artifacts-tab)
  + [Compare tab](#compare-tab-)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/deploy/run-visibility.md)

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