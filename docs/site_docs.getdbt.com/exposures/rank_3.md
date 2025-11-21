# Source: https://docs.getdbt.com/docs/dbt-cloud-apis/discovery-schema-job-exposures

Exposures object schema | dbt Developer Hub

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
    - [Job](/docs/dbt-cloud-apis/discovery-schema-job)

      * [Job](/docs/dbt-cloud-apis/discovery-schema-job)
      * [Model](/docs/dbt-cloud-apis/discovery-schema-job-model)
      * [Models](/docs/dbt-cloud-apis/discovery-schema-job-models)
      * [Source](/docs/dbt-cloud-apis/discovery-schema-job-source)
      * [Sources](/docs/dbt-cloud-apis/discovery-schema-job-sources)
      * [Seed](/docs/dbt-cloud-apis/discovery-schema-job-seed)
      * [Seeds](/docs/dbt-cloud-apis/discovery-schema-job-seeds)
      * [Snapshots](/docs/dbt-cloud-apis/discovery-schema-job-snapshots)
      * [Test](/docs/dbt-cloud-apis/discovery-schema-job-test)
      * [Tests](/docs/dbt-cloud-apis/discovery-schema-job-tests)
      * [Exposure](/docs/dbt-cloud-apis/discovery-schema-job-exposure)
      * [Exposures](/docs/dbt-cloud-apis/discovery-schema-job-exposures)
* [Semantic Layer APIs](/docs/dbt-cloud-apis/sl-api-overview)

* [Discovery API](/docs/dbt-cloud-apis/discovery-api)
* [Schema](/docs/dbt-cloud-apis/discovery-schema-about)
* [Job](/docs/dbt-cloud-apis/discovery-schema-job)
* Exposures

Copy page

On this page

Exposures object schema
=======================

The exposures object allows you to query information about all exposures in a given job. To learn more, refer to [Add Exposures to your DAG](/docs/build/exposures).

### Arguments[​](#arguments "Direct link to Arguments")

When querying for `exposures`, the following arguments are available.

Fetching data...
================

Below we show some illustrative example queries and outline the schema of the exposures object.

### Example query[​](#example-query "Direct link to Example query")

The example below queries information about all exposures in a given job including the owner's name and email, the URL, and information about parent sources and parent models for each exposure.

```
{  
  job(id: 123) {  
    exposures(jobId: 123) {  
      runId  
      projectId  
      name  
      uniqueId  
      resourceType  
      ownerName  
      url  
      ownerEmail  
      parentsSources {  
        uniqueId  
        sourceName  
        name  
        state  
        maxLoadedAt  
        criteria {  
          warnAfter {  
            period  
            count  
          }  
          errorAfter {  
            period  
            count  
          }  
        }  
        maxLoadedAtTimeAgoInS  
      }  
      parentsModels {  
        uniqueId  
      }  
    }  
  }  
}
```

### Fields[​](#fields "Direct link to Fields")

When querying for `exposures`, the following fields are available:

Fetching data...
================

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/dbt-cloud-apis/schema-discovery-job-exposures.mdx)

Last updated on **Nov 19, 2025**

[Previous

Exposure](/docs/dbt-cloud-apis/discovery-schema-job-exposure)[Next

Semantic Layer APIs](/docs/dbt-cloud-apis/sl-api-overview)

* [Arguments[​](#arguments "Direct link to Arguments")](#arguments)
* [Example query[​](#example-query "Direct link to Example query")](#example-query)
* [Fields[​](#fields "Direct link to Fields")](#fields)
* [Was this page helpful?](#feedback-header)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/dbt-cloud-apis/schema-discovery-job-exposures.mdx)

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