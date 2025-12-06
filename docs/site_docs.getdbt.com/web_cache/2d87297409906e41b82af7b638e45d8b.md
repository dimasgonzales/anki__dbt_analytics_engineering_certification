# Source: https://docs.getdbt.com/reference/commands/source

About dbt source command | dbt Developer Hub

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
* [Commands](/reference/dbt-commands)

  + [dbt Command reference](/reference/dbt-commands)
  + [List of commands](/category/list-of-commands)

    - [build](/reference/commands/build)
    - [clean](/reference/commands/clean)
    - [clone](/reference/commands/clone)
    - [docs](/reference/commands/cmd-docs)
    - [compile](/reference/commands/compile)
    - [debug](/reference/commands/debug)
    - [deps](/reference/commands/deps)
    - [environment](/reference/commands/dbt-environment)
    - [init](/reference/commands/init)
    - [invocation](/reference/commands/invocation)
    - [ls (list)](/reference/commands/list)
    - [parse](/reference/commands/parse)
    - [retry](/reference/commands/retry)
    - [rpc](/reference/commands/rpc)
    - [run](/reference/commands/run)
    - [run-operation](/reference/commands/run-operation)
    - [seed](/reference/commands/seed)
    - [show](/reference/commands/show)
    - [snapshot](/reference/commands/snapshot)
    - [source](/reference/commands/source)
    - [test](/reference/commands/test)
    - [version](/reference/commands/version)
  + [Node selection](/reference/node-selection/syntax)
  + [Flags (global configs)](/reference/global-configs/about-global-configs)
  + [Events and logs](/reference/events-logging)
  + [Exit codes](/reference/exit-codes)
  + [Deprecations](/reference/deprecations)
  + [Project Parsing](/reference/parsing)
  + [Programmatic invocations](/reference/programmatic-invocations)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Commands](/reference/dbt-commands)
* [List of commands](/category/list-of-commands)
* source

Copy page

On this page

About dbt source command
========================

The `dbt source` command provides subcommands that are useful when working with source data. This command provides one subcommand, `dbt source freshness`.

### dbt source freshness[​](#dbt-source-freshness "Direct link to dbt source freshness")

If your dbt project is [configured with sources](/docs/build/sources), then the `dbt source freshness` command will query all of your defined source tables, determining the "freshness" of these tables. If the tables are stale (based on the `freshness` config specified for your sources) then dbt will report a warning or error accordingly. If a source table is in a stale state, then dbt will exit with a nonzero exit code.

You can also use [source freshness commands](/reference/commands/source#source-freshness-commands) to help make sure the data you get is new and not old or outdated.

### Configure source freshness[​](#configure-source-freshness "Direct link to Configure source freshness")

The example below, shows how to configure source freshness in dbt. Refer to [Declaring source freshness](/docs/build/sources#declaring-source-freshness) for more information.

models/<filename>.yml

```
sources:  
  - name: jaffle_shop  
    database: raw  
    config:  
      freshness: # changed to config in v1.9  
        warn_after: {count: 12, period: hour}  
        error_after: {count: 24, period: hour}  
  
      loaded_at_field: _etl_loaded_at # changed to config in v1.10  
  
    tables:  
      - name: customers  
  
      - name: orders  
        config:  
          freshness:   
            warn_after: {count: 6, period: hour}  
            error_after: {count: 12, period: hour}  
            filter: datediff('day', _etl_loaded_at, current_timestamp) < 2  
  
      - name: product_skus  
        config:  
          freshness: null
```

This helps to monitor the data pipeline health.

You can also configure source freshness in the **Execution settings** section in your dbt job **Settings** page. For more information, refer to [Enabling source freshness snapshots](/docs/deploy/source-freshness#enabling-source-freshness-snapshots).

### Source freshness commands[​](#source-freshness-commands "Direct link to Source freshness commands")

Source freshness commands ensure you're receiving the most up-to-date, relevant, and accurate information.

Some of the typical commands you can use are:

| **Command** | **Description** |
| --- | --- |
| [`dbt source freshness`](/reference/commands/source#dbt-source-freshness) | Checks the "freshness" for all sources. |
| [`dbt source freshness --output target/source_freshness.json`](/reference/commands/source#configuring-source-freshness-output) | Output of "freshness" information to a different path. |
| [`dbt source freshness --select "source:source_name"`](/reference/commands/source#specifying-sources-to-snapshot) | Checks the "freshness" for specific sources. |

### Specifying sources to snapshot[​](#specifying-sources-to-snapshot "Direct link to Specifying sources to snapshot")

By default, `dbt source freshness` will calculate freshness information for all of the sources in your project. To snapshot freshness for a subset of these sources, use the `--select` flag.

```
# Snapshot freshness for all Snowplow tables:  
$ dbt source freshness --select "source:snowplow"  
  
# Snapshot freshness for a particular source table:  
$ dbt source freshness --select "source:snowplow.event"
```

### Configuring source freshness output[​](#configuring-source-freshness-output "Direct link to Configuring source freshness output")

When `dbt source freshness` completes, a JSON file containing information about the freshness of your sources will be saved to `target/sources.json`. An example `sources.json` will look like:

target/sources.json

```
{  
    "meta": {  
        "generated_at": "2019-02-15T00:53:03.971126Z",  
        "elapsed_time": 0.21452808380126953  
    },  
    "sources": {  
        "source.project_name.source_name.table_name": {  
            "max_loaded_at": "2019-02-15T00:45:13.572836+00:00Z",  
            "snapshotted_at": "2019-02-15T00:53:03.880509+00:00Z",  
            "max_loaded_at_time_ago_in_s": 481.307673,  
            "state": "pass",  
            "criteria": {  
                "warn_after": {  
                    "count": 12,  
                    "period": "hour"  
                },  
                "error_after": {  
                    "count": 1,  
                    "period": "day"  
                }  
            }  
        }  
    }  
}
```

To override the destination for this `sources.json` file, use the `-o` (or `--output`) flag:

```
# Output source freshness info to a different path  
$ dbt source freshness --output target/source_freshness.json
```

### Using source freshness[​](#using-source-freshness "Direct link to Using source freshness")

Snapshots of source freshness can be used to understand:

1. If a specific data source is in a delayed state
2. The trend of data source freshness over time

This command can be run manually to determine the state of your source data freshness at any time. It is also recommended that you run this command on a schedule, storing the results of the freshness snapshot at regular intervals. These longitudinal snapshots will make it possible to be alerted when source data freshness SLAs are violated, as well as understand the trend of freshness over time.

dbt makes it easy to snapshot source freshness on a schedule, and provides a dashboard out of the box indicating the state of freshness for all of the sources defined in your project. For more information on snapshotting freshness in dbt, check out the [docs](/docs/build/sources#source-data-freshness).

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/source.md)

Last updated on **Nov 19, 2025**

[Previous

snapshot](/reference/commands/snapshot)[Next

test](/reference/commands/test)

* [dbt source freshness](#dbt-source-freshness)
* [Configure source freshness](#configure-source-freshness)
* [Source freshness commands](#source-freshness-commands)
* [Specifying sources to snapshot](#specifying-sources-to-snapshot)
* [Configuring source freshness output](#configuring-source-freshness-output)
* [Using source freshness](#using-source-freshness)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/commands/source.md)

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