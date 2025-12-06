# Source: https://docs.getdbt.com/best-practices/how-we-mesh/mesh-1-intro

Intro to dbt Mesh | dbt Developer Hub

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

    - [Who is dbt Mesh for?](/best-practices/how-we-mesh/mesh-2-who-is-dbt-mesh-for)
    - [Deciding how to structure your dbt Mesh](/best-practices/how-we-mesh/mesh-3-structures)
    - [Implementing your mesh plan](/best-practices/how-we-mesh/mesh-4-implementation)
    - [dbt Mesh FAQs](/best-practices/how-we-mesh/mesh-5-faqs)
  + [Materialization best practices](/best-practices/materializations/1-guide-overview)
  + [Don't nest your curlies](/best-practices/dont-nest-your-curlies)
  + [Clone incremental models as the first step of your CI job](/best-practices/clone-incremental-models)
  + [Writing custom generic data tests](/best-practices/writing-custom-generic-tests)
  + [Best practices for workflows](/best-practices/best-practice-workflows)
  + [Best practices for dbt and Unity Catalog](/best-practices/dbt-unity-catalog-best-practices)

* [Best practices](/best-practices)
* How we build our dbt Mesh projects

Copy page

On this page

Intro to dbt Mesh
=================

What is dbt Mesh?[​](#what-is-dbt-mesh "Direct link to What is dbt Mesh?")
--------------------------------------------------------------------------

Organizations of all sizes rely upon dbt to manage their data transformations, from small startups to large enterprises. At scale, it can be challenging to coordinate all the organizational and technical requirements demanded by your stakeholders within the scope of a single dbt project.

To date, there also hasn't been a first-class way to effectively manage the dependencies, governance, and workflows between multiple dbt projects.

That's where **Mesh** comes in - empowering data teams to work *independently and collaboratively*; sharing data, code, and best practices without sacrificing security or autonomy.

Mesh is not a single product - it is a pattern enabled by a convergence of several features in dbt:

* **[Cross-project references](/docs/mesh/govern/project-dependencies#how-to-write-cross-project-ref)** - this is the foundational feature that enables the multi-project deployments. `{{ ref() }}`s now work across dbt projects on Enterprise and Enterprise+ plans.
* **[Catalog](/docs/explore/explore-projects)** - dbt's metadata-powered documentation platform, complete with full, cross-project lineage.
* **Governance** - dbt's governance features allow you to manage access to your dbt models both within and across projects.
  + **[Groups](/docs/mesh/govern/model-access#groups)** - With groups, you can organize nodes in your dbt DAG that share a logical connection (for example, by functional area) and assign an owner to the entire group.
  + **[Access](/docs/mesh/govern/model-access#access-modifiers)** - access configs allow you to control who can reference models.
  + **[Model Versions](/docs/mesh/govern/model-versions)** - when coordinating across projects and teams, we recommend treating your data models as stable APIs. Model versioning is the mechanism to allow graceful adoption and deprecation of models as they evolve.
  + **[Model Contracts](/docs/mesh/govern/model-contracts)** - data contracts set explicit expectations on the shape of the data to ensure data changes upstream of dbt or within a project's logic don't break downstream consumers' data products.

When is the right time to use dbt Mesh?[​](#when-is-the-right-time-to-use-dbt-mesh "Direct link to When is the right time to use dbt Mesh?")
--------------------------------------------------------------------------------------------------------------------------------------------

The multi-project architecture helps organizations with mature, complex transformation workflows in dbt increase the flexibility and performance of their dbt projects. If you're already using dbt and your project has started to experience any of the following, you're likely ready to start exploring this paradigm:

* The **number of models** in your project is degrading performance and slowing down development.
* Teams have developed **separate workflows** and need to decouple development from each other.
* Teams are experiencing **communication challenges**, and the reliability of some of your data products has started to deteriorate.
* **Security and governance** requirements are increasing and would benefit from increased isolation.

dbt is designed to coordinate the features above and simplify the complexity to solve for these problems.

If you're just starting your dbt journey, don't worry about building a multi-project architecture right away. You can *incrementally* adopt the features in this guide as you scale. The collection of features work effectively as independent tools. Familiarizing yourself with the tooling and features that make up a multi-project architecture, and how they can apply to your organization will help you make better decisions as you grow.

For additional information, refer to the [Mesh FAQs](/best-practices/how-we-mesh/mesh-5-faqs).

Learning goals[​](#learning-goals "Direct link to Learning goals")
------------------------------------------------------------------

* Understand the **purpose and tradeoffs** of building a multi-project architecture.
* Develop an intuition for various **Mesh patterns** and how to design a multi-project architecture for your organization.
* Establish recommended steps to **incrementally adopt** these patterns in your dbt implementation.

tip

To help you get started, check out our [Quickstart with Mesh](/guides/mesh-qs) or our online [Mesh course](https://learn.getdbt.com/courses/dbt-mesh) to learn more!

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/how-we-mesh/mesh-1-intro.md)

Last updated on **Nov 19, 2025**

[Previous

Best practices](/best-practices/how-we-build-our-metrics/semantic-layer-9-conclusion)[Next

Who is dbt Mesh for?](/best-practices/how-we-mesh/mesh-2-who-is-dbt-mesh-for)

* [What is dbt Mesh?](#what-is-dbt-mesh)
* [When is the right time to use dbt Mesh?](#when-is-the-right-time-to-use-dbt-mesh)
* [Learning goals](#learning-goals)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/best-practices/how-we-mesh/mesh-1-intro.md)

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