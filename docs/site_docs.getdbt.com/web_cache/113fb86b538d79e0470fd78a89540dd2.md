# Source: https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-v1.7

Upgrading to v1.7 | dbt Developer Hub

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

  + [Available dbt versions](/docs/dbt-versions/about-versions)
  + [About dbt Core versions](/docs/dbt-versions/core)
  + [About release tracks](/docs/dbt-versions/cloud-release-tracks)
  + [Upgrade versions in dbt platform](/docs/dbt-versions/upgrade-dbt-version-in-cloud)
  + [Product lifecycles](/docs/dbt-versions/product-lifecycles)
  + [Preview new dbt platform features](/docs/dbt-versions/experimental-features)
  + [dbt version upgrade guides](/docs/dbt-versions/core-upgrade)

    - [Upgrading to the dbt Fusion engine (v2.0)](/docs/dbt-versions/core-upgrade/upgrading-to-fusion)
    - [Upgrading to v1.11 (beta)](/docs/dbt-versions/core-upgrade/upgrading-to-v1.11)
    - [Upgrading to v1.10](/docs/dbt-versions/core-upgrade/upgrading-to-v1.10)
    - [Upgrading to v1.9](/docs/dbt-versions/core-upgrade/upgrading-to-v1.9)
    - [Upgrading to v1.8](/docs/dbt-versions/core-upgrade/upgrading-to-v1.8)
    - [Upgrading to v1.7](/docs/dbt-versions/core-upgrade/upgrading-to-v1.7)
    - [Older versions](/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.6)
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [Available dbt versions](/docs/dbt-versions/about-versions)
* [dbt version upgrade guides](/docs/dbt-versions/core-upgrade)
* Upgrading to v1.7

Copy page

On this page

Upgrading to v1.7
=================

