# Source: https://docs.getdbt.com/blog/managing-surrogate-keys

Surrogate keys in dbt: Integers or hashes? | dbt Developer Blog

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

[dbt Docs](/ "dbt Docs")[Developer Blog](/blog "Blog")[Surrogate keys in dbt: Integers or hashes?](# "Surrogate keys in dbt: Integers or hashes?")

On this page

Surrogate keys in dbt: Integers or hashes?
==========================================

August 24, 2022 · 12 min read

[![Dave Connors](/img/blog/authors/dconnors.jpeg)](/blog/authors/dave-connors)

[Dave Connors](/blog/authors/dave-connors)

Staff Developer Experience Advocate at dbt Labs

Those who have been building data warehouses for a long time have undoubtedly encountered the challenge of building surrogate keys on their data models. Having a column that uniquely represents each entity helps ensure your data model is complete, does not contain duplicates, and able to join across different data models in your warehouse.

Sometimes, we are lucky enough to have data sources with these keys built right in — Shopify data synced via their API, for example, has easy-to-use keys on all the tables written to your warehouse. If this is not the case, or if you build a data model with a compound key (aka the data is unique across multiple dimensions), you will have to rely on some strategy for creating and maintaining these keys yourself. How can you do this with dbt? Let’s dive in.

How were surrogate keys managed in the past?[​](#how-were-surrogate-keys-managed-in-the-past "Direct link to How were surrogate keys managed in the past?")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Before the advent of the analytical warehouse tools we use today, the data warehouse architecture had a few key constraints that led to the rise of the Kimball-style warehouse with a snowflake schema. This was because storage was expensive — it was more efficient to store data as few times as possible, and rely on joins to connect data tog ether when a report required it. And to make those joins efficient, it became standard practice to use **monotonically increasing integer surrogate keys (MIISKs)**, a fancy way to say “count each record starting at one” so that your data model would look something like this (you are a cheesemonger):

| product\_id | product\_name | created\_by | created\_at |
| --- | --- | --- | --- |
| 1 | mozzarella | 23 | 0001-05-05 |
| 2 | cheddar | 24 | 1150-02-03 |
| 3 | gruyere | 25 | 1655-04-03 |

| order\_line\_id | order\_id | product\_id | amount | created\_at |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | 40 | 2022-07-01 |
| 2 | 2 | 1 | 50 | 2022-07-05 |
| 3 | 3 | 1 | 10 | 2022-07-07 |
| 4 | 3 | 2 | 30 | 2022-07-07 |

| order\_id | customer\_id | created\_at |
| --- | --- | --- |
| 1 | 5 | 2022-07-01 |
| 2 | 8 | 2022-07-05 |
| 3 | 10 | 2022-07-07 |

There are some clear benefits here!

* There are clear, intuitive relationships between these entities!
* The fact that the keys here are small integers, the database can a) not worry about storage costs for this data b) index this field easily, making joins quick and efficient.

However, there are also some clear maintenance issues here. Making updates to, say, your products table will require some careful surgical work to ensure the association of cheddar to id 2 is never accidentally changed. You may have heard of the phrase “load your dims before your facts” — this refers to the careful work required to maintain this referential integrity. Additionally, you need to know about the *exact state of the data* before making any updates. This data is **stateful**, making it rigid and more difficult to work with should there be any losses to this data. Imagine trying to rebuild these relationships from scratch!

