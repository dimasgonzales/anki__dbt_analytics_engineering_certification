# Source: https://docs.getdbt.com/docs/mesh/govern/model-access

Model access | dbt Developer Hub

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
* [Build dbt Mesh](/docs/mesh/about-mesh)

  + [About dbt Mesh](/docs/mesh/about-mesh)
  + [Model governance](/docs/mesh/govern/about-model-governance)

    - [About model governance](/docs/mesh/govern/about-model-governance)
    - [Model access](/docs/mesh/govern/model-access)
    - [Model contracts](/docs/mesh/govern/model-contracts)
    - [Model versions](/docs/mesh/govern/model-versions)
    - [Project dependencies](/docs/mesh/govern/project-dependencies)
  + [Apache Iceberg](/docs/mesh/iceberg/apache-iceberg-support)
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

* [Build dbt Mesh](/docs/mesh/about-mesh)
* [Model governance](/docs/mesh/govern/about-model-governance)
* Model access

Copy page

On this page

Model access
============

"Model access" is not "User access"

**Model groups and access** and **user groups and access** mean two different things. "User groups and access" is a specific term used in dbt to manage permissions. Refer to [User access](/docs/cloud/manage-access/about-user-access) for more info.

The two concepts will be closely related, as we develop multi-project collaboration workflows this year:

* Users with access to develop in a dbt project can view and modify **all** models in that project, including private models.
* Users in the same dbt account *without* access to develop in a project cannot view that project's private models, and they can take a dependency on its public models only.

