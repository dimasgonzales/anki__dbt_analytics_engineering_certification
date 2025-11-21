# Source: https://docs.getdbt.com/reference/global-configs/command-line-options

Command line options | dbt Developer Hub

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
  + [Node selection](/reference/node-selection/syntax)
  + [Flags (global configs)](/reference/global-configs/about-global-configs)

    - [About flags (global configs)](/reference/global-configs/about-global-configs)
    - [Behavior changes](/reference/global-configs/behavior-changes)
    - [Adapter behavior changes](/reference/global-configs/adapter-behavior-changes)
    - [Setting flags](/category/setting-flags)

      * [Command line options](/reference/global-configs/command-line-options)
      * [Environment variable configs](/reference/global-configs/environment-variable-configs)
      * [Project flags](/reference/global-configs/project-flags)
    - [Available flags](/category/available-flags)
  + [Events and logs](/reference/events-logging)
  + [Exit codes](/reference/exit-codes)
  + [Deprecations](/reference/deprecations)
  + [Project Parsing](/reference/parsing)
  + [Programmatic invocations](/reference/programmatic-invocations)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Commands](/reference/dbt-commands)
* [Flags (global configs)](/reference/global-configs/about-global-configs)
* [Setting flags](/category/setting-flags)
* Command line options

Copy page

On this page

Command line options
====================

For consistency, command-line interface (CLI) flags should come right after the `dbt` prefix and its subcommands. This includes "global" flags (supported for all commands). For a list of all Cloud CLI flags you can set, refer to [Available flags](/reference/global-configs/about-global-configs#available-flags). When set, CLI flags override [environment variables](/reference/global-configs/environment-variable-configs) and [project flags](/reference/global-configs/project-flags).

Environment variables contain a `DBT_` prefix.

For example, instead of using:

```
dbt --no-populate-cache run
```

You should use:

```
dbt run --no-populate-cache
```

Historically, passing flags (such as "global flags") *before* the subcommand is a legacy functionality that dbt Labs can remove at any time. We do not support using the same flag before and after the subcommand.

Using boolean and non-boolean flags[​](#using-boolean-and-non-boolean-flags "Direct link to Using boolean and non-boolean flags")
---------------------------------------------------------------------------------------------------------------------------------

You can construct your commands with boolean flags to enable or disable or with non-boolean flags that use specific values, such as strings.

* Non-boolean config
* Boolean config

Use this non-boolean config structure:

* Replacing `<SUBCOMMAND>` with the command this config applies to.
* `<THIS-CONFIG>` with the config you are enabling or disabling, and
* `<SETTING>` with the new setting for the config.

CLI flags

```
<SUBCOMMAND> --<THIS-CONFIG>=<SETTING>
```

### Example[​](#example "Direct link to Example")

CLI flags

```
dbt run --printer-width=80   
dbt test --indirect-selection=eager
```

To enable or disable boolean configs:

* Use `<SUBCOMMAND>` this config applies to.
* Followed by `--<THIS-CONFIG>` to turn it on, or `--no-<THIS-CONFIG>` to turn it off.
* Replace `<THIS-CONFIG>` with the config you are enabling or disabling

CLI flags

```
dbt <SUBCOMMAND> --<THIS-CONFIG>   
dbt <SUBCOMMAND> --no-<THIS-CONFIG>
```

### Example[​](#example-1 "Direct link to Example")

CLI flags

```
dbt run --version-check  
dbt run --no-version-check
```

Config precedence[​](#config-precedence "Direct link to Config precedence")
---------------------------------------------------------------------------

There are multiple ways of setting flags, which depend on the use case:

* **[Project-level `flags` in `dbt_project.yml`](/reference/global-configs/project-flags):** Define version-controlled defaults for everyone running this project. Also, opt in or opt out of [behavior changes](/reference/global-configs/behavior-changes) to manage your migration off legacy functionality.
* **[Environment variables](/reference/global-configs/environment-variable-configs):** Define different behavior in different runtime environments (development vs. production vs. [continuous integration](/docs/deploy/continuous-integration), or different behavior for different users in development (based on personal preferences).
* **[CLI options](/reference/global-configs/command-line-options):** Define behavior specific to *this invocation*. Supported for all dbt commands.

The most specific setting "wins." If you set the same flag in all three places, the CLI option will take precedence, followed by the environment variable, and finally, the value in `dbt_project.yml`. If you set the flag in none of those places, it will use the default value defined within dbt.

Most flags can be set in all three places:

```
# dbt_project.yml  
flags:  
  # set default for running this project -- anywhere, anytime, by anyone  
  fail_fast: true
```

```
# set this environment variable to 'True' (bash syntax)  
export DBT_FAIL_FAST=1  
dbt run
```

```
dbt run --fail-fast # set to True for this specific invocation  
dbt run --no-fail-fast # set to False
```

There are two categories of exceptions:

1. **Flags setting file paths:** Flags for file paths that are relevant to runtime execution (for example, `--log-path` or `--state`) cannot be set in `dbt_project.yml`. To override defaults, pass CLI options or set environment variables (`DBT_LOG_PATH`, `DBT_STATE`). Flags that tell dbt where to find project resources (for example, `model-paths`) are set in `dbt_project.yml`, but as a top-level key, outside the `flags` dictionary; these configs are expected to be fully static and never vary based on the command or execution environment.
2. **Opt-in flags:** Flags opting in or out of [behavior changes](/reference/global-configs/behavior-changes) can *only* be defined in `dbt_project.yml`. These are intended to be set in version control and migrated via pull/merge request. Their values should not diverge indefinitely across invocations, environments, or users.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/global-configs/command-line-options.md)

Last updated on **Nov 19, 2025**

[Previous

Setting flags](/category/setting-flags)[Next

Environment variable configs](/reference/global-configs/environment-variable-configs)

* [Using boolean and non-boolean flags](#using-boolean-and-non-boolean-flags)
  + [Example](#example)
  + [Example](#example-1)
* [Config precedence](#config-precedence)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/global-configs/command-line-options.md)

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