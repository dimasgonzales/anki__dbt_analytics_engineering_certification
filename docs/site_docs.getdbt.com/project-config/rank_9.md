# Source: https://docs.getdbt.com/reference/project-configs/version

version | dbt Developer Hub

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

  + [dbt\_project.yml](/reference/dbt_project.yml)
  + [.dbtignore](/reference/dbtignore)
  + [analysis-paths](/reference/project-configs/analysis-paths)
  + [asset-paths](/reference/project-configs/asset-paths)
  + [clean-targets](/reference/project-configs/clean-targets)
  + [config-version](/reference/project-configs/config-version)
  + [dispatch (config)](/reference/project-configs/dispatch-config)
  + [docs-paths](/reference/project-configs/docs-paths)
  + [function-paths](/reference/project-configs/function-paths)
  + [macro-paths](/reference/project-configs/macro-paths)
  + [name](/reference/project-configs/name)
  + [on-run-start & on-run-end](/reference/project-configs/on-run-start-on-run-end)
  + [packages-install-path](/reference/project-configs/packages-install-path)
  + [profile](/reference/project-configs/profile)
  + [query-comment](/reference/project-configs/query-comment)
  + [quoting](/reference/project-configs/quoting)
  + [require-dbt-version](/reference/project-configs/require-dbt-version)
  + [snapshot-paths](/reference/project-configs/snapshot-paths)
  + [seed-paths](/reference/project-configs/seed-paths)
  + [model-paths](/reference/project-configs/model-paths)
  + [test-paths](/reference/project-configs/test-paths)
  + [version](/reference/project-configs/version)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Project configs](/category/project-configs)
* version

Copy page

On this page

version
=======

Model versions, dbt\_project.yml versions, and .yml versions

Take note that [model versions](/docs/mesh/govern/model-versions) are different from [dbt\_project.yml versions](/reference/project-configs/version#dbt_projectyml-versions) and [.yml property file versions](/reference/project-configs/version#yml-property-file-versions).

Model versions is a *feature* that enables better governance and data model management by allowing you to track changes and updates to models over time. dbt\_project.yml versions refer to the compatibility of the dbt project with a specific version of dbt. Version numbers within .yml property files inform how dbt parses those YAML files. The latter two are completely optional starting from dbt v1.5.

dbt projects have two distinct types of `version` tags. This field has a different meaning depending on its location.

`dbt_project.yml` versions[​](#dbt_projectyml-versions "Direct link to dbt_projectyml-versions")
------------------------------------------------------------------------------------------------

The version tag in a `dbt_project` file represents the version of your dbt project.

Starting in dbt version 1.5, `version` in the `dbt_project.yml` is an *optional parameter*. If used, the version must be in a [semantic version](https://semver.org/) format, such as `1.0.0`. The default value is `None` if not specified. For users on dbt version 1.4 or lower, this tag is required, though it isn't currently used meaningfully by dbt.

For more on Core versions, see [About dbt Core versions](/docs/dbt-versions/core).

dbt\_project.yml

```
version: version
```

`.yml` property file versions[​](#yml-property-file-versions "Direct link to yml-property-file-versions")
---------------------------------------------------------------------------------------------------------

A version tag in a `.yml` property file provides the control tag, which informs how dbt processes property files.

Starting from version 1.5, dbt will no longer require this configuration in your resource `.yml` files. If you want to know more about why this tag was previously required, you can refer to the [FAQs](#faqs). For users on dbt version 1.4 or lower, this tag is required,

For more on property files, see their general [documentation](/reference/define-properties) on the same page.

* Resource property file with version specified
* Resource property file without version specified

<any valid filename>.yml

```
version: 2  # Only 2 is accepted by dbt versions up to 1.4.latest.  
  
models:   
    ...
```

<any valid filename>.yml

```
models:   
    ...
```

FAQS[​](#faqs "Direct link to FAQS")
------------------------------------

Why do model and source YAML files always start with `version: 2`?

Once upon a time, the structure of these `.yml` files was very different (s/o to anyone who was using dbt back then!). Adding `version: 2` allowed us to make this structure more extensible.

From [dbt Core v1.5](/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.5#quick-hits), the top-level `version:` key is optional in all resource YAML files. If present, only `version: 2` is supported.

Also starting in v1.5, both the [`config-version: 2`](/reference/project-configs/config-version) and the top-level `version:` key in the `dbt_project.yml` are optional.

Resource YAML files do not currently require this config. We only support `version: 2` if it's specified. Although we do not expect to update YAML files to `version: 3` soon, having this config will make it easier for us to introduce new structures in the future

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/project-configs/version.md)

Last updated on **Nov 19, 2025**

[Previous

test-paths](/reference/project-configs/test-paths)[Next

Platform-specific configs](/reference/resource-configs/resource-configs)

* [`dbt_project.yml` versions](#dbt_projectyml-versions)
* [`.yml` property file versions](#yml-property-file-versions)
* [FAQS](#faqs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/project-configs/version.md)

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