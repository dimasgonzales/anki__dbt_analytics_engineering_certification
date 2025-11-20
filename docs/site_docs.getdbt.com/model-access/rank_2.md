# Source: https://docs.getdbt.com/reference/resource-configs/access

access | dbt Developer Hub

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

  + [About resource paths](/reference/resource-configs/resource-path)
  + [Configs and properties](/reference/configs-and-properties)
  + [General properties](/category/general-properties)
  + [General configs](/category/general-configs)

    - [Advanced usage](/reference/advanced-config-usage)
    - [access](/reference/resource-configs/access)
    - [alias](/reference/resource-configs/alias)
    - [database](/reference/resource-configs/database)
    - [docs](/reference/resource-configs/docs)
    - [enabled](/reference/resource-configs/enabled)
    - [event\_time](/reference/resource-configs/event-time)
    - [full\_refresh](/reference/resource-configs/full_refresh)
    - [grants](/reference/resource-configs/grants)
    - [group](/reference/resource-configs/group)
    - [meta](/reference/resource-configs/meta)
    - [persist\_docs](/reference/resource-configs/persist_docs)
    - [Using the + prefix](/reference/resource-configs/plus-prefix)
    - [pre-hook & post-hook](/reference/resource-configs/pre-hook-post-hook)
    - [schema](/reference/resource-configs/schema)
    - [static\_analysis](/reference/resource-configs/static-analysis)
    - [tags](/reference/resource-configs/tags)
    - [unique\_key](/reference/resource-configs/unique_key)
  + [For models](/reference/model-properties)
  + [For seeds](/reference/seed-properties)
  + [For snapshots](/reference/snapshot-properties)
  + [For data tests](/reference/data-test-configs)
  + [For unit tests](/reference/resource-properties/unit-tests)
  + [For sources](/reference/source-properties)
  + [For analyses](/reference/analysis-properties)
  + [For exposures](/reference/exposure-properties)
  + [For macros](/reference/macro-properties)
  + [For functions](/reference/function-properties)
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Resource configs and properties](/reference/resource-configs/resource-path)
* [General configs](/category/general-configs)
* access

Copy page

On this page

access
======

models/<schema>.yml

```
models:  
  - name: model_name  
    config:  
      access: private | protected | public # changed to config in v1.10
```

You can apply `access` modifiers in config files, including the `dbt_project.yml`, or to models one-by-one in `properties.yml`. Applying `access` configs to a subfolder modifies the default for all models in that subfolder, so make sure you intend for this behavior. When setting individual model access, a group or subfolder might contain a variety of access levels, so when you designate a model with `access: public` make sure you intend for this behavior.

Note that for backwards compatibility, `access` is supported as a top-level key, but without the capabilities of config inheritance.

There are multiple approaches to configuring access:

* In `properties.yml` using the older method:

  models/properties\_my\_public\_model.yml

  ```
  models:  
    - name: my_public_model  
      config:  
        access: public # Older method, still supported  
          # changed to config in v1.10
  ```
* In `properties.yml` using the new method (for v1.7 or higher). Use either the older method or the new method, but not both for the same model:

  models/properties\_my\_public\_model.yml

  ```
  models:  
    - name: my_public_model  
      config:  
        access: public
  ```
* In `dbt_project.yml`:

  dbt\_project.yml

  ```
  models:  
    my_project_name:  
      subfolder_name:  
        +group: my_group  
        +access: private  # sets default for all models in this subfolder
  ```
* In the `my_public_model.sql` file:

  models/my\_public\_model.sql

  ```
  -- models/my_public_model.sql  
    
  {{ config(access = "public") }}  
    
  select ...
  ```

After you define `access`, rerun a production job to apply the change.

Definition[​](#definition "Direct link to Definition")
------------------------------------------------------

The access level of the model you are declaring properties for.

Some models (not all) are designed to be referenced through the [ref](/reference/dbt-jinja-functions/ref) function across [groups](/docs/build/groups).

| Access | Referenceable by |
| --- | --- |
| private | Same group |
| protected | Same project/package |
| public | Any group, package, or project. When defined, rerun a production job to apply the change. |

If you try to reference a model outside of its supported access, you will see an error:

```
dbt run -s marketing_model  
...  
dbt.exceptions.DbtReferenceError: Parsing Error  
  Node model.jaffle_shop.marketing_model attempted to reference node model.jaffle_shop.finance_model,   
  which is not allowed because the referenced node is private to the finance group.
```

Default[​](#default "Direct link to Default")
---------------------------------------------

By default, all models are "protected." This means that other models in the same project can reference them.

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [Model Access](/docs/mesh/govern/model-access#groups)
* [Group configuration](/reference/resource-configs/group)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/access.md)

Last updated on **Nov 19, 2025**

[Previous

Advanced usage](/reference/advanced-config-usage)[Next

alias](/reference/resource-configs/alias)

* [Definition](#definition)
* [Default](#default)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/access.md)

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