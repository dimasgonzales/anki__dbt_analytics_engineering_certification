# Source: https://docs.getdbt.com/sql-reference/comments

Working with the SQL Comments

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

[![dbt Logo](/img/dbt-logo.svg?v=2)![dbt Logo](/img/dbt-logo-light.svg?v=2)](/)

* [SQL Reference](/sql-reference)

  + [Statements](/sql-reference/select)
  + [Aggregate Functions](/sql-reference/avg)
  + [Clauses](/sql-reference/where)
  + [Date Functions](/sql-reference/dateadd)
  + [String Functions](/sql-reference/upper)
  + [Window Functions](/sql-reference/rank)
  + [Operators](/sql-reference/between)
  + [Joins](/sql-reference/inner-join)
  + [Data Types](/sql-reference/data-types)
  + [Other](/sql-reference/cast)

    - [SQL CAST](/sql-reference/cast)
    - [SQL Comments](/sql-reference/comments)

* [SQL Reference](/sql-reference)
* Other
* SQL Comments

Copy page

On this page

SQL Comments
============

SQL comments…a two-folded thing: Are we talking about comments *inline* in SQL? Or comments on a table or view in the database?

Why not both!?

In this page, we’ll unpack how to create both inline and database object-level comments, general best practices around SQL comments, and how dbt can help you improve (and version-control) your comments.

How to create SQL comments[​](#how-to-create-sql-comments "Direct link to How to create SQL comments")
------------------------------------------------------------------------------------------------------

Inline SQL comments will begin with two dashes (--) in front of them in a query or dbt model; any text following these dashes is therefore what you’d call “commented out.” For longer, multi-line comments, you’ll typically see this syntax `/* your multi-line comment here */` used.

### SQL comment example[​](#sql-comment-example "Direct link to SQL comment example")

```
/* these lines form a multi-line SQL comment; if it’s uncommented,   
it will make this query error out */  
select  
	customer_id,  
	-- order_id, this row is commented out  
	order_date  
from {{ ref ('orders') }}
```

In practice, you’ll likely see SQL comments at the beginning of complex code logic, to help future developers or even advanced business users understand what specific blocks of code are accomplishing. Other times, you’ll see comments like the code above, that are commenting out lines no longer needed (or in existence) for that query or model. We’ll dive more into best practices around inline comments later on this page.

For comments *on* database objects, such as views and tables, there’s a different syntax to add these explicit comments:

```
comment on [database object type] <database object name> is 'comment text here';
```

These database object-level comments are more useful for adding additional context or metadata to these objects versus inline comments being useful for explaining code functionality. Alternatively, these table and view-level comments can be easily abstracted out and version-controlled using [model descriptions in dbt](/reference/resource-properties/description) and persisted in the objects using the [persist\_docs config](/reference/resource-configs/persist_docs) in dbt.

SQL comments in Snowflake, Databricks, BigQuery, and Redshift[​](#sql-comments-in-snowflake-databricks-bigquery-and-redshift "Direct link to SQL comments in Snowflake, Databricks, BigQuery, and Redshift")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Google BigQuery, Amazon Redshift, Snowflake, and Databricks all support the ability to add inline SQL comments. With the exception of BigQuery, these data warehouses also support native database object-level comments; BigQuery does, however, support native field-level descriptions.

SQL commenting best practices[​](#sql-commenting-best-practices "Direct link to SQL commenting best practices")
---------------------------------------------------------------------------------------------------------------

In general, inline SQL comments should be used thoughtfully; another analytics engineer should be able to pair your comments with your code to clearly understand model functionality.

We recommend leveraging inline comments in the following situations:

* Explain complex code logic that if you had to scratch your head at, someone else will have to scratch their head at
* Explain niche, unique-to-your-business logic
* Separate out field types (ex. Ids, booleans, strings, dates, numerics, and timestamps) in [staging models](/best-practices/how-we-structure/2-staging) to create more readable, organized, and formulaic models
* Clearly label tech debt (`-- [TODO]: TECH DEBT`) in queries or models

If you find your inline SQL comments are getting out of control, less scannable and readable, that’s a sign to lean more heavily on dbt Docs and markdown files in your dbt project. dbt supports [descriptions](/reference/resource-properties/description), which allow you to add robust model (or macro, source, snapshot, seed, and source) and column descriptions that will populate in hosted dbt Docs. For models or columns that need more thorough or customizable documentation, leverage [doc blocks in markdown and YAML files](/reference/resource-properties/description#use-a-docs-block-in-a-description) to create more detailed explanations and comments.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/sql-reference/other/sql-comments.md)

Last updated on **Nov 19, 2025**

[Previous

SQL CAST](/sql-reference/cast)

* [How to create SQL comments](#how-to-create-sql-comments)
  + [SQL comment example](#sql-comment-example)
* [SQL comments in Snowflake, Databricks, BigQuery, and Redshift](#sql-comments-in-snowflake-databricks-bigquery-and-redshift)
* [SQL commenting best practices](#sql-commenting-best-practices)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/sql-reference/other/sql-comments.md)

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