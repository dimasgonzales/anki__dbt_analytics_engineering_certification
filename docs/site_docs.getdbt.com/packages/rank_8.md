# Source: https://docs.getdbt.com/faqs/Troubleshooting/runtime-packages.yml

Why am I receiving a Runtime Error in my packages? | dbt Developer Hub

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
  + [Troubleshooting](/category/troubleshooting)

    - [Generate HAR files](/faqs/Troubleshooting/generate-har-file)
    - [Error when trying to query from Google Drive](/faqs/Troubleshooting/access-gdrive-credential)
    - [Receiving `authentication has expired` error in the IDE](/faqs/Troubleshooting/auth-expired-error)
    - [Could not parse dbt\_project.yml error in dbt](/faqs/Troubleshooting/could-not-parse-project)
    - [Could not find package error](/faqs/Troubleshooting/dispatch-could-not-find-package)
    - [Errors importing a repository on dbt project set up](/faqs/Troubleshooting/error-importing-repo)
    - [Receiving `Failed to connect to database` error](/faqs/Troubleshooting/failed-snowflake-oauth-connection)
    - [Receiving git rev-list master error in the IDE](/faqs/Troubleshooting/git-revlist-error)
    - [How to fix your .gitignore file](/faqs/Troubleshooting/gitignore)
    - [GitLab authentication out of date](/faqs/Troubleshooting/gitlab-authentication)
    - [Unable to trigger a CI job](/faqs/Troubleshooting/gitlab-webhook)
    - [Receiving unknown error in the IDE](/faqs/Troubleshooting/ide-session-unknown-error)
    - [Service token 403 error: Forbidden: Access denied](/faqs/Troubleshooting/ip-restrictions)
    - [Job failures due to exceeded memory limits](/faqs/Troubleshooting/job-memory-limits)
    - [Debug long-running sessions in dbt CLI](/faqs/Troubleshooting/long-sessions-cloud-cli)
    - [NoneType error in the IDE](/faqs/Troubleshooting/nonetype-ide-error)
    - [Partial\_parse error in the IDE](/faqs/Troubleshooting/partial-parsing-error)
    - [Could not find profile named user"error in the IDE](/faqs/Troubleshooting/runtime-error-could-not-find-profile)
    - [Runtime error in packages.yml file](/faqs/Troubleshooting/runtime-packages.yml)
    - [Use SSL exception to resolve `Failed ALPN` error](/faqs/Troubleshooting/sl-alpn-error)
    - [How to debug SQL or database error](/faqs/Troubleshooting/sql-errors)
    - [Receiving an unused model configurations error](/faqs/Troubleshooting/unused-model-configurations)
  + [Warehouse](/category/warehouse)

* [Frequently asked questions](/docs/faqs)
* [Troubleshooting](/category/troubleshooting)
* Runtime error in packages.yml file

Copy page

Why am I receiving a Runtime Error in my packages?
==================================================

If you're receiving the runtime error below in your packages.yml folder, it may be due to an old version of your dbt\_utils package that isn't compatible with your current dbt version.

```
Running with dbt=xxx  
Runtime Error  
  Failed to read package: Runtime Error  
    Invalid config version: 1, expected 2    
  Error encountered in dbt_utils/dbt_project.yml
```

Try updating the old version of the dbt\_utils package in your packages.yml to the latest version found in the [dbt hub](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/):

```
packages:  
- package: dbt-labs/dbt_utils  
  
version: xxx
```

If you've tried the workaround above and are still experiencing this behavior - reach out to the Support team at [support@getdbt.com](mailto:support@getdbt.com) and we'll be happy to help!

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/faqs/Troubleshooting/runtime-packages.yml.md)

Last updated on **Nov 19, 2025**

[Previous

Could not find profile named user"error in the IDE](/faqs/Troubleshooting/runtime-error-could-not-find-profile)[Next

Use SSL exception to resolve `Failed ALPN` error](/faqs/Troubleshooting/sl-alpn-error)

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