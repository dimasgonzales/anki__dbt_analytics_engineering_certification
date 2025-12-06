# Source: https://docs.getdbt.com/docs/deploy/deployments

Deploy dbt | dbt Developer Hub

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

* Deploy dbt

Copy page

Deploy dbt
==========

Use dbt's capabilities to seamlessly run a dbt job in production or staging environments. Rather than run dbt commands manually from the command line, you can leverage the [dbt's in-app scheduling](/docs/deploy/job-scheduler) to automate how and when you execute dbt.

The dbt platform offers the easiest and most reliable way to run your dbt project in production. Effortlessly promote high quality code from development to production and build fresh data assets that your business intelligence tools and end users query to make business decisions. Deploying with dbt lets you:

* Keep production data fresh on a timely basis
* Ensure CI and production pipelines are efficient
* Identify the root cause of failures in deployment environments
* Maintain high-quality code and data in production
* Gain visibility into the [health](/docs/explore/data-tile) of deployment jobs, models, and tests
* Uses [exports](/docs/use-dbt-semantic-layer/exports) to write [saved queries](/docs/build/saved-queries) in your data platform for reliable and fast metric reporting
* [Visualize](/docs/cloud-integrations/downstream-exposures-tableau) and [orchestrate](/docs/cloud-integrations/orchestrate-exposures) downstream exposures to understand how models are used in downstream tools and proactively refresh the underlying data sources during scheduled dbt jobs. [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
* Use [dbt's Git repository caching](/docs/cloud/account-settings#git-repository-caching) to protect against third-party outages and improve job run reliability. [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")
* Use [Hybrid projects](/docs/deploy/hybrid-projects) to upload dbt artifacts into the dbt platform for central visibility, cross-project referencing, and easier collaboration. [Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing") Preview

Before continuing, make sure you understand dbt's approach to [deployment environments](/docs/deploy/deploy-environments).

Learn how to use dbt's features to help your team ship timely and quality production data more easily.

Deploy with dbt[​](#deploy-with-dbt "Direct link to Deploy with dbt")
---------------------------------------------------------------------

[![](/img/icons/dbt-bit.svg)

#### Job scheduler

The job scheduler is the backbone of running jobs in the dbt platform, bringing power and simplicity to building data pipelines in both continuous integration and production environments.](/docs/deploy/job-scheduler)

[![](/img/icons/dbt-bit.svg)

#### Deploy jobs

Create and schedule jobs for the job scheduler to run.   
  
Runs on a schedule, by API, or after another job completes.](/docs/deploy/deploy-jobs)

[![](/img/icons/dbt-bit.svg)

#### State-aware orchestration

Intelligently determines which models to build by detecting changes in code or data at each job run.](/docs/deploy/state-aware-about)

[![](/img/icons/dbt-bit.svg)

#### Continuous integration

Set up CI checks so you can build and test any modified code in a staging environment when you open PRs and push new commits to your dbt repository.](/docs/deploy/continuous-integration)

[![](/img/icons/dbt-bit.svg)

#### Continuous deployment

Set up merge jobs to ensure the latest code changes are always in production when pull requests are merged to your Git repository.](/docs/deploy/continuous-deployment)

[![](/img/icons/dbt-bit.svg)

#### Job commands

Configure which dbt commands to execute when running a dbt job.](/docs/deploy/job-commands)

  

Monitor jobs and alerts[​](#monitor-jobs-and-alerts "Direct link to Monitor jobs and alerts")
---------------------------------------------------------------------------------------------

[![](/img/icons/dbt-bit.svg)

#### Visualize and orchestrate exposures

Learn how to use dbt to automatically generate downstream exposures from dashboards and proactively refresh the underlying data sources during scheduled dbt jobs.](/docs/deploy/orchestrate-exposures)

[![](/img/icons/dbt-bit.svg)

#### Artifacts

dbt generates and saves artifacts for your project, which it uses to power features like creating docs for your project and reporting the freshness of your sources.](/docs/deploy/artifacts)

[![](/img/icons/dbt-bit.svg)

#### Job notifications

Receive email or Slack channel notifications when a job run succeeds, fails, or is canceled so you can respond quickly and begin remediation if necessary.](/docs/deploy/job-notifications)

[![](/img/icons/dbt-bit.svg)

#### Model notifications

Receive email notifications in real time about issues encountered by your models and tests while a job is running.](/docs/deploy/model-notifications)

[![](/img/icons/dbt-bit.svg)

#### Run visibility

View the history of your runs and the model timing dashboard to help identify where improvements can be made to the scheduled jobs.](/docs/deploy/run-visibility)

[![](/img/icons/dbt-bit.svg)

#### Retry jobs

Rerun your errored jobs from start or the failure point.](/docs/deploy/retry-jobs)

[![](/img/icons/dbt-bit.svg)

#### Source freshness

Enable snapshots to capture the freshness of your data sources and configure how frequent these snapshots should be taken. This can help you determine whether your source data freshness is meeting your SLAs.](/docs/deploy/source-freshness)

[![](/img/icons/dbt-bit.svg)

#### Webhooks

Create outbound webhooks to send events about your dbt jobs' statuses to other systems in your organization.](/docs/deploy/webhooks)

  

Hybrid projects [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing") Preview[​](#hybrid-projects-- "Direct link to hybrid-projects--")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![](/img/icons/dbt-bit.svg)

#### Hybrid projects

Use Hybrid projects to upload dbt Core artifacts into the dbt platform for central visibility, cross-project referencing, and easier collaboration.](/docs/deploy/hybrid-projects)

  

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Use exports to materialize saved queries](/docs/use-dbt-semantic-layer/exports)
* [Integrate with other orchestration tools](/docs/deploy/deployment-tools)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [scheduler](/tags/scheduler)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/deploy/deployment-overview.md)

Last updated on **Nov 19, 2025**

[Next

Job scheduler](/docs/deploy/job-scheduler)

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