# Source: https://docs.getdbt.com/reference/commands/clone

About dbt clone command | dbt Developer Hub

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

* [About References](/reference/references-overview)
* [Project configs](/category/project-configs)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)
* [Commands](/reference/dbt-commands)

  + [dbt Command reference](/reference/dbt-commands)
  + [List of commands](/category/list-of-commands)

    - [build](/reference/commands/build)
    - [clean](/reference/commands/clean)
    - [clone](/reference/commands/clone)
    - [docs](/reference/commands/cmd-docs)
    - [compile](/reference/commands/compile)
    - [debug](/reference/commands/debug)
    - [deps](/reference/commands/deps)
    - [environment](/reference/commands/dbt-environment)
    - [init](/reference/commands/init)
    - [invocation](/reference/commands/invocation)
    - [ls (list)](/reference/commands/list)
    - [parse](/reference/commands/parse)
    - [retry](/reference/commands/retry)
    - [rpc](/reference/commands/rpc)
    - [run](/reference/commands/run)
    - [run-operation](/reference/commands/run-operation)
    - [seed](/reference/commands/seed)
    - [show](/reference/commands/show)
    - [snapshot](/reference/commands/snapshot)
    - [source](/reference/commands/source)
    - [test](/reference/commands/test)
    - [version](/reference/commands/version)
  + [Node selection](/reference/node-selection/syntax)
  + [Flags (global configs)](/reference/global-configs/about-global-configs)
  + [Events and logs](/reference/events-logging)
  + [Exit codes](/reference/exit-codes)
  + [Deprecations](/reference/deprecations)
  + [Project Parsing](/reference/parsing)
  + [Programmatic invocations](/reference/programmatic-invocations)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Commands](/reference/dbt-commands)
* [List of commands](/category/list-of-commands)
* clone

Copy page

On this page

About dbt clone command
=======================

The `dbt clone` command clones selected nodes from the [specified state](/reference/node-selection/syntax#establishing-state) to the target schema(s). This command makes use of the `clone` materialization:

* If your data platform supports zero-copy cloning of tables (Snowflake, Databricks, or BigQuery), and this model exists as a table in the source environment, dbt will create it in your target environment as a clone.
* Otherwise, dbt will create a simple pointer view (`select * from` the source object)
* By default, `dbt clone` will not recreate pre-existing relations in the current target. To override this, use the `--full-refresh` flag.
* You may want to specify a higher number of [threads](/docs/running-a-dbt-project/using-threads) to decrease execution time since individual clone statements are independent of one another.

The `clone` command is useful for:

* blue/green continuous deployment (on data warehouses that support zero-copy cloning tables)
* cloning current production state into development schema(s)
* handling incremental models in dbt CI jobs (on data warehouses that support zero-copy cloning tables)
* testing code changes on downstream dependencies in your BI tool

```
# clone all of my models from specified state to my target schema(s)  
dbt clone --state path/to/artifacts  
  
# clone one_specific_model of my models from specified state to my target schema(s)  
dbt clone --select "one_specific_model" --state path/to/artifacts  
  
# clone all of my models from specified state to my target schema(s) and recreate all pre-existing relations in the current target  
dbt clone --state path/to/artifacts --full-refresh  
  
# clone all of my models from specified state to my target schema(s), running up to 50 clone statements in parallel  
dbt clone --state path/to/artifacts --threads 50
```

### When to use `dbt clone` instead of [deferral](/reference/node-selection/defer)?[​](#when-to-use-dbt-clone-instead-of-deferral "Direct link to when-to-use-dbt-clone-instead-of-deferral")

Unlike deferral, `dbt clone` requires some compute and creation of additional objects in your data warehouse. In many cases, deferral is a cheaper and simpler alternative to `dbt clone`. However, `dbt clone` covers additional use cases where deferral may not be possible.

For example, by creating actual data warehouse objects, `dbt clone` allows you to test out your code changes on downstream dependencies *outside of dbt* (such as a BI tool).

As another example, you could `clone` your modified incremental models as the first step of your dbt CI job to prevent costly `full-refresh` builds for warehouses that support zero-copy cloning.

Cloning in dbt[​](#cloning-in-dbt "Direct link to Cloning in dbt")
------------------------------------------------------------------

You can clone nodes between states in dbt using the `dbt clone` command. This is available in the [Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud) and the [Cloud CLI](/docs/cloud/cloud-cli-installation) and relies on the [`--defer`](/reference/node-selection/defer) feature. For more details on defer in dbt, read [Using defer in dbt](/docs/cloud/about-cloud-develop-defer).

* **Using Cloud CLI** — The `dbt clone` command in the Cloud CLI automatically includes the `--defer` flag. This means you can use the `dbt clone` command without any additional setup.
* **Using Studio IDE** — To use the `dbt clone` command in the Studio IDE, follow these steps before running the `dbt clone` command:

  + Set up your **Production environment** and have a successful job run.
  + Enable **Defer to production** by toggling the switch in the lower-right corner of the command bar.

    [![Select the 'Defer to production' toggle on the bottom right of the command bar to enable defer in the Studio IDE.](/img/docs/dbt-cloud/defer-toggle.png?v=2 "Select the 'Defer to production' toggle on the bottom right of the command bar to enable defer in the Studio IDE.")](#)Select the 'Defer to production' toggle on the bottom right of the command bar to enable defer in the Studio IDE.
  + Run the `dbt clone` command from the command bar.

Check out [this Developer blog post](/blog/to-defer-or-to-clone) for more details on best practices when to use `dbt clone` vs. deferral.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/clone.md)

Last updated on **Nov 19, 2025**

[Previous

clean](/reference/commands/clean)[Next

docs](/reference/commands/cmd-docs)

* [When to use `dbt clone` instead of deferral?](#when-to-use-dbt-clone-instead-of-deferral)
* [Cloning in dbt](#cloning-in-dbt)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/clone.md)

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