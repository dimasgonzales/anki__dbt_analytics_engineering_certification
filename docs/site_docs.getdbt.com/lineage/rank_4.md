# Source: https://docs.getdbt.com/guides/explorer-quickstart

Quickstart for the dbt Catalog workshop | dbt Developer Hub

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

Copy page

Quickstart for the dbt Catalog workshop
=======================================

[Back to guides](/guides)

Explorer

Snowflake

dbt platform

Quickstart

Catalog

Beginner

Menu




Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

Unlock the power of [Catalog](/docs/explore/explore-projects) in this hands-on workshop designed for analytics engineers, data analysts, stakeholders, and data leaders.

This quickstart guide accompanies the Catalog hands-on workshop and helps you dive into a production-level Mesh implementation and discover how to explore your data workflows.⁠ Whether you're looking to streamline your data operations, improve data quality, or self-serve information about your data platform, this workshop will equip you with the tools and knowledge to take your dbt projects to the next level.

By the end of the guide and workshop, you'll understand how to leverage Catalog and have the confidence to navigate multiple dbt projects, trace dependencies, and identify opportunities to improve performance and data quality.

### What you'll learn[​](#what-youll-learn "Direct link to What you'll learn")

In this guide, you will learn how to:

* Navigate multiple dbt projects using Catalog
* Self-serve on data documentation
* Trace dependencies at the model and column level
* Identify opportunities to improve performance and data quality

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Familiarity with data platforms

