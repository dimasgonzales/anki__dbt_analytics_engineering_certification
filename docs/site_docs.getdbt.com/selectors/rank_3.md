# Source: https://docs.getdbt.com/reference/node-selection/graph-operators

Graph operators | dbt Developer Hub

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

* [About References](/reference/references-overview)
* [Project configs](/category/project-configs)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)
* [Commands](/reference/dbt-commands)

  + [dbt Command reference](/reference/dbt-commands)
  + [List of commands](/category/list-of-commands)
  + [Node selection](/reference/node-selection/syntax)

    - [Syntax overview](/reference/node-selection/syntax)
    - [Exclude](/reference/node-selection/exclude)
    - [Defer](/reference/node-selection/defer)
    - [Graph operators](/reference/node-selection/graph-operators)
    - [Set operators](/reference/node-selection/set-operators)
    - [Node selector methods](/reference/node-selection/methods)
    - [Putting it together](/reference/node-selection/putting-it-together)
    - [YAML Selectors](/reference/node-selection/yaml-selectors)
    - [Test selection examples](/reference/node-selection/test-selection-examples)
    - [About state selection](/reference/node-selection/state-selection)
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
* [Node selection](/reference/node-selection/syntax)
* Graph operators

Copy page

On this page

Graph operators
===============

### The "plus" operator[​](#the-plus-operator "Direct link to The \"plus\" operator")

The `+` operator expands your selection to include ancestors (upstream dependencies) or descendants (downstream dependencies) of a resource. This operator works for individual models, tags, and other resources.

* Placed after a model/resource — Includes the resource itself and all its descendants (downstream dependencies).
* Placed before a model/resource — Includes the resource itself and all its ancestors (upstream dependencies).
* Placed on both sides of a model/resource — Includes the resource itself, all its ancestors, and all its descendants.

```
dbt run --select "my_model+"         # select my_model and all descendants  
dbt run --select "+my_model"         # select my_model and all ancestors  
dbt run --select "+my_model+"        # select my_model, and all of its ancestors and descendants
```

You can use it with selectors for a more specific scope in your commands. You can also combine it with [`--exclude`](/reference/node-selection/exclude) flag for even more finer control over what gets included in your command.

### The "n-plus" operator[​](#the-n-plus-operator "Direct link to The \"n-plus\" operator")

You can adjust the behavior of the `+` operator by quantifying the number of edges
to step through.

```
dbt run --select "my_model+1"        # select my_model and its first-degree descendants  
dbt run --select "2+my_model"        # select my_model, its first-degree ancestors ("parents"), and its second-degree ancestors ("grandparents")  
dbt run --select "3+my_model+4"      # select my_model, its ancestors up to the 3rd degree, and its descendants down to the 4th degree
```

### The "at" operator[​](#the-at-operator "Direct link to The \"at\" operator")

The `@` operator is similar to `+`, but will also include *all ancestors of all descendants of the selected model*. This is useful in continuous integration environments where you want to build a model and all of its descendants, but the *ancestors* of those descendants might not exist in the schema yet. The `@` operator (which can only be placed at the front of the model name) will select as many degrees of ancestors ("parents," "grandparents," and so on) as is needed to successfully build all descendants of the specified model.

The selector `@snowplow_web_page_context` will build all three models shown in the diagram below.

[![@snowplow_web_page_context will select all of the models shown here](/img/docs/running-a-dbt-project/command-line-interface/1643e30-Screen_Shot_2019-03-11_at_7.18.20_PM.png?v=2 "@snowplow_web_page_context will select all of the models shown here")](#)@snowplow\_web\_page\_context will select all of the models shown here

```
dbt run --select "@my_model"         # select my_model, its descendants, and the ancestors of its descendants
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/graph-operators.md)

Last updated on **Nov 19, 2025**

[Previous

Defer](/reference/node-selection/defer)[Next

Set operators](/reference/node-selection/set-operators)

* [The "plus" operator[​](#the-plus-operator "Direct link to The \"plus\" operator")](#the-plus-operator)
* [The "n-plus" operator[​](#the-n-plus-operator "Direct link to The \"n-plus\" operator")](#the-n-plus-operator)
* [The "at" operator[​](#the-at-operator "Direct link to The \"at\" operator")](#the-at-operator)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/node-selection/graph-operators.md)

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