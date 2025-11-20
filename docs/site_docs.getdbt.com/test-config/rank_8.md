# Source: https://docs.getdbt.com/reference/define-configs

Define configs | dbt Developer Hub

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

    - [Configs and properties](/reference/configs-and-properties)
    - [Define configs](/reference/define-configs)
    - [Define properties](/reference/define-properties)
  + [General properties](/category/general-properties)
  + [General configs](/category/general-configs)
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
* [Configs and properties](/reference/configs-and-properties)
* Define configs

Copy page

On this page

Define configs
==============

Learn how to define configurations for your resources in a dbt project

Depending on the resource type, you can define configurations in a dbt project and also in an installed package by:

Config inheritance[​](#config-inheritance "Direct link to Config inheritance")
------------------------------------------------------------------------------

The most specific config always takes precedence. This generally follows the order above: an in-file `config()` block --> properties defined in a `.yml` file --> config defined in the project file.

Note - Generic data tests work a little differently when it comes to specificity. See [test configs](/reference/data-test-configs).

Within the project file, configurations are also applied hierarchically. The most specific config always takes precedence. In the project file, for example, configurations applied to a `marketing` subdirectory will take precedence over configurations applied to the entire `jaffle_shop` project. To apply a configuration to a model or directory of models, define the [resource path](/reference/resource-configs/resource-path) as nested dictionary keys.

Configurations in your root dbt project have *higher* precedence than configurations in installed packages. This enables you to override the configurations of installed packages, providing more control over your dbt runs.

Combining configs[​](#combining-configs "Direct link to Combining configs")
---------------------------------------------------------------------------

Most configurations are "clobbered" when applied hierarchically. Whenever a more specific value is available, it will completely replace the less specific value. Note that a few configs have different merge behavior:

* [`tags`](/reference/resource-configs/tags) are additive. If a model has some tags configured in `dbt_project.yml`, and more tags are applied in its `.sql` file, the final set of tags will include all of them.
* [`meta`](/reference/resource-configs/meta) dictionaries are merged (a more specific key-value pair replaces a less specific value with the same key).
* When using the [`freshness`](/reference/resource-configs/freshness) config, a more specific key-value pair replaces a less specific value with the same key.
* [`pre-hook` and `post-hook`](/reference/resource-configs/pre-hook-post-hook) are also additive.
* For clobbering and merging configurations that are inherited from multiple levels, the general rules are:
  + Node-level configs (more specific) clobber project-level configs (less specific).
  + For sources, table-level configs (more specific) clobber source-level configs (less specific).
  + The root project's configuration in `dbt_project.yml` clobbers configuration within package files. This is so that users can control the behavior of packages they are installing using `dbt deps` without needing to edit the code in those package files directly.

The `+` prefix[​](#the--prefix "Direct link to the--prefix")
------------------------------------------------------------

dbt demarcates between a folder name and a configuration by using a `+` prefix before the configuration name. The `+` prefix is used for configs *only* and applies to `dbt_project.yml` under the corresponding resource key. It doesn't apply to:

* `config()` Jinja macro within a resource file
* config property in a `.yml` file.

For more info, see the [Using the `+` prefix](/reference/resource-configs/plus-prefix).

Example[​](#example "Direct link to Example")
---------------------------------------------

Here's an example that defines both `sources` and `models` for a project:

models/jaffle\_shop.yml

```
version: 2  
  
sources:  
  - name: raw_jaffle_shop  
    description: A replica of the postgres database used to power the jaffle_shop app.  
    tables:  
      - name: customers  
        columns:  
          - name: id  
            description: Primary key of the table  
            data_tests:  
              - unique  
              - not_null  
  
      - name: orders  
        columns:  
          - name: id  
            description: Primary key of the table  
            data_tests:  
              - unique  
              - not_null  
  
          - name: user_id  
            description: Foreign key to customers  
  
          - name: status  
            data_tests:  
              - accepted_values:  
                  arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                    values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']  
  
  
models:  
  - name: stg_jaffle_shop__customers #  Must match the filename of a model -- including case sensitivity.  
    config:  
      tags: ['pii']  
    columns:  
      - name: customer_id  
        data_tests:  
          - unique  
          - not_null  
  
  - name: stg_jaffle_shop__orders  
    config:  
      materialized: view  
    columns:  
      - name: order_id  
        data_tests:  
          - unique  
          - not_null  
      - name: status  
        data_tests:  
          - accepted_values:  
              values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']  
              config:  
                severity: warn
```

Related documentation[​](#related-documentation "Direct link to Related documentation")
---------------------------------------------------------------------------------------

You can find an exhaustive list of each supported property and config, broken down by resource type:

* Model [properties](/reference/model-properties) and [configs](/reference/model-configs)
* Source [properties](/reference/source-properties) and [configs](/reference/source-configs)
* Seed [properties](/reference/seed-properties) and [configs](/reference/seed-configs)
* Snapshot [properties](/reference/snapshot-properties)
* Analysis [properties](/reference/analysis-properties)
* Macro [properties](/reference/macro-properties)
* Exposure [properties](/reference/exposure-properties)

FAQs[​](#faqs "Direct link to FAQs")
------------------------------------

Does my `.yml` file containing tests and descriptions need to be named `schema.yml`?

No! You can name this file whatever you want (including `whatever_you_want.yml`), so long as:

* The file is in your `models/` directory¹
* The file has `.yml` extension

Check out the [docs](/reference/configs-and-properties) for more information.

¹If you're declaring properties for seeds, snapshots, or macros, you can also place this file in the related directory — `seeds/`, `snapshots/` and `macros/` respectively.

If I can name these files whatever I'd like, what should I name them?

It's up to you! Here's a few options:

* Default to the existing terminology: `schema.yml` (though this does make it hard to find the right file over time)
* Use the same name as your directory (assuming you're using sensible names for your directories)
* If you test and document one model (or seed, snapshot, macro etc.) per file, you can give it the same name as the model (or seed, snapshot, macro etc.)

Choose what works for your team. We have more recommendations in our guide on [structuring dbt projects](/best-practices/how-we-structure/1-guide-overview).

Should I use separate files to declare resource properties, or one large file?

It's up to you:

* Some folks find it useful to have one file per model (or source / snapshot / seed etc)
* Some find it useful to have one per directory, documenting and testing multiple models in one file

Choose what works for your team. We have more recommendations in our guide on [structuring dbt projects](/best-practices/how-we-structure/1-guide-overview).

Can I add tests and descriptions in a config block?

dbt has the ability to define node configs in `.yml` files, in addition to `config()` blocks and `dbt_project.yml`. But the reverse isn't always true: there are some things in `.yml` files that can *only* be defined there.

Certain properties are special, because:

* They have a unique Jinja rendering context
* They create new project resources
* They don't make sense as hierarchical configuration
* They're older properties that haven't yet been redefined as configs

These properties are:

* [`description`](/reference/resource-properties/description)
* [`tests`](/reference/resource-properties/data-tests)
* [`docs`](/reference/resource-configs/docs)
* `columns`
* [`quote`](/reference/resource-properties/columns#quote)
* [`source` properties](/reference/source-properties) (e.g. `loaded_at_field`, `freshness`)
* [`exposure` properties](/reference/exposure-properties) (e.g. `type`, `maturity`)
* [`macro` properties](/reference/resource-properties/arguments) (e.g. `arguments`)

Why do model and source YAML files always start with `version: 2`?

Once upon a time, the structure of these `.yml` files was very different (s/o to anyone who was using dbt back then!). Adding `version: 2` allowed us to make this structure more extensible.

From [dbt Core v1.5](/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.5#quick-hits), the top-level `version:` key is optional in all resource YAML files. If present, only `version: 2` is supported.

Also starting in v1.5, both the [`config-version: 2`](/reference/project-configs/config-version) and the top-level `version:` key in the `dbt_project.yml` are optional.

Resource YAML files do not currently require this config. We only support `version: 2` if it's specified. Although we do not expect to update YAML files to `version: 3` soon, having this config will make it easier for us to introduce new structures in the future

Can I use a YAML file extension?

No. At present, dbt will only search for files with a `.yml` file extension. In a future release of dbt, dbt will also search for files with a `.yaml` file extension.

Troubleshooting common errors[​](#troubleshooting-common-errors "Direct link to Troubleshooting common errors")
---------------------------------------------------------------------------------------------------------------

 Invalid test config given in [model name]

This error occurs when your `.yml` file does not conform to the structure expected by dbt. A full error message might look like:

```
* Invalid test config given in models/schema.yml near {'namee': 'event', ...}  
  Invalid arguments passed to "UnparsedNodeUpdate" instance: 'name' is a required property, Additional properties are not allowed ('namee' was unexpected)
```

While verbose, an error like this should help you track down the issue. Here, the `name` field was provided as `namee` by accident. To fix this error, ensure that your `.yml` conforms to the expected structure described in this guide.

 Invalid syntax in your schema.yml file

If your `.yml` file is not valid yaml, then dbt will show you an error like this:

```
Runtime Error  
  Syntax error near line 6  
  ------------------------------  
  5  |   - name: events  
  6  |     description; "A table containing clickstream events from the marketing website"  
  7  |  
  
  Raw Error:  
  ------------------------------  
  while scanning a simple key  
    in "<unicode string>", line 6, column 5:  
          description; "A table containing clickstream events from the marketing website"  
          ^
```

This error occurred because a semicolon (`;`) was accidentally used instead of a colon (`:`) after the `description` field. To resolve issues like this, find the `.yml` file referenced in the error message and fix any syntax errors present in the file. There are online YAML validators that can be helpful here, but please be mindful of submitting sensitive information to third-party applications!

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/define-configs.md)

Last updated on **Nov 19, 2025**

[Previous

Configs and properties](/reference/configs-and-properties)[Next

Define properties](/reference/define-properties)

* [Config inheritance](#config-inheritance)
* [Combining configs](#combining-configs)
* [The `+` prefix](#the--prefix)
* [Example](#example)
* [Related documentation](#related-documentation)
* [FAQs](#faqs)
* [Troubleshooting common errors](#troubleshooting-common-errors)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/define-configs.md)

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