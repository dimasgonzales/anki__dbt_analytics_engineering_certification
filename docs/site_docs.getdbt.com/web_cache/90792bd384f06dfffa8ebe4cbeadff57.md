# Source: https://docs.getdbt.com/guides/building-packages

Building dbt packages | dbt Developer Hub

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

Copy page

Building dbt packages
=====================

[Back to guides](/guides)

dbt Core

Advanced

Menu




Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

Creating packages is an **advanced use of dbt**. If you're new to the tool, we recommend that you first use the product for your own analytics before attempting to create a package for others.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

A strong understanding of:

* [packages](/docs/build/packages)
* administering a repository on GitHub
* [semantic versioning](https://semver.org/)

### Assess whether a package is the right solution[​](#assess-whether-a-package-is-the-right-solution "Direct link to Assess whether a package is the right solution")

Packages typically contain either:

* macros that solve a particular analytics engineering problem — for example, [auditing the results of a query](https://hub.getdbt.com/dbt-labs/audit_helper/latest/), [generating code](https://hub.getdbt.com/dbt-labs/codegen/latest/), or [adding additional schema tests to a dbt project](https://hub.getdbt.com/calogica/dbt_expectations/latest/).
* models for a common dataset — for example a dataset for software products like [MailChimp](https://hub.getdbt.com/fivetran/mailchimp/latest/) or [Snowplow](https://hub.getdbt.com/dbt-labs/snowplow/latest/), or even models for metadata about your data stack like [Snowflake query spend](https://hub.getdbt.com/gitlabhq/snowflake_spend/latest/) and [the artifacts produced by `dbt run`](https://hub.getdbt.com/tailsdotcom/dbt_artifacts/latest/). In general, there should be a shared set of industry-standard metrics that you can model (e.g. email open rate).

Packages are *not* a good fit for sharing models that contain business-specific logic, for example, writing code for marketing attribution, or monthly recurring revenue. Instead, consider sharing a blog post and a link to a sample repo, rather than bundling this code as a package (here's our blog post on [marketing attribution](https://blog.getdbt.com/modeling-marketing-attribution/) as an example).

Create your new project[​](#create-your-new-project "Direct link to Create your new project")
---------------------------------------------------------------------------------------------

Using the command line for package development

We tend to use the command line interface for package development. The development workflow often involves installing a local copy of your package in another dbt project — at present dbt is not designed for this workflow.

1. Use the [dbt init](/reference/commands/init) command to create a new dbt project, which will be your package:

```
$ dbt init [package_name]
```

2. Create a public GitHub¹ repo, named `dbt-<package-name>`, e.g. `dbt-mailchimp`. Follow the GitHub instructions to link this to the dbt project you just created.
3. Update the `name:` of the project in `dbt_project.yml` to your package name, e.g. `mailchimp`.
4. Define the allowed dbt versions by using the [`require-dbt-version` config](/reference/project-configs/require-dbt-version).

¹Currently, our package registry only supports packages that are hosted in GitHub.

Develop your package[​](#develop-your-package "Direct link to Develop your package")
------------------------------------------------------------------------------------

We recommend that first-time package authors first develop macros and models for use in their own dbt project. Once your new package is created, you can get to work on moving them across, implementing some additional package-specific design patterns along the way.

When working on your package, we often find it useful to install a local copy of the package in another dbt project — this workflow is described [here](https://discourse.getdbt.com/t/contributing-to-an-external-dbt-package/657).

### Follow best practices[​](#follow-best-practices "Direct link to Follow best practices")

*Modeling packages only*

Use our [dbt coding conventions](https://github.com/dbt-labs/corp/blob/main/dbt_style_guide.md), our article on [how we structure our dbt projects](/best-practices/how-we-structure/1-guide-overview), and our [best practices](/best-practices) for all of our advice on how to build your dbt project.

This is where it comes in especially handy to have worked on your own dbt project previously.

### Make the location of raw data configurable[​](#make-the-location-of-raw-data-configurable "Direct link to Make the location of raw data configurable")

*Modeling packages only*

Not every user of your package is going to store their Mailchimp data in a schema named `mailchimp`. As such, you'll need to make the location of raw data configurable.

We recommend using [sources](/docs/build/sources) and [variables](/docs/build/project-variables) to achieve this. Check out [this package](https://github.com/fivetran/dbt_facebook_ads_source/blob/main/models/src_facebook_ads.yml#L5-L6) for an example — notably, the README [includes instructions](https://github.com/fivetran/dbt_facebook_ads_source#configuration) on how to override the default schema from a `dbt_project.yml` file.

### Install upstream packages from hub.getdbt.com[​](#install-upstream-packages-from-hubgetdbtcom "Direct link to Install upstream packages from hub.getdbt.com")

If your package relies on another package (for example, you use some of the cross-database macros from [dbt-utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/)), we recommend you install the package from [hub.getdbt.com](https://hub.getdbt.com), specifying a version range like so:

packages.yml

```
packages:  
  - package: dbt-labs/dbt_utils  
    version: [">0.6.5", "0.7.0"]
```

When packages are installed from hub.getdbt.com, dbt is able to handle duplicate dependencies.

### Implement cross-database compatibility[​](#implement-cross-database-compatibility "Direct link to Implement cross-database compatibility")

Many SQL functions are specific to a particular database. For example, the function name and order of arguments to calculate the difference between two dates varies between Redshift, Snowflake and BigQuery, and no similar function exists on Postgres!

If you wish to support multiple warehouses, we have a number of tricks up our sleeve:

* We've written a number of macros that compile to valid SQL snippets on each of the original four adapters. Where possible, leverage these macros.
* If you need to implement cross-database compatibility for one of your macros, use the [`adapter.dispatch` macro](/reference/dbt-jinja-functions/dispatch) to achieve this. Check out the cross-database macros in dbt-utils for examples.
* If you're working on a modeling package, you may notice that you need write different models for each warehouse (for example, if the EL tool you are working with stores data differently on each warehouse). In this case, you can write different versions of each model, and use the [`enabled` config](/reference/resource-configs/enabled), in combination with [`target.type`](/reference/dbt-jinja-functions/target) to enable the correct models — check out [this package](https://github.com/fivetran/dbt_facebook_ads_creative_history/blob/main/dbt_project.yml#L11-L16) as an example.

If your package has only been written to work for one data warehouse, make sure you document this in your package README.

### Use specific model names[​](#use-specific-model-names "Direct link to Use specific model names")

*Modeling packages only*

Many datasets have a concept of a "user" or "account" or "session". To make sure things are unambiguous in dbt, prefix all of your models with `[package_name]_`. For example, `mailchimp_campaigns.sql` is a good name for a model, whereas `campaigns.sql` is not.

### Default to views[​](#default-to-views "Direct link to Default to views")

*Modeling packages only*

dbt makes it possible for users of your package to override your model materialization settings. In general, default to materializing models as `view`s instead of `table`s.

The major exception to this is when working with data sources that benefit from incremental modeling (for example, web page views). Implementing incremental logic on behalf of your end users is likely to be helpful in this case.

### Test and document your package[​](#test-and-document-your-package "Direct link to Test and document your package")

It's critical that you [test](/docs/build/data-tests) your models and sources. This will give your end users confidence that your package is actually working on top of their dataset as intended.

Further, adding [documentation](/docs/build/documentation) via descriptions will help communicate your package to end users, and benefit their stakeholders that use the outputs of this package.

### Include useful GitHub artifacts[​](#include-useful-github-artifacts "Direct link to Include useful GitHub artifacts")

Over time, we've developed a set of useful GitHub artifacts that make administering our packages easier for us. In particular, we ensure that we include:

* A useful README, that has:
  + installation instructions that refer to the latest version of the package on hub.getdbt.com, and includes any configurations requires ([example](https://github.com/dbt-labs/segment))
  + Usage examples for any macros ([example](https://github.com/dbt-labs/dbt-audit-helper#macros))
  + Descriptions of the main models included in the package ([example](https://github.com/dbt-labs/snowplow))
* GitHub templates, including PR templates and issue templates ([example](https://github.com/dbt-labs/dbt-audit-helper/tree/master/.github))

Add integration tests[​](#add-integration-tests "Direct link to Add integration tests")
---------------------------------------------------------------------------------------

*Optional*

We recommend that you implement integration tests to confirm that the package works as expected — this is an even *more* advanced step, so you may find that you build up to this.

This pattern can be seen most packages, including the [`audit-helper`](https://github.com/dbt-labs/dbt-audit-helper/tree/master/integration_tests) and [`snowplow`](https://github.com/dbt-labs/snowplow/tree/master/integration_tests) packages.

As a rough guide:

1. Create a subdirectory named `integration_tests`
2. In this subdirectory, create a new dbt project — you can use the `dbt init` command to do this. However, our preferred method is to copy the files from an existing `integration_tests` project, like the ones [here](https://github.com/dbt-labs/dbt-codegen/tree/HEAD/integration_tests) (removing the contents of the `macros`, `models` and `tests` folders since they are project-specific)
3. Install the package in the `integration_tests` subdirectory by using the `local` syntax, and then running `dbt deps`

packages.yml

```
packages:  
    - local: ../ # this means "one directory above the current directory"
```

4. Add resources to the package (seeds, models, tests) so that you can successfully run your project, and compare the output with what you expect. The exact approach here will vary depending on your packages. In general you will find that you need to:

   * Add mock data via a [seed](/docs/build/seeds) with a few sample (anonymized) records. Configure the `integration_tests` project to point to the seeds instead of raw data tables.
   * Add more seeds that represent the expected output of your models, and use the [dbt\_utils.equality](https://github.com/dbt-labs/dbt-utils#equality-source) test to confirm the output of your package, and the expected output matches.
5. Confirm that you can run `dbt run` and `dbt test` from your command line successfully.
6. (Optional) Use a CI tool, like CircleCI or GitHub Actions, to automate running your dbt project when you open a new Pull Request. For inspiration, check out one of our [CircleCI configs](https://github.com/dbt-labs/snowplow/blob/main/.circleci/config.yml), which runs tests against our four main warehouses. Note: this is an advanced step — if you are going down this path, you may find it useful to say hi on [dbt Slack](https://community.getdbt.com/).

Deploy the docs for your package[​](#deploy-the-docs-for-your-package "Direct link to Deploy the docs for your package")
------------------------------------------------------------------------------------------------------------------------

*Optional*

A dbt docs site can help a prospective user of your package understand the code you've written. As such, we recommend that you deploy the site generated by `dbt docs generate` and link to the deployed site from your package.

The easiest way we've found to do this is to use [GitHub Pages](https://pages.github.com/).

1. On a new git branch, run `dbt docs generate`. If you have integration tests set up (above), use the integration-test project to do this.
2. Move the following files into a directory named `docs` ([example](https://github.com/fivetran/dbt_ad_reporting/tree/HEAD/docs)): `catalog.json`, `index.html`, `manifest.json`, `run_results.json`.
3. Merge these changes into the main branch
4. Enable GitHub pages on the repo in the settings tab, and point it to the “docs” subdirectory
5. GitHub should then deploy the docs at `<org-name>.github.io/<repo-name>`, like so: [fivetran.github.io/dbt\_ad\_reporting](https://fivetran.github.io/dbt_ad_reporting/)

Release your package[​](#release-your-package "Direct link to Release your package")
------------------------------------------------------------------------------------

Create a new [release](https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository) once you are ready for others to use your work! Be sure to use [semantic versioning](https://semver.org/) when naming your release.

In particular, if new changes will cause errors for users of earlier versions of the package, be sure to use *at least* a minor release (e.g. go from `0.1.1` to `0.2.0`).

The release notes should contain an overview of the changes introduced in the new version. Be sure to call out any changes that break the existing interface!

Add the package to hub.getdbt.com[​](#add-the-package-to-hubgetdbtcom "Direct link to Add the package to hub.getdbt.com")
-------------------------------------------------------------------------------------------------------------------------

Our package registry, [hub.getdbt.com](https://hub.getdbt.com/), gets updated by the [hubcap script](https://github.com/dbt-labs/hubcap). To add your package to hub.getdbt.com, create a PR on the [hubcap repository](https://github.com/dbt-labs/hubcap) to include it in the `hub.json` file.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [dbt Core](/tags/dbt-core)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/guides/building-packages.md)

Last updated on **Nov 19, 2025**

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