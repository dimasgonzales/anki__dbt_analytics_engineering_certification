# Source: https://docs.getdbt.com/blog/to-defer-or-to-clone

To defer or to clone, that is the question | dbt Developer Blog

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

[dbt Docs](/ "dbt Docs")[Developer Blog](/blog "Blog")[To defer or to clone, that is the question](# "To defer or to clone, that is the question")

On this page

To defer or to clone, that is the question
==========================================

October 31, 2023 · 6 min read

[![Kshitij Aranke](/img/blog/authors/kshitij-aranke.jpg)](/blog/authors/kshitij-aranke)

[Kshitij Aranke](/blog/authors/kshitij-aranke)

Senior Software Engineer at dbt Labs

[![Doug Beatty](/img/blog/authors/dbeatty.jpeg)](/blog/authors/doug-beatty)

[Doug Beatty](/blog/authors/doug-beatty)

Senior Developer Experience Advocate at dbt Labs

Hi all, I’m Kshitij, a senior software engineer on the Core team at dbt Labs.
One of the coolest moments of my career here thus far has been shipping the new `dbt clone` command as part of the dbt-core v1.6 release.

However, one of the questions I’ve received most frequently is guidance around “when” to clone that goes beyond [the documentation on “how” to clone](https://docs.getdbt.com/reference/commands/clone).
In this blog post, I’ll attempt to provide this guidance by answering these FAQs:

1. What is `dbt clone`?
2. How is it different from deferral?
3. Should I defer or should I clone?

What is `dbt clone`?[​](#what-is-dbt-clone "Direct link to what-is-dbt-clone")
------------------------------------------------------------------------------

`dbt clone` is a new command in dbt 1.6 that leverages native zero-copy clone functionality on supported warehouses to **copy entire schemas for free, almost instantly**.

### How is this possible?[​](#how-is-this-possible "Direct link to How is this possible?")

Well, the warehouse “cheats” by only copying metadata from the `source` schema to the `target` schema; the underlying data remains at rest during this operation.
This metadata includes materialized objects like tables and views, which is why you see a **clone** of these objects in the target schema.

In computer science jargon, `clone` makes a copy of the pointer from the `source` schema to the underlying data; after the operation there are now two pointers (`source` and `target` schemas) that each point to the same underlying data.

How is cloning different from deferral?[​](#how-is-cloning-different-from-deferral "Direct link to How is cloning different from deferral?")
--------------------------------------------------------------------------------------------------------------------------------------------

On the surface, cloning and deferral seem similar – **they’re both ways to save costs in the data warehouse.**
They do this by bypassing expensive model re-computations – clone by [eagerly copying](https://en.wikipedia.org/wiki/Evaluation_strategy#Eager_evaluation) an entire schema into the target schema, and defer by [lazily referencing](https://en.wikipedia.org/wiki/Lazy_evaluation) pre-built models in the source schema.

Let’s unpack this sentence and explore its first-order effects:

|  | defer | clone |
| --- | --- | --- |
| **How do I use it?** | Implicit via the `--defer` flag | Explicit via the `dbt clone` command |
| **What are its outputs?** | Doesn't create any objects itself, but dbt might create objects in the target schema if they’ve changed from those in the source schema. | Copies objects from source schema to target schema in the data warehouse, which are persisted after operation is finished. |
| **How does it work?** | Compares manifests between source and target dbt runs and overrides ref to resolve models not built in the target run to point to objects built in the source run. | Uses zero-copy cloning if available to copy objects from source to target schemas, else creates pointer views (`select * from my_model`) |

These first-order effects lead to the following second-order effects that truly distinguish clone and defer from each other:

|  | defer | clone |
| --- | --- | --- |
| **Where can I use objects built in the target schema?** | Only within the context of dbt | Any downstream tool (e.g. BI) |
| **Can I safely modify objects built in the target schema?** | No, since this would modify production data | Yes, cloning is a cheap way to create a sandbox of production data for experimentation |
| **Will data in the target schema drift from data in the source schema?** | No, since deferral will always point to the latest version of the source schema | Yes, since clone is a point-in-time operation |
| **Can I use multiple source schemas at once?** | Yes, defer can dynamically switch between source schemas e.g. ref unchanged models from production and changed models from staging | No, clone copies objects from one source schema to one target schema |

Should I defer or should I clone?[​](#should-i-defer-or-should-i-clone "Direct link to Should I defer or should I clone?")
--------------------------------------------------------------------------------------------------------------------------

Putting together all the points above, here’s a handy cheat sheet for when to defer and when to clone:

|  | defer | clone |
| --- | --- | --- |
| **Save time & cost by avoiding re-computation** | ✅ | ✅ |
| **Create database objects to be available in downstream tools (e.g. BI)** | ❌ | ✅ |
| **Safely modify objects in the target schema** | ❌ | ✅ |
| **Avoid creating new database objects** | ✅ | ❌ |
| **Avoid data drift** | ✅ | ❌ |
| **Support multiple dynamic sources** | ✅ | ❌ |

To absolutely drive this point home:

1. If you send someone this cheatsheet by linking to this page, you are deferring to this page
2. If you print out this page and write notes in the margins, you have cloned this page

Putting it in practice[​](#putting-it-in-practice "Direct link to Putting it in practice")
------------------------------------------------------------------------------------------

Using the cheat sheet above, let’s explore a few common scenarios and explore whether we should use defer or clone for each:

1. **Testing staging datasets in BI**

   In this scenario, we want to:

   1. Make a copy of our production dataset available in our downstream BI tool
   2. To safely iterate on this copy without breaking production datasets

   Therefore, we should use **clone** in this scenario.
2. **[Slim CI](https://discourse.getdbt.com/t/how-we-sped-up-our-ci-runs-by-10x-using-slim-ci/2603)**

   In this scenario, we want to:

   1. Refer to production models wherever possible to speed up continuous integration (CI) runs
   2. Only run and test models in the CI staging environment that have changed from the production environment
   3. Reference models from different environments – prod for unchanged models, and staging for modified models

   Therefore, we should use **defer** in this scenario.

Use `dbt clone` in CI jobs to test incremental models

Learn how to [use `dbt clone` in CI jobs](/best-practices/clone-incremental-models) to efficiently test modified incremental models, simulating post-merge behavior while avoiding full-refresh costs.

3. **[Blue/Green Deployments](https://discourse.getdbt.com/t/performing-a-blue-green-deploy-of-your-dbt-project-on-snowflake/1349)**

   In this scenario, we want to:

   1. Ensure that all tests are always passing on the production dataset, even if that dataset is slightly stale
   2. Atomically rollback a promotion to production if tests aren’t passing across the entire staging dataset

   In this scenario, we can use **clone** to implement a deployment strategy known as blue-green deployments where we build the entire staging dataset and then run tests against it, and only clone it over to production if all tests pass.

As a rule of thumb, deferral lends itself better to continuous integration (CI) use cases whereas cloning lends itself better to continuous deployment (CD) use cases.

Wrapping Up[​](#wrapping-up "Direct link to Wrapping Up")
---------------------------------------------------------

In this post, we covered what `dbt clone` is, how it is different from deferral, and when to use each. Often, they can be used together within the same project in different parts of the deployment lifecycle.

Thanks for reading, and I look forward to seeing what you build with `dbt clone`.

*Thanks to [Jason Ganz](https://docs.getdbt.com/author/jason_ganz) and [Gwen Windflower](https://www.linkedin.com/in/gwenwindflower/) for reviewing drafts of this article*

**Tags:**

* [analytics craft](/blog/tags/analytics-craft)

#### Comments

![Loading](/img/loader-icon.svg)

[Newer post

Why you should specify a production environment in dbt Cloud](/blog/specify-prod-environment)[Older post

Optimizing Materialized Views with dbt](/blog/announcing-materialized-views)

* [What is `dbt clone`?](#what-is-dbt-clone)
  + [How is this possible?](#how-is-this-possible)
* [How is cloning different from deferral?](#how-is-cloning-different-from-deferral)
* [Should I defer or should I clone?](#should-i-defer-or-should-i-clone)
* [Putting it in practice](#putting-it-in-practice)
* [Wrapping Up](#wrapping-up)

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