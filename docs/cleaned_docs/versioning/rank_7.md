Copy page

On this page

About dbt\_version variable
===========================

The `dbt_version` variable returns the installed version of dbt that is
currently running. It can be used for debugging or auditing purposes. For details about release versioning, refer to [Versioning](/reference/commands/version#versioning).

Example usages[​](#example-usages "Direct link to Example usages")
------------------------------------------------------------------

macros/get\_version.sql

```
{% macro get_version() %}  
  
  {% do log("The installed version of dbt is: " ~ dbt_version, info=true) %}  
  
{% endmacro %}
```

```
$ dbt run-operation get_version  
The installed version of dbt is 1.6.0
```