# Source: https://docs.getdbt.com/docs/build/seeds

Add Seeds to your DAG | dbt Developer Hub

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

  + [About dbt projects](/docs/build/projects)
  + [dbt tips and tricks](/docs/build/dbt-tips)
  + [Build your DAG](/docs/build/models)

    - [Models](/docs/build/models)
    - [Tests](/docs/build/data-tests)
    - [Documentation](/docs/build/documentation)
    - [Snapshots](/docs/build/snapshots)
    - [Seeds](/docs/build/seeds)
    - [Jinja and macros](/docs/build/jinja-macros)
    - [User-defined functions](/docs/build/udfs)
    - [Sources](/docs/build/sources)
    - [Exposures](/docs/build/exposures)
    - [Groups](/docs/build/groups)
    - [Analyses](/docs/build/analyses)
  + [Build your metrics](/docs/build/build-metrics-intro)
  + [Enhance your models](/docs/build/enhance-your-models)
  + [Enhance your code](/docs/build/enhance-your-code)
  + [Organize your outputs](/docs/build/organize-your-outputs)
  + [Optimize development](/docs/build/empty-flag)
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
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [Build dbt projects](/docs/build/projects)
* [Build your DAG](/docs/build/models)
* Seeds

Copy page

On this page

Add Seeds to your DAG
=====================

Related reference docs[​](#related-reference-docs "Direct link to Related reference docs")
------------------------------------------------------------------------------------------

* [Seed configurations](/reference/seed-configs)
* [Seed properties](/reference/seed-properties)
* [`seed` command](/reference/commands/seed)

Overview[​](#overview "Direct link to Overview")
------------------------------------------------

Seeds are CSV files in your dbt project (typically in your `seeds` directory), that dbt can load into your data warehouse using the `dbt seed` command.

Seeds can be referenced in downstream models the same way as referencing models — by using the [`ref` function](/reference/dbt-jinja-functions/ref).

Because these CSV files are located in your dbt repository, they are version controlled and code reviewable. Seeds are best suited to static data which changes infrequently.

Good use-cases for seeds:

* A list of mappings of country codes to country names
* A list of test emails to exclude from analysis
* A list of employee account IDs

Poor use-cases of dbt seeds:

* Loading raw data that has been exported to CSVs
* Any kind of production data containing sensitive information. For example
  personal identifiable information (PII) and passwords.

Example[​](#example "Direct link to Example")
---------------------------------------------

To load a seed file in your dbt project:

1. Add the file to your `seeds` directory, with a `.csv` file extension, for example, `seeds/country_codes.csv`

seeds/country\_codes.csv

```
country_code,country_name  
US,United States  
CA,Canada  
GB,United Kingdom  
...
```

2. Run the `dbt seed` [command](/reference/commands/seed) — a new table will be created in your warehouse in your target schema, named `country_codes`

```
$ dbt seed  
  
Found 2 models, 3 tests, 0 archives, 0 analyses, 53 macros, 0 operations, 1 seed file  
  
14:46:15 | Concurrency: 1 threads (target='dev')  
14:46:15 |  
14:46:15 | 1 of 1 START seed file analytics.country_codes........................... [RUN]  
14:46:15 | 1 of 1 OK loaded seed file analytics.country_codes....................... [INSERT 3 in 0.01s]  
14:46:16 |  
14:46:16 | Finished running 1 seed in 0.14s.  
  
Completed successfully  
  
Done. PASS=1 ERROR=0 SKIP=0 TOTAL=1
```

3. Refer to seeds in downstream models using the `ref` function.

models/orders.sql

```
-- This refers to the table created from seeds/country_codes.csv  
select * from {{ ref('country_codes') }}
```

Configuring seeds[​](#configuring-seeds "Direct link to Configuring seeds")
---------------------------------------------------------------------------

Seeds are configured in your `dbt_project.yml`, check out the [seed configurations](/reference/seed-configs) docs for a full list of available configurations.

Documenting and testing seeds[​](#documenting-and-testing-seeds "Direct link to Documenting and testing seeds")
---------------------------------------------------------------------------------------------------------------

You can document and test seeds in YAML by declaring properties — check out the docs on [seed properties](/reference/seed-properties) for more information.

FAQs[​](#faqs "Direct link to FAQs")
------------------------------------

Can I use seeds to load raw data?

Seeds should **not** be used to load raw data (for example, large CSV exports from a production database).

Since seeds are version controlled, they are best suited to files that contain business-specific logic, for example a list of country codes or user IDs of employees.

Loading CSVs using dbt's seed functionality is not performant for large files. Consider using a different tool to load these CSVs into your data warehouse.

Can I store my seeds in a directory other than the `seeds` directory in my project?

By default, dbt expects your seed files to be located in the `seeds` subdirectory
of your project.

To change this, update the [seed-paths](/reference/project-configs/seed-paths) configuration in your `dbt_project.yml`
file, like so:

dbt\_project.yml

```
seed-paths: ["custom_seeds"]
```

The columns of my seed changed, and now I get an error when running the `seed` command, what should I do?

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

How do I test and document seeds?

To test and document seeds, use a [schema file](/reference/configs-and-properties) and nest the configurations under a `seeds:` key

Example[​](#example "Direct link to Example")
---------------------------------------------

seeds/schema.yml

```
version: 2  
  
seeds:  
  - name: country_codes  
    description: A mapping of two letter country codes to country names  
    columns:  
      - name: country_code  
        data_tests:  
          - unique  
          - not_null  
      - name: country_name  
        data_tests:  
          - unique  
          - not_null
```

How do I set a datatype for a column in my seed?

dbt will infer the datatype for each column based on the data in your CSV.

You can also explicitly set a datatype using the `column_types` [configuration](/reference/resource-configs/column_types) like so:

dbt\_project.yml

```
seeds:  
  jaffle_shop: # you must include the project name  
    warehouse_locations:  
      +column_types:  
        zipcode: varchar(5)
```

How do I run models downstream of a seed?

You can run models downstream of a seed using the [model selection syntax](/reference/node-selection/syntax), and treating the seed like a model.

For example, the following would run all models downstream of a seed named `country_codes`:

```
$ dbt run --select country_codes+
```

How do I preserve leading zeros in a seed?

If you need to preserve leading zeros (for example in a zipcode or mobile number), include leading zeros in your seed file, and use the `column_types` [configuration](/reference/resource-configs/column_types) with a varchar datatype of the correct length.

How do I build one seed at a time?

You can use a `--select` option with the `dbt seed` command, like so:

```
$ dbt seed --select country_codes
```

There is also an `--exclude` option.

Check out more in the [model selection syntax](/reference/node-selection/syntax) documentation.

Do hooks run with seeds?

Yes! The following hooks are available:

* [pre-hooks & post-hooks](/reference/resource-configs/pre-hook-post-hook)
* [on-run-start & on-run-end hooks](/reference/project-configs/on-run-start-on-run-end)

Configure these in your `dbt_project.yml` file.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/seeds.md)

Last updated on **Nov 19, 2025**

[Previous

Snapshots](/docs/build/snapshots)[Next

Jinja and macros](/docs/build/jinja-macros)

* [Related reference docs](#related-reference-docs)
* [Overview](#overview)
* [Example](#example)
* [Configuring seeds](#configuring-seeds)
* [Documenting and testing seeds](#documenting-and-testing-seeds)
* [FAQs](#faqs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/seeds.md)

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