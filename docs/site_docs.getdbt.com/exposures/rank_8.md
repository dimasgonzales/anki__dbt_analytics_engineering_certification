# Source: https://docs.getdbt.com/docs/cloud-integrations/orchestrate-exposures

Orchestrate downstream exposures | dbt Developer Hub

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
* [Explore your data](/docs/explore/explore-your-data)
* [Use the dbt Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl)
* dbt AI
* [Copilot](/docs/cloud/dbt-copilot)
* [dbt MCP](/docs/dbt-ai/about-mcp)
* Additional tools
* [dbt integrations](/docs/cloud-integrations/overview)

  + [About dbt integrations](/docs/cloud-integrations/overview)
  + [Visualize and orchestrate exposures](/docs/cloud-integrations/downstream-exposures)

    - [Visualize and orchestrate downstream exposures](/docs/cloud-integrations/downstream-exposures)
    - [Set up automatic exposures](/docs/cloud-integrations/downstream-exposures-tableau)
    - [Orchestrate exposures](/docs/cloud-integrations/orchestrate-exposures)
  + [Semantic Layer integrations](/docs/cloud-integrations/avail-sl-integrations)
* [Cost management](/docs/cloud/cost-management)
* Release information
* [Available dbt versions](/docs/dbt-versions/about-versions)
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [dbt integrations](/docs/cloud-integrations/overview)
* [Visualize and orchestrate exposures](/docs/cloud-integrations/downstream-exposures)
* Orchestrate exposures

Copy page

On this page

Orchestrate downstream exposures [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Beta](https://docs.getdbt.com/docs/dbt-versions/product-lifecycles "Go to https://docs.getdbt.com/docs/dbt-versions/product-lifecycles")
==================================================================================================================================================================================================================================================================================================================================================

Use dbt [Cloud job scheduler](/docs/deploy/job-scheduler) to proactively refresh downstream exposures and the underlying data sources (extracts) that power your Tableau Workbooks.

Available in private beta

Orchestrating exposures is currently available in private beta to dbt Enterprise accounts. To join the beta, contact your account representative.

Orchestrating exposures integrates with [downstream exposures](/docs/cloud-integrations/downstream-exposures-tableau) and uses your `dbt build` job to ensure that Tableau extracts are updated regularly.

Control the frequency of these refreshes by configuring environment variables in your dbt environment.

 Differences between visualizing and orchestrating downstream exposures

The following table summarizes the differences between visualizing and orchestrating downstream exposures:

| Info | Set up and visualize downstream exposures | Orchestrate downstream exposures [Beta](https://docs.getdbt.com/docs/dbt-versions/product-lifecycles "Go to https://docs.getdbt.com/docs/dbt-versions/product-lifecycles") |
| --- | --- | --- |
| Purpose | Automatically brings downstream assets into your dbt lineage. | Proactively refreshes the underlying data sources during scheduled dbt jobs. |
| Benefits | Provides visibility into data flow and dependencies. | Ensures BI tools always have up-to-date data without manual intervention. |
| Location | Exposed in [Catalog](/docs/explore/explore-projects) | Exposed in [dbt scheduler](/docs/deploy/deployments) |
| Supported BI tool | Tableau | Tableau |
| Use case | Helps users understand how models are used and reduces incidents. | Optimizes timeliness and reduces costs by running models when needed. |

Prerequisites[​](#prerequisites "Direct link to Prerequisites")
---------------------------------------------------------------

To orchestrate downstream exposures, you should meet the following:

* [Configured downstream exposures](/docs/cloud-integrations/downstream-exposures-tableau) and ensured desired exposures are included in your lineage
* Verified your environment and jobs are on a supported dbt [release track](/docs/dbt-versions/cloud-release-tracks).
* Have a dbt account on the [Enterprise or Enterprise+ plan](https://www.getdbt.com/pricing/).
* Created a [production](/docs/deploy/deploy-environments#set-as-production-environment) deployment environment for each project you want to explore, with at least one successful job run.
* Have [admin permissions](/docs/cloud/manage-access/enterprise-permissions) in dbt to edit project settings or production environment settings.

Orchestrate downstream exposures[​](#orchestrate-downstream-exposures "Direct link to Orchestrate downstream exposures")
------------------------------------------------------------------------------------------------------------------------

To orchestrate downstream exposures and see the refresh happen automatically during scheduled dbt jobs:

1. In the dbt, click **Deploy**, then **Environments**, and select the **Environment variables** tab.
2. Click **Add variable** and set the [environment level variable](/docs/build/environment-variables#setting-and-overriding-environment-variables) `DBT_ACTIVE_EXPOSURES` to `1` within the environment you want the refresh to happen.
3. Then set the `DBT_ACTIVE_EXPOSURES_BUILD_AFTER` to control the maximum refresh frequency (in minutes) you want between each exposure refresh.
4. Set the variable to **1440** minutes (24 hours) by default. This means that downstream exposures won’t refresh Tableau extracts more often than this set interval, even if the related models run more frequently.

   [![Set the environment variable `DBT_ACTIVE_EXPOSURES` to `1`.](/img/docs/cloud-integrations/auto-exposures/active-exposures-env-var.jpg?v=2 "Set the environment variable `DBT_ACTIVE_EXPOSURES` to `1`.")](#)Set the environment variable `DBT\_ACTIVE\_EXPOSURES` to `1`.
5. Run a job in production. You will see the update each time a job runs in production.
   * If a job runs before the set interval has passed, dbt skips the downstream exposure refresh and marks it as `skipped` in the job logs.
6. View the downstream exposure logs in the dbt run job logs.

   [![View the downstream exposure logs in the dbt run job logs.](/img/docs/cloud-integrations/auto-exposures/active-exposure-log.jpg?v=2 "View the downstream exposure logs in the dbt run job logs.")](#)View the downstream exposure logs in the dbt run job logs.

   * View more details in the debug logs for any troubleshooting.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud-integrations/orchestrate-exposures.md)

Last updated on **Nov 19, 2025**

[Previous

Set up automatic exposures](/docs/cloud-integrations/downstream-exposures-tableau)[Next

Available integrations](/docs/cloud-integrations/avail-sl-integrations)

* [Prerequisites](#prerequisites)
* [Orchestrate downstream exposures](#orchestrate-downstream-exposures)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud-integrations/orchestrate-exposures.md)

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