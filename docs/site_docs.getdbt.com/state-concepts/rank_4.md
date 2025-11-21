# Source: https://docs.getdbt.com/docs/build/incremental-models-overview

About incremental models | dbt Developer Hub

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

  + [About dbt projects](/docs/build/projects)
  + [dbt tips and tricks](/docs/build/dbt-tips)
  + [Build your DAG](/docs/build/models)
  + [Build your metrics](/docs/build/build-metrics-intro)
  + [Enhance your models](/docs/build/enhance-your-models)

    - [Enhance your models](/docs/build/enhance-your-models)
    - [Materializations](/docs/build/materializations)
    - [Incremental models](/docs/build/incremental-models-overview)

      * [About incremental models](/docs/build/incremental-models-overview)
      * [Configure incremental models](/docs/build/incremental-models)
      * [Incremental strategy](/docs/build/incremental-strategy)
      * [Microbatch incremental models](/docs/build/incremental-microbatch)
      * [Parallel microbatch execution](/docs/build/parallel-batch-execution)
  + [Enhance your code](/docs/build/enhance-your-code)
  + [Organize your outputs](/docs/build/organize-your-outputs)
  + [Optimize development](/docs/build/empty-flag)
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
* [Cost management](/docs/cloud/cost-management)
* Release information
* [Available dbt versions](/docs/dbt-versions/about-versions)
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [Build dbt projects](/docs/build/projects)
* [Enhance your models](/docs/build/enhance-your-models)
* Incremental models

Copy page

On this page

About incremental models
========================

This is an introduction on incremental models, when to use them, and how they work in dbt.

Incremental models in dbt is a [materialization](/docs/build/materializations) strategy designed to efficiently update your data warehouse tables by only transforming and loading new or changed data since the last run. Instead of processing your entire dataset every time, incremental models append or update only the new rows, significantly reducing the time and resources required for your data transformations.

This page will provide you with a brief overview of incremental models, their importance in data transformations, and the core concepts of incremental materializations in dbt.

[![A visual representation of how incremental models work. Source: Materialization best practices guide (/best-practices/materializations/1-guide-overview)](/img/docs/building-a-dbt-project/incremental-diagram.jpg?v=2 "A visual representation of how incremental models work. Source: Materialization best practices guide (/best-practices/materializations/1-guide-overview)")](#)A visual representation of how incremental models work. Source: Materialization best practices guide (/best-practices/materializations/1-guide-overview)

Learn by video!

For video tutorials on Incremental models, go to dbt Learn and check out the [Incremental models course](https://learn.getdbt.com/courses/incremental-models).

Understand incremental models[​](#understand-incremental-models "Direct link to Understand incremental models")
---------------------------------------------------------------------------------------------------------------

Incremental models enable you to significantly reduce the build time by just transforming new records. This is particularly useful for large datasets, where the cost of processing the entire dataset is high.

Incremental models [require extra configuration](/docs/build/incremental-models) and are an advanced usage of dbt. We recommend using them when your dbt runs are becoming too slow.

### When to use an incremental model[​](#when-to-use-an-incremental-model "Direct link to When to use an incremental model")

Building models as tables in your data warehouse is often preferred for better query performance. However, using `table` materialization can be computationally intensive, especially when:

* Source data has millions or billions of rows.
* Data transformations on the source data are computationally expensive (take a long time to execute) and complex, like when using Regex or UDFs.

Incremental models offer a balance between complexity and improved performance compared to `view` and `table` materializations and offer better performance of your dbt runs.

In addition to these considerations for incremental models, it's important to understand their limitations and challenges, particularly with large datasets. For more insights into efficient strategies, performance considerations, and the handling of late-arriving data in incremental models, refer to the [On the Limits of Incrementality](https://discourse.getdbt.com/t/on-the-limits-of-incrementality/303) discourse discussion or to our [Materialization best practices](/best-practices/materializations/2-available-materializations) page.

### How incremental models work in dbt[​](#how-incremental-models-work-in-dbt "Direct link to How incremental models work in dbt")

dbt's [incremental materialization strategy](/docs/build/incremental-strategy) works differently on different databases. Where supported, a `merge` statement is used to insert new records and update existing records.

On warehouses that do not support `merge` statements, a merge is implemented by first using a `delete` statement to delete records in the target table that are to be updated, and then an `insert` statement.

Transaction management, a process used in certain data platforms, ensures that a set of actions is treated as a single unit of work (or task). If any part of the unit of work fails, dbt will roll back open transactions and restore the database to a good state.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Incremental models](/docs/build/incremental-models) to learn how to configure incremental models in dbt.
* [Incremental strategies](/docs/build/incremental-strategy) to understand how dbt implements incremental models on different databases.
* [Microbatch](/docs/build/incremental-microbatch) to understand a new incremental strategy intended for efficient and resilient processing of very large time-series datasets.
* [Materializations best practices](/best-practices/materializations/1-guide-overview) to learn about the best practices for using materializations in dbt.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/incremental-models-overview.md)

Last updated on **Nov 19, 2025**

[Next

Configure incremental models](/docs/build/incremental-models)

* [Understand incremental models](#understand-incremental-models)
  + [When to use an incremental model](#when-to-use-an-incremental-model)
  + [How incremental models work in dbt](#how-incremental-models-work-in-dbt)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/incremental-models-overview.md)

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