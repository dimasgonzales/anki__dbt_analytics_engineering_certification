# Source: https://docs.getdbt.com/docs/build/exposures

Add Exposures to your DAG | dbt Developer Hub

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

    - [Models](/docs/build/models)
    - [Tests](/docs/build/data-tests)
    - [Documentation](/docs/build/documentation)
    - [Snapshots](/docs/build/snapshots)
    - [Seeds](/docs/build/seeds)
    - [Jinja and macros](/docs/build/jinja-macros)
    - [User-defined functions](/docs/build/udfs)
    - [Sources](/docs/build/sources)
    - [Exposures](/docs/build/exposures)
    - [Groups](/docs/build/groups)
    - [Analyses](/docs/build/analyses)
  + [Build your metrics](/docs/build/build-metrics-intro)
  + [Enhance your models](/docs/build/enhance-your-models)
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
* [Build your DAG](/docs/build/models)
* Exposures

Copy page

On this page

Add Exposures to your DAG
=========================

Exposures make it possible to define and describe a downstream use of your dbt project, such as in a dashboard, application, or data science pipeline. By defining exposures, you can then:

* run, test, and list resources that feed into your exposure
* populate a dedicated page in the auto-generated [documentation](/docs/build/documentation) site with context relevant to data consumers

Exposures can be defined in two ways:

* Manual — Declared [explicitly](/docs/build/exposures#declaring-an-exposure) in your project’s YAML files.
* Automatic — dbt [creates and visualizes downstream exposures](/docs/cloud-integrations/downstream-exposures) automatically for supported integrations, removing the need for manual YAML definitions. These downstream exposures are stored in dbt’s metadata system, appear in [Catalog](/docs/explore/explore-projects), and behave like manual exposures. However, they don’t exist in YAML files.

### Declaring an exposure[​](#declaring-an-exposure "Direct link to Declaring an exposure")

Exposures are defined in `.yml` files nested under an `exposures:` key.

The following example shows an exposure definition in a `models/<filename>.yml` file:

models/<filename>.yml

```
exposures:  
  
  - name: weekly_jaffle_metrics  
    label: Jaffles by the Week  
    type: dashboard  
    maturity: high  
    url: https://bi.tool/dashboards/1  
    description: >  
      Did someone say "exponential growth"?  
  
    depends_on:  
      - ref('fct_orders')  
      - ref('dim_customers')  
      - source('gsheets', 'goals')  
      - metric('count_orders')  
  
    owner:  
      name: Callum McData  
      email: data@jaffleshop.com
```

### Available properties[​](#available-properties "Direct link to Available properties")

*Required:*

* **name**: a unique exposure name written in [snake case](https://en.wikipedia.org/wiki/Snake_case)
* **type**: one of `dashboard`, `notebook`, `analysis`, `ml`, `application` (used to organize in docs site)
* **owner**: `name` or `email` required; additional properties allowed

*Expected:*

* **depends\_on**: list of refable nodes, including `metric`, `ref`, and `source`. While possible, it is highly unlikely you will ever need an `exposure` to depend on a `source` directly.

*Optional:*

* **label**: May contain spaces, capital letters, or special characters.
* **url**: Activates and populates the link to **View this exposure** in the upper right corner of the generated documentation site
* **maturity**: Indicates the level of confidence or stability in the exposure. One of `high`, `medium`, or `low`. For example, you could use `high` maturity for a well-established dashboard, widely used and trusted within your organization. Use `low` maturity for a new or experimental analysis.

*General properties (optional)*

* [**description**](/reference/resource-properties/description)
* [**tags**](/reference/resource-configs/tags)
* [**meta**](/reference/resource-configs/meta)
* [**enabled**](/reference/resource-configs/enabled) — You can set this property at the exposure level or at the project level in the [`dbt_project.yml`](/reference/dbt_project.yml) file.

### Referencing exposures[​](#referencing-exposures "Direct link to Referencing exposures")

Once an exposure is defined, you can run commands that reference it:

```
dbt run -s +exposure:weekly_jaffle_report  
dbt test -s +exposure:weekly_jaffle_report
```

When we generate the [Catalog site](/docs/explore/explore-projects), you'll see the exposure appear:

[![Exposures has a dedicated section, under the 'Resources' tab in dbt Catalog, which lists each exposure in your project.](/img/docs/building-a-dbt-project/dbt-explorer-exposures.jpg?v=2 "Exposures has a dedicated section, under the 'Resources' tab in dbt Catalog, which lists each exposure in your project.")](#)Exposures has a dedicated section, under the 'Resources' tab in dbt Catalog, which lists each exposure in your project.

[![Exposures appear as nodes in the dbt Catalog DAG. It displays an orange 'EXP' indicator within the node. ](/img/docs/building-a-dbt-project/dag-exposures.png?v=2 "Exposures appear as nodes in the dbt Catalog DAG. It displays an orange 'EXP' indicator within the node. ")](#)Exposures appear as nodes in the dbt Catalog DAG. It displays an orange 'EXP' indicator within the node.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Exposure properties](/reference/exposure-properties)
* [`exposure:` selection method](/reference/node-selection/methods#exposure)
* [Data health tiles](/docs/explore/data-tile)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/exposures.md)

Last updated on **Nov 19, 2025**

[Previous

Sources](/docs/build/sources)[Next

Groups](/docs/build/groups)

* [Declaring an exposure](#declaring-an-exposure)
* [Available properties](#available-properties)
* [Referencing exposures](#referencing-exposures)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/exposures.md)

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