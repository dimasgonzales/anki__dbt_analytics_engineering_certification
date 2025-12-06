# Source: https://docs.getdbt.com/docs/dbt-cloud-apis/discovery-schema-environment-applied-lineage

Lineage object schema | dbt Developer Hub

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

* [APIs Overview](/docs/dbt-cloud-apis/overview)
* [API Access](/docs/dbt-cloud-apis/authentication)
* [Administrative API](/docs/dbt-cloud-apis/admin-cloud-api)
* [Discovery API](/docs/dbt-cloud-apis/discovery-api)

  + [About the Discovery API](/docs/dbt-cloud-apis/discovery-api)
  + [Uses and examples](/docs/dbt-cloud-apis/discovery-use-cases-and-examples)
  + [Project state in dbt](/docs/dbt-cloud-apis/project-state)
  + [Query the Discovery API](/docs/dbt-cloud-apis/discovery-querying)
  + [Schema](/docs/dbt-cloud-apis/discovery-schema-about)

    - [About the schema](/docs/dbt-cloud-apis/discovery-schema-about)
    - [Environment (recommended)](/docs/dbt-cloud-apis/discovery-schema-environment)

      * [Environment](/docs/dbt-cloud-apis/discovery-schema-environment)
      * [Applied](/docs/dbt-cloud-apis/discovery-schema-environment-applied)

        + [Applied](/docs/dbt-cloud-apis/discovery-schema-environment-applied)
        + [Tests](/docs/dbt-cloud-apis/discovery-schema-environment-applied-tests)
        + [Sources](/docs/dbt-cloud-apis/discovery-schema-environment-applied-sources)
        + [Snapshots](/docs/dbt-cloud-apis/discovery-schema-environment-applied-snapshots)
        + [Seeds](/docs/dbt-cloud-apis/discovery-schema-environment-applied-seeds)
        + [Resources](/docs/dbt-cloud-apis/discovery-schema-environment-applied-resources)
        + [Models](/docs/dbt-cloud-apis/discovery-schema-environment-applied-models)
        + [Exposures](/docs/dbt-cloud-apis/discovery-schema-environment-applied-exposures)
        + [Exposure tile](/docs/dbt-cloud-apis/discovery-schema-environment-applied-exposure-tile)
        + [Tags](/docs/dbt-cloud-apis/discovery-schema-environment-applied-tags)
        + [Packages](/docs/dbt-cloud-apis/discovery-schema-environment-applied-packages)
        + [Owners](/docs/dbt-cloud-apis/discovery-schema-environment-applied-owners)
        + [Model historical runs](/docs/dbt-cloud-apis/discovery-schema-environment-applied-modelHistoricalRuns)
        + [Lineage](/docs/dbt-cloud-apis/discovery-schema-environment-applied-lineage)
      * [Definition](/docs/dbt-cloud-apis/discovery-schema-environment-definition)
    - [Job](/docs/dbt-cloud-apis/discovery-schema-job)
* [Semantic Layer APIs](/docs/dbt-cloud-apis/sl-api-overview)

* [Discovery API](/docs/dbt-cloud-apis/discovery-api)
* [Schema](/docs/dbt-cloud-apis/discovery-schema-about)
* [Environment (recommended)](/docs/dbt-cloud-apis/discovery-schema-environment)
* [Applied](/docs/dbt-cloud-apis/discovery-schema-environment-applied)
* Lineage

Copy page

On this page

Lineage object schema
=====================

The lineageData lineage provides a holistic view of how data moves through an organization, where it’s transformed and consumed. object allows you to query lineage across your resources.

The [Example query](#example-query) illustrates a few fields you can query with the `lineage` object. Refer to [Fields](#fields) to view the entire schema, which provides all possible fields you can query.

### Arguments[​](#arguments "Direct link to Arguments")

When querying for `lineage`, you can use the following arguments:

Fetching data...
================

### Example query[​](#example-query "Direct link to Example query")

You can specify the `environmentId` and filter by "Model" as the resource type to see lineage information for all models in this environment, including their dependencies, materialization type, and metadata:

```
query {  
  environment(id: 834) {  
    applied {  
      lineage(  
        filter: {"types": ["Model"]} # Return results for the Model type  
      ) {  
        name  
        resourceType  
        filePath  
        projectId  
        materializationType  
        parentIds  
        tags  
        uniqueId  
      }  
    }  
  }  
}
```

### Fields[​](#fields "Direct link to Fields")

When querying for `lineage`, you can use the following fields:

Fetching data...
================

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/dbt-cloud-apis/schema-discovery-environment-applied-lineage.mdx)

Last updated on **Nov 19, 2025**

[Previous

Model historical runs](/docs/dbt-cloud-apis/discovery-schema-environment-applied-modelHistoricalRuns)[Next

Definition](/docs/dbt-cloud-apis/discovery-schema-environment-definition)

![Loading](/img/loader-icon.svg "Loading")

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