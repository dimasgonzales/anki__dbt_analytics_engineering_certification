# Source: https://docs.getdbt.com/docs/build/dimensions

Dimensions | dbt Developer Hub

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

* About
* [What is dbt?](/docs/introduction)
* [dbt Fusion engine](/docs/fusion)
* [About the dbt platform](/docs/cloud/about-cloud/dbt-cloud-features)
* [Supported data platforms](/docs/supported-data-platforms)
* Get started
* [Get started with dbt](/docs/get-started-dbt)
* [Set up dbt](/docs/about-setup)
* Build and develop
* [Develop with dbt](/docs/cloud/about-develop-dbt)
* [Build dbt projects](/docs/build/projects)

  + [About dbt projects](/docs/build/projects)
  + [dbt tips and tricks](/docs/build/dbt-tips)
  + [Build your DAG](/docs/build/models)
  + [Build your metrics](/docs/build/build-metrics-intro)

    - [Build your metrics](/docs/build/build-metrics-intro)
    - [Quickstart with the dbt Semantic Layer](/guides/sl-snowflake-qs)
    - [About MetricFlow](/docs/build/about-metricflow)
    - [Semantic models](/docs/build/semantic-models)

      * [Semantic models](/docs/build/semantic-models)
      * [Dimensions](/docs/build/dimensions)
      * [Entities](/docs/build/entities)
      * [Measures](/docs/build/measures)
    - [Metrics](/docs/build/metrics-overview)
    - [Saved queries](/docs/build/saved-queries)
    - [Advanced data modeling](/docs/build/advanced-topics)
  + [Enhance your models](/docs/build/enhance-your-models)
  + [Enhance your code](/docs/build/enhance-your-code)
  + [Organize your outputs](/docs/build/organize-your-outputs)
  + [Optimize development](/docs/build/empty-flag)
* [Build dbt Mesh](/docs/mesh/about-mesh)
* Deploy and explore
* [Deploy dbt](/docs/deploy/deployments)
* [Explore your data](/docs/explore/explore-your-data)
* [Use the dbt Semantic Layer](/docs/use-dbt-semantic-layer/dbt-sl)
* dbt AI
* [Copilot](/docs/cloud/dbt-copilot)
* [dbt MCP](/docs/dbt-ai/about-mcp)
* Additional tools
* [dbt integrations](/docs/cloud-integrations/overview)
* [Cost management](/docs/cloud/cost-management)
* Release information
* [Available dbt versions](/docs/dbt-versions/about-versions)
* [dbt release notes](/docs/dbt-versions/dbt-cloud-release-notes)

* [Build dbt projects](/docs/build/projects)
* [Build your metrics](/docs/build/build-metrics-intro)
* [Semantic models](/docs/build/semantic-models)
* Dimensions

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

