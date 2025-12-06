# Source: https://docs.getdbt.com/best-practices/materializations/1-guide-overview

Materializations best practices | dbt Developer Hub

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

* [Best practices](/best-practices)

  + [How we structure our dbt projects](/best-practices/how-we-structure/1-guide-overview)
  + [How we style our dbt projects](/best-practices/how-we-style/0-how-we-style-our-dbt-projects)
  + [How we build our metrics](/best-practices/how-we-build-our-metrics/semantic-layer-1-intro)
  + [How we build our dbt Mesh projects](/best-practices/how-we-mesh/mesh-1-intro)
  + [Materialization best practices](/best-practices/materializations/1-guide-overview)

    - [Available materializations](/best-practices/materializations/2-available-materializations)
    - [Configuring materializations](/best-practices/materializations/3-configuring-materializations)
    - [Incremental models in-depth](/best-practices/materializations/4-incremental-models)
    - [Best practices for materializations](/best-practices/materializations/5-best-practices)
    - [Examining our builds](/best-practices/materializations/6-examining-builds)
    - [Conclusion](/best-practices/materializations/7-conclusion)
  + [Don't nest your curlies](/best-practices/dont-nest-your-curlies)
  + [Clone incremental models as the first step of your CI job](/best-practices/clone-incremental-models)
  + [Writing custom generic data tests](/best-practices/writing-custom-generic-tests)
  + [Best practices for workflows](/best-practices/best-practice-workflows)
  + [Best practices for dbt and Unity Catalog](/best-practices/dbt-unity-catalog-best-practices)

* [Best practices](/best-practices)
* Materialization best practices

Copy page

On this page

Materializations best practices
===============================

What *really* happens when you type `dbt build`? Contrary to popular belief, a crack team of microscopic data elves do *not* construct your data row by row, although the truth feels equally magical. This guide explores the real answer to that question, with an introductory look at the objects that get built into your warehouse, why they matter, and how dbt knows what to build.

Learn by video!

For video tutorials on Snapshots, go to dbt Learn and check out the [Snapshots course](https://learn.getdbt.com/courses/snapshots).

The configurations that tell dbt how to construct these objects are called *materializations,* and knowing how to use them is a crucial skill for effective analytics engineering. When you’ve completed this guide, you will have that ability to use the three core materializations that cover most common analytics engineering situations.

info

😌 **Materializations abstract away DDL and DML**. Typically in raw SQL- or python-based [data transformation](https://www.getdbt.com/analytics-engineering/transformation/), you have to write specific imperative instructions on how to build or modify your data objects. dbt’s materializations make this declarative, we tell dbt how we want things to be constructed and it figures out how to do that given the unique conditions and qualities of our warehouse.

### Learning goals[​](#learning-goals "Direct link to Learning goals")

By the end of this guide you should have a solid understanding of:

* 🛠️ what **materializations** are
* 👨‍👨‍👧 how the three main materializations that ship with dbt — **table**, **view**, and **incremental** — differ
* 🗺️ **when** and **where** to use specific materializations to optimize your development and production builds
* ⚙️ how to **configure materializations** at various scopes, from an individual model to entire folder

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* 📒 You’ll want to have worked through the [quickstart guide](/guides) and have a project setup to work through these concepts.
* 🏃🏻‍♀️ Concepts like dbt runs, `ref()` statements, and models should be familiar to you.
* 🔧 [**Optional**] Reading through the [How we structure our dbt projects](/best-practices/how-we-structure/1-guide-overview) Guide will be beneficial for the last section of this guide, when we review best practices for materializations using the dbt project approach of staging models and marts.

### Guiding principle[​](#guiding-principle "Direct link to Guiding principle")

We’ll explore this in-depth throughout, but the basic guideline is **start as simple as possible**. We’ll follow a tiered approached, only moving up a tier when it’s necessary.

* 🔍 **Start with a view.** When the view gets too long to *query* for end users,
* ⚒️ **Make it a table.** When the table gets too long to *build* in your dbt Jobs,
* 📚 **Build it incrementally.** That is, layer the data on in chunks as it comes in.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/materializations/materializations-guide-1-guide-overview.md)

Last updated on **Nov 19, 2025**

[Previous

dbt Mesh FAQs](/best-practices/how-we-mesh/mesh-5-faqs)[Next

Available materializations](/best-practices/materializations/2-available-materializations)

* [Learning goals[​](#learning-goals "Direct link to Learning goals")](#learning-goals)
* [Prerequisites[​](#prerequisites "Direct link to Prerequisites")](#prerequisites)
* [Guiding principle[​](#guiding-principle "Direct link to Guiding principle")](#guiding-principle)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/materializations/materializations-guide-1-guide-overview.md)

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