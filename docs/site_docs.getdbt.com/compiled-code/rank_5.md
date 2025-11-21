# Source: https://docs.getdbt.com/docs/build/analyses

Analyses | dbt Developer Hub

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

    - [Models](/docs/build/models)
    - [Tests](/docs/build/data-tests)
    - [Documentation](/docs/build/documentation)
    - [Snapshots](/docs/build/snapshots)
    - [Seeds](/docs/build/seeds)
    - [Jinja and macros](/docs/build/jinja-macros)
    - [User-defined functions](/docs/build/udfs)
    - [Sources](/docs/build/sources)
    - [Exposures](/docs/build/exposures)
    - [Groups](/docs/build/groups)
    - [Analyses](/docs/build/analyses)
  + [Build your metrics](/docs/build/build-metrics-intro)
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
* [Build your DAG](/docs/build/models)
* Analyses

Copy page

On this page

Analyses
========

Overview[​](#overview "Direct link to Overview")
------------------------------------------------

dbt's notion of `models` makes it easy for data teams to version control and collaborate on data transformations. Sometimes though, a certain SQL statement doesn't quite fit into the mold of a dbt model. These more "analytical" SQL files can be versioned inside of your dbt project using the `analysis` functionality of dbt.

Any `.sql` files found in the `analyses/` directory of a dbt project will be compiled, but not executed. This means that analysts can use dbt functionality like `{{ ref(...) }}` to select from models in an environment-agnostic way.

In practice, an analysis file might look like this (via the [open source Quickbooks models](https://github.com/dbt-labs/quickbooks)):

analyses/running\_total\_by\_account.sql

```
-- analyses/running_total_by_account.sql  
  
with journal_entries as (  
  
  select *  
  from {{ ref('quickbooks_adjusted_journal_entries') }}  
  
), accounts as (  
  
  select *  
  from {{ ref('quickbooks_accounts_transformed') }}  
  
)  
  
select  
  txn_date,  
  account_id,  
  adjusted_amount,  
  description,  
  account_name,  
  sum(adjusted_amount) over (partition by account_id order by id rows unbounded preceding)  
from journal_entries  
order by account_id, id
```

To compile this analysis into runnable sql, run:

```
dbt compile
```

Then, look for the compiled SQL file in `target/compiled/{project name}/analyses/running_total_by_account.sql`. This SQL can then be pasted into a data visualization tool, for instance. Note that no `running_total_by_account` relation will be materialized in the database as this is an `analysis`, not a `model`.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/analyses.md)

Last updated on **Nov 19, 2025**

[Previous

Groups](/docs/build/groups)

* [Overview](#overview)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/analyses.md)

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