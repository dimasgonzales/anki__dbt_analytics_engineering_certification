# Source: https://docs.getdbt.com/best-practices/how-we-style/3-how-we-style-our-python

How we style our Python | dbt Developer Hub

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

    - [How we style our dbt models](/best-practices/how-we-style/1-how-we-style-our-dbt-models)
    - [How we style our SQL](/best-practices/how-we-style/2-how-we-style-our-sql)
    - [How we style our Python](/best-practices/how-we-style/3-how-we-style-our-python)
    - [How we style our Jinja](/best-practices/how-we-style/4-how-we-style-our-jinja)
    - [How we style our YAML](/best-practices/how-we-style/5-how-we-style-our-yaml)
    - [Now it's your turn](/best-practices/how-we-style/6-how-we-style-conclusion)
  + [How we build our metrics](/best-practices/how-we-build-our-metrics/semantic-layer-1-intro)
  + [How we build our dbt Mesh projects](/best-practices/how-we-mesh/mesh-1-intro)
  + [Materialization best practices](/best-practices/materializations/1-guide-overview)
  + [Don't nest your curlies](/best-practices/dont-nest-your-curlies)
  + [Clone incremental models as the first step of your CI job](/best-practices/clone-incremental-models)
  + [Writing custom generic data tests](/best-practices/writing-custom-generic-tests)
  + [Best practices for workflows](/best-practices/best-practice-workflows)
  + [Best practices for dbt and Unity Catalog](/best-practices/dbt-unity-catalog-best-practices)

* [Best practices](/best-practices)
* [How we style our dbt projects](/best-practices/how-we-style/0-how-we-style-our-dbt-projects)
* How we style our Python

Copy page

On this page

How we style our Python
=======================

Python tooling[​](#python-tooling "Direct link to Python tooling")
------------------------------------------------------------------

* 🐍 Python has a more mature and robust ecosystem for formatting and linting (helped by the fact that it doesn't have a million distinct dialects). We recommend using those tools to format and lint your code in the style you prefer.
* 🛠️ Our current recommendations are

  + [black](https://pypi.org/project/black/) formatter
  + [ruff](https://pypi.org/project/ruff/) linter

  info

  ☁️ dbt comes with the [black formatter built-in](/docs/cloud/dbt-cloud-ide/lint-format) to automatically lint and format their Python. You don't need to download or configure anything, just click `Format` in a Python model and you're good to go!

Example Python[​](#example-python "Direct link to Example Python")
------------------------------------------------------------------

```
import pandas as pd  
  
  
def model(dbt, session):  
    # set length of time considered a churn  
    pd.Timedelta(days=2)  
  
    dbt.config(enabled=False, materialized="table", packages=["pandas==1.5.2"])  
  
    orders_relation = dbt.ref("stg_orders")  
  
    # converting a DuckDB Python Relation into a pandas DataFrame  
    orders_df = orders_relation.df()  
  
    orders_df.sort_values(by="ordered_at", inplace=True)  
    orders_df["previous_order_at"] = orders_df.groupby("customer_id")[  
        "ordered_at"  
    ].shift(1)  
    orders_df["next_order_at"] = orders_df.groupby("customer_id")["ordered_at"].shift(  
        -1  
    )  
    return orders_df
```

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/how-we-style/3-how-we-style-our-python.md)

Last updated on **Nov 19, 2025**

[Previous

How we style our SQL](/best-practices/how-we-style/2-how-we-style-our-sql)[Next

How we style our Jinja](/best-practices/how-we-style/4-how-we-style-our-jinja)

* [Python tooling](#python-tooling)
* [Example Python](#example-python)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/how-we-style/3-how-we-style-our-python.md)

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