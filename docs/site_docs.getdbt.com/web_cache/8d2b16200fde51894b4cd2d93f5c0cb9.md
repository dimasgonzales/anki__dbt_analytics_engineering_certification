# Source: https://docs.getdbt.com/reference/dbt-jinja-functions

dbt Jinja functions | dbt Developer Hub

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
* dbt Jinja functions

dbt Jinja functions
===================

In addition to the standard Jinja library, we've added additional functions and variables to the Jinja context that are useful when working with a dbt project.

[📄️ adapter
----------

Wrap the internal database adapter with the Jinja object `adapter`.](/reference/dbt-jinja-functions/adapter)

[📄️ as\_bool
-----------

Use this filter to coerce a Jinja output into boolean value.](/reference/dbt-jinja-functions/as_bool)

[📄️ as\_native
-------------

Use this filter to coerce Jinja-compiled output into its native python.](/reference/dbt-jinja-functions/as_native)

[📄️ as\_number
-------------

Use this filter to convert Jinja-compiled output to a numeric value..](/reference/dbt-jinja-functions/as_number)

[📄️ builtins
-----------

Read this guide to understand the builtins Jinja variable in dbt.](/reference/dbt-jinja-functions/builtins)

[📄️ config
---------

Read this guide to understand the config Jinja function in dbt.](/reference/dbt-jinja-functions/config)

[📄️ cross-database macros
------------------------

Read this guide to understand cross-database macros in dbt.](/reference/dbt-jinja-functions/cross-database-macros)

[📄️ dbt\_project.yml context
---------------------------

The context methods and variables available when configuring resources in the dbt\_project.yml file.](/reference/dbt-jinja-functions/dbt-project-yml-context)

[📄️ dbt\_version
---------------

Read this guide to understand the dbt\_version Jinja function in dbt.](/reference/dbt-jinja-functions/dbt_version)

[📄️ debug
--------

The `{{ debug() }}` macro will open an iPython debugger.](/reference/dbt-jinja-functions/debug-method)

[📄️ dispatch
-----------

dbt extends functionality across data platforms using multiple dispatch.](/reference/dbt-jinja-functions/dispatch)

[📄️ doc
------

Use the `doc` to reference docs blocks in description fields.](/reference/dbt-jinja-functions/doc)

[📄️ env\_var
-----------

Incorporate environment variables using `en\_var` function.](/reference/dbt-jinja-functions/env_var)

[📄️ exceptions
-------------

Raise warnings/errors with the `exceptions` namespace.](/reference/dbt-jinja-functions/exceptions)

[📄️ execute
----------

Use `execute` to return True when dbt is in 'execute' mode.](/reference/dbt-jinja-functions/execute)

[📄️ flags
--------

The `flags` variable contains values of flags provided on the cli.](/reference/dbt-jinja-functions/flags)

[📄️ fromjson
-----------

Deserialize a JSON string into python with `fromjson` context method.](/reference/dbt-jinja-functions/fromjson)

[📄️ fromyaml
-----------

Deserialize a YAML string into python with `fromyaml` context method.](/reference/dbt-jinja-functions/fromyaml)

[📄️ graph
--------

The `graph` context variable contains info about nodes in your project.](/reference/dbt-jinja-functions/graph)

[📄️ invocation\_id
-----------------

The `invocation\_id` outputs a UUID generated for this dbt command.](/reference/dbt-jinja-functions/invocation_id)

[📄️ local\_md5
-------------

Calculate an MD5 hash of a string with `local\_md5` context variable.](/reference/dbt-jinja-functions/local_md5)

[📄️ log
------

Learn more about the log Jinja function in dbt.](/reference/dbt-jinja-functions/log)

[📄️ model
--------

`model` is the dbt graph object (or node) for the current model.](/reference/dbt-jinja-functions/model)

[📄️ modules
----------

`modules` Jinja variables has useful Python modules to operate data.](/reference/dbt-jinja-functions/modules)

[📄️ on-run-end context
---------------------

Use these variables in the context for `on-run-end` hooks.](/reference/dbt-jinja-functions/on-run-end-context)

[📄️ print
--------

Use the `print()` to print messages to the log file and stdout.](/reference/dbt-jinja-functions/print)

[📄️ profiles.yml context
-----------------------

Use these context methods to configure resources in `profiles.yml` file.](/reference/dbt-jinja-functions/profiles-yml-context)

[📄️ project\_name
----------------

Read this guide to understand the project\_name Jinja function in dbt.](/reference/dbt-jinja-functions/project_name)

[📄️ properties.yml context
-------------------------

The context methods and variables available when configuring resources in a properties.yml file.](/reference/dbt-jinja-functions/dbt-properties-yml-context)

[📄️ ref
------

Read this guide to understand the ref Jinja function in dbt.](/reference/dbt-jinja-functions/ref)

[📄️ return
---------

Read this guide to understand the return Jinja function in dbt.](/reference/dbt-jinja-functions/return)

[📄️ run\_query
-------------

Use `run\_query` macro to run queries and fetch results.](/reference/dbt-jinja-functions/run_query)

[📄️ run\_started\_at
-------------------

Use `run\_started\_at` to output the timestamp the run started.](/reference/dbt-jinja-functions/run_started_at)

[📄️ schema
---------

The schema that the model is configured to be materialized in.](/reference/dbt-jinja-functions/schema)

[📄️ schemas
----------

A list of schemas where dbt built objects during the current run.](/reference/dbt-jinja-functions/schemas)

[📄️ selected\_resources
----------------------

Contains a list of all the nodes selected by current dbt command.](/reference/dbt-jinja-functions/selected_resources)

[📄️ set
------

Converts any iterable to a sequence of iterable and unique elements.](/reference/dbt-jinja-functions/set)

[📄️ source
---------

Read this guide to understand the source Jinja function in dbt.](/reference/dbt-jinja-functions/source)

[📄️ statement blocks
-------------------

SQL queries that hit database and return results to your Jinja context.](/reference/dbt-jinja-functions/statement-blocks)

[📄️ target
---------

The `target` variable contains information about your connection to the warehouse.](/reference/dbt-jinja-functions/target)

[📄️ this
-------

Represents the current model in the database.](/reference/dbt-jinja-functions/this)

[📄️ thread\_id
-------------

The `thread\_id` outputs an identifier for the current Python thread.](/reference/dbt-jinja-functions/thread_id)

[📄️ tojson
---------

Use this context method to serialize a Python object primitive.](/reference/dbt-jinja-functions/tojson)

[📄️ toyaml
---------

Used to serialize a Python object primitive.](/reference/dbt-jinja-functions/toyaml)

[📄️ var
------

Pass variables from `dbt\_project.yml` file into models.](/reference/dbt-jinja-functions/var)

[📄️ zip
------

Use this context method to return an iterator of tuples.](/reference/dbt-jinja-functions/zip)

[Previous

Jinja reference](/category/jinja-reference)[Next

adapter](/reference/dbt-jinja-functions/adapter)

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