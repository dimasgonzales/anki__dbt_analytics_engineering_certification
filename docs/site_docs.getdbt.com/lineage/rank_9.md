# Source: https://docs.getdbt.com/blog/dbt-explorer

Column-Level Lineage, Model Performance, and Recommendations: ship trusted data products with dbt Explorer | dbt Developer Blog

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

[dbt Docs](/ "dbt Docs")[Developer Blog](/blog "Blog")[Column-Level Lineage, Model Performance, and Recommendations: ship trusted data products with dbt Explorer](# "Column-Level Lineage, Model Performance, and Recommendations: ship trusted data products with dbt Explorer")

On this page

Column-Level Lineage, Model Performance, and Recommendations: ship trusted data products with dbt Explorer
==========================================================================================================

February 13, 2024 · 9 min read

[![Dave Connors](/img/blog/authors/dconnors.jpeg)](/blog/authors/dave-connors)

[Dave Connors](/blog/authors/dave-connors)

Staff Developer Experience Advocate at dbt Labs

What’s in a data platform?[​](#whats-in-a-data-platform "Direct link to What’s in a data platform?")
----------------------------------------------------------------------------------------------------

[Raising a dbt project](https://docs.getdbt.com/blog/how-to-build-a-mature-dbt-project-from-scratch) is hard work. We, as data professionals, have poured ourselves into raising happy healthy data products, and we should be proud of the insights they’ve driven. It certainly wasn’t without its challenges though — we remember the terrible twos, where we worked hard to just get the platform to walk straight. We remember the angsty teenage years where tests kept failing, seemingly just to spite us. A lot of blood, sweat, and tears are shed in the service of clean data!

Once the project could dress and feed itself, we also worked hard to get buy-in from our colleagues who put their trust in our little project. Without deep trust and understanding of what we built, our colleagues who depend on your data (or even those involved in developing it with you — it takes a village after all!) are more likely to be in your DMs with questions than in their BI tools, generating insights.

When our teammates ask about where the data in their reports come from, how fresh it is, or about the right calculation for a metric, what a joy! This means they want to put what we’ve built to good use — the challenge is that, historically, *it hasn’t been all that easy to answer these questions well.* That has often meant a manual, painstaking process of cross checking run logs and your dbt documentation site to get the stakeholder the information they need.

Enter [dbt Explorer](https://www.getdbt.com/product/dbt-explorer)! dbt Explorer centralizes documentation, lineage, and execution metadata to reduce the work required to ship trusted data products faster.

dbt Explorer: an upgrade to data discovery[​](#dbt-explorer-an-upgrade-to-data-discovery "Direct link to dbt Explorer: an upgrade to data discovery")
-----------------------------------------------------------------------------------------------------------------------------------------------------

In the days of yore, answering a question about your data platform may have required a bit of cryptography, sifting through possibly-up-to-date documentation in your internal wiki, run logs to figure out when your models were executed, and slacking the data team member with the most tenure. In the past several years, dbt Docs helped centralize the documentation workflow and dramatically improved the documentation process. While useful, dbt Docs only ever provides a single point in time snapshot, and lacks any sense of your platform’s deployment and execution information. dbt Explorer supercharges the docs experience by providing stateful awareness of your data platform, making support and triage of your platform easier than ever — it even proactively lets you know what to focus on to build even higher quality data products!

### Where’s this data coming from?[​](#wheres-this-data-coming-from "Direct link to Where’s this data coming from?")

Your stakeholders and fellow developers both need a way to orient themselves within your dbt project, and a way to know the full provenance of the number staring at them in their spreadsheet. *Where did this info come from? Does it include XYZ data source, or just ABC?*

It’s the classic stakeholder question for a reason! Knowing data lineage inherently increases your level of trust in the reporting you use to make the right decisions. The dbt DAG has long served as the map of your data flows, tracing the flow from raw data to ready-to-query data mart.

[![Look at that lineage!](/img/blog/2024-02-13-dbt-explorer/full-lineage.png?v=2 "Look at that lineage!")](#)Look at that lineage!

dbt Explorer builds on this experience in three key ways:

* **Lineage 🤝 Docs** - dbt Explorer’s lineage is embedded into the documentation page for each resource, meaning there’s no need to toggle between your DAG and your docs, and lose valuable context. Similarly, when you’re navigating the DAG in full screen mode, clicking on a resource in your project loads a summary panel of the most critical info about the resource you’re interested in (including execution status, data contract info, you name it). Understanding the lineage via the DAG and the context from your written documentation is one workflow in Explorer, not two.
* **Cross project lineage -** if you’re using the new [dbt Mesh](https://www.getdbt.com/product/dbt-mesh) architecture, you may trace your data back to the end of the DAG and find its source is not raw data, but in fact the output of another team’s dbt project! Luckily, dbt Explorer provides first class support for visualizing and understanding cross project lineage when using the dbt Mesh:
  + **Account View + Project DAG:** dbt Explorer provides a higher level view of the relationships between all your projects in your dbt Cloud Account — you can trace the lineage across the projects, and easily drill down into each project. When you click on a project in this view, the side panel includes a list of all the public models available for use. Double clicking opens up the lineage for that specific project, making it easy to traverse across your organization’s knowledge graph!
  + **Cross Project Icons:** When you’re in a project’s lineage, dbt Explorer marks cross-project relationships to make it clear when there are dependencies that span multiple projects. Stakeholders can quickly understand which project owners they may need to contact if they need more information about a dataset.
* **Column level lineage -** long time listeners of the pod know that column level lineage is a frequently requested feature within dbt. It’s one thing to know how data flows between models, but the column level relationships help you understand *precisely* how data is used in models — this makes debugging data issues a lot simpler! We’re stoked to announce that dbt Explorer offers this feature embedded alongside your model lineage as well.

[![You can trace the data in a column from the source to the end of your DAG!](/img/blog/2024-02-13-dbt-explorer/column-level-lineage.png?v=2 "You can trace the data in a column from the source to the end of your DAG!")](#)You can trace the data in a column from the source to the end of your DAG!

With dbt Explorer, you can answer any question about your data’s lineage at any grain, whether its project to project, model to model, or column to column.

### Ok but is it fresh? Is it *right*?[​](#ok-but-is-it-fresh-is-it-right "Direct link to ok-but-is-it-fresh-is-it-right")

Once the data’s journey to your BI tool is clear, there’s a natural second question one would ask before using it — is it, uh, *good data?* Just knowing where it came from is not enough to build trust in the data product — you need to know if it’s timely and accurate.

dbt Explorer marries the execution metadata to the documentation experience — it reflects the latest state of your project across all your job runs in your [production environment,](https://docs.getdbt.com/docs/deploy/deploy-environments#set-as-production-environment) and embeds the execution information throughout the product. For each model, seed, or snapshot, Explorer displays its latest execution status, as well as statuses for any tests run against those resources. Sources show the latest source freshness info, and exposures embed the aggregate test and freshness info right into the details page! No more leaving the docs site to check the most recent logs to see what’s fresh and what’s not — Explorer centralizes everything so you don’t have to!

[![passing model! passing tests!](/img/blog/2024-02-13-dbt-explorer/embedded-metadata-model.png?v=2 "passing model! passing tests!")](#)passing model! passing tests!

[![have you ever seen a fresher source?](/img/blog/2024-02-13-dbt-explorer/embedded-metadata-source.png?v=2 "have you ever seen a fresher source?")](#)have you ever seen a fresher source?

### Is the project healthy? Are we managing it properly?[​](#is-the-project-healthy-are-we-managing-it-properly "Direct link to Is the project healthy? Are we managing it properly?")

Beyond building solid data products and making sure they are trusted and used, developers need to know how they may improve their projects’ quality, or what areas may need some focus for refactoring and optimization in the next quarter. There’s always a balance between maintaining a data platform and adding new features to it. Historically, it’s been hard to know exactly where to invest time and effort to improve the health of your project — dbt Explorer provides two features that shine a light on possible areas for improvement within your project.

#### Recommendations[​](#recommendations "Direct link to Recommendations")

One of dbt’s more popular open source packages is [dbt\_project\_evaluator](https://github.com/dbt-labs/dbt-project-evaluator) , which tests your project against a set of well established dbt best practices. dbt Explorer now surfaces many of the same recommendations directly within the explorer UI using the metadata from the Discovery API, without any need to download and run the package!

Each model and source has a `Recommendations` tab on their resource details page, with specific recommendations on how to improve the quality of that resource. Explorer also offers a global view, showing *****all***** the recommendations across the project, and includes some top level metrics measuring the test and documentation coverage of the models in your project. These recommendations provide insight into how you can build a more well documented, well tested, and well built project, leading to less confusion and more trust.

[![The recommendations summary — I’ve got some work to do!](/img/blog/2024-02-13-dbt-explorer/recommendations.png?v=2 "The recommendations summary — I’ve got some work to do!")](#)The recommendations summary — I’ve got some work to do!

#### Model Performance Trends[​](#model-performance-trends "Direct link to Model Performance Trends")

A huge pain point for analytics engineers is trying to understand if their [dbt models are taking longer or are running less efficiently over time](https://docs.getdbt.com/blog/how-we-shaved-90-minutes-off-model). A model that worked great when your data was small may not work so great when your platform matures! Unless things start to actively break, it can be hard to know where to focus your refactoring work.

dbt Explorer now surfaces model execution metadata to take the guesswork out of fine tuning your dbt runs. There’s a new high level overview page to highlight models that are taking the longest to run, erroring the most, and that have the highest rate of test failures. Each model details page also has a new `Performance` tab, which shows that particular model’s execution history for up to three months of job runs. Spotting an ominous slow increase in runtimes may indicate it’s time for some refactoring — no need to comb through countless `run_results.json` files yourself! dbt Explorer gets you the data you need where you need it.

[![maybe I should check on that one long run!](/img/blog/2024-02-13-dbt-explorer/model-execution.png?v=2 "maybe I should check on that one long run!")](#)maybe I should check on that one long run!

Bon voyage![​](#bon-voyage "Direct link to Bon voyage!")
--------------------------------------------------------

They say the best time to ~~invest~~ ~~plant a tree~~ document your dbt project is yesterday, and the second best time is today. With all the bells and whistles that supercharge your documentation experience in dbt Explorer, there’s no time like the present! Leaning into your documentation and taking advantage of your metadata in dbt Explorer will lead to better data products shipped faster — get out there and explore!

**Tags:**

* [analytics craft](/blog/tags/analytics-craft)

#### Comments

[Start a discussion](https://discourse.getdbt.com/t/12031 "Start a discussion")

[Newer post

LLM-powered Analytics Engineering: How we're using AI inside of our dbt project, today, with no new tools.](/blog/dbt-models-with-snowflake-cortex)[Older post

Serverless, free-tier data stack with dlt + dbt core.](/blog/serverless-dlt-dbt-stack)

* [What’s in a data platform?](#whats-in-a-data-platform)
* [dbt Explorer: an upgrade to data discovery](#dbt-explorer-an-upgrade-to-data-discovery)
  + [Where’s this data coming from?](#wheres-this-data-coming-from)
  + [Ok but is it fresh? Is it *right*?](#ok-but-is-it-fresh-is-it-right)
  + [Is the project healthy? Are we managing it properly?](#is-the-project-healthy-are-we-managing-it-properly)
* [Bon voyage!](#bon-voyage)

#### Live virtual event

Experience the dbt Fusion engine with Tristan Handy and Elias DeFaria on October 28th

[Save your seat](https://www.getdbt.com/resources/webinars/speed-simplicity-cost-savings-experience-the-dbt-fusion-engine "Save your seat")

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