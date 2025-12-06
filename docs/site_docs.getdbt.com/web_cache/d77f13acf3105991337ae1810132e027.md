# Source: https://docs.getdbt.com/docs/dbt-cloud-apis/discovery-schema-job-sources

Sources object schema | dbt Developer Hub

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
* Sources

Copy page

On this page

Sources object schema
=====================

The sources object allows you to query information about all sources in a given job.

### Arguments[​](#arguments "Direct link to Arguments")

When querying for `sources`, the following arguments are available.

Fetching data...
================

Below we show some illustrative example queries and outline the schema of the sources object.

### Example queries[​](#example-queries "Direct link to Example queries")

The database, schema, and identifier arguments are optional. This means that with this endpoint you can:

* Find a specific source by providing `<database>.<schema>.<identifier>`
* Find all of the sources in a database and/or schema by providing `<database>` and/or `<schema>`

#### Finding sources by their database, schema, and identifier[​](#finding-sources-by-their-database-schema-and-identifier "Direct link to Finding sources by their database, schema, and identifier")

The example query below finds a source by its unique database, schema, and identifier.

```
{  
  job(id: 123) {  
    sources(  
      database: "analytics"  
      schema: "analytics"  
      identifier: "dim_customers"  
    ) {  
      uniqueId  
    }  
  }  
}
```

#### Finding sources by their schema[​](#finding-sources-by-their-schema "Direct link to Finding sources by their schema")

The example query below finds all sources in this schema and their respective states (pass, error, fail).

```
{  
  job(id: 123) {  
    sources(schema: "analytics") {  
      uniqueId  
      state  
    }  
  }  
}
```

### Fields[​](#fields "Direct link to Fields")

The sources object can access the *same fields* as the [source node](/docs/dbt-cloud-apis/discovery-schema-job-source). The difference is that the sources object can output a list so instead of querying for fields for one specific source, you can query for those parameters for all sources within a jobID, database, and so on.

When querying for `sources`, the following fields are available:

Fetching data...
================

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/dbt-cloud-apis/schema-discovery-job-sources.mdx)

Last updated on **Nov 19, 2025**

[Previous

Source](/docs/dbt-cloud-apis/discovery-schema-job-source)[Next

Seed](/docs/dbt-cloud-apis/discovery-schema-job-seed)

* [Arguments](#arguments)
* [Example queries](#example-queries)
* [Fields](#fields)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/dbt-cloud-apis/schema-discovery-job-sources.mdx)

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