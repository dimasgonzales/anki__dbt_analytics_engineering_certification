# Source: https://docs.getdbt.com/reference/dbt-jinja-functions/target

About target variables | dbt Developer Hub

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
* [Jinja reference](/category/jinja-reference)

  + [dbt Jinja functions](/reference/dbt-jinja-functions)

    - [adapter](/reference/dbt-jinja-functions/adapter)
    - [as\_bool](/reference/dbt-jinja-functions/as_bool)
    - [as\_native](/reference/dbt-jinja-functions/as_native)
    - [as\_number](/reference/dbt-jinja-functions/as_number)
    - [builtins](/reference/dbt-jinja-functions/builtins)
    - [config](/reference/dbt-jinja-functions/config)
    - [cross-database macros](/reference/dbt-jinja-functions/cross-database-macros)
    - [dbt\_project.yml context](/reference/dbt-jinja-functions/dbt-project-yml-context)
    - [dbt\_version](/reference/dbt-jinja-functions/dbt_version)
    - [debug](/reference/dbt-jinja-functions/debug-method)
    - [dispatch](/reference/dbt-jinja-functions/dispatch)
    - [doc](/reference/dbt-jinja-functions/doc)
    - [env\_var](/reference/dbt-jinja-functions/env_var)
    - [exceptions](/reference/dbt-jinja-functions/exceptions)
    - [execute](/reference/dbt-jinja-functions/execute)
    - [flags](/reference/dbt-jinja-functions/flags)
    - [fromjson](/reference/dbt-jinja-functions/fromjson)
    - [fromyaml](/reference/dbt-jinja-functions/fromyaml)
    - [graph](/reference/dbt-jinja-functions/graph)
    - [invocation\_id](/reference/dbt-jinja-functions/invocation_id)
    - [local\_md5](/reference/dbt-jinja-functions/local_md5)
    - [log](/reference/dbt-jinja-functions/log)
    - [model](/reference/dbt-jinja-functions/model)
    - [modules](/reference/dbt-jinja-functions/modules)
    - [on-run-end context](/reference/dbt-jinja-functions/on-run-end-context)
    - [print](/reference/dbt-jinja-functions/print)
    - [profiles.yml context](/reference/dbt-jinja-functions/profiles-yml-context)
    - [project\_name](/reference/dbt-jinja-functions/project_name)
    - [properties.yml context](/reference/dbt-jinja-functions/dbt-properties-yml-context)
    - [ref](/reference/dbt-jinja-functions/ref)
    - [return](/reference/dbt-jinja-functions/return)
    - [run\_query](/reference/dbt-jinja-functions/run_query)
    - [run\_started\_at](/reference/dbt-jinja-functions/run_started_at)
    - [schema](/reference/dbt-jinja-functions/schema)
    - [schemas](/reference/dbt-jinja-functions/schemas)
    - [selected\_resources](/reference/dbt-jinja-functions/selected_resources)
    - [set](/reference/dbt-jinja-functions/set)
    - [source](/reference/dbt-jinja-functions/source)
    - [statement blocks](/reference/dbt-jinja-functions/statement-blocks)
    - [target](/reference/dbt-jinja-functions/target)
    - [this](/reference/dbt-jinja-functions/this)
    - [thread\_id](/reference/dbt-jinja-functions/thread_id)
    - [tojson](/reference/dbt-jinja-functions/tojson)
    - [toyaml](/reference/dbt-jinja-functions/toyaml)
    - [var](/reference/dbt-jinja-functions/var)
    - [zip](/reference/dbt-jinja-functions/zip)
  + [dbt Classes](/reference/dbt-classes)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Jinja reference](/category/jinja-reference)
* [dbt Jinja functions](/reference/dbt-jinja-functions)
* target

Copy page

On this page

About target variables
======================

The `target` variable contains information about your connection to the warehouse.