Setup[​](#setup "Direct link to Setup")
---------------------------------------

Now we’ll be creating your dbt account and connecting it to a data warehouse.

1. Go to this URL (sign out if you're already logged in): <https://cloud.getdbt.com/coalesce-workshop-signup>
2. Enter your first name and last name.
3. Select the **Exploring a Mesh implementation with Catalog** option.
4. Use the passcode provided by the workshop facilitator.
5. Agree to the terms of service and click the **Complete Registration** button.
6. Wait about 30 seconds, you’ll be in the dbt account for this workshop and already connected to a data warehouse.
7. Toggle into the **Platform project**. Go to the **Orchestration** tab and select **Jobs** from the dropdown menu.
8. Run each job you see by clicking on the job and then selecting **Run now**. This will run the *upstream* project job in both a production and staging environment.
9. Toggle into the **Analytics project**. Go to the **Orchestration** tab and select **Jobs** from the dropdown menu.
10. Run each job you see by clicking on the job and then selecting **Run now**. This will run the *downstream* project job in both a production and staging environment.

[![Run the jobs](/img/quickstarts/dbt-cloud/run_job.png?v=2 "Run the jobs")](#)Run the jobs

Performance[​](#performance "Direct link to Performance")
---------------------------------------------------------

[![dbt Catalog's Performance tab](/img/quickstarts/dbt-cloud/explorer_performance_tab.png?v=2 "dbt Catalog's Performance tab")](#)dbt Catalog's Performance tab

Catalog will show you your project's most executed models, longest model executions, most failed models and tests, and most consumed models all in one place: The performance tab.

### Hands-On[​](#hands-on "Direct link to Hands-On")

* Trigger the Daily Prod job to run again.
* Explore the **Performance** tab on the **Project details** page.
  + Which model took the longest over the last two weeks? Over the last month?
  + Which model failed the most tests?
  + Click on the model that took the longest to run in the *Longest model executions* graph.
    - What is the average duration time over the last two weeks? Over the last month?
    - How often is the model being built? What is the Model Test Failure Rate?

Resources[​](#resources "Direct link to Resources")
---------------------------------------------------

With Catalog, you can view your project's resources (such as models, tests, and metrics), their lineage, and model consumption to gain a better understanding of its latest production state.

Navigate and manage your projects within dbt to help you and other data developers, analysts, and consumers discover and leverage your dbt resources.

[![dbt Catalog's Models tab](/img/quickstarts/dbt-cloud/explorer_models_tab.png?v=2 "dbt Catalog's Models tab")](#)dbt Catalog's Models tab

### Hands-On[​](#hands-on-1 "Direct link to Hands-On")

* Explore the **Model** tab
  + Pick a model. What’s its row count?
  + Use the test results drop down to see if this model’s tests passed. What other models does it depend on?
* Explore the **Tests** tab
  + What tests do we see? Which tests have warnings? Failures?
* Explore the **Sources** tab
  + What sources can we see? Which sources have stale data? Which sources have fresh data?
* Explore **Exposures**
  + Use the lineage graph to find an exposure. Which models and metrics does the Exposure reference?

Lineage[​](#lineage "Direct link to Lineage")
---------------------------------------------

Catalog provides a visualization of your project’s DAG that you can interact with. The nodes in the lineage graph represent the project’s resources and the edges represent the relationships between the nodes. Nodes are color-coded and include iconography according to their resource type.

* Use the search bar and [node selectors](/reference/node-selection/syntax) to filter your DAG.
* [Lenses](/docs/explore/explore-projects#lenses) make it easier to understand your project’s contextual metadata at scales, especially to distinguish a particular model or a subset of models.
  + Applying a lens adds tags to the nodes, showing metadata like layer values, with color coding to help you distinguish them.

[![dbt Catalog's lineage graph](/img/quickstarts/dbt-cloud/dbt_explorer_dag.png?v=2 "dbt Catalog's lineage graph")](#)dbt Catalog's lineage graph

* Use the [advanced search](/docs/explore/explore-projects#search-resources) feature to locate resources in your project.
  + Perform hard searches and keyword searches.
  + All resource names, column names, resource descriptions, warehouse relations, and code matching your search criteria will appear in the center of the page.
  + Apply filters to fully refine your search.
* When searching for a column name, the results show all relational nodes containing that column in their schemas.

[![dbt Catalog's advanced search feature](/img/quickstarts/dbt-cloud/dbt_explorer_advanced_search.png?v=2 "dbt Catalog's advanced search feature")](#)dbt Catalog's advanced search feature

### Hands-On[​](#hands-on-2 "Direct link to Hands-On")

* Explore **Project-Level lineage**
  + Pick a model and review its upstream and downstream dependencies
  + Which sources does this model depend on? Which models depend on this model?
* Explore **Lenses**
  + Apply the Test Status Lenses. Which models passed tests? Which had warnings?
  + Explore different lenses (Model Layer, Materialization Type, Resource). What information do you see?
* Explore **Column-Level Lineage**
  + Navigate to the model’s **Model resource** page and explore the primary key column’s **Column-Level Lineage**

Multi-project[​](#multi-project "Direct link to Multi-project")
---------------------------------------------------------------

Use Catalog to gain a deeper understanding of *all* your dbt projects with its [multi-project capabilities](/docs/explore/explore-multiple-projects).

* See the number of public, protected, and private models, as well as metrics for each project.
* View cross-project lineage and navigate between individual projects’ lineage graphs.
* Explore column-level lineage across projects.

### Hands-On[​](#hands-on-3 "Direct link to Hands-On")

* In the lineage graph, filter the Platform Project’s Project-Level Lineage for Public models using the `access:public` filter
  + Make a note of which models are referenced by the analytics project.
* Explore the Analytics Project’s lineage
  + Choose a model in the Platform project referenced by the Analytics project.
  + Look at the multi-project column-level lineage of its primary key column.
  + Open the Analytics project’s lineage graph. Which models does it reference?

Project recommendations[​](#project-recommendations "Direct link to Project recommendations")
---------------------------------------------------------------------------------------------

These recommendations are designed to build trust in your project and reduce confusion.

To learn more about the specific suggestions and the reasons behind them, check out [our docs](/docs/explore/project-recommendations).

[![dbt Catalog's project recommendation tab](/img/quickstarts/dbt-cloud/dbt_explorer_project_recs.png?v=2 "dbt Catalog's project recommendation tab")](#)dbt Catalog's project recommendation tab

### Hands-On[​](#hands-on-4 "Direct link to Hands-On")

* Review your project recommendations.
* Find the project recommendation for the model `agg_daily_returned_orders`.
* Add documentation to this model in the `aggregates.yml` file.

What's next[​](#whats-next "Direct link to What's next")
--------------------------------------------------------

Congratulations! You've completed the Catalog workshop. You now have the tools and knowledge to navigate multiple dbt projects, trace dependencies, and identify opportunities to improve performance and data quality.

You've learned how to:

* Use Catalog to visualize your project’s lineage and interact with the DAG
* Search for resources in your project and apply filters to refine your search
* Explore lenses and find table materializations in your current project
* Navigate multiple dbt projects using Catalog
* Trace dependencies at the model and column level
* Review project recommendations and implement improvements

For the next steps, you can check out the [Catalog documentation](/docs/explore/explore-projects) and [FAQs](/docs/explore/dbt-explorer-faqs) to learn more about how to use Catalog.

Keep an eye out for new features coming out soon, like:

* [Visualize downstream exposures](/docs/cloud-integrations/downstream-exposures-tableau) integrations (like Tableau).
* [Model query history](/docs/explore/model-query-history) for additional warehouses (like Redshift and Databricks)
* Improvements to [data health tiles](/docs/explore/data-tile)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [Explorer](/tags/explorer)
* [Snowflake](/tags/snowflake)
* [dbt platform](/tags/dbt-platform)
* [Quickstart](/tags/quickstart)
* [Catalog](/tags/catalog)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/guides/explorer-qs.md)

Last updated on **Nov 19, 2025**

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