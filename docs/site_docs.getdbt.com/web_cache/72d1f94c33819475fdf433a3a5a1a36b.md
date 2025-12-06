# Source: https://docs.getdbt.com/blog/announcing-materialized-views

Optimizing Materialized Views with dbt | dbt Developer Blog

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

[dbt Docs](/ "dbt Docs")[Developer Blog](/blog "Blog")[Optimizing Materialized Views with dbt](# "Optimizing Materialized Views with dbt")

On this page

Optimizing Materialized Views with dbt
======================================

August 3, 2023 · 11 min read

[![Amy Chen](/img/blog/authors/achen.png)](/blog/authors/amy-chen)

[Amy Chen](/blog/authors/amy-chen)

Product Manager at dbt Labs

note

This blog post was updated on December 18, 2023 to cover the support of MVs on dbt-bigquery
and updates on how to test MVs.

Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

The year was 2020. I was a kitten-only household, and dbt Labs was still Fishtown Analytics. A enterprise customer I was working with, Jetblue, asked me for help running their dbt models every 2 minutes to meet a 5 minute SLA.

After getting over the initial terror, we talked through the use case and soon realized there was a better option. Together with my team, I created [lambda views](https://discourse.getdbt.com/t/how-to-create-near-real-time-models-with-just-dbt-sql/1457) to meet the need.

Flash forward to 2023. I’m writing this as my giant dog snores next to me (don’t worry the cats have multiplied as well). Jetblue has outgrown lambda views due to performance constraints (a view can only be so performant) and we are at another milestone in dbt’s journey to support streaming. What. a. time.

Today we are announcing that we now support Materialized Views in dbt. So, what does that mean?

Materialized views are now an out of the box materialization in your dbt project once you upgrade to the latest version of dbt v1.6 on these following adapters:

* [dbt-postgres](/reference/resource-configs/postgres-configs#materialized-views)
* [dbt-redshift](/reference/resource-configs/redshift-configs#materialized-views)
* [dbt-snowflake](/reference/resource-configs/snowflake-configs#dynamic-tables)
* [dbt-databricks](/reference/resource-configs/databricks-configs#materialized-views-and-streaming-tables)
* [dbt-materialize\*](/reference/resource-configs/materialize-configs#incremental-models-materialized-views)
* [dbt-trino\*](/reference/resource-configs/trino-configs#materialized-view)
* [dbt-bigquery (available on 1.7)](/reference/resource-configs/bigquery-configs#materialized-views)

\*These adapters have supported materialized views in their adapter prior 1.6.

Just like you would materialize your SQL model as  `table` or `view`  today, you can use `materialized_view` in your model configuration, dbt\_project.yml, and resources.yml files. At release, python models will not be supported.

For Postgres/Redshift/Databricks/Bigquery

```
{{  
config(  
    materialized = 'materialized_view',  
)  
}}
```

For Snowflake:

```
{{  
config(  
    materialized = 'dynamic_table',  
)  
}}
```

note

We are only supporting dynamic tables on Snowflake, not Snowflake’s materialized views (for a comparison between Snowflake Dynamic Tables and Materialized Views, refer [docs](https://docs.snowflake.com/en/user-guide/dynamic-tables-comparison#dynamic-tables-compared-to-materialized-views). Dynamic tables are better suited for continuous transformations due to functionality like the ability to join, union, and aggregate on base tables, views , and other dynamic tables. Due to those features, they are also more aligned with what other data platforms are calling Materialized Views. For the sake of simplicity, when I refer to materialized views in this blog, I mean dynamic tables in Snowflake.

Now that we support materialized views: how do you fit them into your dbt workflow? It’s easy to imagine a world of unregulated computation because you didn’t put in proper guardrails and now you have materialized views running rampant unbeknownst to you in your data platform.

Materialized views, just like any other materialization, fit a need and you should utilize them while taking into consideration the additional complexity they will add to your project. They are a tool in your analytics engineering toolbox, one of many.

In this blog, we will go over when to pull this tool out of your toolbox, how to wield it successfully, and how to promote materialized views with governance in mind. Now this is a new functionality and I expect this to be the first of many posts to come, defining our best practices (or even redefining them). Also I will not be discussing dbt’s interactions upstream from the data platform like how to manage your Kafka topics using dbt, but would highly recommend [this post from Charlie Summers](https://docs.getdbt.com/blog/demystifying-event-streams) if that’s something you’re interested in.

Additionally, if you want to get a more detailed understanding of your data platform’s support of materialized views, I recommend checking out dbt’s and your data platform’s documentation site. This blog post is intended to be a high level, platform agnostic overview to get you started.

What are Materialized Views?[​](#what-are-materialized-views "Direct link to What are Materialized Views?")
-----------------------------------------------------------------------------------------------------------

Starting out with, **what are materialized views (MVs)?** While specific features will vary by data platform, materialized views at their core are database objects that have stored the results of a query as a physically materialized table. What makes them distinct from a regular table is that the data in a materialized view is periodically refreshed to reflect the latest changes in the underlying table. Because they’re precomputed and the results are stored, you have faster query times when accessing them because you aren’t recomputing the data from scratch. This is great when you have low latency requirements for your data pipelines.

Now you might have noticed that MVs sound a lot like incremental models, and you are not wrong! It can be worthwhile to think of materialized views as a successor of sorts to incremental models. In fact, depending on your needs and data platform of choice, you might wish to replace all of your incremental dbt models with materialized view models. By doing this, you will no longer have to manually craft specific incremental strategies, detailing how dbt should update the underlying table. Awesome, right?

The tradeoff (outside of any data platform specific ones) is that you will have less fine-grained control over the incremental logic and orchestration. This is because you are handing defining the logic of what and how to update the existing table over to the data platform to perform for you.

Other factors to consider when deciding on when/how to use a materialized view:

* What are the costs associated with running the materialized view versus a batched incremental model? (this will vary depending on your data platform as some will require different compute nodes)
* Does your data platform support joins, aggregations, and window functions on MVs if you need them?
* What are the latency needs of your development environment? In production? (If not near real time, you can make the choice between a batch incremental model or a MV with a longer refresh schedule.)
* How often do your upstream dependencies update? If your answer is `not frequent`, you may not need a MV.
* How large is your dataset?(It might be cheaper to use MVs for extremely large datasets)
* How often do you need your query refreshed? What are your downstream dependencies and their stakeholders? (If near real time is important, MVs might be the right choice).
* Do you have real time machine learning models training or applications using your transformed dataset?

Materialized Views in the dbt Workflow[​](#materialized-views-in-the-dbt-workflow "Direct link to Materialized Views in the dbt Workflow")
------------------------------------------------------------------------------------------------------------------------------------------

### Development[​](#development "Direct link to Development")

When we talk about using materialized views in development, the question to think about is not so much “should you execute your dbt models as materialized views in your sandbox?,” but rather “should you schedule them to refresh in your sandbox?”. For development, you do need to create them and test them out in your sandbox but how do you do this in a way that doesn’t drive up your cloud bill unnecessarily? Or keeping a post-it note on your laptop as a reminder to drop all of the running materialized views in your sandbox before you sign off? Let’s talk about it!

Outside of the scheduling part, development will be pretty standard. Your pipeline is likely going to look something like this:

[![A Real Time Pipeline](/img/blog/2023-08-01-announcing-materialized-views/streaming-pipeline.png?v=2 "A Real Time Pipeline")](#)A Real Time Pipeline

This is assuming you have a near real time pipeline where you are pulling from a streaming data source like a Kafka Topic via an ingestion tool of your choice like Snowpipe for Streaming into your data platform. After your data is in the data platform, you will:

1. Create the dbt model with the SQL transformation logic that you need.
2. Look at the logic and answer these questions:
   1. Does my data platform support the functionality I need in materialized views?
   2. How often do you need the data refreshed? Do you need any flexibility in that?
   3. How am I promoting this into production? Either you will run the transformation logic in the production environment (recommended) and create a separate object or promote the object created from development.

Depending on your answer, this will decide if you want a materialized view in the first place (versus a view, table, or incremental model). If you have decided on a materialized view as meeting your needs, by default do not schedule a refresh. You can run manual refreshes as needed. Why’s that? In your development environment, you are likely validating three things: the dependencies, the SQL logic, and the transformation output. All of those can be tested by creating a materialized view without scheduling and running manually refreshes.

Your configuration during development:

For Postgres:

Every time you run a `dbt run`, that will result in a manual refresh unless you set the `on_configuration_change` to `continue` which will skip running the model.

```
{{  
config(  
    materialized = 'materialized_view',  
    on_configuration_change = 'apply',  
)  
}}
```

For Redshift:

```
{{  
config(  
    materialized = 'materialized_view',  
    on_configuration_change = 'apply',  
    auto_refresh = False  
)  
}}
```

For Bigquery

```
{{  
config(  
    materialized = 'materialized_view',  
    on_configuration_change = 'apply',  
    enable_refresh = True,  
    refresh_interval_minutes = 30  
    max_staleness = 'INTERVAL 60 MINUTE'  
)  
}}
```

For Databricks:

```
{{  
config(  
     materialized='materialized_view',  
)  
}}
```

By default, materialized views are not refreshed on a schedule on Databricks in this materialization. To set up scheduling, you can use a post-hook to alter the MV with a cron schedule that will run in Databricks Workflows. That could look like something like this

```
post_hook = 'ALTER MATERIALIZED VIEW {{this}} ADD SCHEDULE CRON "0 0 0 * * ? *" AT TIME ZONE "America/Los_Angeles";'
```

For Snowflake:

```
{{  
config(  
    materialized = 'dynamic_table',  
    snowflake_warehouse = '<warehouse>',  
    target_lag = '<desired_lag>',  
    on_configuration_change = 'apply',  
)  
}}
```

Now if you do need to more fully build out your development pipeline (making sure scheduling/syncs do happen), you can schedule but make sure to drop the materialized views when you are done with them. I encourage you to invest in an operations macro that drops all MVs in the schema that you use as your sandbox and run it as needed. You could even create a dbt Cloud job to manage that. This way, you don’t have any stray MVs running in your sandbox, consuming credits unnecessarily.

### Testing[​](#testing "Direct link to Testing")

Now let’s dive into the second question: how do you test? In development and QA, this will look the same as any tests you might have while developing your batch pipelines. You can run `dbt build` or  `dbt test` and then have the tests run after execution as validation. But in production, what changes?

I recommend that you update any tests applied to a materialized view/dynamic table with the
[store\_failures\_as](/reference/resource-configs/store_failures_as) configuration set to true and materialized as a view. This allows you to create a view that will provide all the rows that failed your test at time of query. Please note that this does not provide a historical look. You can also create alerting onto the view if it fails your expectations.

In order to promote materialized views into production, the process will look very much like it did with your incremental models. Use [CI jobs](https://docs.getdbt.com/docs/deploy/ci-jobs) with defer so you can build them into your QA environment. For existing MVs without changes, we can skip and defer to the production objects.

### Production[​](#production "Direct link to Production")

When you feel satisfied with your development and testing, for data platforms that offer scheduling via our dbt configurations, you have two options: hardcode the refresh cadence or write in conditional logic based on the environment for the refresh cadence. I recommend using the latter.

The code for having a conditional in your config block looks like this if you want to include in a macro for either the lag or other fields (snowflake\_warehouse, auto\_refresh,etc):

```
{% macro target_lag_environment() %}  
{% set lag = '1 minute' if target.name == "prod" else '35 days' %}  
{{ return(lag) }}  
{% endmacro %}
```

```
{{  
config(  
    materialized = 'dynamic_table',  
    snowflake_warehouse = 'transforming',  
    target_lag = target_lag_environment(),  
    on_configuration_change = 'apply',  
)  
}}
```

You will want a very long lag for development; I recommend the cadence you drop and refresh your development environment. Here I just chose my two favorite numbers.

For orchestration, if your materialized views aren’t able to auto refresh, you can use dbt cloud to orchestrate your refreshes. The beauty of materialized views is that dbt will be able to provide the dependency/testing/documentation but also skip or rerun the models as configured, enabling you to version control your logic. Reasonable guardrails for the modern data stack. ✨

Depending on how you orchestrate your materialized views, you can either run the testing in production as part of a scheduled job (with dbt test or dbt build).

Conclusion[​](#conclusion "Direct link to Conclusion")
------------------------------------------------------

Well, I’m excited for everyone to remove the lines in your packages.yml that installed your experimental package (at least if you’re using it for MVs) and start to get your hands dirty. We are still new in our journey and I look forward to hearing all the things you are creating and how we can better our best practices in this.

**Tags:**

* [analytics craft](/blog/tags/analytics-craft)
* [dbt product updates](/blog/tags/dbt-product-updates)
* [data ecosystem](/blog/tags/data-ecosystem)

#### Comments

* johnmichaelgenao

  Yo lo quiero jugar ![:pleading_face:](https://emoji.discourse-cdn.com/apple/pleading_face.png?v=12 ":pleading_face:")
[Continue discussion](https://discourse.getdbt.com/t/9401 "Continue discussion")

[Newer post

To defer or to clone, that is the question](/blog/to-defer-or-to-clone)[Older post

Create dbt Documentation and Tests 10x faster with ChatGPT](/blog/create-dbt-documentation-10x-faster-with-ChatGPT)

* [Introduction](#introduction)
* [What are Materialized Views?](#what-are-materialized-views)
* [Materialized Views in the dbt Workflow](#materialized-views-in-the-dbt-workflow)
  + [Development](#development)
  + [Testing](#testing)
  + [Production](#production)
* [Conclusion](#conclusion)

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