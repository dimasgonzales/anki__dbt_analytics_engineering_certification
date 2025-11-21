Copy page

On this page

Model configurations
====================

Related documentation[​](#related-documentation "Direct link to Related documentation")
---------------------------------------------------------------------------------------

* [Models](/docs/build/models)
* [`run` command](/reference/commands/run)

Available configurations[​](#available-configurations "Direct link to Available configurations")
------------------------------------------------------------------------------------------------

### Model-specific configurations[​](#model-specific-configurations "Direct link to Model-specific configurations")

Resource-specific configurations are applicable to only one dbt resource type rather than multiple resource types. You can define these settings in the project file (`dbt_project.yml`), a property file (`models/properties.yml` for models, similarly for other resources), or within the resource’s file using the `{{ config() }}` macro.

The following resource-specific configurations are only available to Models:

* Project file
* Property file
* Config block

dbt\_project.yml

models/<model\_name>.sql

### General configurations[​](#general-configurations "Direct link to General configurations")

General configurations provide broader operational settings applicable across multiple resource types. Like resource-specific configurations, these can also be set in the project file, property files, or within resource-specific files.

* Project file
* Property file
* Config block

dbt\_project.yml

models/properties.yml

models/<model\_name>.sql

### Warehouse-specific configurations[​](#warehouse-specific-configurations "Direct link to Warehouse-specific configurations")

* [BigQuery configurations](/reference/resource-configs/bigquery-configs)
* [Redshift configurations](/reference/resource-configs/redshift-configs)
* [Snowflake configurations](/reference/resource-configs/snowflake-configs)
* [Databricks configurations](/reference/resource-configs/databricks-configs)
* [Spark configurations](/reference/resource-configs/spark-configs)

Configuring models[​](#configuring-models "Direct link to Configuring models")
------------------------------------------------------------------------------

Model configurations are applied hierarchically. You can configure models from within an installed package and also from within your dbt project in the following ways, listed in order of precedence:

1. Using a `config()` Jinja macro within a model.
2. Using a `config` [resource property](/reference/model-properties) in a `.yml` file.
3. From the `dbt_project.yml` project file, under the `models:` key. In this case, the model that's nested the deepest will have the highest priority.

The most specific configuration always takes precedence. In the project file, for example, configurations applied to a `marketing` subdirectory will take precedence over configurations applied to the entire `jaffle_shop` project. To apply a configuration to a model or directory of models, define the [resource path](/reference/resource-configs/resource-path) as nested dictionary keys.

Model configurations in your root dbt project have *higher* precedence than configurations in installed packages. This enables you to override the configurations of installed packages, providing more control over your dbt runs.

Example[​](#example "Direct link to Example")
---------------------------------------------

### Configuring directories of models in `dbt_project.yml`[​](#configuring-directories-of-models-in-dbt_projectyml "Direct link to configuring-directories-of-models-in-dbt_projectyml")

To configure models in your `dbt_project.yml` file, use the `models:` configuration option. Be sure to namespace your configurations to your project (shown below):

dbt\_project.yml

```
name: dbt_labs  
  
models:  
  # Be sure to namespace your model configs to your project name  
  dbt_labs:  
  
    # This configures models found in models/events/  
    events:  
      +enabled: true  
      +materialized: view  
  
      # This configures models found in models/events/base  
      # These models will be ephemeral, as the config above is overridden  
      base:  
        +materialized: ephemeral  
  
      ...
```

### Apply configurations to one model only[​](#apply-configurations-to-one-model-only "Direct link to Apply configurations to one model only")

Some types of configurations are specific to a particular model. In these cases, placing configurations in the `dbt_project.yml` file can be unwieldy. Instead, you can specify these configurations at the top of a model `.sql` file, or in its individual YAML properties.

models/events/base/base\_events.sql

```
{{  
  config(  
    materialized = "table",  
    tags = ["core", "events"]  
  )  
}}  
  
  
select * from {{ ref('raw_events') }}
```

models/events/base/properties.yml

```
models:  
  - name: base_events  
    description: "Standardized event data from raw sources"  
    columns:  
      - name: user_id  
        description: "Unique identifier for a user"  
        data_tests:  
          - not_null  
          - unique  
      - name: event_type  
        description: "Type of event recorded (click, purchase, etc.)"
```