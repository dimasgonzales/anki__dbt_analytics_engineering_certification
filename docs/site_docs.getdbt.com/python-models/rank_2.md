# Source: https://docs.getdbt.com/guides/dbt-python-bigframes

Using BigQuery DataFrames with dbt Python models | dbt Developer Hub

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

Copy page

Using BigQuery DataFrames with dbt Python models
================================================

[Back to guides](/guides)

BigQuery

Google

GCP

BigFrames

Quickstart

Intermediate

Menu

* 1 Introduction​
* 2 Configure Google Cloud​
* 3 Create, configure, and execute your Python models​

Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

In this guide, you'll learn how to set up dbt so you can use it with BigQuery DataFrames (BigFrames):

* Build scalable data transformation pipelines using dbt and Google Cloud, with SQL and Python.
* Leverage BigFrames from dbt for scalable BigQuery SQL.

In addition to the existing dataproc/pyspark based submission methods for executing python models, you can now use the BigFrames submission method to execute Python models with pandas-like and scikit-like APIs, without the need of any Spark setup or knowledge.

BigQuery DataFrames is an open source Python package that transpiles pandas and scikit-learn code to scalable BigQuery SQL. The dbt-bigquery adapter relies on the BigQuery Studio Notebook Executor Service to run the Python client side code.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* A [Google Cloud account](https://cloud.google.com/free)
* A [dbt account](https://www.getdbt.com/signup/)
* Basic to intermediate SQL and python.
* Basic understanding of dbt fundamentals. We recommend the [dbt Fundamentals course](https://learn.getdbt.com).

During setup, you’ll need to select the **BigQuery (Legacy)** adapter and enter values for your **Google Cloud Storage Bucket** and **Dataproc Region** in the dbt platform. See [Configure BigQuery in dbt platform](/guides/dbt-python-bigframes?step=2#configure-bigquery-in-dbt-platform) for details.

### What you'll build[​](#what-youll-build "Direct link to What you'll build")

Here's what you'll build in two parts:

* Google Cloud project setup
  + A one-time setup to configure the Google Cloud project you’ll be working with.
* Build and Run the Python Model
  + Create, configure, and execute a Python model using BigQuery DataFrames and dbt.

You will set up the environments, build scalable pipelines in dbt, and execute a python model.

[![Implementation of the BigFrames submission method](/img/guides/gcp-guides/gcp-bigframes-architecture.png?v=2 "Implementation of the BigFrames submission method")](#)Implementation of the BigFrames submission method

**Figure 1** - Implementation of the BigFrames submission method for dbt python models

BackNext

Configure Google Cloud[​](#configure-google-cloud "Direct link to Configure Google Cloud")
------------------------------------------------------------------------------------------

The dbt BigFrames submission method supports both service account and OAuth credentials. You will use the service account in the following steps.

1. **Create a new Google Cloud Project**

   a. Your new project will have the following list of APIs already enabled, including BigQuery, which is required.

   * [Default APIs](https://cloud.google.com/service-usage/docs/enabled-service#default)

   b. Enable the BigQuery API which also enables the following additional APIs automatically

   * [BigQuery API's](https://cloud.google.com/bigquery/docs/enable-assets#automatic-api-enablement)

   c. Required API's:

   * **BigQuery API:** For all core BigQuery operations.
   * **Vertex AI API:** To use the Colab Enterprise executor service.
   * **Cloud Storage API:** For staging code and logs.
   * **IAM API:** For managing permissions.
   * **Compute Engine API:** As an underlying dependency for the notebook runtime environment.
   * **Dataform API:** For managing the notebook code assets within BigQuery.
2. **Create a service account and grant IAM permissions**

   This service account will be used by dbt to read and write data on BigQuery and use BigQuery Studio Notebooks.

   Create the service account with IAM permissions:

   ```
   #Create Service Account  
   gcloud iam service-accounts create dbt-bigframes-sa  
   #Grant BigQuery User Role  
   gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} --member=serviceAccount:dbt-bigframes-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com --role=roles/bigquery.user  
   #Grant BigQuery Data Editor role. This can be restricted at dataset level  
   gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} --member=serviceAccount:dbt-bigframes-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com --role=roles/bigquery.dataEditor  
   #Grant Service Account user   
   gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} --member=serviceAccount:dbt-bigframes-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com --role=roles/iam.serviceAccountUser  
   #Grant Colab Entperprise User  
   gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} --member=serviceAccount:dbt-bigframes-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com --role=roles/aiplatform.colabEnterpriseUser
   ```

   When using a Shared VPC

   When using Colab Enterprise in a Shared VPC environment, additional roles are required for the following service accounts on the Shared VPC host project:

   * Vertex AI P4SA (`service-<PROJECT_NUMBER>@gcp-sa-aiplatform.iam.gserviceaccount.com`): This service account always requires the Compute Network User (`roles/compute.networkUser`) role on the Shared VPC host
     project. Replace `<PROJECT_NUMBER>` with the project number.
   * Colab Enterprise P6SA (`service-<PROJECT_NUMBER>@gcp-sa-vertex-nb.iam.gserviceaccount.com`): This service account also needs the Compute Network User (`roles/compute.networkUser`) role on the Shared VPC host
     project. Replace `<PROJECT_NUMBER>` with the project number.
3. *(Optional)* **Create a test BigQuery Dataset**

   Create a new BigQuery Dataset if you don't already have one:

   ```
   #Create BQ dataset   
   bq mk --location=${REGION} echo "${GOOGLE_CLOUD_PROJECT}" | tr '-' '_'_dataset
   ```
4. **Create a GCS bucket to stage the python code, and store logs**

   For temporary log and code storage, please create a GCS bucket and assign the required permissions:

   ```
   #Create GCS bucket  
   gcloud storage buckets create gs://${GOOGLE_CLOUD_PROJECT}-bucket --location=${REGION}  
   #Grant Storage Admin over the bucket to your SA   
     
   gcloud storage buckets add-iam-policy-binding gs://${GOOGLE_CLOUD_PROJECT}-bucket --member=serviceAccount:dbt-bigframes-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com --role=roles/storage.admin
   ```

### Configure BigQuery in the dbt platform[​](#configure-bigquery-in-the-dbt-platform "Direct link to Configure BigQuery in the dbt platform")

To set up your BigQuery DataFrames connection in the dbt platform, refer to the following steps:

1. Go to **Account settings** > **Connections**. Click **New connection**.
2. In the **Type** section, select **BigQuery**.
3. Select **BigQuery (Legacy)** as your adapter.
4. Under **Optional settings**, enter values for the following fields:
   * **Google Cloud Storage Bucket** (for example: `dbt_name_bucket`)
   * **Dataproc Region** (for example: `us-central1`)
5. Click **Save**.

This is required so that BigFrames jobs execute correctly.

Refer to [Connect to BigQuery](/docs/cloud/connect-data-platform/connect-bigquery) for more info on how to connect to BigQuery in the dbt platform.

[![Configure BigQuery in the dbt platform](/img/guides/gcp-guides/dbt-platform-bq.png?v=2 "Configure BigQuery in the dbt platform")](#)Configure BigQuery in the dbt platform

BackNext

Create, configure, and execute your Python models[​](#create-configure-and-execute-your-python-models "Direct link to Create, configure, and execute your Python models")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. In your dbt project, create a SQL model in your models directory, ending in the `.sql` file extension. Name it `my_sql_model.sql`.
2. In the file, copy this SQL into it.

   ```
      select   
      1 as foo,  
      2 as bar
   ```
3. Now create a new model file in the models directory, named `my_first_python_model.py`.
4. In the `my_first_python_model.py` file, add this code:

   ```
   def model(dbt, session):  
      dbt.config(submission_method="bigframes")  
      bdf = dbt.ref("my_sql_model") #loading from prev step  
      return bdf
   ```
5. Configure the BigFrames submission method by using either:

   a. Project level configuration via dbt\_project.yml

   ```
   models:  
   my_dbt_project:  
      submission_method: bigframes  
      python_models:  
         +materialized: view
   ```

   or

   b. The Python code via dbt.config in the my\_first\_python\_model.py file

   ```
   def model(dbt, session):  
      dbt.config(submission_method="bigframes")  
      # rest of the python code...
   ```
6. Run `dbt run`
7. You can view the logs in [dbt logs](/reference/events-logging). You can optionally view the codes and logs (including previous executions) from the [Colab Enterprise Executions](https://console.cloud.google.com/vertex-ai/colab/execution-jobs) tab and [GCS bucket](https://console.cloud.google.com/storage/browser) from the GCP console.
8. Congrats! You just created your first two python models to run on BigFrames!

BackNext

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [BigQuery](/tags/big-query)
* [Google](/tags/google)
* [GCP](/tags/gcp)
* [BigFrames](/tags/big-frames)
* [Quickstart](/tags/quickstart)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/guides/dbt-python-bigframes.md)

Last updated on **Nov 19, 2025**

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