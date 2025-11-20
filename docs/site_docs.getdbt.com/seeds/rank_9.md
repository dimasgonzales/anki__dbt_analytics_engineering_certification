# Source: https://docs.getdbt.com/faqs/Seeds/full-refresh-seed

The columns of my seed changed, and now I get an error when running the `seed` command, what should I do? | dbt Developer Hub

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

    - [Build one seed at a time](/faqs/Seeds/build-one-seed)
    - [How to name seeds directory](/faqs/Seeds/configurable-data-path)
    - [debug error when columns of seed changes](/faqs/Seeds/full-refresh-seed)
    - [Include leading zeroes in your seed file](/faqs/Seeds/leading-zeros-in-seed)
    - [Seed data files requirements](/faqs/Seeds/load-raw-data-with-seed)
    - [Build seeds in a schema outside target schema](/faqs/Seeds/seed-custom-schemas)
    - [Set a datatype for a column in seed](/faqs/Seeds/seed-datatypes)
    - [Use hooks to run with seeds](/faqs/Seeds/seed-hooks)
  + [Snapshots](/category/snapshots)
  + [Tests](/category/tests)
  + [Troubleshooting](/category/troubleshooting)
  + [Warehouse](/category/warehouse)

* [Frequently asked questions](/docs/faqs)
* [Seeds](/category/seeds)
* debug error when columns of seed changes

Copy page

The columns of my seed changed, and now I get an error when running the `seed` command, what should I do?
=========================================================================================================

If you changed the columns of your seed, you may get a `Database Error`:

* Snowflake
* Redshift

```
$ dbt seed  
Running with dbt=1.6.0-rc2  
Found 0 models, 0 tests, 0 snapshots, 0 analyses, 130 macros, 0 operations, 1 seed file, 0 sources  
  
12:12:27 | Concurrency: 8 threads (target='dev_snowflake')  
12:12:27 |  
12:12:27 | 1 of 1 START seed file dbt_claire.country_codes...................... [RUN]  
12:12:30 | 1 of 1 ERROR loading seed file dbt_claire.country_codes.............. [ERROR in 2.78s]  
12:12:31 |  
12:12:31 | Finished running 1 seed in 10.05s.  
  
Completed with 1 error and 0 warnings:  
  
Database Error in seed country_codes (seeds/country_codes.csv)  
  000904 (42000): SQL compilation error: error line 1 at position 62  
  invalid identifier 'COUNTRY_NAME'  
  
Done. PASS=0 WARN=0 ERROR=1 SKIP=0 TOTAL=1
```

```
$ dbt seed  
Running with dbt=1.6.0-rc2  
Found 0 models, 0 tests, 0 snapshots, 0 analyses, 149 macros, 0 operations, 1 seed file, 0 sources  
  
12:14:46 | Concurrency: 1 threads (target='dev_redshift')  
12:14:46 |  
12:14:46 | 1 of 1 START seed file dbt_claire.country_codes...................... [RUN]  
12:14:46 | 1 of 1 ERROR loading seed file dbt_claire.country_codes.............. [ERROR in 0.23s]  
12:14:46 |  
12:14:46 | Finished running 1 seed in 1.75s.  
  
Completed with 1 error and 0 warnings:  
  
Database Error in seed country_codes (seeds/country_codes.csv)  
  column "country_name" of relation "country_codes" does not exist  
  
Done. PASS=0 WARN=0 ERROR=1 SKIP=0 TOTAL=1
```

In this case, you should rerun the command with a `--full-refresh` flag, like so:

```
dbt seed --full-refresh
```

**Why is this the case?**

When you typically run dbt seed, dbt truncates the existing table and reinserts the data. This pattern avoids a `drop cascade` command, which may cause downstream objects (that your BI users might be querying!) to get dropped.

However, when column names are changed, or new columns are added, these statements will fail as the table structure has changed.

The `--full-refresh` flag will force dbt to `drop cascade` the existing table before rebuilding it.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/faqs/Seeds/full-refresh-seed.md)

Last updated on **Nov 19, 2025**

[Previous

How to name seeds directory](/faqs/Seeds/configurable-data-path)[Next

Include leading zeroes in your seed file](/faqs/Seeds/leading-zeros-in-seed)

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