Copy page

On this page

About source function
=====================

```
select * from {{ source("source_name", "table_name") }}
```

Definition[​](#definition "Direct link to Definition")
------------------------------------------------------

This function:

* Returns a [Relation](/reference/dbt-classes#relation) for a [source](/docs/build/sources)
* Creates dependencies between a source and the current model, which is useful for documentation and [node selection](/reference/node-selection/syntax)
* Compiles to the full object name in the database

Related guides[​](#related-guides "Direct link to Related guides")
------------------------------------------------------------------

* [Using sources](/docs/build/sources)

Arguments[​](#arguments "Direct link to Arguments")
---------------------------------------------------

* `source_name`: The `name:` defined under a `sources:` key
* `table_name`: The `name:` defined under a `tables:` key

Example[​](#example "Direct link to Example")
---------------------------------------------

Consider a source defined as follows:

models/<filename>.yml

```
sources:  
  - name: jaffle_shop # this is the source_name  
    database: raw  
  
    tables:  
      - name: customers # this is the table_name  
      - name: orders
```

Select from the source in a model:

models/orders.sql

```
select  
  ...  
  
from {{ source('jaffle_shop', 'customers') }}  
  
left join {{ source('jaffle_shop', 'orders') }} using (customer_id)
```