Resources[​](#resources "Direct link to Resources")
---------------------------------------------------

* [Changelog](https://github.com/dbt-labs/dbt-core/blob/1.7.latest/CHANGELOG.md)
* [dbt Core CLI Installation guide](/docs/core/installation-overview)
* [Cloud upgrade guide](/docs/dbt-versions/upgrade-dbt-version-in-cloud)
* [Release schedule](https://github.com/dbt-labs/dbt-core/issues/8260)

What to know before upgrading[​](#what-to-know-before-upgrading "Direct link to What to know before upgrading")
---------------------------------------------------------------------------------------------------------------

dbt Labs is committed to providing backward compatibility for all versions 1.x, with the exception of any changes explicitly mentioned below. If you encounter an error upon upgrading, please let us know by [opening an issue](https://github.com/dbt-labs/dbt-core/issues/new).

### Behavior changes[​](#behavior-changes "Direct link to Behavior changes")

dbt Core v1.7 expands the amount of sources you can configure freshness for. Previously, freshness was limited to sources with a `loaded_at_field`; now, freshness can be generated from warehouse metadata tables when available.

As part of this change, the `loaded_at_field` is no longer required to generate source freshness. If a source has a `freshness:` block, dbt will attempt to calculate freshness for that source:

* If a `loaded_at_field` is provided, dbt will calculate freshness via a select query (previous behavior).
* If a `loaded_at_field` is *not* provided, dbt will calculate freshness via warehouse metadata tables when possible (new behavior).

This is a relatively small behavior change, but worth calling out in case you notice that dbt is calculating freshness for *more* sources than before. To exclude a source from freshness calculations, explicitly set `freshness: null`.

Beginning with v1.7, running [`dbt deps`](/reference/commands/deps) creates or updates the `package-lock.yml` file in the *project\_root* where `packages.yml` is recorded. The `package-lock.yml` file contains a record of all packages installed and, if subsequent `dbt deps` runs contain no updated packages in `dependencies.yml` or `packages.yml`, dbt-core installs from `package-lock.yml`.

To retain the behavior prior to v1.7, there are two main options:

1. Use `dbt deps --upgrade` everywhere `dbt deps` was used previously.
2. Add `package-lock.yml` to your `.gitignore` file.

New and changed features and functionality[​](#new-and-changed-features-and-functionality "Direct link to New and changed features and functionality")
------------------------------------------------------------------------------------------------------------------------------------------------------

* [`dbt docs generate`](/reference/commands/cmd-docs) now supports `--select` to generate [catalog metadata](/reference/artifacts/catalog-json) for a subset of your project.
* [Source freshness](/docs/deploy/source-freshness) can now be generated from warehouse metadata tables.

### MetricFlow enhancements[​](#metricflow-enhancements "Direct link to MetricFlow enhancements")

* Automatically create metrics on measures with [`create_metric: true`](/docs/build/semantic-models).
* Optional [`label`](/docs/build/semantic-models) in semantic\_models, measures, dimensions, and entities.
* New configurations for semantic models - [enable/disable](/reference/resource-configs/enabled), [group](/reference/resource-configs/group), and [meta](/reference/resource-configs/meta).
* Support `fill_nulls_with` and `join_to_timespine` for metric nodes.
* `saved_queries` extends governance beyond the semantic objects to their consumption.

### For consumers of dbt artifacts (metadata)[​](#for-consumers-of-dbt-artifacts-metadata "Direct link to For consumers of dbt artifacts (metadata)")

* The [manifest](/reference/artifacts/manifest-json) schema version has been updated to v11.
* The [run\_results](/reference/artifacts/run-results-json) schema version has been updated to v5.
* There are a few specific changes to the [catalog.json](/reference/artifacts/catalog-json):
  + Added [node attributes](/reference/artifacts/run-results-json) related to compilation (`compiled`, `compiled_code`, `relation_name`) to the `catalog.json`.
  + The nodes dictionary in the `catalog.json` can now be "partial" if `dbt docs generate` is run with a selector.

### Model governance[​](#model-governance "Direct link to Model governance")

dbt Core v1.5 introduced model governance which we're continuing to refine. v1.7 includes these additional features and functionality:

* **[Breaking change detection](/reference/resource-properties/versions#detecting-breaking-changes) for models with contracts enforced:** When dbt detects a breaking change to a model with an enforced contract during state comparison, it will now raise an error for versioned models and a warning for models that are not versioned.
* **[Set `access` as a config](/reference/resource-configs/access):** You can now set a model's `access` within config blocks in the model's file or in the `dbt_project.yml` for an entire subfolder at once.
* **[Type aliasing for model contracts](/reference/resource-configs/contract):** dbt will use each adapter's built-in type aliasing for user-provided data types—meaning you can now write `string` always, and dbt will translate to `text` on Postgres/Redshift. This is "on" by default, but you can opt-out.
* **[Raise warning for numeric types](/reference/resource-configs/contract):** Because of issues when putting `numeric` in model contracts without considering that default values such as `numeric(38,0)` might round decimals accordingly. dbt will now warn you if it finds a numeric type without specified precision/scale.

### dbt clean[​](#dbt-clean "Direct link to dbt clean")

[dbt clean](/reference/commands/clean) only cleans paths within the current working directory. The `--no-clean-project-files-only` flag will delete all paths specified in the `clean-targets` section of `dbt_project.yml`, even if they're outside the dbt project.

Supported flags:

* `--clean-project-files-only` (default)
* `--no-clean-project-files-only`

### Additional attributes in run\_results.json[​](#additional-attributes-in-run_resultsjson "Direct link to Additional attributes in run_results.json")

The run\_results.json now includes three attributes related to the `applied` state that complement `unique_id`:

* `compiled`: Boolean entry of the node compilation status (`False` after parsing, but `True` after compiling).
* `compiled_code`: Rendered string of the code that was compiled (empty after parsing, but full string after compiling).
* `relation_name`: The fully-qualified name of the object that was (or will be) created/updated within the database.

### Deprecated functionality[​](#deprecated-functionality "Direct link to Deprecated functionality")

The ability for installed packages to override built-in materializations without explicit opt-in from the user is being deprecated.

* Overriding a built-in materialization from an installed package raises a deprecation warning.
* Using a custom materialization from an installed package does not raise a deprecation warning.
* Using a built-in materialization package override from the root project via a wrapping materialization is still supported. For example:

  ```
  {% materialization view, default %}  
  {{ return(my_cool_package.materialization_view_default()) }}  
  {% endmaterialization %}
  ```

### Quick hits[​](#quick-hits "Direct link to Quick hits")

With these quick hits, you can now:

* Configure a [`delimiter`](/reference/resource-configs/delimiter) for a seed file.
* Use packages with the same git repo and unique subdirectory.
* Access the `date_spine` macro directly from dbt-core (moved over from dbt-utils).
* Syntax for `DBT_ENV_SECRET_` has changed to `DBT_ENV_SECRET` and no longer requires the closing underscore.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/dbt-versions/core-upgrade/08-upgrading-to-v1.7.md)

Last updated on **Nov 19, 2025**

[Previous

Upgrading to v1.8](/docs/dbt-versions/core-upgrade/upgrading-to-v1.8)[Next

Upgrading to v1.6](/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.6)

* [Resources](#resources)
* [What to know before upgrading](#what-to-know-before-upgrading)
  + [Behavior changes](#behavior-changes)
* [New and changed features and functionality](#new-and-changed-features-and-functionality)
  + [MetricFlow enhancements](#metricflow-enhancements)
  + [For consumers of dbt artifacts (metadata)](#for-consumers-of-dbt-artifacts-metadata)
  + [Model governance](#model-governance)
  + [dbt clean](#dbt-clean)
  + [Additional attributes in run\_results.json](#additional-attributes-in-run_resultsjson)
  + [Deprecated functionality](#deprecated-functionality)
  + [Quick hits](#quick-hits)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/dbt-versions/core-upgrade/08-upgrading-to-v1.7.md)

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