Related documentation[​](#related-documentation "Direct link to Related documentation")
---------------------------------------------------------------------------------------

* [`groups`](/docs/build/groups)
* [`access`](/reference/resource-configs/access)

Groups[​](#groups "Direct link to Groups")
------------------------------------------

Models can be grouped under a common designation with a shared owner. For example, you could group together all models owned by a particular team, or related to modeling a specific data source (`github`).

Why define model `groups`? There are two reasons:

* It turns implicit relationships into an explicit grouping, with a defined owner. By thinking about the interface boundaries *between* groups, you can have a cleaner (less entangled) DAG. In the future, those interface boundaries could be appropriate as the interfaces between separate projects.
* It enables you to designate certain models as having "private" access—for use exclusively within that group. Other models will be restricted from referencing (taking a dependency on) those models. In the future, they won't be visible to other teams taking a dependency on your project—only "public" models will be.

If you follow our [best practices for structuring a dbt project](/best-practices/how-we-structure/1-guide-overview), you're probably already using subdirectories to organize your dbt project. It's easy to apply a `group` label to an entire subdirectory at once:

dbt\_project.yml

```
models:  
  my_project_name:  
    marts:  
      customers:  
        +group: customer_success  
      finance:  
        +group: finance
```

Each model can only belong to one `group`, and groups cannot be nested. If you set a different `group` in that model's YAML or in-file config, it will override the `group` applied at the project level.

#### Considerations[​](#considerations "Direct link to Considerations")

There are some considerations to keep in mind when using model governance features:

* Model governance features like model access, contracts, and versions strengthen trust and stability in your dbt project. Because they add structure, they can make rollbacks harder (for example, removing model access) and increase maintenance if adopted too early.
  Before adding governance features, consider whether your dbt project is ready to benefit from them. Introducing governance while models are still changing can complicate future changes.
* Governance features are model-specific. They don't apply to other resource types, including snapshots, seeds, or sources. This is because these objects can change structure over time (for example, snapshots capture evolving historical data) and aren't suited to guarantees like contracts, access, or versioning.

Access modifiers[​](#access-modifiers "Direct link to Access modifiers")
------------------------------------------------------------------------

Some models are implementation details, meant for reference only within their group of related models. Other models should be accessible through the [ref](/reference/dbt-jinja-functions/ref) function across groups and projects. Models can set an [access modifier](https://en.wikipedia.org/wiki/Access_modifiers) to indicate their intended level of accessibility.

| Access | Referenceable by |
| --- | --- |
| private | Same group |
| protected | Same project (or installed as a package) |
| public | Any group, package, or project. When defined, rerun a production job to apply the change |

If you try to reference a model outside of its supported access, you will see an error:

```
dbt run -s marketing_model  
...  
dbt.exceptions.DbtReferenceError: Parsing Error  
  Node model.jaffle_shop.marketing_model attempted to reference node model.jaffle_shop.finance_model,   
  which is not allowed because the referenced node is private to the finance group.
```

By default, all models are `protected`. This means that other models in the same project can reference them, regardless of their group. This is largely for backward compatibility when assigning groups to an existing set of models, as there may already be existing references across group assignments.

However, it is recommended to set the access modifier of a new model to `private` to prevent other project resources from taking dependencies on models not intentionally designed for sharing across groups.

models/marts/customers.yml

```
# First, define the group and owner  
groups:  
  - name: customer_success  
    owner:  
      name: Customer Success Team  
      email: cx@jaffle.shop  
  
# Then, add 'group' + 'access' modifier to specific models  
models:  
  # This is a public model -- it's a stable & mature interface for other teams/projects  
  - name: dim_customers  
    config:  
      group: customer_success # changed to config in v1.10  
      access: public # changed to config in v1.10  
      
  # This is a private model -- it's an intermediate transformation intended for use in this context *only*  
  - name: int_customer_history_rollup  
    config:  
      group: customer_success # changed to config in v1.10  
      access: private # changed to config in v1.10  
      
  # This is a protected model -- it might be useful elsewhere in *this* project,  
  # but it shouldn't be exposed elsewhere  
  - name: stg_customer__survey_results  
    config:  
      group: customer_success # changed to config in v1.10  
      access: protected # changed to config in v1.10
```

Models with `materialized` set to `ephemeral` cannot have the access property set to public.

For example, if you have a model config set as:

models/my\_model.sql

```
{{ config(materialized='ephemeral') }}
```

And the model access is defined:

models/my\_project.yml

```
models:  
  - name: my_model  
    config:  
      access: public # changed to config in v1.10
```

It will lead to the following error:

```
❯ dbt parse  
02:19:30  Encountered an error:  
Parsing Error  
  Node model.jaffle_shop.my_model with 'ephemeral' materialization has an invalid value (public) for the access field
```

FAQs[​](#faqs "Direct link to FAQs")
------------------------------------

### How does model access relate to database permissions?[​](#how-does-model-access-relate-to-database-permissions "Direct link to How does model access relate to database permissions?")

These are different!

Specifying `access: public` on a model does not trigger dbt to automagically grant `select` on that model to every user or role in your data platform when you materialize it. You have complete control over managing database permissions on every model/schema, as makes sense to you & your organization.

Of course, dbt can facilitate this by means of [the `grants` config](/reference/resource-configs/grants), and other flexible mechanisms. For example:

* Grant access to downstream queriers on public models
* Restrict access to private models, by revoking default/future grants, or by landing them in a different schema

As we continue to develop multi-project collaboration, `access: public` will mean that other teams are allowed to start taking a dependency on that model. This assumes that they've requested, and you've granted them access, to select from the underlying dataset.

### How do I ref a model from another project?[​](#how-do-i-ref-a-model-from-another-project "Direct link to How do I ref a model from another project?")

You can `ref` a model from another project in two ways:

1. [Project dependency](/docs/mesh/govern/project-dependencies): In dbt Enterprise, you can use project dependencies to `ref` a model. dbt uses a behind-the-scenes metadata service to resolve the reference, enabling efficient collaboration across teams and at scale.
2. ["Package" dependency](/docs/build/packages): Another way to `ref` a model from another project is to treat the other project as a package dependency. This requires installing the other project as a package, including its full source code, as well as its upstream dependencies.

### How do I restrict access to models defined in a package?[​](#how-do-i-restrict-access-to-models-defined-in-a-package "Direct link to How do I restrict access to models defined in a package?")

Source code installed from a package becomes part of your runtime environment. You can call macros and run models as if they were macros and models that you had defined in your own project.

For this reason, model access restrictions are "off" by default for models defined in packages. You can reference models from that package regardless of their `access` modifier.

The project is installed as a package can optionally restrict external `ref` access to just its public models. The package maintainer does this by setting a `restrict-access` config to `True` in `dbt_project.yml`.

By default, the value of this config is `False`. This means that:

* Models in the package with `access: protected` may be referenced by models in the root project, as if they were defined in the same project
* Models in the package with `access: private` may be referenced by models in the root project, so long as they also have the same `group` config

When `restrict-access: True`:

* Any `ref` from outside the package to a protected or private model in that package will fail.
* Only models with `access: public` can be referenced outside the package.

dbt\_project.yml

```
restrict-access: True  # default is False
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/mesh/govern/model-access.md)

Last updated on **Nov 19, 2025**

[Previous

About model governance](/docs/mesh/govern/about-model-governance)[Next

Model contracts](/docs/mesh/govern/model-contracts)

* [Related documentation](#related-documentation)
* [Groups](#groups)
* [Access modifiers](#access-modifiers)
* [FAQs](#faqs)
  + [How does model access relate to database permissions?](#how-does-model-access-relate-to-database-permissions)
  + [How do I ref a model from another project?](#how-do-i-ref-a-model-from-another-project)
  + [How do I restrict access to models defined in a package?](#how-do-i-restrict-access-to-models-defined-in-a-package)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/mesh/govern/model-access.md)

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