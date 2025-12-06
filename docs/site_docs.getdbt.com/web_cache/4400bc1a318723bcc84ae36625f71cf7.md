# Source: https://docs.getdbt.com/reference/exposure-properties

Exposure properties | dbt Developer Hub

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

* [About References](/reference/references-overview)
* [Project configs](/category/project-configs)
* [Platform-specific configs](/reference/resource-configs/resource-configs)
* [Resource configs and properties](/reference/resource-configs/resource-path)

  + [About resource paths](/reference/resource-configs/resource-path)
  + [Configs and properties](/reference/configs-and-properties)
  + [General properties](/category/general-properties)
  + [General configs](/category/general-configs)
  + [For models](/reference/model-properties)
  + [For seeds](/reference/seed-properties)
  + [For snapshots](/reference/snapshot-properties)
  + [For data tests](/reference/data-test-configs)
  + [For unit tests](/reference/resource-properties/unit-tests)
  + [For sources](/reference/source-properties)
  + [For analyses](/reference/analysis-properties)
  + [For exposures](/reference/exposure-properties)

    - [Exposure properties](/reference/exposure-properties)
  + [For macros](/reference/macro-properties)
  + [For functions](/reference/function-properties)
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Resource configs and properties](/reference/resource-configs/resource-path)
* For exposures

Copy page

On this page

Exposure properties
===================

Related documentation[​](#related-documentation "Direct link to Related documentation")
---------------------------------------------------------------------------------------

* [Using exposures](/docs/build/exposures)
* [Declaring resource properties](/reference/configs-and-properties)

Overview[​](#overview "Direct link to Overview")
------------------------------------------------

Exposures are defined in `properties.yml` files nested under an `exposures:` key. You may define `exposures` in YAML files that also define `sources` or `models`. Exposure properties are "special properties" in that you can't configure them in the `dbt_project.yml` file or using `config()` blocks. Refer to  [Configs and properties](https://docs.getdbt.com/reference/define-properties#which-properties-are-not-also-configs) for more info.

Note that while most exposure properties must be configured directly in these YAML files, you can set the [`enabled`](/reference/resource-configs/enabled) config at the [project level](#project-level-configs) in the`dbt_project.yml` file.

You can name these files `whatever_you_want.yml`, and nest them arbitrarily deeply in subfolders within the `models/` directory.

Exposure names must contain only letters, numbers, and underscores (no spaces or special characters). For a short human-friendly name with title casing, spaces, and special characters, use the `label` property.

models/<filename>.yml

```
exposures:  
  - name: <string_with_underscores>  
    description: <markdown_string>  
    type: {dashboard, notebook, analysis, ml, application}  
    url: <string>  
    maturity: {high, medium, low}  # Indicates level of confidence or stability in the exposure  
    enabled: true | false  
    config: # 'tags' and 'meta' changed to config in v1.10  
      tags: [<string>]   
      meta: {<dictionary>}  
      enabled: true | false  
    owner: # supports 'name' and 'email' only  
      name: <string>  
      email: <string>  
      
    depends_on:  
      - ref('model')  
      - ref('seed')  
      - source('name', 'table')  
      - metric('metric_name')  
        
    label: "Human-Friendly Name for this Exposure!"  
  
  - name: ... # declare properties of additional exposures
```

Example[​](#example "Direct link to Example")
---------------------------------------------

models/jaffle/exposures.yml

```
exposures:  
  
  - name: weekly_jaffle_metrics  
    label: Jaffles by the Week              # optional  
    type: dashboard                         # required  
    maturity: high                          # optional  
    url: https://bi.tool/dashboards/1       # optional  
    description: >                          # optional  
      Did someone say "exponential growth"?  
  
    depends_on:                             # expected  
      - ref('fct_orders')  
      - ref('dim_customers')  
      - source('gsheets', 'goals')  
      - metric('count_orders')  
  
    owner:  
      name: Callum McData  
      email: data@jaffleshop.com  
  
  
        
  - name: jaffle_recommender  
    maturity: medium  
    type: ml  
    url: https://jupyter.org/mycoolalg  
    description: >  
      Deep learning to power personalized "Discover Sandwiches Weekly"  
      
    depends_on:  
      - ref('fct_orders')  
        
    owner:  
      name: Data Science Drew  
      email: data@jaffleshop.com  
  
        
  - name: jaffle_wrapped  
    type: application  
    description: Tell users about their favorite jaffles of the year  
    depends_on: [ ref('fct_orders') ]  
    owner: { email: summer-intern@jaffleshop.com }
```

#### Project-level configs[​](#project-level-configs "Direct link to Project-level configs")

You can define project-level configs for exposures in the `dbt_project.yml` file under the `exposures:` key using the `+` prefix. Currently, only the [`enabled` config](/reference/resource-configs/enabled) is supported:

dbt\_project.yml

```
name: 'project_name'  
  
# rest of dbt_project.yml  
  
exposures:  
  +enabled: true
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/exposure-properties.md)

Last updated on **Nov 19, 2025**

[Previous

Analysis properties](/reference/analysis-properties)[Next

Exposure properties](/reference/exposure-properties)

* [Related documentation](#related-documentation)
* [Overview](#overview)
* [Example](#example)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/exposure-properties.md)

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