# Source: https://docs.getdbt.com/docs/use-dbt-semantic-layer/deploy-sl

Deploy your metrics | dbt Developer Hub

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

  + [About the dbt Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl)
  + [Quickstart with the dbt Semantic Layer](/guides/sl-snowflake-qs)
  + [Configure](/docs/use-dbt-semantic-layer/setup-sl)
  + [Deploy metrics](/docs/use-dbt-semantic-layer/deploy-sl)

    - [Deploy your metrics](/docs/use-dbt-semantic-layer/deploy-sl)
    - [Write queries with exports](/docs/use-dbt-semantic-layer/exports)
    - [Cache common queries](/docs/use-dbt-semantic-layer/sl-cache)
  + [Consume](/docs/use-dbt-semantic-layer/consume-metrics)
  + [Semantic Layer FAQs](/docs/use-dbt-semantic-layer/sl-faqs)
* dbt AI
* [Copilot](/docs/cloud/dbt-copilot)
* [dbt MCP](/docs/dbt-ai/about-mcp)
* Additional tools
* [dbt integrations](/docs/cloud-integrations/overview)
* [Cost management](/docs/cloud/cost-management)
* Release information
* [Available dbt versions](/docs/dbt-versions/about-versions)
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [Use the dbt Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl)
* Deploy metrics

Copy page

On this page

Deploy your metrics [Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
============================================================================================================================================================================================================================================================================



This section explains how you can perform a job run in your deployment environment in dbt to materialize and deploy your metrics. Currently, the deployment environment is only supported.

1. Once you’ve [defined your semantic models and metrics](/guides/sl-snowflake-qs?step=10), commit and merge your metric changes in your dbt project.
2. In dbt, create a new [deployment environment](/docs/deploy/deploy-environments#create-a-deployment-environment) or use an existing environment on dbt 1.6 or higher.

   * Note — Deployment environment is currently supported (*development experience coming soon*)
3. To create a new environment, navigate to **Deploy** in the navigation menu, select **Environments**, and then select **Create new environment**.
4. Fill in your deployment credentials with your Snowflake username and password. You can name the schema anything you want. Click **Save** to create your new production environment.
5. [Create a new deploy job](/docs/deploy/deploy-jobs#create-and-schedule-jobs) that runs in the environment you just created. Go back to the **Deploy** menu, select **Jobs**, select **Create job**, and click **Deploy job**.
6. Set the job to run a `dbt parse` job to parse your projects and generate a [`semantic_manifest.json` artifact](/reference/artifacts/sl-manifest) file. Although running `dbt build` isn't required, you can choose to do so if needed.

   note

   If you are on the dbt Fusion engine, add the `dbt docs generate` command to your job to successfully deploy your metrics.
7. Run the job by clicking the **Run now** button. Monitor the job's progress in real-time through the **Run summary** tab.

   Once the job completes successfully, your dbt project, including the generated documentation, will be fully deployed and available for use in your production environment. If any issues arise, review the logs to diagnose and address any errors.

What’s happening internally?

* Merging the code into your main branch allows dbt to pull those changes and build the definition in the manifest produced by the run.
* Re-running the job in the deployment environment helps materialize the models, which the metrics depend on, in the data platform. It also makes sure that the manifest is up to date.
* The Semantic Layer APIs pull in the most recent manifest and enables your integration to extract metadata from it.

Next steps[​](#next-steps "Direct link to Next steps")
------------------------------------------------------

After you've executed a job and deployed your Semantic Layer:

* [Set up your Semantic Layer](/docs/use-dbt-semantic-layer/setup-sl) in dbt.
* Discover the [available integrations](/docs/cloud-integrations/avail-sl-integrations), such as Tableau, Google Sheets, Microsoft Excel, and more.
* Start querying your metrics with the [API query syntax](/docs/dbt-cloud-apis/sl-jdbc#querying-the-api-for-metric-metadata).

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Optimize querying performance](/docs/use-dbt-semantic-layer/sl-cache) using declarative caching.
* [Validate semantic nodes in CI](/docs/deploy/ci-jobs#semantic-validations-in-ci) to ensure code changes made to dbt models don't break these metrics.
* If you haven't already, learn how to [build your metrics and semantic models](/docs/build/build-metrics-intro) in your development tool of choice.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [Semantic Layer](/tags/semantic-layer)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/use-dbt-semantic-layer/deploy-sl.md)

Last updated on **Nov 19, 2025**

[Previous

Semantic Layer architecture](/docs/use-dbt-semantic-layer/sl-architecture)[Next

Write queries with exports](/docs/use-dbt-semantic-layer/exports)

* [Next steps[​](#next-steps "Direct link to Next steps")](#next-steps)
* [Related docs[​](#related-docs "Direct link to Related docs")](#related-docs)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/use-dbt-semantic-layer/deploy-sl.md)

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