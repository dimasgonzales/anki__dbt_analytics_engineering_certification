# Source: https://docs.getdbt.com/best-practices/materializations/3-configuring-materializations

Configuring materializations | dbt Developer Hub

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
* [Materialization best practices](/best-practices/materializations/1-guide-overview)
* Configuring materializations

Copy page

On this page

Configuring materializations
============================

Configuring materializations[​](#configuring-materializations "Direct link to Configuring materializations")
------------------------------------------------------------------------------------------------------------

Choosing which materialization is as simple as setting any other configuration in dbt. We’ll look first at how we select our materializations for individual models, then at more powerful ways of setting materializations for entire folders of models.

### Configuring tables and views[​](#configuring-tables-and-views "Direct link to Configuring tables and views")

Let’s look at how we can use tables and views to get started with materializations:

* ⚙️ We can configure an individual model’s materialization using a **Jinja `config` block**, and passing in the **`materialized` argument**. This tells dbt what materialization to use.
* 🚰 The underlying specifics of what is run depends on [which **adapter** you’re using](/docs/supported-data-platforms), but the end results will be equivalent.
* 😌 This is one of the many valuable aspects of dbt: it lets us use a **declarative** approach, specifying the *outcome* that we want in our code, rather than *specific steps* to achieve it (the latter is an *imperative* approach if you want to get computer science-y about it 🤓).
* 🔍 In the below case, we want to create a SQL **view**, and can **declare** that in a **single line of code**. Note that python models [do not support materializing as views](/docs/build/materializations#python-materializations) at this time.

```
    {{  
        config(  
            materialized='view'  
        )  
    }}  
  
    select ...
```

info

🐍 **Not all adapters support python yet**, check the [docs here to be sure](/docs/build/python-models#specific-data-platforms) before spending time writing python models.

* Configuring a model to materialize as a `table` is simple, and possible for both SQL and python models.

* SQL
* Python

```
{{  
    config(  
        materialized='table'  
    )  
}}  
  
select ...
```

```
def model(dbt, session):  
  
    dbt.config(materialized="table")  
  
    # model logic  
  
    return model_df
```

Go ahead and try some of these out!

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/materializations/materializations-guide-3-configuring-materializations.md)

Last updated on **Nov 19, 2025**

[Previous

Available materializations](/best-practices/materializations/2-available-materializations)[Next

Incremental models in-depth](/best-practices/materializations/4-incremental-models)

* [Configuring materializations](#configuring-materializations)
  + [Configuring tables and views](#configuring-tables-and-views)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/materializations/materializations-guide-3-configuring-materializations.md)

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