Copy page

On this page

group
=====

dbt\_project.yml

```
models:  
  
  <resource-path>:  
    +group: GROUP_NAME
```

models/schema.yml

```
models:  
  - name: MODEL_NAME  
    config:  
      group: GROUP # changed to config in v1.10
```

models/<modelname>.sql

```
{{ config(  
  group='GROUP_NAME'  
) }}  
  
select ...
```

dbt\_project.yml

```
models:  
  <resource-path>:  
    +group: GROUP_NAME
```

seeds/properties.yml

```
seeds:  
  - name: [SEED_NAME]  
    config:  
      group: GROUP_NAME # changed to config in v1.10
```

dbt\_project.yml

```
snapshots:  
  <resource-path>:  
    +group: GROUP_NAME
```

snapshots/<filename>.sql

```
{% snapshot snapshot_name %}  
  
{{ config(  
  group='GROUP_NAME'  
) }}  
  
select ...  
  
{% endsnapshot %}
```

dbt\_project.yml

```
data_tests:  
  <resource-path>:  
    +group: GROUP_NAME
```

tests/properties.yml

```
<resource_type>:  
  - name: <resource_name>  
    data_tests:  
      - <test_name>:  
          config:  
            group: GROUP_NAME
```

tests/<filename>.sql

```
{% test <testname>() %}  
  
{{ config(  
  group='GROUP_NAME'  
) }}  
  
select ...  
  
{% endtest %}
```

tests/<filename>.sql

```
{{ config(  
  group='GROUP_NAME'  
) }}
```

analyses/<filename>.yml

```
analyses:  
  - name: ANALYSIS_NAME  
    config:  
      group: GROUP_NAME # changed to config in v1.10
```

dbt\_project.yml

```
metrics:  
  <resource-path>:  
    +group: GROUP_NAME
```

models/metrics.yml

```
metrics:  
  - name: [METRIC_NAME]  
    config:  
      group: GROUP_NAME
```

dbt\_project.yml

```
semantic-models:  
  <resource-path>:  
    +group: GROUP_NAME
```

models/semantic\_models.yml

```
semantic_models:  
  - name: SEMANTIC_MODEL_NAME  
    config:  
      group: GROUP_NAME
```

dbt\_project.yml

```
saved-queries:  
  <resource-path>:  
    +group: GROUP_NAME
```

models/semantic\_models.yml

```
saved_queries:  
  - name: SAVED_QUERY_NAME  
    config:  
      group: GROUP_NAME
```

Note that for backwards compatibility, `group` is supported as a top-level key, but without the capabilities of config inheritance.

Definition[​](#definition "Direct link to Definition")
------------------------------------------------------

An optional configuration for assigning a group to a resource. When a resource is grouped, dbt will allow it to reference private models within the same group.

For more details on reference access between resources in groups, check out [model access](/docs/mesh/govern/model-access#groups).

Examples[​](#examples "Direct link to Examples")
------------------------------------------------

### Prevent a 'marketing' group model from referencing a private 'finance' group model[​](#prevent-a-marketing-group-model-from-referencing-a-private-finance-group-model "Direct link to Prevent a 'marketing' group model from referencing a private 'finance' group model")

This is useful if you want to prevent other groups from building on top of models that are rapidly changing, experimental, or otherwise internal to a group or team.

models/schema.yml

```
models:  
  - name: finance_model  
    config:  
      group: finance # changed to config in v1.10  
      access: private # changed to config in v1.10  
  - name: marketing_model  
    config:  
      group: marketing # changed to config in v1.10
```

models/marketing\_model.sql

```
select * from {{ ref('finance_model') }}
```

```
$ dbt run -s marketing_model  
...  
dbt.exceptions.DbtReferenceError: Parsing Error  
  Node model.jaffle_shop.marketing_model attempted to reference node model.jaffle_shop.finance_model,   
  which is not allowed because the referenced node is private to the finance group.
```

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------