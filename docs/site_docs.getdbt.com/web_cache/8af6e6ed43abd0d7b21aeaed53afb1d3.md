# Source: https://docs.getdbt.com/sql-reference/inner-join

Working with inner joins in SQL

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

* [SQL Reference](/sql-reference)

  + [Statements](#)
  + [Aggregate Functions](#)
  + [Clauses](#)
  + [Date Functions](#)
  + [String Functions](#)
  + [Window Functions](#)
  + [Operators](#)
  + [Joins](#)

    - [SQL INNER JOINS](/sql-reference/inner-join)
    - [SQL OUTER JOIN](/sql-reference/outer-join)
    - [SQL SELF JOINS](/sql-reference/self-join)
    - [SQL CROSS JOIN](/sql-reference/cross-join)
    - [SQL LEFT JOIN](/sql-reference/left-join)
    - [SQL RIGHT JOIN](/sql-reference/right-join)
  + [Data Types](#)
  + [Other](#)

* [SQL Reference](/sql-reference)
* Joins
* SQL INNER JOINS

Copy page

On this page

SQL INNER JOINS
===============

The cleanest and easiest of SQL joins: the humble inner join. Just as its name suggests, an inner join between two database objects returns all rows that have matching join keys; any keys that don’t match are omitted from the query result.

How to create an inner join[​](#how-to-create-an-inner-join "Direct link to How to create an inner join")
---------------------------------------------------------------------------------------------------------

Like all joins, you need some database objects (ie tablesIn simplest terms, a table is the direct storage of data in rows and columns. Think excel sheet with raw values in each of the cells./viewsA view (as opposed to a table) is a defined passthrough SQL query that can be run against a database (or data warehouse).), keys to join on, and a [select statement](/sql-reference/select) to perform an inner join:

```
select  
    <fields>  
from <table_1> as t1  
inner join <table_2> as t2  
on t1.id = t2.id
```

In this example above, there’s only one field from each table being used to join the two together; if you’re joining between two database objects that require multiple fields, you can leverage AND/OR operators, and more preferably, surrogate keysA surrogate key is a unique identifier derived from the data itself. It often takes the form of a hashed value of multiple columns that will create a uniqueness constraint for each row.. You may additionally add [WHERE](/sql-reference/where), [GROUP BY](/sql-reference/group-by), [ORDER BY](/sql-reference/order-by), [HAVING](/sql-reference/having), and other clauses after your joins to create filtering, ordering, and performing aggregations.

As with any query, you can perform as many joins as you want in a singular query. A general word of advice: try to keep data models modularDRY is a software development principle that stands for “Don’t Repeat Yourself.” Living by this principle means that your aim is to reduce repetitive patterns and duplicate code and logic in favor of modular and referenceable code. by performing regular DAGA DAG is a Directed Acyclic Graph, a type of graph whose nodes are directionally related to each other and don’t form a directional closed loop. audits. If you join certain tables further upstream, are those individual tables needed again further downstream? If your query involves multiple joins and complex logic and is exposed to end business users, ensure that you leverage table or [incremental materializations](/docs/build/incremental-models).

### SQL inner join example[​](#sql-inner-join-example "Direct link to SQL inner join example")

Table A `car_type`

| user\_id | car\_type |
| --- | --- |
| 1 | van |
| 2 | sedan |
| 3 | truck |

Table B `car_color`

| user\_id | car\_color |
| --- | --- |
| 1 | red |
| 3 | green |
| 4 | yellow |

```
select  
   car_type.user_id as user_id,  
   car_type.car_type as type,  
   car_color.car_color as color  
from {{ ref('car_type') }} as car_type  
inner join {{ ref('car_color') }} as car_color  
on car_type.user_id = car_color.user_id
```

This simple query will return all rows that have the same `user_id` in both Table A and Table B:

| user\_id | type | color |
| --- | --- | --- |
| 1 | van | red |
| 3 | truck | green |

Because there’s no `user_id` = 4 in Table A and no `user_id` = 2 in Table B, rows with ids 2 and 4 (from either table) are omitted from the inner join query results.

SQL inner join use cases[​](#sql-inner-join-use-cases "Direct link to SQL inner join use cases")
------------------------------------------------------------------------------------------------

There are probably countless scenarios where you’d want to inner join multiple tables together—perhaps you have some really nicely structured tables with the exact same primary keysA primary key is a non-null column in a database object that uniquely identifies each row. that should really just be one larger, wider table or you’re joining two tables together don’t want any null or missing column values if you used a left or right join—it’s all pretty dependent on your source data and end use cases. Where you will not (and should not) see inner joins is in [staging models](/best-practices/how-we-structure/2-staging) that are used to clean and prep raw source data for analytics uses. Any joins in your dbt projects should happen further downstream in [intermediate](/best-practices/how-we-structure/3-intermediate) and [mart models](/best-practices/how-we-structure/4-marts) to improve modularity and DAG cleanliness.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/sql-reference/joins/sql-inner-join.md)

Last updated on **Nov 19, 2025**

[Previous

SQL ANY and ALL](/sql-reference/any-all)[Next

SQL OUTER JOIN](/sql-reference/outer-join)

* [How to create an inner join[​](#how-to-create-an-inner-join "Direct link to How to create an inner join")](#how-to-create-an-inner-join)
  + [SQL inner join example[​](#sql-inner-join-example "Direct link to SQL inner join example")](#sql-inner-join-example)
* [SQL inner join use cases[​](#sql-inner-join-use-cases "Direct link to SQL inner join use cases")](#sql-inner-join-use-cases)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/sql-reference/joins/sql-inner-join.md)

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