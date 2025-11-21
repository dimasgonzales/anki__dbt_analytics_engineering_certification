# Source: https://docs.getdbt.com/reference/artifacts/run-results-json

Run results JSON file | dbt Developer Hub

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
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)

  + [About dbt artifacts](/reference/artifacts/dbt-artifacts)
  + [Catalog](/reference/artifacts/catalog-json)
  + [Manifest](/reference/artifacts/manifest-json)
  + [Run results](/reference/artifacts/run-results-json)
  + [Sources](/reference/artifacts/sources-json)
  + [Semantic manifest](/reference/artifacts/sl-manifest)
  + [Other artifacts](/reference/artifacts/other-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* Run results

Copy page

On this page

Run results JSON file
=====================

**Current schema**: [`v6`](https://schemas.getdbt.com/dbt/run-results/v6/index.html)

**Produced by:**
[`build`](/reference/commands/build)
[`clone`](/reference/commands/clone)
[`compile`](/reference/commands/compile)
[`docs generate`](/reference/commands/cmd-docs)
[`retry`](/reference/commands/retry)
[`run`](/reference/commands/run)
[`seed`](/reference/commands/seed)
[`show`](/reference/commands/show)
[`snapshot`](/reference/commands/snapshot)
[`test`](/reference/commands/test)
[`run-operation`](/reference/commands/run-operation)

This file contains information about a completed invocation of dbt, including timing and status info for each node (model, test, etc) that was executed. In aggregate, many `run_results.json` can be combined to calculate average model runtime, test failure rates, the number of record changes captured by snapshots, etc.

Note that only executed nodes appear in the run results. If you have multiple run or test steps with different critiera, each will produce different run results.

Note: `dbt source freshness` produces a different artifact, [`sources.json`](/reference/artifacts/sources-json), with similar attributes.

### Top-level keys[​](#top-level-keys "Direct link to Top-level keys")

* [`metadata`](/reference/artifacts/dbt-artifacts#common-metadata)
* `args`: Dictionary of arguments passed to the CLI command or RPC method that produced this artifact. Most useful is `which` (command) or `rpc_method`. This dict excludes null values, and includes default values if they are not null. Equivalent to [`invocation_args_dict`](/reference/dbt-jinja-functions/flags#invocation_args_dict) in the dbt-Jinja context.
* `elapsed_time`: Total invocation time in seconds.
* `results`: Array of node execution details.

Each entry in `results` is a [`Result` object](/reference/dbt-classes#result-objects), with one difference: Instead of including the entire `node` object, only the `unique_id` is included. (The full `node` object is recorded in [`manifest.json`](/reference/artifacts/manifest-json).)

* `unique_id`: Unique node identifier, which maps results to `nodes` in the [manifest](/reference/artifacts/manifest-json)
* `status`: dbt's interpretation of runtime success, failure, or error
* `thread_id`: Which thread executed this node? E.g. `Thread-1`
* `execution_time`: Total time spent executing this node
* `timing`: Array that breaks down execution time into steps (often `compile` + `execute`)
* `message`: How dbt will report this result on the CLI, based on information returned from the database

* `adapter_response`: Dictionary of metadata returned from the database, which varies by adapter. For example, success `code`, number of `rows_affected`, total `bytes_processed`, and so on. Not applicable for [data tests](/docs/build/data-tests).
  + `rows_affected` returns the number of rows modified by the last statement executed. In cases where the query's row count can't be determined or isn't applicable (such as when creating a view), a [standard value](https://peps.python.org/pep-0249/#rowcount) of `-1` is returned for `rowcount`.

The run\_results.json includes three attributes related to the `applied` state that complement `unique_id`:

* `compiled`: Boolean entry of the node compilation status (`False` after parsing, but `True` after compiling).
* `compiled_code`: Rendered string of the code that was compiled (empty after parsing, but full string after compiling).
* `relation_name`: The fully-qualified name of the object that was (or will be) created/updated within the database.

Continue to look up additional information about the `logical` state of nodes using the full node object in manifest.json via the `unique_id`.

Examples[​](#examples "Direct link to Examples")
------------------------------------------------

Here are a few examples and the resulting output to the `run_results.json` file.

### Compile model results[​](#compile-model-results "Direct link to Compile model results")

Let's say that you have a model that looks like this:

models/my\_model.sql

```
select {{ dbt.current_timestamp() }} as created_at
```

Compile the model:

```
dbt compile -s my_model
```

Here's a printed snippet from the `run_results.json`:

```
    {  
      "status": "success",  
      "timing": [  
        {  
          "name": "compile",  
          "started_at": "2023-10-12T16:35:28.510434Z",  
          "completed_at": "2023-10-12T16:35:28.519086Z"  
        },  
        {  
          "name": "execute",  
          "started_at": "2023-10-12T16:35:28.521633Z",  
          "completed_at": "2023-10-12T16:35:28.521641Z"  
        }  
      ],  
      "thread_id": "Thread-2",  
      "execution_time": 0.0408780574798584,  
      "adapter_response": {},  
      "message": null,  
      "failures": null,  
      "unique_id": "model.my_project.my_model",  
      "compiled": true,  
      "compiled_code": "select now() as created_at",  
      "relation_name": "\"postgres\".\"dbt_dbeatty\".\"my_model\""  
    }
```

### Run generic data tests[​](#run-generic-data-tests "Direct link to Run generic data tests")

Use the [`store_failures_as`](/reference/resource-configs/store_failures_as) config to store failures for only one data test in the database:

models/\_models.yml

```
models:  
  - name: my_model  
    columns:  
      - name: created_at  
        data_tests:  
          - not_null:  
              config:  
                store_failures_as: view  
          - unique:  
              config:  
                store_failures_as: ephemeral
```

Run the built-in `unique` test and store the failures as a table:

```
dbt test -s my_model
```

Here's a printed snippet from the `run_results.json`:

```
  "results": [  
    {  
      "status": "pass",  
      "timing": [  
        {  
          "name": "compile",  
          "started_at": "2023-10-12T17:20:51.279437Z",  
          "completed_at": "2023-10-12T17:20:51.317312Z"  
        },  
        {  
          "name": "execute",  
          "started_at": "2023-10-12T17:20:51.319812Z",  
          "completed_at": "2023-10-12T17:20:51.441967Z"  
        }  
      ],  
      "thread_id": "Thread-2",  
      "execution_time": 0.1807551383972168,  
      "adapter_response": {  
        "_message": "SELECT 1",  
        "code": "SELECT",  
        "rows_affected": 1  
      },  
      "message": null,  
      "failures": 0,  
      "unique_id": "test.my_project.unique_my_model_created_at.a9276afbbb",  
      "compiled": true,  
      "compiled_code": "\n    \n    \n\nselect\n    created_at as unique_field,\n    count(*) as n_records\n\nfrom \"postgres\".\"dbt_dbeatty\".\"my_model\"\nwhere created_at is not null\ngroup by created_at\nhaving count(*) > 1\n\n\n",  
      "relation_name": null  
    },  
    {  
      "status": "pass",  
      "timing": [  
        {  
          "name": "compile",  
          "started_at": "2023-10-12T17:20:51.274049Z",  
          "completed_at": "2023-10-12T17:20:51.295237Z"  
        },  
        {  
          "name": "execute",  
          "started_at": "2023-10-12T17:20:51.296361Z",  
          "completed_at": "2023-10-12T17:20:51.491327Z"  
        }  
      ],  
      "thread_id": "Thread-1",  
      "execution_time": 0.22345590591430664,  
      "adapter_response": {  
        "_message": "SELECT 1",  
        "code": "SELECT",  
        "rows_affected": 1  
      },  
      "message": null,  
      "failures": 0,  
      "unique_id": "test.my_project.not_null_my_model_created_at.9b412fbcc7",  
      "compiled": true,  
      "compiled_code": "\n    \n    \n\n\n\nselect *\nfrom \"postgres\".\"dbt_dbeatty\".\"my_model\"\nwhere created_at is null\n\n\n",  
      "relation_name": "\"postgres\".\"dbt_dbeatty_dbt_test__audit\".\"not_null_my_model_created_at\""  
    }  
  ],
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/artifacts/run-results-json.md)

Last updated on **Nov 19, 2025**

[Previous

Manifest](/reference/artifacts/manifest-json)[Next

Sources](/reference/artifacts/sources-json)

* [Top-level keys](#top-level-keys)
* [Examples](#examples)
  + [Compile model results](#compile-model-results)
  + [Run generic data tests](#run-generic-data-tests)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/artifacts/run-results-json.md)

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