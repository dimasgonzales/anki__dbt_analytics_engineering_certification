# Source: https://docs.getdbt.com/guides/manual-install

Quickstart for dbt Core from a manual install | dbt Developer Hub

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

Quickstart for dbt Core from a manual install
=============================================

[Back to guides](/guides)

dbt Core

Quickstart

Beginner

Menu

* 1 Introduction​
* 2 Create a repository​
* 3 Create a project​
* 4 Connect to BigQuery​
* 5 Perform your first dbt run​
* 6 Commit your changes​
* 7 Checkout a new git branch​
* 8 Build your first model​
* 9 Change the way your model is materialized​
* 10 Delete the example models​
* 11 Build models on top of other models​
* 12 Add tests to your models​
* 13 Document your models​
* 14 Commit updated changes​
* 15 Schedule a job​

Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

When you use dbt Core to work with dbt, you will be editing files locally using a code editor, and running projects using a command line interface (CLI).

If you want to edit files and run projects using the web-based dbt Integrated Development Environment (Studio IDE), refer to the [dbt quickstarts](/guides). You can also develop and run dbt commands using the [dbt CLI](/docs/cloud/cloud-cli-installation) — a dbt powered command line.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* To use dbt Core, it's important that you know some basics of the Terminal. In particular, you should understand `cd`, `ls` and `pwd` to navigate through the directory structure of your computer easily.
* Install dbt Core using the [installation instructions](/docs/core/installation-overview) for your operating system.
* Complete appropriate Setting up and Loading data steps in the Quickstart for dbt series. For example, for BigQuery, complete [Setting up (in BigQuery)](/guides/bigquery?step=2) and [Loading data (BigQuery)](/guides/bigquery?step=3).
* [Create a GitHub account](https://github.com/join) if you don't already have one.

### Create a starter project[​](#create-a-starter-project "Direct link to Create a starter project")

After setting up BigQuery to work with dbt, you are ready to create a starter project with example models, before building your own models.

BackNext

Create a repository[​](#create-a-repository "Direct link to Create a repository")
---------------------------------------------------------------------------------

The following steps use [GitHub](https://github.com/) as the Git provider for this guide, but you can use any Git provider. You should have already [created a GitHub account](https://github.com/join).

1. [Create a new GitHub repository](https://github.com/new) named `dbt-tutorial`.
2. Select one of the following (You can always change this setting later):

   * **Private (recommended):** To secure your environment and prevent private information (like credentials) from being public.
   * **Public:** If you need to easily collaborate and share with others, especially outside of your organization.
3. Leave the default values for all other settings.
4. Click **Create repository**.
5. Save the commands from "…or create a new repository on the command line" to use later in [Commit your changes](/guides/manual-install?step=6).

BackNext

Create a project[​](#create-a-project "Direct link to Create a project")
------------------------------------------------------------------------

Learn how to use a series of commands using the command line of the Terminal to create your project. dbt Core includes an `init` command that helps scaffold a dbt project.

To create your dbt project:

1. Make sure you have dbt Core installed and check the version using the `dbt --version` command:

```
dbt --version
```

2. Initiate the `jaffle_shop` project using the `init` command:

```
dbt init jaffle_shop
```

3. Navigate into your project's directory:

```
cd jaffle_shop
```

4. Use `pwd` to confirm that you are in the right spot:

```
$ pwd  
> Users/BBaggins/dbt-tutorial/jaffle_shop
```

5. Use a code editor like Atom or VSCode to open the project directory you created in the previous steps, which we named jaffle\_shop. The content includes folders and `.sql` and `.yml` files generated by the `init` command.

[![The starter project in a code editor](/img/starter-project-dbt-cli.png?v=2 "The starter project in a code editor")](#)The starter project in a code editor

6. dbt provides the following values in the `dbt_project.yml` file:

dbt\_project.yml

```
name: jaffle_shop # Change from the default, `my_new_project`  
  
...  
  
profile: jaffle_shop # Change from the default profile name, `default`  
  
...  
  
models:  
    jaffle_shop: # Change from `my_new_project` to match the previous value for `name:`  
    ...
```

BackNext

Connect to BigQuery[​](#connect-to-bigquery "Direct link to Connect to BigQuery")
---------------------------------------------------------------------------------

When developing locally, dbt connects to your data warehouseA data warehouse is a data management system used for data storage and computing that allows for analytics activities such as transforming and sharing data. using a [profile](/docs/core/connect-data-platform/connection-profiles), which is a YAML file with all the connection details to your warehouse.

1. Create a file in the `~/.dbt/` directory named `profiles.yml`.
2. Move your BigQuery keyfile into this directory.
3. Copy the following and paste into the new profiles.yml file. Make sure you update the values where noted.

profiles.yml

```
jaffle_shop: # this needs to match the profile in your dbt_project.yml file  
    target: dev  
    outputs:  
        dev:  
            type: bigquery  
            method: service-account  
            keyfile: /Users/BBaggins/.dbt/dbt-tutorial-project-331118.json # replace this with the full path to your keyfile  
            project: grand-highway-265418 # Replace this with your project id  
            dataset: dbt_bbagins # Replace this with dbt_your_name, e.g. dbt_bilbo  
            threads: 1  
            timeout_seconds: 300  
            location: US  
            priority: interactive
```

4. Run the `debug` command from your project to confirm that you can successfully connect:

```
$ dbt debug  
> Connection test: OK connection ok
```

[![A successful dbt debug command](/img/successful-dbt-debug.png?v=2 "A successful dbt debug command")](#)A successful dbt debug command

### FAQs[​](#faqs "Direct link to FAQs")

My data team uses a different data warehouse. What should my profiles.yml file look like for my warehouse?

The structure of a profile looks different on each warehouse. Check out the [Supported Data Platforms](/docs/supported-data-platforms) page, and navigate to the `Profile Setup` section for your warehouse.

Why are profiles stored outside of my project?

Profiles are stored separately to dbt projects to avoid checking credentials into version control. Database credentials are extremely sensitive information and should **never be checked into version control**.

What should I name my profile?

We typically use a company name for a profile name, and then use targets to differentiate between `dev` and `prod`. Check out the docs on [environments in dbt Core](/docs/core/dbt-core-environments) for more information.

What should I name my target?

We typically use targets to differentiate between development and production runs of dbt, naming the targets `dev` and `prod`, respectively. Check out the docs on [managing environments in dbt Core](/docs/core/dbt-core-environments) for more information.

Can I use environment variables in my profile?

Yes! Check out the docs on [environment variables](/reference/dbt-jinja-functions/env_var) for more information.

BackNext

Perform your first dbt run[​](#perform-your-first-dbt-run "Direct link to Perform your first dbt run")
------------------------------------------------------------------------------------------------------

Our sample project has some example models in it. We're going to check that we can run them to confirm everything is in order.

1. Enter the `run` command to build example models:

```
dbt run
```

You should have an output that looks like this:

[![A successful dbt run command](/img/successful-dbt-run.png?v=2 "A successful dbt run command")](#)A successful dbt run command

BackNext

Commit your changes[​](#commit-your-changes "Direct link to Commit your changes")
---------------------------------------------------------------------------------

Commit your changes so that the repository contains the latest code.

1. Link the GitHub repository you created to your dbt project by running the following commands in Terminal. Make sure you use the correct git URL for your repository, which you should have saved from step 5 in [Create a repository](/guides/manual-install?step=2).

```
git init  
git branch -M main  
git add .  
git commit -m "Create a dbt project"  
git remote add origin https://github.com/USERNAME/dbt-tutorial.git  
git push -u origin main
```

2. Return to your GitHub repository to verify your new files have been added.

### Build your first models[​](#build-your-first-models "Direct link to Build your first models")

Now that you set up your sample project, you can get to the fun part — [building models](/docs/build/sql-models)!
In the next steps, you will take a sample query and turn it into a model in your dbt project.

BackNext

Checkout a new git branch[​](#checkout-a-new-git-branch "Direct link to Checkout a new git branch")
---------------------------------------------------------------------------------------------------

Check out a new git branch to work on new code:

1. Create a new branch by using the `checkout` command and passing the `-b` flag:

```
$ git checkout -b add-customers-model  
>  Switched to a new branch `add-customer-model`
```

BackNext

Build your first model[​](#build-your-first-model "Direct link to Build your first model")
------------------------------------------------------------------------------------------

1. Open your project in your favorite code editor.
2. Create a new SQL file in the `models` directory, named `models/customers.sql`.
3. Paste the following query into the `models/customers.sql` file.

* BigQuery
* Databricks
* Redshift
* Snowflake

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

```
with customers as (  
  
    select  
        id as customer_id,  
        first_name,  
        last_name  
  
    from jaffle_shop_customers  
  
),  
  
orders as (  
  
    select  
        id as order_id,  
        user_id as customer_id,  
        order_date,  
        status  
  
    from jaffle_shop_orders  
  
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

```
with customers as (  
  
    select  
        id as customer_id,  
        first_name,  
        last_name  
  
    from jaffle_shop.customers  
  
),  
  
orders as (  
  
    select  
        id as order_id,  
        user_id as customer_id,  
        order_date,  
        status  
  
    from jaffle_shop.orders  
  
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

```
with customers as (  
  
    select  
        id as customer_id,  
        first_name,  
        last_name  
  
    from raw.jaffle_shop.customers  
  
),  
  
orders as (  
  
    select  
        id as order_id,  
        user_id as customer_id,  
        order_date,  
        status  
  
    from raw.jaffle_shop.orders  
  
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

4. From the command line, enter `dbt run`.

[![A successful run with the dbt Core CLI](/img/first-model-dbt-cli.png?v=2 "A successful run with the dbt Core CLI")](#)A successful run with the dbt Core CLI

When you return to the BigQuery console, you can `select` from this model.

### FAQs[​](#faqs-1 "Direct link to FAQs")

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

BackNext

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

dbt ships with five materializationsThe exact Data Definition Language (DDL) that dbt will use when creating the model’s equivalent in a data warehouse.: `view`, `table`, `incremental`, `ephemeral` and `materialized_view`.
Check out the documentation on [materializations](/docs/build/materializations) for more information on each of these options.

You can also create your own [custom materializations](/guides/create-new-materializations), if required however this is an advanced feature of dbt.

Which materialization should I use for my model?

Start out with viewsA view (as opposed to a table) is a defined passthrough SQL query that can be run against a database (or data warehouse)., and then change models to tables when required for performance reasons (i.e. downstream queries have slowed).

Check out the [docs on materializations](/docs/build/materializations) for advice on when to use each materializationThe exact Data Definition Language (DDL) that dbt will use when creating the model’s equivalent in a data warehouse..

What model configurations exist?

You can also configure:

* [tags](/reference/resource-configs/tags) to support easy categorization and graph selection
* [custom schemas](/reference/resource-properties/schema) to split your models across multiple schemas
* [aliases](/reference/resource-configs/alias) if your viewA view (as opposed to a table) is a defined passthrough SQL query that can be run against a database (or data warehouse)./tableIn simplest terms, a table is the direct storage of data in rows and columns. Think excel sheet with raw values in each of the cells. name should differ from the filename
* Snippets of SQL to run at the start or end of a model, known as [hooks](/docs/build/hooks-operations)
* Warehouse-specific configurations for performance (e.g. `sort` and `dist` keys on Redshift, `partitions` on BigQuery)

Check out the docs on [model configurations](/reference/model-configs) to learn more.

BackNext

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

(This can also happen when you switch a model from being a viewA view (as opposed to a table) is a defined passthrough SQL query that can be run against a database (or data warehouse). or tableIn simplest terms, a table is the direct storage of data in rows and columns. Think excel sheet with raw values in each of the cells., to ephemeral)

When you remove models from your dbt project, you should manually drop the related relations from your schema.

I got an "unused model configurations" error message, what does this mean?

You might have forgotten to nest your configurations under your project name, or you might be trying to apply configurations to a directory that doesn't exist.

Check out this [article](https://discourse.getdbt.com/t/faq-i-got-an-unused-model-configurations-error-message-what-does-this-mean/112) to understand more.

BackNext

Build models on top of other models[​](#build-models-on-top-of-other-models "Direct link to Build models on top of other models")
---------------------------------------------------------------------------------------------------------------------------------

As a best practice in SQL, you should separate logic that cleans up your data from logic that transforms your data. You have already started doing this in the existing query by using common table expressions (CTEs).

Now you can experiment by separating the logic out into separate models and using the [ref](/reference/dbt-jinja-functions/ref) function to build models on top of other models:

[![The DAG we want for our dbt project](/img/dbt-dag.png?v=2 "The DAG we want for our dbt project")](#)The DAG we want for our dbt project

1. Create a new SQL file, `models/stg_customers.sql`, with the SQL from the `customers` CTE in our original query.
2. Create a second new SQL file, `models/stg_orders.sql`, with the SQL from the `orders` CTE in our original query.

* BigQuery
* Databricks
* Redshift
* Snowflake

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

models/stg\_customers.sql

```
select  
    id as customer_id,  
    first_name,  
    last_name  
  
from jaffle_shop_customers
```

models/stg\_orders.sql

```
select  
    id as order_id,  
    user_id as customer_id,  
    order_date,  
    status  
  
from jaffle_shop_orders
```

models/stg\_customers.sql

```
select  
    id as customer_id,  
    first_name,  
    last_name  
  
from jaffle_shop.customers
```

models/stg\_orders.sql

```
select  
    id as order_id,  
    user_id as customer_id,  
    order_date,  
    status  
  
from jaffle_shop.orders
```

models/stg\_customers.sql

```
select  
    id as customer_id,  
    first_name,  
    last_name  
  
from raw.jaffle_shop.customers
```

models/stg\_orders.sql

```
select  
    id as order_id,  
    user_id as customer_id,  
    order_date,  
    status  
  
from raw.jaffle_shop.orders
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

### FAQs[​](#faq-2 "Direct link to FAQs")

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

### Next steps[​](#next-steps "Direct link to Next steps")

Before moving on from building your first models, make a change and see how it affects your results:

* Write some bad SQL to cause an error — can you debug the error?
* Run only a single model at a time. For more information, see [Syntax overview](/reference/node-selection/syntax).
* Group your models with a `stg_` prefix into a `staging` subdirectory. For example, `models/staging/stg_customers.sql`.
  + Configure your `staging` models to be views.
  + Run only the `staging` models.

You can also explore:

* The `target` directory to see all of the compiled SQL. The `run` directory shows the create or replace table statements that are running, which are the select statements wrapped in the correct DDL.
* The `logs` file to see how dbt Core logs all of the action happening within your project. It shows the select statements that are running and the python logging happening when dbt runs.

BackNext

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

We recommend that every model has a data test on a primary keyA primary key is a non-null column in a database object that uniquely identifies each row., that is, a column that is `unique` and `not_null`.

We also recommend that you test any assumptions on your source data. For example, if you believe that your payments can only be one of three payment methods, you should test that assumption regularly — a new payment method may introduce logic errors in your SQL.

In advanced dbt projects, we recommend using [sources](/docs/build/sources) and running these source data-integrity tests against the sources rather than models.

When should I run my data tests?

You should run your data tests whenever you are writing new code (to ensure you haven't broken any existing models by changing SQL), and whenever you run your transformations in production (to ensure that your assumptions about your source data are still valid).

BackNext

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
2. Run `dbt docs generate` to generate the documentation for your project. dbt introspects your project and your warehouse to generate a JSONJSON (JavaScript Object Notation) is a minimal format for semi-structured data used to capture relationships between fields and values. file with rich documentation about your project.

3. Run `dbt docs serve` command to launch the documentation in a local website.

#### FAQs[​](#faqs-2 "Direct link to FAQs")

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

If you're using dbt to deploy your project and have a [Starter, Enterprise, or Enterprise+ plan](https://www.getdbt.com/pricing/), you can use Catalog to view your project's [resources](/docs/build/projects) (such as models, tests, and metrics) and their lineageData lineage provides a holistic view of how data moves through an organization, where it’s transformed and consumed. to gain a better understanding of its latest production state.

Access Catalog in dbt by clicking the **Explore** link in the navigation. You can have up to 5 read-only users access the documentation for your project.

dbt developer plan and dbt Core users can use [dbt Docs](/docs/explore/build-and-view-your-docs#dbt-docs), which generates basic documentation but it doesn't offer the same speed, metadata, or visibility as Catalog.

#### Next steps[​](#next-steps-1 "Direct link to Next steps")

Before moving on from testing, make a change and see how it affects your results:

* Write a test that fails, for example, omit one of the order statuses in the `accepted_values` list. What does a failing test look like? Can you debug the failure?
* Run the tests for one model only. If you grouped your `stg_` models into a directory, try running the tests for all the models in that directory.
* Use a [docs block](/docs/build/documentation#using-docs-blocks) to add a Markdown description to a model.

BackNext

Commit updated changes[​](#commit-updated-changes "Direct link to Commit updated changes")
------------------------------------------------------------------------------------------

You need to commit the changes you made to the project so that the repository has your latest code.

1. Add all your changes to git: `git add -A`
2. Commit your changes: `git commit -m "Add customers model, tests, docs"`
3. Push your changes to your repository: `git push`
4. Navigate to your repository, and open a pull request to merge the code into your master branch.

BackNext

Schedule a job[​](#schedule-a-job "Direct link to Schedule a job")
------------------------------------------------------------------

We recommend using dbt as the easiest and most reliable way to [deploy jobs](/docs/deploy/deployments) and automate your dbt project in production.

For more info on how to get started, refer to [create and schedule jobs](/docs/deploy/deploy-jobs#create-and-schedule-jobs).

[![Overview of a dbt job run, which includes the job run details, trigger type, commit SHA, environment name, detailed run steps, logs, and more.](/img/docs/dbt-cloud/deployment/run-overview.png?v=2 "Overview of a dbt job run, which includes the job run details, trigger type, commit SHA, environment name, detailed run steps, logs, and more.")](#)Overview of a dbt job run, which includes the job run details, trigger type, commit SHA, environment name, detailed run steps, logs, and more.

For more information about using dbt Core to schedule a job, refer [dbt airflow](/blog/dbt-airflow-spiritual-alignment) blog post.

BackNext

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

**Tags:**

* [dbt Core](/tags/dbt-core)
* [Quickstart](/tags/quickstart)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/guides/manual-install-qs.md)

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