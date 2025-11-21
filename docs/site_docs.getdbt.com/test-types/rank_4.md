# Source: https://docs.getdbt.com/faqs/Tests/available-tests

What data tests are available for me to use in dbt? | dbt Developer Hub

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

    - [Available data test to use in dbt](/faqs/Tests/available-tests)
    - [How to name data tests directory](/faqs/Tests/configurable-data-test-path)
    - [How to set failure thresholds in test](/faqs/Tests/custom-test-thresholds)
    - [Recommended data tests for project](/faqs/Tests/recommended-tests)
    - [Testing one model at a time](/faqs/Tests/test-one-model)
    - [Test and document seeds](/faqs/Tests/testing-seeds)
    - [Run data tests on all sources](/faqs/Tests/testing-sources)
    - [Test the uniqueness of two columns](/faqs/Tests/uniqueness-two-columns)
    - [When to run data tests](/faqs/Tests/when-to-test)
  + [Troubleshooting](/category/troubleshooting)
  + [Warehouse](/category/warehouse)

* [Frequently asked questions](/docs/faqs)
* [Tests](/category/tests)
* Available data test to use in dbt

Copy page

What data tests are available for me to use in dbt?
===================================================

Out of the box, dbt ships with the following data tests:

* `unique`
* `not_null`
* `accepted_values`
* `relationships` (i.e. referential integrity)

You can also write your own [custom schema data tests](/docs/build/data-tests).

Some additional custom schema tests have been open-sourced in the [dbt-utils package](https://github.com/dbt-labs/dbt-utils?#generic-tests), check out the docs on [packages](/docs/build/packages) to learn how to make these tests available in your project.

Note that although you can't document data tests as of yet, we recommend checking out [this dbt Core discussion](https://github.com/dbt-labs/dbt-core/issues/2578) where the dbt community shares ideas.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/faqs/Tests/available-tests.md)

Last updated on **Nov 19, 2025**

[Previous

Tests](/category/tests)[Next

How to name data tests directory](/faqs/Tests/configurable-data-test-path)

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