* [Dimensions types](#dimensions-types)
* [Categorical](#categorical)
* [Time](#time)
  + [SCD Type II](#scd-type-ii)
    - [Basic structure](#basic-structure)
    - [Semantic model parameters and keys](#semantic-model-parameters-and-keys)
    - [Implementation](#implementation)
    - [SCD examples](#scd-examples)

Categorical[​](#categorical "Direct link to Categorical")
---------------------------------------------------------

Categorical dimensions are used to group metrics by different attributes, features, or characteristics such as product type. They can refer to existing columns in your dbt model or be calculated using a SQL expression with the `expr` parameter. An example of a categorical dimension is `is_bulk_transaction`, which is a group created by applying a case statement to the underlying column `quantity`. This allows users to group or filter the data based on bulk transactions.

```
dimensions:   
  - name: is_bulk_transaction  
    type: categorical  
    expr: case when quantity > 10 then true else false end  
    config:  
      meta:  
        usage: "Filter to identify bulk transactions, like where quantity > 10."
```

Time[​](#time "Direct link to Time")
------------------------------------

Time has additional parameters specified under the `type_params` section. When you query one or more metrics, the default time dimension for each metric is the aggregation time dimension, which you can refer to as `metric_time` or use the dimension's name.

You can use multiple time groups in separate metrics. For example, the `users_created` metric uses `created_at`, and the `users_deleted` metric uses `deleted_at`:

```
# dbt users  
dbt sl query --metrics users_created,users_deleted --group-by metric_time__year --order-by metric_time__year  
  
# dbt Core users  
mf query --metrics users_created,users_deleted --group-by metric_time__year --order-by metric_time__year
```

You can set `is_partition` for time to define specific time spans. Additionally, use the `type_params` section to set `time_granularity` to adjust aggregation details (daily, weekly, and so on).

* is\_partition
* time\_granularity

Use `is_partition: True` to show that a dimension exists over a specific time window. For example, a date-partitioned dimensional table. When you query metrics from different tables, the Semantic Layer uses this parameter to ensure that the correct dimensional values are joined to measures.

```
dimensions:   
  - name: created_at  
    type: time  
    label: "Date of creation"  
    expr: ts_created # ts_created is the underlying column name from the table   
    config:  
      meta:  
        notes: "Only valid for orders from 2022 onward"  
    is_partition: True  
    type_params:  
      time_granularity: day  
  - name: deleted_at  
    type: time  
    label: "Date of deletion"  
    expr: ts_deleted # ts_deleted is the underlying column name from the table  
    is_partition: True   
    type_params:  
      time_granularity: day  
  
measures:  
  - name: users_deleted  
    expr: 1  
    agg: sum  
    agg_time_dimension: deleted_at  
  - name: users_created  
    expr: 1  
    agg: sum
```

`time_granularity` specifies the grain of a time dimension. MetricFlow will transform the underlying column to the specified granularity. For example, if you add hourly granularity to a time dimension column, MetricFlow will run a `date_trunc` function to convert the timestamp to hourly. You can easily change the time grain at query time and aggregate it to a coarser grain, for example, from hourly to monthly. However, you can't go from a coarser grain to a finer grain (monthly to hourly).

Our supported granularities are:

* nanosecond (Snowflake only)
* microsecond
* millisecond
* second
* minute
* hour
* day
* week
* month
* quarter
* year

Aggregation between metrics with different granularities is possible, with the Semantic Layer returning results at the coarsest granularity by default. For example, when querying two metrics with daily and monthly granularity, the resulting aggregation will be at the monthly level.

```
dimensions:   
  - name: created_at  
    type: time  
    label: "Date of creation"  
    expr: ts_created # ts_created is the underlying column name from the table   
    is_partition: True   
    type_params:  
      time_granularity: hour   
  - name: deleted_at  
    type: time  
    label: "Date of deletion"  
    expr: ts_deleted # ts_deleted is the underlying column name from the table   
    is_partition: True   
    type_params:  
      time_granularity: day   
  
measures:  
  - name: users_deleted  
    expr: 1  
    agg: sum   
    agg_time_dimension: deleted_at  
  - name: users_created  
    expr: 1  
    agg: sum
```

### SCD Type II[​](#scd-type-ii "Direct link to SCD Type II")

caution

Currently, semantic models with SCD Type II dimensions cannot contain measures.

MetricFlow supports joins against dimensions values in a semantic model built on top of a slowly changing dimension (SCD) Type II table. This is useful when you need a particular metric sliced by a group that changes over time, such as the historical trends of sales by a customer's country.

#### Basic structure[​](#basic-structure "Direct link to Basic structure")

SCD Type II are groups that change values at a coarser time granularity. SCD Type II tables typically have two time columns that indicate the validity period of a dimension: `valid_from` (or `tier_start`) and `valid_to` (or `tier_end`). This creates a range of valid rows with different dimension values for a metric or measure.

MetricFlow associates the metric with the earliest available dimension value within a coarser time window, such as a month. By default, it uses the group valid at the start of this time granularity.

MetricFlow supports the following basic structure of an SCD Type II data platform table:

| entity\_key | dimensions\_1 | dimensions\_2 | ... | dimensions\_x | valid\_from | valid\_to |
| --- | --- | --- | --- | --- | --- | --- |

* `entity_key` (required): A unique identifier for each row in the table, such as a primary key or another unique identifier specific to the entity.
* `valid_from` (required): Start date timestamp for when the dimension is valid. Use `validity_params: is_start: True` in the semantic model to specify this.
* `valid_to` (required): End date timestamp for when the dimension is valid. Use `validity_params: is_end: True` in the semantic model to specify this.

#### Semantic model parameters and keys[​](#semantic-model-parameters-and-keys "Direct link to Semantic model parameters and keys")

When configuring an SCD Type II table in a semantic model, use `validity_params` to specify the start (`valid_from`) and end (`valid_to`) of the validity window for each dimension.

* `validity_params`: Parameters that define the validity window.
  + `is_start: True`: Indicates the start of the validity period. Displayed as `valid_from` in the SCD table.
  + `is_end: True`: Indicates the end of the validity period. Displayed as `valid_to` in the SCD table.

Here’s an example configuration:

```
- name: tier_start #  The name of the dimension.  
  type: time # The type of dimension (such as time)  
  label: "Start date of tier" # A readable label for the dimension  
  expr: start_date # Expression or column name the dimension represents  
  type_params: # Additional parameters for the dimension type  
    time_granularity: day # Specifies the granularity of the time dimension (such as day)  
    validity_params: # Defines the validity window  
      is_start: True # Indicates the start of the validity period.   
- name: tier_end   
  type: time  
  label: "End date of tier"  
  expr: end_date  
  type_params:  
    time_granularity: day  
    validity_params:  
      is_end: True # Indicates the end of the validity period.
```

SCD Type II tables have a specific dimension with a start and end date. To join tables:

* Set the additional [entity `type`](/docs/build/entities#entity-types) parameter to the `natural` key.
* Use a `natural` key as an [entity `type`](/docs/build/entities#entity-types), which means you don't need a `primary` key.
* In most instances, SCD tables don't have a logically usable `primary` key because `natural` keys map to multiple rows.

#### Implementation[​](#implementation "Direct link to Implementation")

Here are some guidelines to follow when implementing SCD Type II tables:

* The SCD table must have `valid_to` and `valid_from` time dimensions, which are logical constructs.
* The `valid_from` and `valid_to` properties must be specified exactly once per SCD table configuration.
* The `valid_from` and `valid_to` properties shouldn't be used or specified on the same time dimension.
* The `valid_from` and `valid_to` time dimensions must cover a non-overlapping period where one row matches each natural key value (meaning they must not overlap and should be distinct).
* We recommend defining the underlying dbt model with [dbt snapshots](/docs/build/snapshots). This supports the SCD Type II table layout and ensures that the table is updated with the latest data.

This is an example of SQL code that shows how a sample metric called `num_events` is joined with versioned dimensions data (stored in a table called `scd_dimensions`) using a primary key made up of the `entity_key` and `timestamp` columns.

```
select metric_time, dimensions_1, sum(1) as num_events  
from events a  
left outer join scd_dimensions b  
on   
  a.entity_key = b.entity_key   
  and a.metric_time >= b.valid_from   
  and (a.metric_time < b. valid_to or b.valid_to is null)  
group by 1, 2
```

#### SCD examples[​](#scd-examples "Direct link to SCD examples")

The following are examples of how to use SCD Type II tables in a semantic model:

 SCD dimensions for sales tiers and the time length of that tier.

This example shows how to create slowly changing dimensions (SCD) using a semantic model. The SCD table contains information about salespersons' tier and the time length of that tier. Suppose you have the underlying SCD table:

| sales\_person\_id | tier | start\_date | end\_date |
| --- | --- | --- | --- |
| 111 | 1 | 2019-02-03 | 2020-01-05 |
| 111 | 2 | 2020-01-05 | 2048-01-01 |
| 222 | 2 | 2020-03-05 | 2048-01-01 |
| 333 | 2 | 2020-08-19 | 2021-10-22 |
| 333 | 3 | 2021-10-22 | 2048-01-01 |

As mentioned earlier, the `validity_params` include two important arguments that specify the columns in the SCD table that mark the start and end dates (or timestamps) for each tier or dimension:

* `is_start`
* `is_end`

Additionally, the entity is tagged as `natural` to differentiate it from a `primary` entity. In a `primary` entity, each entity value has one row. In contrast, a `natural` entity has one row for each combination of entity value and its validity period.

```
semantic_models:  
  - name: sales_person_tiers  
    description: SCD Type II table of tiers for salespeople   
    model: {{ ref('sales_person_tiers') }}  
    defaults:  
      agg_time_dimension: tier_start  
  
    dimensions:  
      - name: tier_start  
        type: time  
        label: "Start date of tier"  
        expr: start_date  
        type_params:  
          time_granularity: day  
          validity_params:  
            is_start: True  
      - name: tier_end   
        type: time  
        label: "End date of tier"  
        expr: end_date  
        type_params:  
          time_granularity: day  
          validity_params:  
            is_end: True  
      - name: tier  
        type: categorical  
  
    primary_entity: sales_person  
  
    entities:  
      - name: sales_person  
        type: natural   
        expr: sales_person_id
```

The following code represents a separate semantic model that holds a fact table for `transactions`:

```
semantic_models:   
  - name: transactions   
    description: |  
      Each row represents one transaction.  
      There is a transaction, product, sales_person, and customer id for   
      every transaction. There is only one transaction id per   
      transaction. The `metric_time` or date is reflected in UTC.  
    model: {{ ref('fact_transactions') }}  
    defaults:  
      agg_time_dimension: metric_time  
  
    entities:  
      - name: transaction_id  
        type: primary  
      - name: customer  
        type: foreign  
        expr: customer_id  
      - name: product  
        type: foreign  
        expr: product_id  
      - name: sales_person  
        type: foreign  
        expr: sales_person_id  
  
    measures:  
      - name: transactions  
        expr: 1  
        agg: sum  
      - name: gross_sales  
        expr: sales_price  
        agg: sum  
      - name: sales_persons_with_a_sale  
        expr: sales_person_id  
        agg: count_distinct  
  
    dimensions:  
      - name: metric_time  
        type: time  
        label: "Date of transaction"  
        is_partition: true  
        type_params:  
          time_granularity: day  
      - name: sales_geo  
        type: categorical
```

You can now access the metrics in the `transactions` semantic model organized by the slowly changing dimension of `tier`.

In the sales tier example, For instance, if a salesperson was Tier 1 from 2022-03-01 to 2022-03-12, and gets promoted to Tier 2 from 2022-03-12 onwards, all transactions from March would be categorized under Tier 1 since the dimensions value of Tier 1 comes earlier (and is the default starting point), even though the salesperson was promoted to Tier 2 on 2022-03-12.

 SCD dimensions with sales tiers and group transactions by month when tiers are missing

This example shows how to create slowly changing dimensions (SCD) using a semantic model. The SCD table contains information about salespersons' tier and the time length of that tier. Suppose you have the underlying SCD table:

| sales\_person\_id | tier | start\_date | end\_date |
| --- | --- | --- | --- |
| 111 | 1 | 2019-02-03 | 2020-01-05 |
| 111 | 2 | 2020-01-05 | 2048-01-01 |
| 222 | 2 | 2020-03-05 | 2048-01-01 |
| 333 | 2 | 2020-08-19 | 2021-10-22 |
| 333 | 3 | 2021-10-22 | 2048-01-01 |

In the sales tier example, if sales\_person\_id 456 is Tier 2 from 2022-03-08 onwards, but there is no associated tier level dimension for this person from 2022-03-01 to 2022-03-08, then all transactions associated with sales\_person\_id 456 for the month of March will be grouped under 'NA' since no tier is present prior to Tier 2.

The following command or code represents how to return the count of transactions generated by each sales tier per month:

```
# dbt platform users  
dbt sl query --metrics transactions --group-by metric_time__month,sales_person__tier --order-by metric_time__month,sales_person__tier  
  
# dbt Core users  
mf query --metrics transactions --group-by metric_time__month,sales_person__tier --order-by metric_time__month,sales_person__tier
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [Metrics](/tags/metrics)
* [Semantic Layer](/tags/semantic-layer)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/dimensions.md)

Last updated on **Nov 19, 2025**

[Previous

Semantic models](/docs/build/semantic-models)[Next

Entities](/docs/build/entities)

* [Dimensions types[​](#dimensions-types "Direct link to Dimensions types")](#dimensions-types)
* [Categorical[​](#categorical "Direct link to Categorical")](#categorical)
* [Time[​](#time "Direct link to Time")](#time)
  + [SCD Type II[​](#scd-type-ii "Direct link to SCD Type II")](#scd-type-ii)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/dimensions.md)

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