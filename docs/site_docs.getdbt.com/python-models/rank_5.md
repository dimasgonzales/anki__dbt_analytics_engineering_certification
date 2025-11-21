# Source: https://docs.getdbt.com/faqs/Core/install-python-compatibility

What version of Python can I use? | dbt Developer Hub

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

* [Frequently asked questions](/docs/faqs)

  + [Accounts](/category/accounts)
  + [dbt Core](/category/dbt-core)

    - [Installing dbt Core with pip](/faqs/Core/install-pip-best-practices.md)
    - [dbt Core system prerequisites](/faqs/Core/install-pip-os-prereqs.md)
    - [Python version](/faqs/Core/install-python-compatibility)
  + [Documentation](/category/documentation)
  + [Environments](/category/environments)
  + [Git](/category/git)
  + [Jinja](/category/jinja)
  + [Models](/category/models)
  + [Projects](/category/projects)
  + [Project\_ref](/faqs/Project_ref/define-private-packages)
  + [Runs](/category/runs)
  + [Seeds](/category/seeds)
  + [Snapshots](/category/snapshots)
  + [Tests](/category/tests)
  + [Troubleshooting](/category/troubleshooting)
  + [Warehouse](/category/warehouse)

* [Frequently asked questions](/docs/faqs)
* [dbt Core](/category/dbt-core)
* Python version

Copy page

On this page

What version of Python can I use?
=================================

Use this table to match dbt Core versions with their compatible Python versions. New [dbt minor versions](/docs/dbt-versions/core#minor-versions) will add support for new Python3 minor versions when all dependencies can support it. In addition, dbt minor versions will withdraw support for old Python3 minor versions before their [end of life](https://endoflife.date/python).

Python compatibility matrix[​](#python-compatibility-matrix "Direct link to Python compatibility matrix")
---------------------------------------------------------------------------------------------------------

| dbt-core version | v1.11 | v1.10 | v1.9 | v1.8 | v1.7 | v1.6 | v1.5 | v1.4 | v1.3 | v1.2 | v1.1 | v1.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python 3.13 | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Python 3.12 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Python 3.11 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Python 3.10 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

⚠️ Python 3.13 is supported in dbt Core v1.10 for the Postgres adapter, with official support for more adapters coming soon.

Adapter plugins and their dependencies are not always compatible with the latest version of Python.

Note that this shouldn't be confused with [dbt Python models](/docs/build/python-models#specific-data-platforms). If you're using a data platform that supports Snowpark, use the `python_version` config to run a Snowpark model with [Python versions](https://docs.snowflake.com/en/developer-guide/snowpark/python/setup) 3.9, 3.10, or 3.11.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/faqs/Core/install-python-compatibility.md)

Last updated on **Nov 19, 2025**

[Previous

dbt Core system prerequisites](/faqs/Core/install-pip-os-prereqs.md)[Next

Documentation](/category/documentation)

* [Python compatibility matrix](#python-compatibility-matrix)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/faqs/Core/install-python-compatibility.md)

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