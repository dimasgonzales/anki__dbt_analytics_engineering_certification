# Source: https://docs.getdbt.com/reference/dbt-jinja-functions/model

About model object | dbt Developer Hub

[Skip to main content](#__docusaurus_skipToContent_fallback)

[✨ Live virtual event - Smarter pipelines, 29% more efficient: How the dbt Fusion engine optimizes data work on December 3rd!](https://www.getdbt.com/resources/webinars/how-the-dbt-fusion-engine-optimizes-data-work)

[![dbt Logo](/img/dbt-logo.svg?v=2)](/)

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

[dbt platform (Latest)](#)

* dbt platform (Latest)
* dbt Fusion engine
* Core v1.11 Beta
* Core v1.10 (Compatible)
* Core v1.9 (Extended)

Search`⌘``K`

[![dbt Logo](/img/dbt-logo.svg?v=2)](/)

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
* model

Copy page

On this page

About model object
==================

`model` is the dbt [graph object](/reference/dbt-jinja-functions/graph) (or node) for the current model. It can be used to:

* Access `config` settings, say, in a post-hook
* Access the path to the model

For example:

```
{% if model.config.materialized == 'view' %}  
  {{ log(model.name ~ " is a view.", info=True) }}  
{% endif %}
```

To view the contents of `model` for a given model:

* Command line interface
* Studio IDE

If you're using the command line interface (CLI), use [log()](/reference/dbt-jinja-functions/log) to print the full contents:

```
{{ log(model, info=True) }}
```

If you're using the Studio IDE, compile the following to print the full contents:

```
{{ model | tojson(indent = 4) }}
```

Batch properties for microbatch models[​](#batch-properties-for-microbatch-models "Direct link to Batch properties for microbatch models")
------------------------------------------------------------------------------------------------------------------------------------------

Starting in dbt Core v1.9, the model object includes a `batch` property (`model.batch`), which provides details about the current batch when executing an [incremental microbatch](/docs/build/incremental-microbatch) model. This property is only populated during the batch execution of a microbatch model.

The following table describes the properties of the `batch` object. Note that dbt appends the property to the `model` and `batch` objects.

| Property | Description | Example |
| --- | --- | --- |
| `id` | The unique identifier for the batch within the context of the microbatch model. | `model.batch.id` |
| `event_time_start` | The start time of the batch's [`event_time`](/reference/resource-configs/event-time) filter (inclusive). | `model.batch.event_time_start` |
| `event_time_end` | The end time of the batch's `event_time` filter (exclusive). | `model.batch.event_time_end` |

### Usage notes[​](#usage-notes "Direct link to Usage notes")

`model.batch` is only available during the execution of a microbatch model batch. Outside of the microbatch execution, `model.batch` is `None`, and its sub-properties aren't accessible.

#### Example of safeguarding access to batch properties[​](#example-of-safeguarding-access-to-batch-properties "Direct link to Example of safeguarding access to batch properties")

We recommend to always check if `model.batch` is populated before accessing its properties. To do this, use an `if` statement for safe access to `batch` properties:

```
{% if model.batch %}  
  {{ log(model.batch.id) }}  # Log the batch ID #  
  {{ log(model.batch.event_time_start) }}  # Log the start time of the batch #  
  {{ log(model.batch.event_time_end) }}  # Log the end time of the batch #  
{% endif %}
```

In this example, the `if model.batch` statement makes sure that the code only runs during a batch execution. `log()` is used to print the `batch` properties for debugging.

#### Example of log batch details[​](#example-of-log-batch-details "Direct link to Example of log batch details")

This is a practical example of how you might use `model.batch` in a microbatch model to log batch details for the `batch.id`:

```
{% if model.batch %}  
  {{ log("Processing batch with ID: " ~ model.batch.id, info=True) }}  
  {{ log("Batch event time range: " ~ model.batch.event_time_start ~ " to " ~ model.batch.event_time_end, info=True) }}  
{% endif %}
```

In this example, the `if model.batch` statement makes sure that the code only runs during a batch execution. `log()` is used to print the `batch` properties for debugging.

Model structure and JSON schema[​](#model-structure-and-json-schema "Direct link to Model structure and JSON schema")
---------------------------------------------------------------------------------------------------------------------

To view the structure of `models` and their definitions:

* Refer to [dbt JSON Schema](https://schemas.getdbt.com/) for describing and consuming dbt generated artifacts
* Select the corresponding manifest version under **Manifest**. For example if you're on dbt v1.8, then you would select Manifest v12
  + The `manifest.json` version number is related to (but not *equal* to) your dbt version, so you *must* use the correct `manifest.json` version for your dbt version. To find the correct `manifest.json` version, refer to [Manifest](/reference/artifacts/manifest-json) and select the dbt version on the top navigation (such as `v1.5`). This will help you find out which tags are associated with your model.
* Then go to `nodes` --> Select Additional properties --> `CompiledModelNode` or view other definitions/objects.

Use the following table to understand how the versioning pattern works and match the Manifest version with the dbt version:

| dbt version | Manifest version |
| --- | --- |
| dbt Fusion Engine v2.0 | v20 (Identical to [v12](https://schemas.getdbt.com/dbt/manifest/v12/index.html)) |
| Core v1.11 | [v12](https://schemas.getdbt.com/dbt/manifest/v12/index.html) |
| Core v1.10 | [v12](https://schemas.getdbt.com/dbt/manifest/v12/index.html) |
| Core v1.9 | [v12](https://schemas.getdbt.com/dbt/manifest/v12/index.html) |
| Core v1.8 | [v12](https://schemas.getdbt.com/dbt/manifest/v12/index.html) |
| Core v1.7 | [v11](https://schemas.getdbt.com/dbt/manifest/v11/index.html) |
| Core v1.6 | [v10](https://schemas.getdbt.com/dbt/manifest/v10/index.html) |
| Core v1.5 | [v9](https://schemas.getdbt.com/dbt/manifest/v9/index.html) |
| Core v1.4 | [v8](https://schemas.getdbt.com/dbt/manifest/v8/index.html) |
| Core v1.3 | [v7](https://schemas.getdbt.com/dbt/manifest/v7/index.html) |

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------

* [dbt JSON Schema](https://schemas.getdbt.com/)

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt-jinja-functions/model.md)

Last updated on **Nov 19, 2025**

[Previous

log](/reference/dbt-jinja-functions/log)[Next

modules](/reference/dbt-jinja-functions/modules)

* [Batch properties for microbatch models](#batch-properties-for-microbatch-models)
  + [Usage notes](#usage-notes)
* [Model structure and JSON schema](#model-structure-and-json-schema)
* [Related docs](#related-docs)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt-jinja-functions/model.md)

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