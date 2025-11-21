Copy page

On this page

Dimensions
==========

Dimensions represent the non-aggregatable columns in your data set, which are the attributes, features, or characteristics that describe or categorize data. In the context of the Semantic Layer, dimensions are part of a larger structure called a semantic model. They are created along with other elements like [entities](/docs/build/entities) and [measures](/docs/build/measures) and used to add more details to your data. In SQL, dimensions are typically included in the `group by` clause of your SQL query.

All dimensions require a `name`, `type`, and can optionally include an `expr` parameter. The `name` for your Dimension must be unique within the same semantic model.

| Parameter | Description | Required | Type |
| --- | --- | --- | --- |
| `name` | Refers to the name of the group that will be visible to the user in downstream tools. It can also serve as an alias if the column name or SQL query reference is different and provided in the `expr` parameter.    Dimension names should be unique within a semantic model, but they can be non-unique across different models as MetricFlow uses [joins](/docs/build/join-logic) to identify the right dimension. | Required | String |
| `type` | Specifies the type of group created in the semantic model. There are two types:  - **Categorical**: Describe attributes or features like geography or sales region.  - **Time**: Time-based dimensions like timestamps or dates. | Required | String |
| `type_params` | Specific type params such as if the time is primary or used as a partition. | Required | Dict |
| `description` | A clear description of the dimension. | Optional | String |
| `expr` | Defines the underlying column or SQL query for a dimension. If no `expr` is specified, MetricFlow will use the column with the same name as the group. You can use the column name itself to input a SQL expression. | Optional | String |
| `label` | Defines the display value in downstream tools. Accepts plain text, spaces, and quotes (such as `orders_total` or `"orders_total"`). | Optional | String |
| [`meta`](/reference/resource-configs/meta) | Set metadata for a resource and organize resources. Accepts plain text, spaces, and quotes. | Optional | Dictionary |

Refer to the following for the complete specification for dimensions:

```
dimensions:  
  - name: Name of the group that will be visible to the user in downstream tools # Required  
    type: Categorical or Time # Required  
    label: Recommended adding a string that defines the display value in downstream tools. # Optional  
    type_params: Specific type params such as if the time is primary or used as a partition # Required  
    description: Same as always # Optional  
    expr: The column name or expression. If not provided the default is the dimension name # Optional
```

Refer to the following example to see how dimensions are used in a semantic model:

```
semantic_models:  
  - name: transactions  
    description: A record for every transaction that takes place. Carts are considered multiple transactions for each SKU.   
    model: {{ ref('fact_transactions') }}  
    defaults:  
      agg_time_dimension: order_date  
# --- entities ---   
  entities:   
    - name: transaction  
      type: primary  
      ...  
# --- measures ---   
  measures:   
      ...   
# --- dimensions ---  
  dimensions:  
    - name: order_date  
      type: time  
      type_params:  
        time_granularity: day  
      label: "Date of transaction" # Recommend adding a label to provide more context to users consuming the data  
      config:   
        meta:  
          data_owner: "Finance team"  
      expr: ts  
    - name: is_bulk  
      type: categorical  
      expr: case when quantity > 10 then true else false end  
    - name: type  
      type: categorical
```

Dimensions are bound to the primary entity of the semantic model they are defined in. For example the dimension `type` is defined in a model that has `transaction` as a primary entity. `type` is scoped to the `transaction` entity, and to reference this dimension you would use the fully qualified dimension name i.e `transaction__type`.

MetricFlow requires that all semantic models have a primary entity. This is to guarantee unique dimension names. If your data source doesn't have a primary entity, you need to assign the entity a name using the `primary_entity` key. It doesn't necessarily have to map to a column in that table and assigning the name doesn't affect query generation. We recommend making these "virtual primary entities" unique across your semantic model. An example of defining a primary entity for a data source that doesn't have a primary entity column is below:

```
semantic_model:  
  name: bookings_monthly_source  
  description: bookings_monthly_source  
  defaults:  
    agg_time_dimension: ds  
  model: ref('bookings_monthly_source')  
  measures:  
    - name: bookings_monthly  
      agg: sum  
      create_metric: true  
  primary_entity: booking_id
```

Dimensions types[​](#dimensions-types "Direct link to Dimensions types")
------------------------------------------------------------------------

This section further explains the dimension definitions, along with examples. Dimensions have the following types: