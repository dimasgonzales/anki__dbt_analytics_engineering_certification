# Source: https://docs.getdbt.com/docs/deploy/jobs

Jobs in the dbt platform | dbt Developer Hub

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
* Jobs

Copy page

Jobs in the dbt platform
========================

These are the available job types in dbt:

* [Deploy jobs](/docs/deploy/deploy-jobs) — Build production data assets. Runs on a schedule, by API, or after another job completes.
* [Continuous integration (CI) jobs](/docs/deploy/continuous-integration) — Test and validate code changes before merging. Triggered by commit to a PR or by API.
* [Merge jobs](/docs/deploy/merge-jobs) — Deploy merged changes into production. Runs after a successful PR merge or by API.
* [State-aware jobs](/docs/deploy/state-aware-about) — Intelligently decide what needs to be rebuilt based on source freshness, code, or upstream data changes. Rebuild models only if they are older than the specified interval.

The following comparison table describes the behaviors of the different job types:

|  | **Deploy jobs** | **CI jobs** | **Merge jobs** | **State-aware jobs** |
| --- | --- | --- | --- | --- |
| Purpose | Builds production data assets. | Builds and tests new code before merging changes into production. | Build merged changes into production or update state for deferral. | Trigger model builds and job runs only when source data is updated. |
| Trigger types | Triggered by a schedule, API, or the successful completion of another job. | Triggered by a commit to a PR or by API. | Triggered by a successful merge into the environment's branch or by API. | Triggered when code, sources, or upstream data changes and at custom refresh intervals and for custom source freshness configurations |
| Destination | Builds into a production database and schema. | Builds into a staging database and ephemeral schema, lived for the lifetime of the PR. | Builds into a production database and schema. | Builds into a production database and schema. |
| Execution mode | Runs execute sequentially, so as to not have collisions on the underlying DAG. | Runs execute in parallel to promote team velocity. | Runs execute sequentially, so as to not have collisions on the underlying DAG. |  |
| Efficiency run savings | Detects over-scheduled jobs and cancels unnecessary runs to avoid queue clog. | Cancels existing runs when a newer commit is pushed to avoid redundant work. | N/A | Runs jobs and build models *only* when source data is updated or if models are older than what you specified in the project refresh interval |
| State comparison | Only sometimes needs to detect state. | Almost always needs to compare state against the production environment to build on modified code and its dependents. | Almost always needs to compare state against the production environment to build on modified code and its dependents. |  |
| Job run duration | Limit is 24 hours. | Limit is 24 hours. | Limit is 24 hours. | Limit is 24 hours. |

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [scheduler](/tags/scheduler)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/deploy/jobs.md)

Last updated on **Nov 19, 2025**

[Previous

Navigating the interface](/docs/deploy/state-aware-interface)[Next

Deploy jobs](/docs/deploy/deploy-jobs)

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