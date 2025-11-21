# Source: https://docs.getdbt.com/reference/resource-configs/delimiter

delimiter | dbt Developer Hub

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

  + [About resource paths](/reference/resource-configs/resource-path)
  + [Configs and properties](/reference/configs-and-properties)
  + [General properties](/category/general-properties)
  + [General configs](/category/general-configs)
  + [For models](/reference/model-properties)
  + [For seeds](/reference/seed-properties)

    - [Seed properties](/reference/seed-properties)
    - [Seed configurations](/reference/seed-configs)
    - [column\_types](/reference/resource-configs/column_types)
    - [delimiter](/reference/resource-configs/delimiter)
    - [quote\_columns](/reference/resource-configs/quote_columns)
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
* [For seeds](/reference/seed-properties)
* delimiter

Copy page

On this page

delimiter
=========

💡Did you know...

Available from dbt v1.7 or with the [dbt "Latest" release track](/docs/dbt-versions/cloud-release-tracks).

Definition[​](#definition "Direct link to Definition")
------------------------------------------------------

You can use this optional seed configuration to customize how you separate values in a [seed](/docs/build/seeds) by providing the one-character string.

* The delimiter defaults to a comma when not specified.
* Explicitly set the `delimiter` configuration value if you want seed files to use a different delimiter, such as "|" or ";".

Usage[​](#usage "Direct link to Usage")
---------------------------------------

Specify a delimiter in your `dbt_project.yml` file to customize the global separator for all seed values:

dbt\_project.yml

```
seeds:  
  <project_name>:  
     +delimiter: "|" # default project delimiter for seeds will be "|"  
    <seed_subdirectory>:  
      +delimiter: "," # delimiter for seeds in seed_subdirectory will be ","
```

Or use a custom delimiter to override the values for a specific seed:

seeds/properties.yml

```
seeds:  
  - name: <seed_name>  
    config:   
      delimiter: "|"
```

Examples[​](#examples "Direct link to Examples")
------------------------------------------------

For a project with:

* `name: jaffle_shop` in the `dbt_project.yml` file
* `seed-paths: ["seeds"]` in the `dbt_project.yml` file

### Use a custom delimiter to override global values[​](#use-a-custom-delimiter-to-override-global-values "Direct link to Use a custom delimiter to override global values")

You can set a default behavior for all seeds with an exception for one seed, `seed_a`, which uses a comma:

dbt\_project.yml

```
seeds:  
  jaffle_shop:   
    +delimiter: "|" # default delimiter for seeds in jaffle_shop project will be "|"  
    seed_a:  
      +delimiter: "," # delimiter for seed_a will be ","
```

Your corresponding seed files would be formatted like this:

seeds/my\_seed.csv

```
col_a|col_b|col_c  
1|2|3  
4|5|6  
...
```

seeds/seed\_a.csv

```
name,id  
luna,1  
doug,2  
...
```

Or you can configure custom behavior for one seed. The `country_codes` uses the ";" delimiter:

seeds/properties.yml

```
seeds:  
  - name: country_codes  
    config:  
      delimiter: ";"
```

The `country_codes` seed file would be formatted like this:

seeds/country\_codes.csv

```
country_code;country_name  
US;United States  
CA;Canada  
GB;United Kingdom  
...
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/delimiter.md)

Last updated on **Nov 19, 2025**

[Previous

column\_types](/reference/resource-configs/column_types)[Next

quote\_columns](/reference/resource-configs/quote_columns)

* [Definition[​](#definition "Direct link to Definition")](#definition)
* [Usage[​](#usage "Direct link to Usage")](#usage)
* [Examples[​](#examples "Direct link to Examples")](#examples)
  + [Use a custom delimiter to override global values[​](#use-a-custom-delimiter-to-override-global-values "Direct link to Use a custom delimiter to override global values")](#use-a-custom-delimiter-to-override-global-values)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-configs/delimiter.md)

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