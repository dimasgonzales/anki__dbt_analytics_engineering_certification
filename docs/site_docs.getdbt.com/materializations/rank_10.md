# Source: https://docs.getdbt.com/best-practices/materializations/4-incremental-models

Incremental models in-depth | dbt Developer Hub

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

* [Best practices](/best-practices)

  + [How we structure our dbt projects](/best-practices/how-we-structure/1-guide-overview)
  + [How we style our dbt projects](/best-practices/how-we-style/0-how-we-style-our-dbt-projects)
  + [How we build our metrics](/best-practices/how-we-build-our-metrics/semantic-layer-1-intro)
  + [How we build our dbt Mesh projects](/best-practices/how-we-mesh/mesh-1-intro)
  + [Materialization best practices](/best-practices/materializations/1-guide-overview)

    - [Available materializations](/best-practices/materializations/2-available-materializations)
    - [Configuring materializations](/best-practices/materializations/3-configuring-materializations)
    - [Incremental models in-depth](/best-practices/materializations/4-incremental-models)
    - [Best practices for materializations](/best-practices/materializations/5-best-practices)
    - [Examining our builds](/best-practices/materializations/6-examining-builds)
    - [Conclusion](/best-practices/materializations/7-conclusion)
  + [Don't nest your curlies](/best-practices/dont-nest-your-curlies)
  + [Clone incremental models as the first step of your CI job](/best-practices/clone-incremental-models)
  + [Writing custom generic data tests](/best-practices/writing-custom-generic-tests)
  + [Best practices for workflows](/best-practices/best-practice-workflows)
  + [Best practices for dbt and Unity Catalog](/best-practices/dbt-unity-catalog-best-practices)

* [Best practices](/best-practices)
* [Materialization best practices](/best-practices/materializations/1-guide-overview)
* Incremental models in-depth

Copy page

On this page

Incremental models in-depth
===========================

So far we’ve looked at tables and views, which map to the traditional objects in the data warehouse. As mentioned earlier, incremental models are a little different. This is where we start to deviate from this pattern with more powerful and complex materializations.

* 📚 **Incremental models generate tables.** They physically persist the data itself to the warehouse, just piece by piece. What’s different is **how we build that table**.
* 💅 **Only apply our transformations to rows of data with new or updated information**, this maximizes efficiency.
  + 🌍  If we have a very large set of data or compute-intensive transformations, or both, it can be very slow and costly to process the entire corpus of source data being input into a model or chain of models. If instead we can identify *only rows that contain new information* (that is, **new or updated records**), we then can process just those rows, building our models *incrementally*.
* 3️⃣  We need **3 key things** in order to accomplish the above:
  + a **filter** to select just the new or updated records
  + a **conditional block** that wraps our filter and only applies it when we want it
  + **configuration** that tells dbt we want to build incrementally and helps apply the conditional filter when needed

Let’s dig into how exactly we can do that in dbt. Let’s say we have an `orders` table that looks like the below:

| order\_id | order\_status | customer\_id | order\_item\_id | ordered\_at | updated\_at |
| --- | --- | --- | --- | --- | --- |
| 123 | shipped | 7 | 5791 | 2022-01-30 | 2022-01-30 |
| 234 | confirmed | 15 | 1643 | 2022-01-31 | 2022-01-31 |

We did our last `dbt build` job on `2022-01-31`, so any new orders since that run won’t appear in our table. When we do our next run (for simplicity let’s say the next day, although for an orders model we’d more realistically run this hourly), we have two options:

* 🏔️ build the table from the **beginning of time again — a *table materialization***
  + Simple and solid, if we can afford to do it (in terms of time, compute, and money — which are all directly correlated in a cloud warehouse). It’s the easiest and most accurate option.
* 🤏 find a way to run **just new and updated rows since our previous run — *an* *incremental materialization***
  + If we *can’t* realistically afford to run the whole table — due to complex transformations or big source data, it takes too long — then we want to build incrementally. We want to just transform and add the row with id 567 below, *not* the previous two with ids 123 and 234 that are already in the table.

| order\_id | order\_status | customer\_id | order\_item\_id | ordered\_at | updated\_at |
| --- | --- | --- | --- | --- | --- |
| 123 | shipped | 7 | 5791 | 2022-01-30 | 2022-01-30 |
| 234 | confirmed | 15 | 1643 | 2022-01-31 | 2022-01-31 |
| 567 | shipped | 61 | 28 | 2022-02-01 | 2022-02-01 |

### Writing incremental logic[​](#writing-incremental-logic "Direct link to Writing incremental logic")

Let’s think through the information we’d need to build such a model that only processes new and updated data. We would need:

* 🕜  **a timestamp indicating when a record was last updated**, let’s call it our `updated_at` timestamp, as that’s a typical convention and what we have in our example above.
* ⌛ the **most recent timestamp from this table *in our warehouse*** *—* that is, the one created by the previous run — to act as a cutoff point. We’ll call the model we’re working in `this`, for ‘this model we’re working in’.

That would lets us construct logic like this:

```
select * from orders  
  
where  
  updated_at > (select max(updated_at) from {{ this }})
```

Let’s break down that `where` clause a bit, because this is where the action is with incremental models. Stepping through the code ***right-to-left*** we:

1. Get our **cutoff.**
   1. Select the `max(updated_at)` timestamp — the **most recent record**
   2. from `{{ this }}` — the table for this model as it exists in the warehouse, as **built in our last run**,
   3. so `max(updated_at) from {{ this }}` the ***most recent record processed in our last run,***
   4. that’s exactly what we want as a **cutoff**!
2. **Filter** the rows we’re selecting to add in this run.
   1. Use the `updated_at` timestamp from our input, the equivalent column to the one in the warehouse, but in the up-to-the-minute **source data we’re selecting from** and
   2. check if it’s **greater than our cutoff,**
   3. if so it will satisfy our where clause, so we’re **selecting all the rows more recent than our cutoff.**

This logic would let us isolate and apply our transformations to just the records that have come in since our last run, and I’ve got some great news: that magic `{{ this }}` keyword [does in fact exist in dbt](/reference/dbt-jinja-functions/this), so we can write exactly this logic in our models.

### Configuring incremental models[​](#configuring-incremental-models "Direct link to Configuring incremental models")

So we’ve found a way to isolate the new rows we need to process. How then do we handle the rest? We still need to:

* ➕  make sure dbt knows to ***add* new rows on top** of the existing table in the warehouse, **not replace** it.
* 👉  If there are **updated rows**, we need a way for dbt to know **which rows to update**.
* 🌍  Lastly, if we’re building into a new environment and there’s **no previous run to reference**, or we need to **build the model from scratch.** Put another way, we’ll want a means to skip the incremental logic and transform all of our input data like a regular table if needed.
* 😎 **Visualized below**, we’ve figured out how to get the red ‘new records’ portion selected, but we need to sort out the step to the right, where we stick those on to our model.

![Diagram visualizing how incremental models work](/assets/images/incremental-diagram-8816eec2768f76dbb493f70c7ec25d99.png)

info

😌 Incremental models can be confusing at first, **take your time reviewing** this visual and the previous steps until you have a **clear mental model.** Be patient with yourself. This materialization will become second nature soon, but it’s tough at first. If you’re feeling confused the [dbt Community is here for you on the Forum and Slack](https://www.getdbt.com/community/join-the-community).

Thankfully dbt has some additional configuration and special syntax just for incremental models.

First, let’s look at a config block for incremental materialization:

```
{{  
    config(  
        materialized='incremental',  
        unique_key='order_id'  
    )  
}}  
  
select ...
```

* 📚 The **`materialized` config** works just like tables and views, we just pass it the value `'incremental'`.
* 🔑 We’ve **added a new config option `unique_key`,** that tells dbt that if it finds a record in our previous run — the data in the warehouse already — with the same unique id (in our case `order_id` for our `orders` table) that exists in the new data we’re adding incrementally, to **update that record instead of adding it as a separate row**.
* 👯 This **hugely broadens the types of data we can build incrementally** from just immutable tables (data where rows only ever get added, never updated) to mutable records (where rows might change over time). As long as we’ve got a column that specifies when records were updated (such as `updated_at` in our example), we can handle almost anything.
* ➕ We’re now **adding records** to the table **and updating existing rows**. That’s 2 of 3 concerns.
* 🆕 We still need to **build the table from scratch** (via `dbt build` or `run` in a job) when necessary — whether because we’re in a new environment so don’t have an initial table to build on, or our model has drifted from the original over time due to data loading latency.
* 🔀 We need to wrap our incremental logic, that is our `where` clause with our `updated_at` cutoff, in a **conditional statement that will only apply it when certain conditions are met**. If you’re thinking this is **a case for a Jinja `{% if %}` statement**, you’re absolutely right!

### Incremental conditions[​](#incremental-conditions "Direct link to Incremental conditions")

So we’re going to use an **if statement** to apply our cutoff filter **only when certain conditions are met**. We want to apply our cutoff filter *if* the **following things are true**:

* ➕  we’ve set the materialization **config** to incremental,
* 🛠️  there is an **existing table** for this model in the warehouse to build on,
* 🙅‍♀️  and the `--full-refresh` **flag was *not* passed.**
  + [full refresh](/reference/resource-configs/full_refresh) is a configuration and flag that is specifically designed to let us override the incremental materialization and build a table from scratch again.

Thankfully, we don’t have to dig into the guts of dbt to sort out each of these conditions individually.

* ⚙️  dbt provides us with a **macro [`is_incremental`](/docs/build/incremental-models#understand-the-is_incremental-macro)** that checks all of these conditions for this exact use case.
* 🔀  By **wrapping our cutoff logic** in this macro, it will only get applied when the macro returns true for all of the above conditions.

Let’s take a look at all these pieces together:

```
{{  
    config(  
        materialized='incremental',  
        unique_key='order_id'  
    )  
}}  
  
select * from orders  
  
{% if is_incremental() %}  
  
where  
  updated_at > (select max(updated_at) from {{ this }})  
  
{% endif %}
```

Fantastic! We’ve got a working incremental model. On our first run, when there is no corresponding table in the warehouse, `is_incremental` will evaluate to false and we’ll capture the entire table. On subsequent runs it will evaluate to true and we’ll apply our filter logic, capturing only the newer data.

### Late arriving facts[​](#late-arriving-facts "Direct link to Late arriving facts")

Our last concern specific to incremental models is what to do when data is inevitably loaded in a less-than-perfect way. Sometimes data loaders will, for a variety of reasons, load data late. Either an entire load comes in late, or some rows come in on a load after those with which they should have. The following is best practice for every incremental model to slow down the drift this can cause.

* 🕐 For example if most of our records for `2022-01-30` come in the raw schema of our warehouse on the morning of `2022-01-31`, but a handful don’t get loaded til `2022-02-02`, how might we tackle that? There will already be `max(updated_at)` timestamps of `2022-01-31` in the warehouse, filtering out those late records. **They’ll never make it to our model.**
* 🪟 To mitigate this, we can add a **lookback window** to our **cutoff** point. By **subtracting a few days** from the `max(updated_at)`, we would capture any late data within the window of what we subtracted.
* 👯 As long as we have a **`unique_key` defined in our config**, we’ll simply update existing rows and avoid duplication. We process more data this way, but in a fixed way, and it keeps our model hewing closer to the source data.

### Long-term considerations[​](#long-term-considerations "Direct link to Long-term considerations")

Late arriving facts point to the biggest tradeoff with incremental models:

* 🪢 In addition to extra **complexity**, they also inevitably **drift from the source data over time.** Due to the imperfection of loaders and the reality of late arriving facts, we can’t help but miss some day in-between our incremental runs, and this accumulates.
* 🪟 We can slow this entropy with the lookback window described above — **the longer the window the less efficient the model, but the slower the drift.** It’s important to note it will still occur though, however slowly. If we have a lookback window of 3 days, and a record comes in 4 days late from the loader, we’re still going to miss it.
* 🌍 Thankfully, there is a way we can reset the relationship of the model to the source data. We can run the model with the **`--full-refresh` flag passed** (such as `dbt build --full-refresh -s orders`). As we saw in the `is_incremental` conditions above, that will make our logic return false, and our `where` clause filter will not be applied, running the whole table.
* 🏗️ This will let us **rebuild the entire table from scratch,** a good practice to do regularly **if the size of the data will allow**.
* 📆 A common pattern for incremental models of manageable size is to run a **full refresh on the weekend** (or any low point in activity), either **weekly or monthly**, to consistently reset the drift from late arriving facts.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/materializations/materializations-guide-4-incremental-models.md)

Last updated on **Nov 19, 2025**

[Previous

Configuring materializations](/best-practices/materializations/3-configuring-materializations)[Next

Best practices for materializations](/best-practices/materializations/5-best-practices)

* [Writing incremental logic](#writing-incremental-logic)
* [Configuring incremental models](#configuring-incremental-models)
* [Incremental conditions](#incremental-conditions)
* [Late arriving facts](#late-arriving-facts)
* [Long-term considerations](#long-term-considerations)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/materializations/materializations-guide-4-incremental-models.md)

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