MIISKs in dbt[​](#miisks-in-dbt "Direct link to MIISKs in dbt")
---------------------------------------------------------------

If this is your preferred modeling approach, dbt can absolutely support this workflow! This will likely require you to take advantage of built-in warehouse functionality to generate these MIISKs — in Snowflake, we can use [sequences](https://docs.snowflake.com/en/user-guide/querying-sequences.html), which are objects built exactly for this purpose. We’ll use Snowflake as the example here, but this approach can likely be adapted for other warehouses as well.

### Creating and maintaining sequences[​](#creating-and-maintaining-sequences "Direct link to Creating and maintaining sequences")

In order to properly maintain the sequence of the surrogate keys in your data models, we’ll need to build and maintain a sequence for each table that needs one. In order to do this at scale, we’ll make use of the [meta](https://docs.getdbt.com/reference/resource-configs/meta) config of dbt model. This configuration allows you to define any metadata dictionary that you want. Using this, we can programmatically apply a surrogate key configuration for each model that needs one, and reference that configuration in a macro to properly create and update surrogate keys when necessary.

Here’s an example configuration:

```
# assign the surrogate key config to your model  
  
version: 2  
  
models:  
  - name: dim_customers  
	description: all customers  
    config:  
      meta:  
        surrogate_key: true
```

This metadata can then be leveraged in a macro in an `on-run-start` operation to ensure all sequences exist for all models that need one before the models execute.

```
# in macros/generate_sequences.sql  
  
{% macro generate_sequences() %}  
  
    {% if execute %}  
        
    {% set models = graph.nodes.values() | selectattr('resource_type', 'eq', 'model') %}  
    {# parse through the graph object, find all models with the meta surrogate key config #}  
    {% set sk_models = [] %}  
    {% for model in models %}  
        {% if model.config.meta.surrogate_key %}  
          {% do sk_models.append(model) %}  
        {% endif %}  
    {% endfor %}  
  
    {% endif %}  
  
    {% for model in sk_models %}  
  
        {% if flags.FULL_REFRESH or model.config.materialized == 'table' %}  
        {# regenerate sequences if necessary #}  
  
        create or replace sequence {{ model.database }}.{{ model.schema }}.{{ model.name }}_seq;  
  
        {% else %}  
        {# create only if not exists for incremental models #}  
      
        create sequence if not exists {{ model.database }}.{{ model.schema }}.{{ model.name }}_seq;  
          
        {% endif %}  
      
    {% endfor %}  
    
{% endmacro %}
```

You can see in the above macro that we’re baking a naming convention here — for any model, the name of the sequence will exist in the same database and schema and follow the naming convention `<model_name>_seq`. Adhering to this pattern allows us to also create an easy macro to increment the sequences in our model definitions without having to hard code the sequence name in every model that needs a surrogate key.

```
# in macros/increment_sequence.sql  
  
{%- macro increment_sequence() -%}  
    
  {{ this.name }}_seq.nextval  
  
{%- endmacro -%}
```

So your model code looks like:

```
# in dim_customers  
...  
  
with cte_name as (  
		...  
)  
...  
  
select  
  
	{{ increment_sequence() }} as customer_id,   
	first_name,   
	last_name  
  
from cte_name  
  
...
```

### Caveats[​](#caveats "Direct link to Caveats")

Despite the relative simplicity of this strategy, there are a handful of drawbacks with regard to making sure these sequences work the way we want them to.

* **dbt Run errors -** If an incremental model that has surrogate keys maintained in this way *fails* due to some SQL error, we may end up with gaps in our surrogate key. When dbt goes to execute the model, the sequence is queried, and therefore incremented, but the model failure prevents changes to the target table model. That means the next time we run the model, the incremental model will start on the wrong value, and we may end up with a column that looks like this:

  | surrogate\_key\_id |
  | --- |
  | 1 |
  | 2 |
  | 3 |
  | 4 |
  | 5 |
  | 8 |

  In fact, most cloud platforms [can’t guarantee](https://docs.snowflake.com/en/user-guide/querying-sequences.html#:~:text=Snowflake%20does%20not%20guarantee%20generating%20sequence%20numbers%20without%20gaps.%20The%20generated%20numbers%20consistently%20increase%20in%20value%20(or%20decrease%20in%20value%20if%20the%20step%20size%20is%20negative)%20but%20are%20not%20necessarily%20contiguous) that sequences will be generated without gaps because of their use of parallel processing, even if we *don’t* have a dbt run error — because queries will be spread across multiple compute clusters, each step might query the sequence at different times, which makes it possible to have an out of order sequence result. This is a major consideration in using sequences — if that’s a deal breaker, you may need additional SQL logic in our models (like a `row_number()` function) to guarantee your keys are monotonically increasing.
* **Views -** Because sequences in Snowflake increment on every query, using them as the surrogate keys for views would mean every time the view is queried, the sequence would increment and therefore change. This strategy would only work for table or incremental models.
* **Ordering -** Since sequences will be regenerated on every run for tables, and every time an incremental model is regenerated, the order of the resulting query determines which records get assigned to each key. In order to maintain referential integrity (i.e. product\_id 1 always means mozzarella), you need to build in `ORDER BY` statements to your models. This can cause adverse performance during table builds.
* **“Load your dims before your facts” -** This strategy can also lead to some very messy DAGs in order to keep relationships intact in your project. As mentioned above, it’s imperative that each product record results in the same surrogate key value every time dbt is run. Additionally, this means that any table that needs to read from this table needs to run downstream of that initial process. This can lead to bottlenecks at runtime.

Even though configuring MIISKs with sequences can be pretty well automated, it’s a bit of a brittle process that relies on a lot of assumptions and requires a whole lot of bandwidth from the data team to recreate the warehouse should anything go haywire.

Hashed surrogate keys[​](#hashed-surrogate-keys "Direct link to Hashed surrogate keys")
---------------------------------------------------------------------------------------

An alternative to using the traditional MIISK strategy is to use cryptographic hashing functions to *derive the surrogate key values from the data itself,* a fancy way of saying “create a random string for every unique combination of values you find in my table”. These hashing functions are **deterministic**, meaning the same set of inputs will always produce the same output. In our SQL models, we can pass the column or columns that represent to the grain to this hashing function and voilà, a consistent, unique identifier is generated automatically! This has been packaged up in the `surrogate_key()` macro in the `dbt_utils` package ([source](https://github.com/dbt-labs/dbt-utils#surrogate_key-source)), and works across warehouse providers! Check out our SQL Magic post that dives deeper into this function [here](https://docs.getdbt.com/blog/sql-surrogate-keys).

```
# in models/reports/daily_user_orders.sql  
with   
  
orders as (  
	select * from {{ ref('fct_orders') }}   
),  
  
agg as (  
  
	select   
		date_trunc(day, order_date) as report_date 	  
		user_id,   
		count(*) as total_orders  
  from orders  
  group by 1,2  
  
),  
  
final as (  
	  
	select  
		{{ dbt_utils.generate_surrogate_key([  
				'report_date',   
				'user_id'  
			])  
		}} as unique_key,   
		*  
	from agg  
  
)  
  
select * from final
```

Using hashed keys makes our transformations idempotent — every dbt run results in the same exact outputs every time. I can safely delete all my non-source objects in my warehouse, execute a dbt run and be right back where I started (though I wouldn’t necessarily recommend this 😅).

The analytical warehouses we use now no longer have the same constraints that traditional warehouses had — joins on strings aren’t notably less performant than those on integers, and storing slightly larger values in the surrogate key column is peanuts given the relative cost of storage on these platforms. This strategy also removes the need for tight coupling of transformations to propagate the surrogate key values across our project — anywhere the inputs for the surrogate keys are present, the hashing function produces the same keys, so we can take advantage of parallel processing in our warehouse and avoid the bottlenecks we had before.

### Caveats[​](#caveats-1 "Direct link to Caveats")

This strategy is not without its caveats either!

* **Collisions -** Although it's *exceedingly* rare, depending on the hashing algorithm you use, it's possible for two different sets of inputs to produce the same outputs, causing erroneous duplicate records in your dataset. Using an MD5 hash (the default for the `dbt_utils.generate_surrogate_key` macro), you have a 50% of a collision when you get up to 2^64 records (1.84 x 10E19 aka a whole lot of data). While [very very very unlikely](https://docs.getdbt.com/terms/surrogate-key#a-note-on-hashing-algorithms), it’s certainly something to consider for truly massive datasets.
* **Datatypes -** If you’re in the process of migrating legacy code to a new warehouse provider, you likely have some constraints on the datatype of your keys from the consumers of your datasets, and may have some issues converting to a string-based key. Luckily, some warehouse providers have hash functions that output integer values (like Snowflake’s `MD5_UPPER/LOWER_64` functions). However, these have fewer bits in the hashing function, so may lead to collision issues on big data sets.
* **Performance -** Hashed keys generally result in long string-type values. On massive datasets on some warehouses, this could cause some performance issues. Unlike MIISKs, string values can’t be easily partitioned to improve query performance. Luckily, as described in the above bullet point, you can choose to utilize hashing functions that output other, more performant datatypes!
* **Storage -** As mentioned above, hash keys will end up with higher storage costs than their MIISK counterparts. Given that the cost of storage in cloud warehouses is extremely cheap, it’s unlikely to be worth the effort to optimize for storage costs.

OK, so which one?[​](#ok-so-which-one "Direct link to OK, so which one?")
-------------------------------------------------------------------------

Surrogate keys are a critical component of a logical data model, and as with most anything, you’ve got options when it comes to generating and maintaining them with dbt. Your business’s unique constraints with respect to maintenance overhead, performance, and data size will likely be the primary drivers for your decision. It will also be important to consider your stakeholders’ needs — are they used to seeing data in a particular format? are there one hundred dashboards that will explode if you change some keys from an integer to a string? For many orgs, this is a non-trivial decision!

For my money, the simplicity of using hashed keys far outweighs the potential benefits of having MIISKs in your data model. Building with dbt works best when all parts of your project are idempotent, and hashed keys require close to zero maintenance. The cost of time spent rebuilding your surrogate keys in your data models if you can’t recreate them with a simple `dbt run` usually offsets any modest performance and storage gains you might be able to achieve with MIISKs.

Big thanks to [Mike Fuller](https://github.com/mikegfuller) and [Bennie Regenold](https://github.com/bennieregenold7) for help ideating on this blog!

**Tags:**

* [analytics craft](/blog/tags/analytics-craft)

#### Comments

![Loading](/img/loader-icon.svg)

[Newer post

An introduction to unit testing your dbt Packages](/blog/unit-testing-dbt-packages)[Older post

Narrative modeling: How structure can tell a story](/blog/narrative-modeling)

* [How were surrogate keys managed in the past?](#how-were-surrogate-keys-managed-in-the-past)
* [MIISKs in dbt](#miisks-in-dbt)
  + [Creating and maintaining sequences](#creating-and-maintaining-sequences)
  + [Caveats](#caveats)
* [Hashed surrogate keys](#hashed-surrogate-keys)
  + [Caveats](#caveats-1)
* [OK, so which one?](#ok-so-which-one)

#### Live virtual event

Experience the dbt Fusion engine with Tristan Handy and Elias DeFaria on October 28th

[Save your seat](https://www.getdbt.com/resources/webinars/speed-simplicity-cost-savings-experience-the-dbt-fusion-engine "Save your seat")

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