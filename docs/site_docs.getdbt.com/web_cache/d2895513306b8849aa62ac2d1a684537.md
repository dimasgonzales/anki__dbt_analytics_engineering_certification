# Source: https://docs.getdbt.com/reference/seed-configs

Seed configurations | dbt Developer Hub

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
* Seed configurations

Copy page

On this page

Seed configurations
===================

Available configurations[​](#available-configurations "Direct link to Available configurations")
------------------------------------------------------------------------------------------------

### Seed-specific configurations[​](#seed-specific-configurations "Direct link to Seed-specific configurations")

Resource-specific configurations are applicable to only one dbt resource type rather than multiple resource types. You can define these settings in the project file (`dbt_project.yml`), a property file (`models/properties.yml` for models, similarly for other resources), or within the resource’s file using the `{{ config() }}` macro.

The following resource-specific configurations are only available to Seeds:

* Project file
* Property file

dbt\_project.yml

```
seeds:  
  <resource-path>:  
    +quote_columns: true | false  
    +column_types: {column_name: datatype}  
    +delimiter: <string>
```

seeds/properties.yml

```
seeds:  
  - name: [<seed-name>]  
    config:  
      quote_columns: true | false  
      column_types: {column_name: datatype}  
      delimiter: <string>
```

### General configurations[​](#general-configurations "Direct link to General configurations")

General configurations provide broader operational settings applicable across multiple resource types. Like resource-specific configurations, these can also be set in the project file, property files, or within resource-specific files.

* Project file
* Property file

dbt\_project.yml

seeds/properties.yml

Configuring seeds[​](#configuring-seeds "Direct link to Configuring seeds")
---------------------------------------------------------------------------

Seeds can only be configured from YAML files, either in `dbt_project.yml` or within an individual seed's YAML properties. It is not possible to configure a seed from within its CSV file.

Seed configurations, like model configurations, are applied hierarchically — configurations applied to a `marketing` subdirectory will take precedence over configurations applied to the entire `jaffle_shop` project, and configurations defined in a specific seed's properties will override configurations defined in `dbt_project.yml`.

### Examples[​](#examples "Direct link to Examples")

#### Apply the `schema` configuration to all seeds[​](#apply-the-schema-configuration-to-all-seeds "Direct link to apply-the-schema-configuration-to-all-seeds")

To apply a configuration to all seeds, including those in any installed [packages](/docs/build/packages), nest the configuration directly under the `seeds` key:

dbt\_project.yml

```
seeds:  
  +schema: seed_data
```

#### Apply the `schema` configuration to all seeds in your project[​](#apply-the-schema-configuration-to-all-seeds-in-your-project "Direct link to apply-the-schema-configuration-to-all-seeds-in-your-project")

To apply a configuration to all seeds in your project only (i.e. *excluding* any seeds in installed packages), provide your [project name](/reference/project-configs/name) as part of the resource path.

For a project named `jaffle_shop`:

dbt\_project.yml

```
seeds:  
  jaffle_shop:  
    +schema: seed_data
```

Similarly, you can use the name of an installed package to configure seeds in that package.

#### Apply the `schema` configuration to one seed only[​](#apply-the-schema-configuration-to-one-seed-only "Direct link to apply-the-schema-configuration-to-one-seed-only")

To apply a configuration to one seed only, provide the full resource path (including the project name, and subdirectories).

seeds/marketing/properties.yml

```
seeds:  
  - name: utm_parameters  
    config:  
      schema: seed_data
```

In older versions of dbt, you must define configurations in `dbt_project.yml` and include the full resource path (including the project name, and subdirectories). For a project named `jaffle_shop`, with a seed file at `seeds/marketing/utm_parameters.csv`, this would look like:

dbt\_project.yml

```
seeds:  
  jaffle_shop:  
    marketing:  
      utm_parameters:  
        +schema: seed_data
```

Example seed configuration[​](#example-seed-configuration "Direct link to Example seed configuration")
------------------------------------------------------------------------------------------------------

The following is a valid seed configuration for a project with:

* `name: jaffle_shop`
* A seed file at `seeds/country_codes.csv`, and
* A seed file at `seeds/marketing/utm_parameters.csv`

dbt\_project.yml

```
name: jaffle_shop  
...  
seeds:  
  jaffle_shop:  
    +enabled: true  
    +schema: seed_data  
    # This configures seeds/country_codes.csv  
    country_codes:  
      # Override column types  
      +column_types:  
        country_code: varchar(2)  
        country_name: varchar(32)  
    marketing:  
      +schema: marketing # this will take precedence
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/seed-configs.md)

Last updated on **Nov 19, 2025**

[Previous

Seed properties](/reference/seed-properties)[Next

column\_types](/reference/resource-configs/column_types)

* [Available configurations](#available-configurations)
  + [Seed-specific configurations](#seed-specific-configurations)
  + [General configurations](#general-configurations)
* [Configuring seeds](#configuring-seeds)
  + [Examples](#examples)
* [Example seed configuration](#example-seed-configuration)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/seed-configs.md)

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