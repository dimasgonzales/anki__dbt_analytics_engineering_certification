# Source: https://docs.getdbt.com/blog/configuring-grants

Updating our permissioning guidelines: grants as configs in dbt Core v1.2 | dbt Developer Blog

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

[dbt Docs](/ "dbt Docs")[Developer Blog](/blog "Blog")[Updating our permissioning guidelines: grants as configs in dbt Core v1.2](# "Updating our permissioning guidelines: grants as configs in dbt Core v1.2")

On this page

Updating our permissioning guidelines: grants as configs in dbt Core v1.2
=========================================================================

July 26, 2022 · 7 min read

[![Jeremy Cohen](/img/blog/authors/jerco.png)](/blog/authors/jeremy-cohen)

[Jeremy Cohen](/blog/authors/jeremy-cohen)

Principal Product Manager at dbt Labs

[![Doug Beatty](/img/blog/authors/dbeatty.jpeg)](/blog/authors/doug-beatty)

[Doug Beatty](/blog/authors/doug-beatty)

Senior Developer Experience Advocate at dbt Labs

If you’ve needed to grant access to a dbt model between 2019 and today, there’s a good chance you’ve come across the ["The exact grant statements we use in a dbt project"](https://discourse.getdbt.com/t/the-exact-grant-statements-we-use-in-a-dbt-project/430) post on Discourse. It explained options for covering two complementary abilities:

1. querying relations via the "select" privilege
2. using the schema those relations are within via the "usage" privilege

The solution then[​](#the-solution-then "Direct link to The solution then")
---------------------------------------------------------------------------

Prior to dbt Core v1.2, we proposed three possible approaches (each coming with [caveats and trade-offs](#caveats-and-trade-offs-of-the-original-guidance)):

1. Using `on-run-end` hooks to `grant select on all` tables/views dbt has just built
2. Using `post-hook` to grant `select` on a model as soon as it’s built
3. Using either default grants (future grants on Snowflake) or a combination of `post-hooks` and `on-run-end` hooks instead

These options were the state of the art... until today!

What’s changed?[​](#whats-changed "Direct link to What’s changed?")
-------------------------------------------------------------------

In v1.2, we [introduced](https://www.getdbt.com/blog/teaching-dbt-about-grants) a [`grants` config](https://docs.getdbt.com/reference/resource-configs/grants) that works a lot like `post-hook`, with two key differences:

* You configure `grants` as a structured dictionary rather than writing all the SQL yourself
* dbt will take *the most efficient path* to apply those grants

### Why `grants` are better than hooks[​](#why-grants-are-better-than-hooks "Direct link to why-grants-are-better-than-hooks")

First of all, [hooks are hard](#issues-related-to-hooks)! Especially that nonsense around [nested curlies](https://docs.getdbt.com/docs/building-a-dbt-project/dont-nest-your-curlies).

#### A problem then[​](#a-problem-then "Direct link to A problem then")

Let’s say you’ve been working on an incremental model. Previously, you granted access on this incremental model directly to `reporter`, so people can query it downstream:

```
-- models/my_incremental_model.sql  
  
{{ config(  
	materialized = 'incremental',  
	post_hook = ["grant select on {{ this }} to reporter"]  
) }}  
  
select ...
```

Over time, this model took on more and more responsibilities and you decided to refactor the incremental model to feed a series of dedicated views instead. Thoughtfully, you also removed the `post_hook` that granted direct access to the incremental model:

```
-- models/my_incremental_model.sql  
  
{{ config(materialized = 'incremental') }}  
  
select ...
```

**The problem?** Until you `--full-refresh` it, your incremental model is still granted to the `reporter` role!

#### The solution today[​](#the-solution-today "Direct link to The solution today")

dbt’s new `grants` implementation takes account of this. It knows whether grants are “carried over” when a model is re-run based on its materialization and your database. It makes up the difference between the existing grants and the ones you actually want.

Try it out!

```
-- models/my_incremental_model.sql  
  
{{ config(  
	materialized = 'incremental',  
	grants = {'select': ['another_user']}  
) }}  
  
select ...
```

Run that, verify that `another_user` can select from your model. Then change your model and run it again:

```
-- models/my_incremental_model.sql  
  
{{ config(  
	materialized = 'incremental',  
	grants = {'select': []}  
) }}  
  
select ...
```

If you check your database, you should see that *no one* can select from the incremental model. You could also see, in the debug-level logs, that dbt has run a `revoke` statement.

(Note that, if `grants` is missing or set to `{}`, dbt will understand that you don’t want it managing grants for this table. So it’s best to explicitly specify the privilege, and that you want *no one* to have it!)

Great! Now that you’re using the `grants` feature in dbt v1.2, you’ve just given this more thought than you should ever need to again 😎

Is there still a place for hooks?[​](#is-there-still-a-place-for-hooks "Direct link to Is there still a place for hooks?")
--------------------------------------------------------------------------------------------------------------------------

Yes, indeed! Some areas that stand out:

* [Granting permissions on other object types](#granting-permissions-on-other-object-types) like granting usage on a schema
* [Advanced permissions](#advanced-permissions-or-other-operations) like row-level access

### Granting permissions on other object types[​](#granting-permissions-on-other-object-types "Direct link to Granting permissions on other object types")

For now, it’s still necessary to grant `usage` on schemas to users that will need to select from objects in those schemas. Even though dbt creates schemas at the start of runs, there isn’t really a way to configure *schemas as their own objects* within dbt.

Here's a couple ways you could approach it:

* Option A -- simple and familiar -- hooks to the rescue
* Option B -- too clever by half -- use the dbt graph to infer which schemas need "usage"

#### Option A: simple and familiar[​](#option-a-simple-and-familiar "Direct link to Option A: simple and familiar")

```
on-run-end:  
	# better as a macro  
	- "{% for schema in schemas %}grant usage on schema {{ schema }} to reporter;{% endfor %}"
```

Upside: Short, sweet, to the point.

Downside: we need to repeat the same list of roles here that we specified in our `grants` config.

#### Option B: Too clever by half[​](#option-b-too-clever-by-half "Direct link to Option B: Too clever by half")

Now that `grants` is a real config in dbt, available via dbt metadata, you can do all sorts of fun things with it. For instance, figure out which schemas have at least one object granting `select` to a role, and then grant `usage` on that schema to that role!

```
-- macros/operations/reporting_grants.sql  
{% macro grant_usage_on_schemas_where_select() %}  
    /*  
      Note: This is pseudo code only, for demonstration purposes  
      For every role that can access at least one object in a schema,  
      grant 'usage' on that schema to the role.  
      That way, users with the role can run metadata queries showing objects  
      in that schema (a common need for BI tools)  
    */  
    {% set schema_grants = {} %}  
    {% if execute %}  
      {% for node in graph.nodes.values() %}  
        {% set grants = node.config.get('grants') %}  
        {% set select_roles = grants['select'] if grants else [] %}  
        {% if select_roles %}  
          {% set database_schema = node.database ~ "." ~ node.schema %}  
          {% if database_schema in database_schemas %}  
            {% do schema_grants[database_schema].add(select_roles) %}  
          {% else %}  
            {% do schema_grants.update({database_schema: set(select_roles)}) %}  
          {% endif %}  
        {% endif %}  
      {% endfor %}  
    {% endif %}  
    {% set grant_list %}  
      {% for schema in schema_grants %}  
        {% for role in schema_grants[schema] %}  
          grant usage on schema {{ schema }} to {{ role }};  
        {% endfor %}  
      {% endfor %}  
    {% endset %}  
    {{ return(grant_list) }}  
{% endmacro %}
```

This is certainly too clever -- but you get the idea, and an illustration of what's possible!

You can even do this at the *start* of the run, right after dbt creates its schemas, rather than waiting until the end. (Although it’s not a huge deal to wait.)

```
on-run-start:  
	- {{ grant_usage_on_schemas_where_select() }}
```

### Advanced permissions (or other operations)[​](#advanced-permissions-or-other-operations "Direct link to Advanced permissions (or other operations)")

Want to restrict access to specific rows in a table for specific users? Or dynamically mask column values depending on who’s asking?

The approach varies by database: in Snowflake, you’ll still want a `post-hook` to apply a [row access policy](https://docs.snowflake.com/en/user-guide/security-row-intro.html) or a column [masking policy](https://docs.snowflake.com/en/sql-reference/sql/create-masking-policy.html) to your table whereas in Databricks you'd use [dynamic view functions](https://docs.databricks.com/security/access-control/table-acls/object-privileges.html#dynamic-view-functions).

It’s good to have hooks and operations as a method to utilize cutting-edge database capabilities. Any cases that become a wide and clearly demonstrated need can be upgraded by being built into `dbt-core`.

Appendix[​](#appendix "Direct link to Appendix")
------------------------------------------------

### Caveats and trade-offs of the original guidance[​](#caveats-and-trade-offs-of-the-original-guidance "Direct link to Caveats and trade-offs of the original guidance")

`on-run-end` hooks:

> for the period of time between when a model runs, and the end of the run, no one will be able to query that model, instead they’ll get a “permission denied” error. This creates downtime in your BI tool.”

`manage grants` privilege:

> It is worth noting that this privilege *is* a global privilege – now anyone using the `transformer` role can change grants on any object as though they are the owner of the object. Up to you if you’re comfortable with this! If not, you may want to use a combination of `post-hooks` and `on-run-end` hooks instead 🙂”

The biggest problems:

* Even if you wrote the [DRYest](https://en.wikipedia.org/wiki/Don't_repeat_yourself) code you could, there are still *thousands* of projects who have all written the same exact [DCL](https://en.wikipedia.org/wiki/Data_control_language) statements, wrapped in the same exact macros.
* Default + future grants—our original recommendation, back in 2019— are *tricky.* They often require extra permissions (superuser status!), they take effect automatically, and they don’t fly for folks at many organizations with tighter security policies.

### Issues related to hooks[​](#issues-related-to-hooks "Direct link to Issues related to hooks")

This is just a sample of the issues we've seen:

* [Post hooks that call macros get parsed with execute = False #2370](https://github.com/dbt-labs/dbt-core/issues/2370)
* [get\_relation returns none in hook context #2938](https://github.com/dbt-labs/dbt-core/issues/2938)
* [this.is\_view and this.is\_table not working in BigQuery inside a hook #3529](https://github.com/dbt-labs/dbt-core/issues/3529)
* [custom table schema path of {{ this }} parsed in correctly in post-hook macro #3985](https://github.com/dbt-labs/dbt-core/issues/3985)
* [Post-hook doesn't resolve custom schema #4023](https://github.com/dbt-labs/dbt-core/issues/4023)
* [[CT-80] [Bug] post-hook macro generates SQL with incorrect source table #4606](https://github.com/dbt-labs/dbt-core/issues/4606)

**Tags:**

* [dbt tutorials](/blog/tags/dbt-tutorials)

#### Comments

![Loading](/img/loader-icon.svg)

[Newer post

Enforcing rules at scale with pre-commit-dbt](/blog/enforcing-rules-pre-commit-dbt)[Older post

Migrating from Stored Procedures to dbt](/blog/migrating-from-stored-procs)

* [The solution then](#the-solution-then)
* [What’s changed?](#whats-changed)
  + [Why `grants` are better than hooks](#why-grants-are-better-than-hooks)
* [Is there still a place for hooks?](#is-there-still-a-place-for-hooks)
  + [Granting permissions on other object types](#granting-permissions-on-other-object-types)
  + [Advanced permissions (or other operations)](#advanced-permissions-or-other-operations)
* [Appendix](#appendix)
  + [Caveats and trade-offs of the original guidance](#caveats-and-trade-offs-of-the-original-guidance)
  + [Issues related to hooks](#issues-related-to-hooks)

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