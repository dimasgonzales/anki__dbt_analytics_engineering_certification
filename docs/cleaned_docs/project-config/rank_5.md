Copy page

On this page

About dbt\_project.yml context
==============================

The following context methods and variables are available when configuring
resources in the `dbt_project.yml` file. This applies to the `models:`, `seeds:`,
and `snapshots:` keys in the `dbt_project.yml` file.

**Available context methods:**

* [env\_var](/reference/dbt-jinja-functions/env_var)
* [var](/reference/dbt-jinja-functions/var) (*Note: only variables defined with `--vars` are available*)

**Available context variables:**

* [target](/reference/dbt-jinja-functions/target)
* [builtins](/reference/dbt-jinja-functions/builtins)

### Example configuration[​](#example-configuration "Direct link to Example configuration")

dbt\_project.yml

```
name: my_project  
version: 1.0.0  
  
# Configure the models in models/facts/ to be materialized as views  
# in development and tables in production/CI contexts  
  
models:  
  my_project:  
    facts:  
      +materialized: "{{ 'view' if target.name == 'dev' else 'table' }}"
```