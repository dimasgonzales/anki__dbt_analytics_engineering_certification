# Source: https://docs.getdbt.com/docs/explore/build-and-view-your-docs

Build and view your docs with dbt | dbt Developer Hub

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
  + [Analyze with dbt Insights](/docs/explore/dbt-insights)
  + [Document your projects](/docs/explore/build-and-view-your-docs)

    - [Build and view your docs with dbt](/docs/explore/build-and-view-your-docs)
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
* Document your projects

Copy page

On this page

Build and view your docs with dbt
=================================

dbt enables you to generate documentation for your project and data platform. The documentation is automatically updated with new information after a fully successful job run, ensuring accuracy and relevance.

The default documentation experience in dbt is [Catalog](/docs/explore/explore-projects), available on [Starter, Enterprise, or Enterprise+ plans](https://www.getdbt.com/pricing/). Use [Catalog](/docs/explore/explore-projects) to view your project's resources (such as models, tests, and metrics) and their lineage to gain a better understanding of its latest production state.

Refer to [documentation](/docs/build/documentation) for more configuration details.

This shift makes [dbt Docs](#dbt-docs) a legacy documentation feature in dbt. dbt Docs is still accessible and offers basic documentation, but it doesn't offer the same speed, metadata, or visibility as Catalog. dbt Docs is available to dbt developer plans or dbt Core users.

Set up a documentation job[​](#set-up-a-documentation-job "Direct link to Set up a documentation job")
------------------------------------------------------------------------------------------------------

Catalog uses the [metadata](/docs/explore/explore-projects#generate-metadata) generated after each job run in the production or staging environment, ensuring it always has the latest project results. To view richer metadata, you can set up documentation for a job in dbt when you edit your job settings or create a new job.

Configure the job to [generate metadata](/docs/explore/explore-projects#generate-metadata) when it runs. If you want to view column and statistics for models, sources, and snapshots in Catalog, then this step is necessary.

To set up a job to generate docs:

1. In the top left, click **Deploy** and select **Jobs**.
2. Create a new job or select an existing job and click **Settings**.
3. Under **Execution Settings**, select **Generate docs on run** and click **Save**.


   [![Setting up a job to generate documentation](/img/docs/dbt-cloud/using-dbt-cloud/documentation-job-execution-settings.png?v=2 "Setting up a job to generate documentation")](#)Setting up a job to generate documentation

*Note, for dbt Docs users you need to configure the job to generate docs when it runs, then manually link that job to your project. Proceed to [configure project documentation](#configure-project-documentation) so your project generates the documentation when this job runs.*

You can also add the [`dbt docs generate` command](/reference/commands/cmd-docs) to the list of commands in the job run steps. However, you can expect different outcomes when adding the command to the run steps compared to configuring a job selecting the **Generate docs on run** checkbox.

Review the following options and outcomes:

| Options | Outcomes |
| --- | --- |
| **Select checkbox** | Select the **Generate docs on run** checkbox to automatically generate updated project docs each time your job runs. If that particular step in your job fails, the job can still be successful if all subsequent steps are successful. |
| **Add as a run step** | Add `dbt docs generate` to the list of commands in the job run steps, in whatever order you prefer. If that particular step in your job fails, the job will fail and all subsequent steps will be skipped. |

Tip — Documentation-only jobs

To create and schedule documentation-only jobs at the end of your production jobs, add the `dbt compile` command in the **Commands** section.

dbt Docs[​](#dbt-docs "Direct link to dbt Docs")
------------------------------------------------

dbt Docs, available on developer plans or dbt Core users, generates a website from your dbt project using the `dbt docs generate` command. It provides a central location to view your project's resources, such as models, tests, and lineage — and helps you understand the data in your warehouse.

### Configure project documentation[​](#configure-project-documentation "Direct link to Configure project documentation")

You configure project documentation to generate documentation when the job you set up in the previous section runs. In the project settings, specify the job that generates documentation artifacts for that project. Once you configure this setting, subsequent runs of the job will automatically include a step to generate documentation.

1. From dbt, click on your account name in the left side menu and select **Account settings**.
2. Navigate to **Projects** and select the project that needs documentation.
3. Click **Edit**.
4. Under **Artifacts**, select the job that should generate docs when it runs and click **Save**.


   [![Configuring project documentation](/img/docs/dbt-cloud/using-dbt-cloud/documentation-project-details.png?v=2 "Configuring project documentation")](#)Configuring project documentation

Use Catalog for a richer documentation experience

For a richer and more interactive experience, try out [Catalog](/docs/explore/explore-projects), available on [Starter, Enterprise, or Enterprise+ plans](https://www.getdbt.com/pricing/). It includes map layers of your DAG, keyword search, interacts with the Studio IDE, model performance, project recommendations, and more.

### Generating documentation[​](#generating-documentation "Direct link to Generating documentation")

To generate documentation in the Studio IDE, run the `dbt docs generate` command in the **Command Bar** in the Studio IDE. This command will generate the documentation for your dbt project as it exists in development in your IDE session.

After running `dbt docs generate` in the Studio IDE, click the icon above the file tree, to see the latest version of your documentation rendered in a new browser window.

### View documentation[​](#view-documentation "Direct link to View documentation")

Once you set up a job to generate documentation for your project, you can click **Explore** in the navigation and then click on **dbt Docs**. Your project's documentation should open. This link will always help you find the most recent version of your project's documentation in dbt.

These generated docs always show the last fully successful run, which means that if you have any failed tasks, including tests, then you will not see changes to the docs by this run. If you don't see a fully successful run, then you won't see any changes to the documentation.

The Studio IDE makes it possible to view [documentation](/docs/build/documentation) for your dbt project while your code is still in development. With this workflow, you can inspect and verify what your project's generated documentation will look like before your changes are released to production.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Documentation](/docs/build/documentation)
* [Catalog](/docs/explore/explore-projects)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/explore/build-and-view-your-docs.md)

Last updated on **Nov 19, 2025**

[Previous

Access and run queries](/docs/explore/access-dbt-insights)

* [Set up a documentation job](#set-up-a-documentation-job)
* [dbt Docs](#dbt-docs)
  + [Configure project documentation](#configure-project-documentation)
  + [Generating documentation](#generating-documentation)
  + [View documentation](#view-documentation)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/explore/build-and-view-your-docs.md)

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