* **dbt Core:** These values are based on the target defined in your [profiles.yml](/docs/core/connect-data-platform/profiles.yml) file. Please note that for certain adapters, additional configuration steps may be required. Refer to the [set up page](/docs/core/connect-data-platform/about-core-connections) for your data platform.
* **dbt** To learn more about setting up your adapter in dbt, refer to [About data platform connections](/docs/cloud/connect-data-platform/about-connections).
  + **[Orchestrator](/docs/deploy/job-scheduler)**: `target.name` is defined per job as described in [Custom target names](/docs/build/custom-target-names). For other attributes, values are defined by the deployment connection. To check these values, click **Deploy** and select **Environments**. Then, select the relevant deployment environment, and click **Settings**.
  + **[Studio IDE](/docs/cloud/dbt-cloud-ide/develop-in-the-cloud)**: These values are defined by your connection and credentials. To edit these values, click on your account name in the left side menu and select **Account settings**. Then, click **Credentials**. Select and edit a project to set up the credentials and target name.

Some configurations are shared between all adapters, while others are adapter-specific.

Common[​](#common "Direct link to Common")
------------------------------------------

| Variable | Example | Description |
| --- | --- | --- |
| `target.profile_name` | jaffle\_shop | The name of the active profile |
| `target.name` | dev | Name of the active target |
| `target.schema` | dbt\_alice | Name of the dbt schema (or, dataset on BigQuery) |
| `target.type` | postgres | The active adapter being used. One of "postgres", "snowflake", "bigquery", "redshift", "databricks" |
| `target.threads` | 4 | The number of threads in use by dbt |

Adapter-specific[​](#adapter-specific "Direct link to Adapter-specific")
------------------------------------------------------------------------

### Snowflake[​](#snowflake "Direct link to Snowflake")

| Variable | Example | Description |
| --- | --- | --- |
| `target.database` | RAW | Database name specified in active target. |
| `target.warehouse` | TRANSFORM | Name of the Snowflake virtual warehouse |
| `target.user` | TRANSFORM\_USER | The user specified in the active target |
| `target.role` | TRANSFORM\_ROLE | The role specified in the active target |
| `target.account` | abc123 | The account specified in the active target |

### Postgres/Redshift[​](#postgresredshift "Direct link to Postgres/Redshift")

| Variable | Example | Description |
| --- | --- | --- |
| `target.dbname` | analytics | Database name specified in active target. |
| `target.host` | abc123.us-west-2.redshift.amazonaws.com | The host specified in active target |
| `target.user` | dbt\_user | The user specified in the active target |
| `target.port` | 5439 | The port specified in the active profile |

### BigQuery[​](#bigquery "Direct link to BigQuery")

| Variable | Example | Description |
| --- | --- | --- |
| `target.project` | abc-123 | The project specified in the active profile |
| `target.dataset` | dbt\_alice | The dataset the active profile |

Examples[​](#examples "Direct link to Examples")
------------------------------------------------

### Use `target.name` to limit data in dev[​](#use-targetname-to-limit-data-in-dev "Direct link to use-targetname-to-limit-data-in-dev")

As long as you use sensible target names, you can perform conditional logic to limit data when working in dev.

```
select  
  *  
from source('web_events', 'page_views')  
{% if target.name == 'dev' %}  
where created_at >= dateadd('day', -3, current_date)  
{% endif %}
```

### Use `target.name` to change your source database[​](#use-targetname-to-change-your-source-database "Direct link to use-targetname-to-change-your-source-database")

If you have specific Snowflake databases configured for your dev/qa/prod environments,
you can set up your sources to compile to different databases depending on your
environment.

```
sources:  
  - name: source_name   
    database: |  
      {%- if  target.name == "dev" -%} raw_dev  
      {%- elif target.name == "qa"  -%} raw_qa  
      {%- elif target.name == "prod"  -%} raw_prod  
      {%- else -%} invalid_database  
      {%- endif -%}  
    schema: source_schema
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt-jinja-functions/target.md)

Last updated on **Nov 19, 2025**

[Previous

statement blocks](/reference/dbt-jinja-functions/statement-blocks)[Next

this](/reference/dbt-jinja-functions/this)

* [Common](#common)
* [Adapter-specific](#adapter-specific)
  + [Snowflake](#snowflake)
  + [Postgres/Redshift](#postgresredshift)
  + [BigQuery](#bigquery)
* [Examples](#examples)
  + [Use `target.name` to limit data in dev](#use-targetname-to-limit-data-in-dev)
  + [Use `target.name` to change your source database](#use-targetname-to-change-your-source-database)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt-jinja-functions/target.md)

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