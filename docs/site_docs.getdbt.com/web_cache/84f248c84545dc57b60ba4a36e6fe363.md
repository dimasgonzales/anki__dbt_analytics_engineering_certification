# Source: https://docs.getdbt.com/guides/using-jinja

Use Jinja to improve your SQL code | dbt Developer Hub

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

Copy page

Use Jinja to improve your SQL code
==================================

[Back to guides](/guides)

Jinja

dbt Core

Advanced

Menu




Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

In this guide, we're going to take a common pattern used in SQL, and then use Jinja to improve our code.

If you'd like to work through this query, add [this CSV](https://github.com/dbt-labs/jaffle_shop/blob/core-v1.0.0/seeds/raw_payments.csv) to the `seeds/` folder of your dbt project, and then execute `dbt seed`.

While working through the steps of this model, we recommend that you have your compiled SQL open as well, to check what your Jinja compiles to. To do this:

* **Using dbt:** Click the compile button to see the compiled SQL in the right hand pane
* **Using dbt Core:** Run `dbt compile` from the command line. Then open the compiled SQL file in the `target/compiled/{project name}/` directory. Use a split screen in your code editor to keep both files open at once.

Write the SQL without Jinja[​](#write-the-sql-without-jinja "Direct link to Write the SQL without Jinja")
---------------------------------------------------------------------------------------------------------

Consider a data model in which an `order` can have many `payments`. Each `payment` may have a `payment_method` of `bank_transfer`, `credit_card` or `gift_card`, and therefore each `order` can have multiple `payment_methods`

From an analytics perspective, it's important to know how much of each `order` was paid for with each `payment_method`. In your dbt project, you can create a model, named `order_payment_method_amounts`, with the following SQL:

models/order\_payment\_method\_amounts.sql

```
select  
order_id,  
sum(case when payment_method = 'bank_transfer' then amount end) as bank_transfer_amount,  
sum(case when payment_method = 'credit_card' then amount end) as credit_card_amount,  
sum(case when payment_method = 'gift_card' then amount end) as gift_card_amount,  
sum(amount) as total_amount  
from {{ ref('raw_payments') }}  
group by 1
```

The SQL for each payment method amount is repetitive, which can be difficult to maintain for a number of reasons:

* If the logic or field name were to change, the code would need to be updated in three places.
* Often this code is created by copying and pasting, which may lead to mistakes.
* Other analysts that review the code are less likely to notice errors as it's common to only scan through repeated code.

So we're going to use Jinja to help us clean it up, or to make our code more "DRY" ("Don't Repeat Yourself").

Use a for loop in models for repeated SQL[​](#use-a-for-loop-in-models-for-repeated-sql "Direct link to Use a for loop in models for repeated SQL")
---------------------------------------------------------------------------------------------------------------------------------------------------

Here, the repeated code can be replaced with a `for` loop. The following will be compiled to the same query, but is significantly easier to maintain.

/models/order\_payment\_method\_amounts.sql

```
select  
order_id,  
{% for payment_method in ["bank_transfer", "credit_card", "gift_card"] %}  
sum(case when payment_method = '{{payment_method}}' then amount end) as {{payment_method}}_amount,  
{% endfor %}  
sum(amount) as total_amount  
from {{ ref('raw_payments') }}  
group by 1
```

Set variables at the top of a model[​](#set-variables-at-the-top-of-a-model "Direct link to Set variables at the top of a model")
---------------------------------------------------------------------------------------------------------------------------------

We recommend setting variables at the top of a model, as it helps with readability, and enables you to reference the list in multiple places if required. This is a practice we've borrowed from many other programming languages.

/models/order\_payment\_method\_amounts.sql

```
{% set payment_methods = ["bank_transfer", "credit_card", "gift_card"] %}  
  
select  
order_id,  
{% for payment_method in payment_methods %}  
sum(case when payment_method = '{{payment_method}}' then amount end) as {{payment_method}}_amount,  
{% endfor %}  
sum(amount) as total_amount  
from {{ ref('raw_payments') }}  
group by 1
```

Use loop.last to avoid trailing commas[​](#use-looplast-to-avoid-trailing-commas "Direct link to Use loop.last to avoid trailing commas")
-----------------------------------------------------------------------------------------------------------------------------------------

In the above query, our last column is outside of the `for` loop. However, this may not always be the case. If the last iteration of a loop is our final column, we need to ensure there isn't a trailing comma at the end.

We often use an `if` statement, along with the Jinja variable `loop.last`, to ensure we don't add an extraneous comma:

/models/order\_payment\_method\_amounts.sql

```
{% set payment_methods = ["bank_transfer", "credit_card", "gift_card"] %}  
  
select  
order_id,  
{% for payment_method in payment_methods %}  
sum(case when payment_method = '{{payment_method}}' then amount end) as {{payment_method}}_amount  
{% if not loop.last %},{% endif %}  
{% endfor %}  
from {{ ref('raw_payments') }}  
group by 1
```

An alternative way to write this is `{{ "," if not loop.last }}`.

Use whitespace control to tidy up compiled code[​](#use-whitespace-control-to-tidy-up-compiled-code "Direct link to Use whitespace control to tidy up compiled code")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you've been checking your code in the `target/compiled` folder, you might have noticed that this code results in a lot of white space:

target/compiled/jaffle\_shop/order\_payment\_method\_amounts.sql

```
select  
order_id,  
  
sum(case when payment_method = 'bank_transfer' then amount end) as bank_transfer_amount  
,  
  
sum(case when payment_method = 'credit_card' then amount end) as credit_card_amount  
,  
  
sum(case when payment_method = 'gift_card' then amount end) as gift_card_amount  
  
  
from raw_jaffle_shop.payments  
group by 1
```

We can use [whitespace control](https://jinja.palletsprojects.com/page/templates/#whitespace-control) to tidy up our code:

models/order\_payment\_method\_amounts.sql

```
{%- set payment_methods = ["bank_transfer", "credit_card", "gift_card"] -%}  
  
select  
order_id,  
{%- for payment_method in payment_methods %}  
sum(case when payment_method = '{{payment_method}}' then amount end) as {{payment_method}}_amount  
{%- if not loop.last %},{% endif -%}  
{% endfor %}  
from {{ ref('raw_payments') }}  
group by 1
```

Getting whitespace control right is often a lot of trial and error! We recommend that you prioritize the readability of your model code over the readability of the compiled code, and only do this as an extra polish.

Use a macro to return payment methods[​](#use-a-macro-to-return-payment-methods "Direct link to Use a macro to return payment methods")
---------------------------------------------------------------------------------------------------------------------------------------

Here, we've hardcoded the list of payment methods in our model. We may need to access this list from another model. A good solution here is to use a [variable](/docs/build/project-variables), but for the purpose of this tutorial, we're going to instead use a macro!

[Macros](/docs/build/jinja-macros#macros) in Jinja are pieces of code that can be called multiple times – they are analogous to a function in Python, and are extremely useful if you find yourself repeating code across multiple models.

Our macro is simply going to return the list of payment methods:

/macros/get\_payment\_methods.sql

```
{% macro get_payment_methods() %}  
{{ return(["bank_transfer", "credit_card", "gift_card"]) }}  
{% endmacro %}
```

There's a few things worth noting here:

* Normally, macros take arguments -- we'll see this later on, but for now, we still need to setup our macro with empty parentheses where the arguments would normally go (i.e. `get_payment_methods()`)
* We've used the [return](/reference/dbt-jinja-functions/return) function to return a list – without this function, the macro would return a string.

Now that we have a macro for our payment methods, we can update our model as follows:

models/order\_payment\_method\_amounts.sql

```
{%- set payment_methods = get_payment_methods() -%}  
  
select  
order_id,  
{%- for payment_method in payment_methods %}  
sum(case when payment_method = '{{payment_method}}' then amount end) as {{payment_method}}_amount  
{%- if not loop.last %},{% endif -%}  
{% endfor %}  
from {{ ref('raw_payments') }}  
group by 1
```

Note that we didn't use curly braces when calling the macro – we're already within a Jinja statement, so there's no need to use the brackets again.

Dynamically retrieve the list of payment methods[​](#dynamically-retrieve-the-list-of-payment-methods "Direct link to Dynamically retrieve the list of payment methods")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

So far, we've been hardcoding the list of possible payment methods. If a new `payment_method` was introduced, or one of the existing methods was renamed, the list would need to be updated.

However, at any given time you could know what `payment_methods` are used to make a payment by running the following query:

```
select distinct  
payment_method  
from {{ ref('raw_payments') }}  
order by 1
```

[Statements](/reference/dbt-jinja-functions/statement-blocks) provide a way to run this query and return the results to your Jinja context. This means that the list of `payment_methods` can be set based on the data in your database rather than a hardcoded value.

The easiest way to use a statement is through the [run\_query](/reference/dbt-jinja-functions/run_query) macro. For the first version, let's check what we get back from the database, by logging the results to the command line using the [log](/reference/dbt-jinja-functions/log) function.

macros/get\_payment\_methods.sql

```
{% macro get_payment_methods() %}  
  
{% set payment_methods_query %}  
select distinct  
payment_method  
from {{ ref('raw_payments') }}  
order by 1  
{% endset %}  
  
{% set results = run_query(payment_methods_query) %}  
  
{{ log(results, info=True) }}  
  
{{ return([]) }}  
  
{% endmacro %}
```

The command line gives us back the following:

```
| column         | data_type |  
| -------------- | --------- |  
| payment_method | Text      |
```

This is actually an [Agate table](https://agate.readthedocs.io/page/api/table.html). To get the payment methods back as a list, we need to do some further transformation.

```
{% macro get_payment_methods() %}  
  
{% set payment_methods_query %}  
select distinct  
payment_method  
from {{ ref('raw_payments') }}  
order by 1  
{% endset %}  
  
{% set results = run_query(payment_methods_query) %}  
  
{% if execute %}  
{# Return the first column #}  
{% set results_list = results.columns[0].values() %}  
{% else %}  
{% set results_list = [] %}  
{% endif %}  
  
{{ return(results_list) }}  
  
{% endmacro %}
```

There's a few tricky pieces in here:

* We used the [execute](/reference/dbt-jinja-functions/execute) variable to ensure that the code runs during the `parse` stage of dbt (otherwise an error would be thrown).
* We used Agate methods to get the column back as a list

Fortunately, our model code doesn't need to be updated, since we're already calling the macro to get the list of payment methods. And now, any new `payment_methods` added to the underlying data model will automatically be handled by the dbt model.

Write modular macros[​](#write-modular-macros "Direct link to Write modular macros")
------------------------------------------------------------------------------------

You may wish to use a similar pattern elsewhere in your dbt project. As a result, you decide to break up your logic into two separate macros -- one to generically return a column from a relation, and the other that calls this macro with the correct arguments to get back the list of payment methods.

macros/get\_payment\_methods.sql

```
{% macro get_column_values(column_name, relation) %}  
  
{% set relation_query %}  
select distinct  
{{ column_name }}  
from {{ relation }}  
order by 1  
{% endset %}  
  
{% set results = run_query(relation_query) %}  
  
{% if execute %}  
{# Return the first column #}  
{% set results_list = results.columns[0].values() %}  
{% else %}  
{% set results_list = [] %}  
{% endif %}  
  
{{ return(results_list) }}  
  
{% endmacro %}  
  
  
{% macro get_payment_methods() %}  
  
{{ return(get_column_values('payment_method', ref('raw_payments'))) }}  
  
{% endmacro %}
```

Use a macro from a package[​](#use-a-macro-from-a-package "Direct link to Use a macro from a package")
------------------------------------------------------------------------------------------------------

Macros let analysts bring software engineering principles to the SQL they write. One of the features of macros that makes them even more powerful is their ability to be shared across projects.

A number of useful dbt macros have already been written in the [dbt-utils package](https://github.com/dbt-labs/dbt-utils). For example, the [get\_column\_values](https://github.com/dbt-labs/dbt-utils#get_column_values-source) macro from dbt-utils could be used instead of the `get_column_values` macro we wrote ourselves (saving us a lot of time, but at least we learnt something along the way!).

Install the [dbt-utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) package in your project (docs [here](/docs/build/packages)), and then update your model to use the macro from the package instead:

models/order\_payment\_method\_amounts.sql

```
{%- set payment_methods = dbt_utils.get_column_values(  
    table=ref('raw_payments'),  
    column='payment_method'  
) -%}  
  
select  
order_id,  
{%- for payment_method in payment_methods %}  
sum(case when payment_method = '{{payment_method}}' then amount end) as {{payment_method}}_amount  
{%- if not loop.last %},{% endif -%}  
{% endfor %}  
from {{ ref('raw_payments') }}  
group by 1
```

You can then remove the macros that we built in previous steps. Whenever you're trying to solve a problem that you think others may have solved previously, it's worth checking the [dbt-utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) package to see if someone has shared their code!

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [Jinja](/tags/jinja)
* [dbt Core](/tags/dbt-core)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/guides/using-jinja.md)

Last updated on **Nov 19, 2025**

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