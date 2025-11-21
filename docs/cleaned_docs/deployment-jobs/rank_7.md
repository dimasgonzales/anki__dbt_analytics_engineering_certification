Copy page

About environments
==================

In software engineering, environments are used to enable engineers to develop and test code without impacting the users of their software. Typically, there are two types of environments in dbt:

* **Deployment or Production** (or *prod*) — Refers to the environment that end users interact with.
* **Development** (or *dev*) — Refers to the environment that engineers work in. This means that engineers can work iteratively when writing and testing new code in *development*. Once they are confident in these changes, they can deploy their code to *production*.

In traditional software engineering, different environments often use completely separate architecture. For example, the dev and prod versions of a website may use different servers and databases. Data warehouses can also be designed to have separate environments — the *production* environment refers to the relations (for example, schemas, tables, and views) that your end users query (often through a BI tool).

Configure environments to tell dbt or dbt Core how to build and execute your project in development and production:

[![](/img/icons/dbt-bit.svg)

#### Environments in dbt

Seamlessly configure development and deployment environments in dbt to control how your project runs in both the Studio IDE, dbt CLI, and dbt jobs.](/docs/dbt-cloud-environments)

[![](/img/icons/command-line.svg)

#### Environments in dbt Core

Setup and maintain separate deployment and development environments through the use of targets within a profile file](/docs/core/dbt-core-environments)

  

Related docs[​](#related-docs "Direct link to Related docs")
------------------------------------------------------------