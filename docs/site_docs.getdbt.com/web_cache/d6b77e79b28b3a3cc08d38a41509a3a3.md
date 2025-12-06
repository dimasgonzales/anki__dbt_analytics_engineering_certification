# Source: https://docs.getdbt.com/reference/dbt-jinja-functions/run_query

About run\_query macro | dbt Developer Hub

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
* run\_query

Copy page

About run\_query macro
======================

The `run_query` macro provides a convenient way to run queries and fetch their results. It is a wrapper around the [statement block](/reference/dbt-jinja-functions/statement-blocks), which is more flexible, but also more complicated to use.

**Args**:

* `sql`: The SQL query to execute

Returns a [Table](https://agate.readthedocs.io/page/api/table.html) object with the result of the query. If the specified query does not return results (eg. a DDL, DML, or maintenance query), then the return value will be `none`.

**Note:** The `run_query` macro will not begin a transaction automatically - if you wish to run your query inside of a transaction, please use `begin` and `commit`  statements as appropriate.

Using run\_query for the first time?

Check out the section of the Getting Started guide on [using Jinja](/guides/using-jinja#dynamically-retrieve-the-list-of-payment-methods) for an example of working with the results of the `run_query` macro!

**Example Usage:**

models/my\_model.sql

```
{% set results = run_query('select 1 as id') %}  
  
{% if results is not none %}  
  {{ log(results.print_table(), info=True) }}  
{% endif %}  
  
{# do something with `results` here... #}
```

macros/run\_grants.sql

```
{% macro run_vacuum(table) %}  
  
  {% set query %}  
    vacuum table {{ table }}  
  {% endset %}  
  
  {% do run_query(query) %}  
{% endmacro %}
```

Here's an example of using this (though if you're using `run_query` to return the values of a column, check out the [get\_column\_values](https://github.com/dbt-labs/dbt-utils#get_column_values-source) macro in the dbt-utils package).

models/my\_model.sql

```
{% set payment_methods_query %}  
select distinct payment_method from app_data.payments  
order by 1  
{% endset %}  
  
{% set results = run_query(payment_methods_query) %}  
  
{% if execute %}  
{# Return the first column #}  
{% set results_list = results.columns[0].values() %}  
{% else %}  
{% set results_list = [] %}  
{% endif %}  
  
select  
order_id,  
{% for payment_method in results_list %}  
sum(case when payment_method = '{{ payment_method }}' then amount end) as {{ payment_method }}_amount,  
{% endfor %}  
sum(amount) as total_amount  
from {{ ref('raw_payments') }}  
group by 1
```

You can also use `run_query` to perform SQL queries that aren't select statements.

macros/run\_vacuum.sql

```
{% macro run_vacuum(table) %}  
  
  {% set query %}  
    vacuum table {{ table }}  
  {% endset %}  
  
  {% do run_query(query) %}  
{% endmacro %}
```

Use the `length` filter to verify whether `run_query` returned any rows or not. Make sure to wrap the logic in an [if execute](/reference/dbt-jinja-functions/execute) block to avoid unexpected behavior during parsing.

```
{% if execute %}  
{% set results = run_query(payment_methods_query) %}  
{% if results|length > 0 %}  
  	-- do something with `results` here...  
{% else %}  
    -- do fallback here...  
{% endif %}  
{% endif %}
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/dbt-jinja-functions/run_query.md)

Last updated on **Nov 19, 2025**

[Previous

return](/reference/dbt-jinja-functions/return)[Next

run\_started\_at](/reference/dbt-jinja-functions/run_started_at)

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