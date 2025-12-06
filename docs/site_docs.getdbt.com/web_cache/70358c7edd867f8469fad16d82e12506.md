# Source: https://docs.getdbt.com/guides/bigquery

Quickstart for dbt and BigQuery | dbt Developer Hub

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

Copy page

Quickstart for dbt and BigQuery
===============================

[Back to guides](/guides)

BigQuery

platform

Quickstart

Beginner

Menu




Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

In this quickstart guide, you'll learn how to use dbt with BigQuery. It will show you how to:

* Create a Google Cloud Platform (GCP) project.
* Access sample data in a public dataset.
* Connect dbt to BigQuery.
* Take a sample query and turn it into a model in your dbt project. A model in dbt is a select statement.
* Add tests to your models.
* Document your models.
* Schedule a job to run.

Videos for you

You can check out [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) for free if you're interested in course learning with videos.

### Prerequisites​[​](#prerequisites "Direct link to Prerequisites​")

* You have a [dbt account](https://www.getdbt.com/signup/).
* You have a [Google account](https://support.google.com/accounts/answer/27441?hl=en).
* You can use a personal or work account to set up BigQuery through [Google Cloud Platform (GCP)](https://cloud.google.com/free).

### Related content[​](#related-content "Direct link to Related content")

* Learn more with [dbt Learn courses](https://learn.getdbt.com)
* [CI jobs](/docs/deploy/continuous-integration)
* [Deploy jobs](/docs/deploy/deploy-jobs)
* [Job notifications](/docs/deploy/job-notifications)
* [Source freshness](/docs/deploy/source-freshness)

Create a new GCP project​[​](#create-a-new-gcp-project "Direct link to Create a new GCP project​")
--------------------------------------------------------------------------------------------------

1. Go to the [BigQuery Console](https://console.cloud.google.com/bigquery) after you log in to your Google account. If you have multiple Google accounts, make sure you’re using the correct one.
2. Create a new project from the [Manage resources page](https://console.cloud.google.com/projectcreate?previousPage=%2Fcloud-resource-manager%3Fwalkthrough_id%3Dresource-manager--create-project%26project%3D%26folder%3D%26organizationId%3D%23step_index%3D1&walkthrough_id=resource-manager--create-project). For more information, refer to [Creating a project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) in the Google Cloud docs. GCP automatically populates the Project name field for you. You can change it to be more descriptive for your use. For example, `dbt Learn - BigQuery Setup`.

Create BigQuery datasets[​](#create-bigquery-datasets "Direct link to Create BigQuery datasets")
------------------------------------------------------------------------------------------------

1. From the [BigQuery Console](https://console.cloud.google.com/bigquery), click **Editor**. Make sure to select your newly created project, which is available at the top of the page.
2. Verify that you can run SQL queries. Copy and paste these queries into the Query Editor:

   ```
   select * from `dbt-tutorial.jaffle_shop.customers`;  
   select * from `dbt-tutorial.jaffle_shop.orders`;  
   select * from `dbt-tutorial.stripe.payment`;
   ```

   Click **Run**, then check for results from the queries. For example:

   [![Bigquery Query Results](/img/bigquery/query-results.png?v=2 "Bigquery Query Results")](#)Bigquery Query Results
3. Create new datasets from the [BigQuery Console](https://console.cloud.google.com/bigquery). For more information, refer to [Create datasets](https://cloud.google.com/bigquery/docs/datasets#create-dataset) in the Google Cloud docs. Datasets in BigQuery are equivalent to schemas in a traditional database. On the **Create dataset** page:

   * **Dataset ID** — Enter a name that fits the purpose. This name is used like schema in fully qualified references to your database objects such as `database.schema.table`. As an example for this guide, create one for `jaffle_shop` and another one for `stripe` afterward.
   * **Data location** — Leave it blank (the default). It determines the GCP location of where your data is stored. The current default location is the US multi-region. All tables within this dataset will share this location.
   * **Enable table expiration** — Leave it unselected (the default). The default for the billing table expiration is 60 days. Because billing isn’t enabled for this project, GCP defaults to deprecating tables.
   * **Google-managed encryption key** — This option is available under **Advanced options**. Allow Google to manage encryption (the default).

   [![Bigquery Create Dataset ID](/img/bigquery/create-dataset-id.png?v=2 "Bigquery Create Dataset ID")](#)Bigquery Create Dataset ID
4. After you create the `jaffle_shop` dataset, create one for `stripe` with all the same values except for **Dataset ID**.

Generate BigQuery credentials[​](#generate-bigquery-credentials "Direct link to Generate BigQuery credentials")
---------------------------------------------------------------------------------------------------------------

In order to let dbt connect to your warehouse, you'll need to generate a keyfile. This is analogous to using a database username and password with most other data warehouses.

1. Start the [GCP credentials wizard](https://console.cloud.google.com/apis/credentials/wizard). Make sure your new project is selected in the header. If you do not see your account or project, click your profile picture to the right and verify you are using the correct email account. For **Credential Type**:
   * From the **Select an API** dropdown, choose **BigQuery API**
   * Select **Application data** for the type of data you will be accessing
   * Click **Next** to create a new service account.
2. Create a service account for your new project from the [Service accounts page](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts?supportedpurview=project). For more information, refer to [Create a service account](https://developers.google.com/workspace/guides/create-credentials#create_a_service_account) in the Google Cloud docs. As an example for this guide, you can:
   * Type `dbt-user` as the **Service account name**
   * From the **Select a role** dropdown, choose **BigQuery Job User** and **BigQuery Data Editor** roles and click **Continue**
   * Leave the **Grant users access to this service account** fields blank
   * Click **Done**
3. Create a service account key for your new project from the [Service accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts?walkthrough_id=iam--create-service-account-keys&start_index=1#step_index=1). For more information, refer to [Create a service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating) in the Google Cloud docs. When downloading the JSON file, make sure to use a filename you can easily remember. For example, `dbt-user-creds.json`. For security reasons, dbt Labs recommends that you protect this JSON file like you would your identity credentials; for example, don't check the JSON file into your version control software.

Connect dbt to BigQuery​[​](#connect-dbt-to-bigquery "Direct link to Connect dbt to BigQuery​")
-----------------------------------------------------------------------------------------------

1. Create a new project in [dbt](/docs/cloud/about-cloud/access-regions-ip-addresses). Navigate to **Account settings** (by clicking on your account name in the left side menu), and click **+ New project**.
2. Enter a project name and click **Continue**.
3. For the warehouse, click **BigQuery** then **Next** to set up your connection.
4. Click **Upload a Service Account JSON File** in settings.
5. Select the JSON file you downloaded in [Generate BigQuery credentials](#generate-bigquery-credentials) and dbt will fill in all the necessary fields.
6. Optional — dbt Enterprise plans can configure developer OAuth with BigQuery, providing an additional layer of security. For more information, refer to [Set up BigQuery OAuth](/docs/cloud/manage-access/set-up-bigquery-oauth).
7. Click **Test Connection**. This verifies that dbt can access your BigQuery account.
8. Click **Next** if the test succeeded. If it failed, you might need to go back and regenerate your BigQuery credentials.

Set up a dbt managed repository[​](#set-up-a-dbt-managed-repository "Direct link to Set up a dbt managed repository")
---------------------------------------------------------------------------------------------------------------------

When you develop in dbt, you can leverage [Git](/docs/cloud/git/git-version-control) to version control your code.

To connect to a repository, you can either set up a dbt-hosted [managed repository](/docs/cloud/git/managed-repository) or directly connect to a [supported git provider](/docs/cloud/git/connect-github). Managed repositories are a great way to trial dbt without needing to create a new repository. In the long run, it's better to connect to a supported git provider to use features like automation and [continuous integration](/docs/deploy/continuous-integration).

To set up a managed repository:

1. Under "Setup a repository", select **Managed**.
2. Type a name for your repo such as `bbaggins-dbt-quickstart`
3. Click **Create**. It will take a few seconds for your repository to be created and imported.
4. Once you see the "Successfully imported repository," click **Continue**.

Initialize your dbt project​ and start developing[​](#initialize-your-dbt-project-and-start-developing "Direct link to Initialize your dbt project​ and start developing")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now that you have a repository configured, you can initialize your project and start development in dbt:

1. Click **Start developing in the Studio IDE**. It might take a few minutes for your project to spin up for the first time as it establishes your git connection, clones your repo, and tests the connection to the warehouse.
2. Above the file tree to the left, click **Initialize dbt project**. This builds out your folder structure with example models.
3. Make your initial commit by clicking **Commit and sync**. Use the commit message `initial commit` and click **Commit**. This creates the first commit to your managed repo and allows you to open a branch where you can add new dbt code.
4. You can now directly query data from your warehouse and execute `dbt run`. You can try this out now:
   * Click **+ Create new file**, add this query to the new file, and click **Save as** to save the new file:

     ```
     select * from `dbt-tutorial.jaffle_shop.customers`
     ```
   * In the command line bar at the bottom, enter `dbt run` and click **Enter**. You should see a `dbt run succeeded` message.

Build your first model[​](#build-your-first-model "Direct link to Build your first model")
------------------------------------------------------------------------------------------

You have two options for working with files in the Studio IDE:

* Create a new branch (recommended) — Create a new branch to edit and commit your changes. Navigate to **Version Control** on the left sidebar and click **Create branch**.
* Edit in the protected primary branch — If you prefer to edit, format, or lint files and execute dbt commands directly in your primary git branch. The Studio IDE prevents commits to the protected branch, so you will be prompted to commit your changes to a new branch.

Name the new branch `add-customers-model`.

1. Click the **...** next to the `models` directory, then select **Create file**.
2. Name the file `customers.sql`, then click **Create**.
3. Copy the following query into the file and click **Save**.

```
with customers as (  
  
    select  
        id as customer_id,  
        first_name,  
        last_name  
  
    from `dbt-tutorial`.jaffle_shop.customers  
  
),  
  
orders as (  
  
    select  
        id as order_id,  
        user_id as customer_id,  
        order_date,  
        status  
  
    from `dbt-tutorial`.jaffle_shop.orders  
  
),  
  
customer_orders as (  
  
    select  
        customer_id,  
  
        min(order_date) as first_order_date,  
        max(order_date) as most_recent_order_date,  
        count(order_id) as number_of_orders  
  
    from orders  
  
    group by 1  
  
),  
  
final as (  
  
    select  
        customers.customer_id,  
        customers.first_name,  
        customers.last_name,  
        customer_orders.first_order_date,  
        customer_orders.most_recent_order_date,  
        coalesce(customer_orders.number_of_orders, 0) as number_of_orders  
  
    from customers  
  
    left join customer_orders using (customer_id)  
  
)  
  
select * from final
```

4. Enter `dbt run` in the command prompt at the bottom of the screen. You should get a successful run and see the three models.

Later, you can connect your business intelligence (BI) tools to these views and tables so they only read cleaned up data rather than raw data in your BI tool.

#### FAQs[​](#faqs "Direct link to FAQs")

How can I see the SQL that dbt is running?

To check out the SQL that dbt is running, you can look in:

* dbt:
  + Within the run output, click on a model name, and then select "Details"
* dbt Core:
  + The `target/compiled/` directory for compiled `select` statements
  + The `target/run/` directory for compiled `create` statements
  + The `logs/dbt.log` file for verbose logging.

How did dbt choose which schema to build my models in?

By default, dbt builds models in your target schema. To change your target schema:

* If you're developing in **dbt**, these are set for each user when you first use a development environment.
* If you're developing with **dbt Core**, this is the `schema:` parameter in your `profiles.yml` file.

If you wish to split your models across multiple schemas, check out the docs on [using custom schemas](/docs/build/custom-schemas).

Note: on BigQuery, `dataset` is used interchangeably with `schema`.

Do I need to create my target schema before running dbt?

Nope! dbt will check if the schema exists when it runs. If the schema does not exist, dbt will create it for you.

If I rerun dbt, will there be any downtime as models are rebuilt?

Nope! The SQL that dbt generates behind the scenes ensures that any relations are replaced atomically (i.e. your business users won't experience any downtime).

The implementation of this varies on each warehouse, check out the [logs](/faqs/Runs/checking-logs) to see the SQL dbt is executing.

What happens if the SQL in my query is bad or I get a database error?

If there's a mistake in your SQL, dbt will return the error that your database returns.

```
$ dbt run --select customers  
Running with dbt=1.9.0  
Found 3 models, 9 tests, 0 snapshots, 0 analyses, 133 macros, 0 operations, 0 seed files, 0 sources  
  
14:04:12 | Concurrency: 1 threads (target='dev')  
14:04:12 |  
14:04:12 | 1 of 1 START view model dbt_alice.customers.......................... [RUN]  
14:04:13 | 1 of 1 ERROR creating view model dbt_alice.customers................. [ERROR in 0.81s]  
14:04:13 |  
14:04:13 | Finished running 1 view model in 1.68s.  
  
Completed with 1 error and 0 warnings:  
  
Database Error in model customers (models/customers.sql)  
  Syntax error: Expected ")" but got identifier `your-info-12345` at [13:15]  
  compiled SQL at target/run/jaffle_shop/customers.sql  
  
Done. PASS=0 WARN=0 ERROR=1 SKIP=0 TOTAL=1
```

Any models downstream of this model will also be skipped. Use the error message and the [compiled SQL](/faqs/Runs/checking-logs) to debug any errors.

Change the way your model is materialized[​](#change-the-way-your-model-is-materialized "Direct link to Change the way your model is materialized")
---------------------------------------------------------------------------------------------------------------------------------------------------

One of the most powerful features of dbt is that you can change the way a model is materialized in your warehouse, simply by changing a configuration value. You can change things between tables and views by changing a keyword rather than writing the data definition language (DDL) to do this behind the scenes.

By default, everything gets created as a view. You can override that at the directory level so everything in that directory will materialize to a different materialization.

1. Edit your `dbt_project.yml` file.

   * Update your project `name` to:

     dbt\_project.yml

     ```
     name: 'jaffle_shop'
     ```
   * Configure `jaffle_shop` so everything in it will be materialized as a table; and configure `example` so everything in it will be materialized as a view. Update your `models` config block to:

     dbt\_project.yml

     ```
     models:  
       jaffle_shop:  
         +materialized: table  
         example:  
           +materialized: view
     ```
   * Click **Save**.
2. Enter the `dbt run` command. Your `customers` model should now be built as a table!

   info

   To do this, dbt had to first run a `drop view` statement (or API call on BigQuery), then a `create table as` statement.
3. Edit `models/customers.sql` to override the `dbt_project.yml` for the `customers` model only by adding the following snippet to the top, and click **Save**:

   models/customers.sql

   ```
   {{  
     config(  
       materialized='view'  
     )  
   }}  
     
   with customers as (  
     
       select  
           id as customer_id  
           ...  
     
   )
   ```
4. Enter the `dbt run` command. Your model, `customers`, should now build as a view.

   * BigQuery users need to run `dbt run --full-refresh` instead of `dbt run` to full apply materialization changes.
5. Enter the `dbt run --full-refresh` command for this to take effect in your warehouse.

### FAQs[​](#faqs "Direct link to FAQs")

What materializations are available in dbt?

dbt ships with five materializations: `view`, `table`, `incremental`, `ephemeral` and `materialized_view`.
Check out the documentation on [materializations](/docs/build/materializations) for more information on each of these options.

You can also create your own [custom materializations](/guides/create-new-materializations), if required however this is an advanced feature of dbt.

Which materialization should I use for my model?

Start out with views, and then change models to tables when required for performance reasons (i.e. downstream queries have slowed).

Check out the [docs on materializations](/docs/build/materializations) for advice on when to use each materialization.

What model configurations exist?

You can also configure:

* [tags](/reference/resource-configs/tags) to support easy categorization and graph selection
* [custom schemas](/reference/resource-properties/schema) to split your models across multiple schemas
* [aliases](/reference/resource-configs/alias) if your view/table name should differ from the filename
* Snippets of SQL to run at the start or end of a model, known as [hooks](/docs/build/hooks-operations)
* Warehouse-specific configurations for performance (e.g. `sort` and `dist` keys on Redshift, `partitions` on BigQuery)

Check out the docs on [model configurations](/reference/model-configs) to learn more.

Delete the example models[​](#delete-the-example-models "Direct link to Delete the example models")
---------------------------------------------------------------------------------------------------

You can now delete the files that dbt created when you initialized the project:

1. Delete the `models/example/` directory.
2. Delete the `example:` key from your `dbt_project.yml` file, and any configurations that are listed under it.

   dbt\_project.yml

   ```
   # before  
   models:  
     jaffle_shop:  
       +materialized: table  
       example:  
         +materialized: view
   ```

   dbt\_project.yml

   ```
   # after  
   models:  
     jaffle_shop:  
       +materialized: table
   ```
3. Save your changes.

#### FAQs[​](#faqs "Direct link to FAQs")

How do I remove deleted models from my data warehouse?

If you delete a model from your dbt project, dbt does not automatically drop the relation from your schema. This means that you can end up with extra objects in schemas that dbt creates, which can be confusing to other users.

(This can also happen when you switch a model from being a view or table, to ephemeral)

When you remove models from your dbt project, you should manually drop the related relations from your schema.

I got an "unused model configurations" error message, what does this mean?

You might have forgotten to nest your configurations under your project name, or you might be trying to apply configurations to a directory that doesn't exist.

Check out this [article](https://discourse.getdbt.com/t/faq-i-got-an-unused-model-configurations-error-message-what-does-this-mean/112) to understand more.

Build models on top of other models[​](#build-models-on-top-of-other-models "Direct link to Build models on top of other models")
---------------------------------------------------------------------------------------------------------------------------------

As a best practice in SQL, you should separate logic that cleans up your data from logic that transforms your data. You have already started doing this in the existing query by using common table expressions (CTEs).

Now you can experiment by separating the logic out into separate models and using the [ref](/reference/dbt-jinja-functions/ref) function to build models on top of other models:

[![The DAG we want for our dbt project](/img/dbt-dag.png?v=2 "The DAG we want for our dbt project")](#)The DAG we want for our dbt project

1. Create a new SQL file, `models/stg_customers.sql`, with the SQL from the `customers` CTE in our original query.
2. Create a second new SQL file, `models/stg_orders.sql`, with the SQL from the `orders` CTE in our original query.

   models/stg\_customers.sql

   ```
   select  
       id as customer_id,  
       first_name,  
       last_name  
     
   from `dbt-tutorial`.jaffle_shop.customers
   ```

   models/stg\_orders.sql

   ```
   select  
       id as order_id,  
       user_id as customer_id,  
       order_date,  
       status  
     
   from `dbt-tutorial`.jaffle_shop.orders
   ```
3. Edit the SQL in your `models/customers.sql` file as follows:

   models/customers.sql

   ```
   with customers as (  
     
       select * from {{ ref('stg_customers') }}  
     
   ),  
     
   orders as (  
     
       select * from {{ ref('stg_orders') }}  
     
   ),  
     
   customer_orders as (  
     
       select  
           customer_id,  
     
           min(order_date) as first_order_date,  
           max(order_date) as most_recent_order_date,  
           count(order_id) as number_of_orders  
     
       from orders  
     
       group by 1  
     
   ),  
     
   final as (  
     
       select  
           customers.customer_id,  
           customers.first_name,  
           customers.last_name,  
           customer_orders.first_order_date,  
           customer_orders.most_recent_order_date,  
           coalesce(customer_orders.number_of_orders, 0) as number_of_orders  
     
       from customers  
     
       left join customer_orders using (customer_id)  
     
   )  
     
   select * from final
   ```
4. Execute `dbt run`.

   This time, when you performed a `dbt run`, separate views/tables were created for `stg_customers`, `stg_orders` and `customers`. dbt inferred the order to run these models. Because `customers` depends on `stg_customers` and `stg_orders`, dbt builds `customers` last. You do not need to explicitly define these dependencies.

Build models on top of sources[​](#build-models-on-top-of-sources "Direct link to Build models on top of sources")
------------------------------------------------------------------------------------------------------------------

Sources make it possible to name and describe the data loaded into your warehouse by your extract and load tools. By declaring these tables as sources in dbt, you can:

* select from source tables in your models using the `{{ source() }}` function, helping define the lineage of your data
* test your assumptions about your source data
* calculate the freshness of your source data

1. Create a new YML file `models/sources.yml`.
2. Declare the sources by copying the following into the file and clicking **Save**.

   models/sources.yml

   ```
   sources:  
       - name: jaffle_shop  
         description: This is a replica of the Postgres database used by our app  
         database: dbt-tutorial  
         schema: jaffle_shop  
         tables:  
             - name: customers  
               description: One record per customer.  
             - name: orders  
               description: One record per order. Includes cancelled and deleted orders.
   ```
3. Edit the `models/stg_customers.sql` file to select from the `customers` table in the `jaffle_shop` source.

   models/stg\_customers.sql

   ```
   select  
       id as customer_id,  
       first_name,  
       last_name  
     
   from {{ source('jaffle_shop', 'customers') }}
   ```
4. Edit the `models/stg_orders.sql` file to select from the `orders` table in the `jaffle_shop` source.

   models/stg\_orders.sql

   ```
   select  
       id as order_id,  
       user_id as customer_id,  
       order_date,  
       status  
     
   from {{ source('jaffle_shop', 'orders') }}
   ```
5. Execute `dbt run`.

   The results of your `dbt run` will be exactly the same as the previous step. Your `stg_customers` and `stg_orders`
   models will still query from the same raw data source in BigQuery. By using `source`, you can
   test and document your raw data and also understand the lineage of your sources.

#### FAQs[​](#faq-2 "Direct link to FAQs")

How do I run one model at a time?

To run one model, use the `--select` flag (or `-s` flag), followed by the name of the model:

```
$ dbt run --select customers
```

Check out the [model selection syntax documentation](/reference/node-selection/syntax) for more operators and examples.

Do ref-able resource names need to be unique?

Within one project: yes! To build dependencies between resources (such as models, seeds, and snapshots), you need to use the `ref` function, and pass in the resource name as an argument. dbt uses that resource name to uniquely resolve the `ref` to a specific resource. As a result, these resource names need to be unique, *even if they are in distinct folders*.

A resource in one project can have the same name as a resource in another project (installed as a dependency). dbt uses the project name to uniquely identify each resource. We call this "namespacing." If you `ref` a resource with a duplicated name, it will resolve to the resource within the same namespace (package or project), or raise an error because of an ambiguous reference. Use [two-argument `ref`](/reference/dbt-jinja-functions/ref#ref-project-specific-models) to disambiguate references by specifying the namespace.

Those resource will still need to land in distinct locations in the data warehouse. Read the docs on [custom aliases](/docs/build/custom-aliases) and [custom schemas](/docs/build/custom-schemas) for details on how to achieve this.

As I create more models, how should I keep my project organized? What should I name my models?

There's no one best way to structure a project! Every organization is unique.

If you're just getting started, check out how we (dbt Labs) [structure our dbt projects](/best-practices/how-we-structure/1-guide-overview).

Add tests to your models[​](#add-tests-to-your-models "Direct link to Add tests to your models")
------------------------------------------------------------------------------------------------

Adding [data tests](/docs/build/data-tests) to a project helps validate that your models are working correctly.

To add data tests to your project:

1. Create a new YAML file in the `models` directory, named `models/schema.yml`
2. Add the following contents to the file:

   models/schema.yml

   ```
   version: 2  
     
   models:  
     - name: customers  
       columns:  
         - name: customer_id  
           data_tests:  
             - unique  
             - not_null  
     
     - name: stg_customers  
       columns:  
         - name: customer_id  
           data_tests:  
             - unique  
             - not_null  
     
     - name: stg_orders  
       columns:  
         - name: order_id  
           data_tests:  
             - unique  
             - not_null  
         - name: status  
           data_tests:  
             - accepted_values:  
                 arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                   values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']  
         - name: customer_id  
           data_tests:  
             - not_null  
             - relationships:  
                 arguments:  
                   to: ref('stg_customers')  
                   field: customer_id
   ```
3. Run `dbt test`, and confirm that all your tests passed.

When you run `dbt test`, dbt iterates through your YAML files, and constructs a query for each test. Each query will return the number of records that fail the test. If this number is 0, then the test is successful.

#### FAQs[​](#faqs "Direct link to FAQs")

What tests are available for me to use in dbt? Can I add my own custom tests?

Out of the box, dbt ships with the following data tests:

* `unique`
* `not_null`
* `accepted_values`
* `relationships` (i.e. referential integrity)

You can also write your own [custom schema data tests](/docs/build/data-tests).

Some additional custom schema tests have been open-sourced in the [dbt-utils package](https://github.com/dbt-labs/dbt-utils?#generic-tests), check out the docs on [packages](/docs/build/packages) to learn how to make these tests available in your project.

Note that although you can't document data tests as of yet, we recommend checking out [this dbt Core discussion](https://github.com/dbt-labs/dbt-core/issues/2578) where the dbt community shares ideas.

How do I test one model at a time?

Running tests on one model looks very similar to running a model: use the `--select` flag (or `-s` flag), followed by the name of the model:

```
dbt test --select customers
```

Check out the [model selection syntax documentation](/reference/node-selection/syntax) for full syntax, and [test selection examples](/reference/node-selection/test-selection-examples) in particular.

One of my tests failed, how can I debug it?

To debug a failing test, find the SQL that dbt ran by:

* dbt:

  + Within the test output, click on the failed test, and then select "Details".
* dbt Core:

  + Open the file path returned as part of the error message.
  + Navigate to the `target/compiled/schema_tests` directory for all compiled test queries.

Copy the SQL into a query editor (in dbt, you can paste it into a new `Statement`), and run the query to find the records that failed.

Does my test file need to be named `schema.yml`?

No! You can name this file whatever you want (including `whatever_you_want.yml`), so long as:

* The file is in your `models/` directory¹
* The file has `.yml` extension

Check out the [docs](/reference/configs-and-properties) for more information.

¹If you're declaring properties for seeds, snapshots, or macros, you can also place this file in the related directory — `seeds/`, `snapshots/` and `macros/` respectively.

Why do model and source YAML files always start with `version: 2`?

Once upon a time, the structure of these `.yml` files was very different (s/o to anyone who was using dbt back then!). Adding `version: 2` allowed us to make this structure more extensible.

From [dbt Core v1.5](/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.5#quick-hits), the top-level `version:` key is optional in all resource YAML files. If present, only `version: 2` is supported.

Also starting in v1.5, both the [`config-version: 2`](/reference/project-configs/config-version) and the top-level `version:` key in the `dbt_project.yml` are optional.

Resource YAML files do not currently require this config. We only support `version: 2` if it's specified. Although we do not expect to update YAML files to `version: 3` soon, having this config will make it easier for us to introduce new structures in the future

What data tests should I add to my project?

We recommend that every model has a data test on a primary key, that is, a column that is `unique` and `not_null`.

We also recommend that you test any assumptions on your source data. For example, if you believe that your payments can only be one of three payment methods, you should test that assumption regularly — a new payment method may introduce logic errors in your SQL.

In advanced dbt projects, we recommend using [sources](/docs/build/sources) and running these source data-integrity tests against the sources rather than models.

When should I run my data tests?

You should run your data tests whenever you are writing new code (to ensure you haven't broken any existing models by changing SQL), and whenever you run your transformations in production (to ensure that your assumptions about your source data are still valid).

Document your models[​](#document-your-models "Direct link to Document your models")
------------------------------------------------------------------------------------

Adding [documentation](/docs/build/documentation) to your project allows you to describe your models in rich detail, and share that information with your team. Here, we're going to add some basic documentation to our project.

1. Update your `models/schema.yml` file to include some descriptions, such as those below.

   models/schema.yml

   ```
   version: 2  
     
   models:  
     - name: customers  
       description: One record per customer  
       columns:  
         - name: customer_id  
           description: Primary key  
           data_tests:  
             - unique  
             - not_null  
         - name: first_order_date  
           description: NULL when a customer has not yet placed an order.  
     
     - name: stg_customers  
       description: This model cleans up customer data  
       columns:  
         - name: customer_id  
           description: Primary key  
           data_tests:  
             - unique  
             - not_null  
     
     - name: stg_orders  
       description: This model cleans up order data  
       columns:  
         - name: order_id  
           description: Primary key  
           data_tests:  
             - unique  
             - not_null  
         - name: status  
           data_tests:  
             - accepted_values:  
                 arguments: # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.  
                   values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']  
         - name: customer_id  
           data_tests:  
             - not_null  
             - relationships:  
                 arguments:  
                   to: ref('stg_customers')  
                   field: customer_id
   ```
2. Run `dbt docs generate` to generate the documentation for your project. dbt introspects your project and your warehouse to generate a JSON file with rich documentation about your project.

3. Click the book icon in the Develop interface to launch documentation in a new tab.

#### FAQs[​](#faqs "Direct link to FAQs")

How do I write long-form explanations in my descriptions?

If you need more than a sentence to explain a model, you can:

1. Split your description over multiple lines using `>`. Interior line breaks are removed and Markdown can be used. This method is recommended for simple, single-paragraph descriptions:

```
  version: 2  
  
  models:  
  - name: customers  
    description: >  
      Lorem ipsum **dolor** sit amet, consectetur adipisicing elit, sed do eiusmod  
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,  
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo  
      consequat.
```

2. Split your description over multiple lines using `|`. Interior line breaks are maintained and Markdown can be used. This method is recommended for more complex descriptions:

```
  version: 2  
  
  models:  
  - name: customers  
    description: |  
      ### Lorem ipsum  
  
      * dolor sit amet, consectetur adipisicing elit, sed do eiusmod  
      * tempor incididunt ut labore et dolore magna aliqua.
```

3. Use a [docs block](/docs/build/documentation#using-docs-blocks) to write the description in a separate Markdown file.

How do I access documentation in dbt Catalog?

If you're using dbt to deploy your project and have a [Starter, Enterprise, or Enterprise+ plan](https://www.getdbt.com/pricing/), you can use Catalog to view your project's [resources](/docs/build/projects) (such as models, tests, and metrics) and their lineage to gain a better understanding of its latest production state.

Access Catalog in dbt by clicking the **Explore** link in the navigation. You can have up to 5 read-only users access the documentation for your project.

dbt developer plan and dbt Core users can use [dbt Docs](/docs/explore/build-and-view-your-docs#dbt-docs), which generates basic documentation but it doesn't offer the same speed, metadata, or visibility as Catalog.

Commit your changes[​](#commit-your-changes "Direct link to Commit your changes")
---------------------------------------------------------------------------------

Now that you've built your customer model, you need to commit the changes you made to the project so that the repository has your latest code.

**If you edited directly in the protected primary branch:**

1. Click the **Commit and sync git** button. This action prepares your changes for commit.
2. A modal titled **Commit to a new branch** will appear.
3. In the modal window, name your new branch `add-customers-model`. This branches off from your primary branch with your new changes.
4. Add a commit message, such as "Add customers model, tests, docs" and and commit your changes.
5. Click **Merge this branch to main** to add these changes to the main branch on your repo.

**If you created a new branch before editing:**

1. Since you already branched out of the primary protected branch, go to **Version Control** on the left.
2. Click **Commit and sync** to add a message.
3. Add a commit message, such as "Add customers model, tests, docs."
4. Click **Merge this branch to main** to add these changes to the main branch on your repo.

Deploy dbt[​](#deploy-dbt "Direct link to Deploy dbt")
------------------------------------------------------

Use dbt's Scheduler to deploy your production jobs confidently and build observability into your processes. You'll learn to create a deployment environment and run a job in the following steps.

### Create a deployment environment[​](#create-a-deployment-environment "Direct link to Create a deployment environment")

1. From the main menu, go to **Orchestration** > **Environments**.
2. Click **Create environment**.
3. In the **Name** field, write the name of your deployment environment. For example, "Production."
4. In the **dbt Version** field, select the latest version from the dropdown.
5. Under **Deployment connection**, enter the name of the dataset you want to use as the target, such as "Analytics". This will allow dbt to build and work with that dataset. For some data warehouses, the target dataset may be referred to as a "schema".
6. Click **Save**.

### Create and run a job[​](#create-and-run-a-job "Direct link to Create and run a job")

Jobs are a set of dbt commands that you want to run on a schedule. For example, `dbt build`.

As the `jaffle_shop` business gains more customers, and those customers create more orders, you will see more records added to your source data. Because you materialized the `customers` model as a table, you'll need to periodically rebuild your table to ensure that the data stays up-to-date. This update will happen when you run a job.

1. After creating your deployment environment, you should be directed to the page for a new environment. If not, select **Orchestration** from the main menu, then click **Jobs**.
2. Click **Create job** > **Deploy job**.
3. Provide a job name (for example, "Production run") and select the environment you just created.
4. Scroll down to the **Execution settings** section.
5. Under **Commands**, add this command as part of your job if you don't see it:
   * `dbt build`
6. Select the **Generate docs on run** option to automatically [generate updated project docs](/docs/explore/build-and-view-your-docs) each time your job runs.
7. For this exercise, do *not* set a schedule for your project to run — while your organization's project should run regularly, there's no need to run this example project on a schedule. Scheduling a job is sometimes referred to as *deploying a project*.
8. Click **Save**, then click **Run now** to run your job.
9. Click the run and watch its progress under **Run summary**.
10. Once the run is complete, click **View Documentation** to see the docs for your project.

Congratulations 🎉! You've just deployed your first dbt project!

#### FAQs[​](#faqs "Direct link to FAQs")

What happens if one of my runs fails?

If you're using dbt, we recommend setting up email and Slack notifications (`Account Settings > Notifications`) for any failed runs. Then, debug these runs the same way you would debug any runs in development.

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [BigQuery](/tags/big-query)
* [platform](/tags/platform)
* [Quickstart](/tags/quickstart)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/guides/bigquery-qs.md)

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