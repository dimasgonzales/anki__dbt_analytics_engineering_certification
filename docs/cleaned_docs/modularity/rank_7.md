Experience the dbt Fusion engine with Tristan Handy and Elias DeFaria on October 28th

[Save your seat](https://www.getdbt.com/resources/webinars/speed-simplicity-cost-savings-experience-the-dbt-fusion-engine "Save your seat")

[![Jialuo Chen](/img/blog/authors/jialuo_chen.jpg)](/blog/authors/jialuo-chen)

[Jialuo Chen
===========](/blog/authors/jialuo-chen)

Software Engineer at Google

[View all authors](/blog/authors)

---

[How to train a linear regression model with dbt and BigFrames](/blog/train-linear-dbt-bigframes)
-------------------------------------------------------------------------------------------------

July 11, 2025 · 5 min read

[![Jialuo Chen](/img/blog/authors/jialuo_chen.jpg)](/blog/authors/jialuo-chen)

[Jialuo Chen](/blog/authors/jialuo-chen)

Software Engineer at Google

Introduction to dbt and BigFrames[​](#introduction-to-dbt-and-bigframes "Direct link to Introduction to dbt and BigFrames")
---------------------------------------------------------------------------------------------------------------------------

**dbt**: A framework for transforming data in modern data warehouses using modular SQL or Python. dbt enables data teams to develop analytics code collaboratively and efficiently by applying software engineering best practices such as version control, modularity, portability, CI/CD, testing, and documentation. For more information, refer to [What is dbt?](/docs/introduction#dbt)

**BigQuery DataFrames (BigFrames)**: An open-source Python library offered by Google. BigFrames scales Python data processing by transpiling common Python data science APIs (pandas and scikit-learn) to BigQuery SQL.

You can read more in the [official BigFrames guide](https://cloud.google.com/bigquery/docs/bigquery-dataframes-introduction) and view the [public BigFrames GitHub repository](https://github.com/googleapis/python-bigquery-dataframes).

By combining dbt with BigFrames via the `dbt-bigquery` adapter (referred to as *"dbt-BigFrames"*), you gain:

* dbt’s modular SQL and Python modeling, dependency management with dbt.ref(), environment configurations, and data testing. With the cloud-based dbt platform, you also get job scheduling and monitoring.
* BigFrames’ ability to execute complex Python transformations (including machine learning) directly in BigQuery.

`dbt-BigFrames` utilizes the **Colab Enterprise notebook executor service** in a GCP project to run Python models. These notebooks execute BigFrames code, which is translated into BigQuery SQL.