# Source: https://docs.getdbt.com/reference/resource-properties/versions

versions | dbt Developer Hub

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

    - [anchors](/reference/resource-properties/anchors)
    - [columns](/reference/resource-properties/columns)
    - [config](/reference/resource-properties/config)
    - [constraints](/reference/resource-properties/constraints)
    - [deprecation\_date](/reference/resource-properties/deprecation_date)
    - [description](/reference/resource-properties/description)
    - [latest\_version](/reference/resource-properties/latest_version)
    - [Data tests](/reference/resource-properties/data-tests)
    - [versions](/reference/resource-properties/versions)
  + [General configs](/category/general-configs)
  + [For models](/reference/model-properties)
  + [For seeds](/reference/seed-properties)
  + [For snapshots](/reference/snapshot-properties)
  + [For data tests](/reference/data-test-configs)
  + [For unit tests](/reference/resource-properties/unit-tests)
  + [For sources](/reference/source-properties)
  + [For analyses](/reference/analysis-properties)
  + [For exposures](/reference/exposure-properties)
  + [For macros](/reference/macro-properties)
  + [For functions](/reference/function-properties)
* [Commands](/reference/dbt-commands)
* [Jinja reference](/category/jinja-reference)
* [dbt Artifacts](/reference/artifacts/dbt-artifacts)
* [Database Permissions](/reference/database-permissions/about-database-permissions)

* [Resource configs and properties](/reference/resource-configs/resource-path)
* [General properties](/category/general-properties)
* versions

Copy page

On this page

versions
========

Model versions, dbt\_project.yml versions, and .yml versions

Take note that [model versions](/docs/mesh/govern/model-versions) are different from [dbt\_project.yml versions](/reference/project-configs/version#dbt_projectyml-versions) and [.yml property file versions](/reference/project-configs/version#yml-property-file-versions).

Model versions is a *feature* that enables better governance and data model management by allowing you to track changes and updates to models over time. dbt\_project.yml versions refer to the compatibility of the dbt project with a specific version of dbt. Version numbers within .yml property files inform how dbt parses those YAML files. The latter two are completely optional starting from dbt v1.5.

models/<schema>.yml

```
models:  
  - name: model_name  
    versions:  
      - v: <version_identifier> # required  
        defined_in: <file_name> # optional -- default is <model_name>_v<v>  
        columns:  
          # specify all columns, or include/exclude columns from the top-level model YAML definition  
          - include: <include_value>  
            exclude: <exclude_list>  
          # specify additional columns  
          - name: <column_name> # required  
      - v: ...  
      
    # optional  
    latest_version: <version_identifier>
```

The standard convention for naming model versions is `<model_name>_v<v>`. This holds for the file where dbt expects to find the model's definition (SQL or Python), and the alias it will use by default when materializing the model in the database.

### `v`[​](#v "Direct link to v")

The version identifier for a version of a model. This value can be numeric (integer or float), or any string.

The value of the version identifier is used to order versions of a model relative to one another. If a versioned model does *not* explicitly configure a [`latest_version`](/reference/resource-properties/latest_version), the highest version number is used as the latest version to resolve `ref` calls to the model without a `version` argument.

In general, we recommend that you use a simple "major versioning" scheme for your models: `1`, `2`, `3`, and so on, where each version reflects a breaking change from previous versions. You are able to use other versioning schemes. dbt will sort your version identifiers alphabetically if the values are not all numeric. You should **not** include the letter `v` in the version identifier, as dbt will do that for you.

To run a model with multiple versions, you can use the [`--select` flag](/reference/node-selection/syntax). Refer to [Model versions](/docs/mesh/govern/model-versions#run-a-model-with-multiple-versions) for more information and syntax.

### `defined_in`[​](#defined_in "Direct link to defined_in")

The name of the model file (excluding the file extension, e.g. `.sql` or `.py`) where the model version is defined.

If `defined_in` is not specified, dbt searches for the definition of a versioned model in a model file named `<model_name>_v<v>`. The **latest** version of a model may also be defined in a file named `<model_name>`, without the version suffix. Model file names must be globally unique, even when defining versioned implementations of a model with a different name.

### `alias`[​](#alias "Direct link to alias")

The default resolved `alias` for a versioned model is `<model_name>_v<v>`. The logic for this is encoded in the `generate_alias_name` macro.

This default can be overwritten in two ways:

* Configuring a custom `alias` within the version yaml, or the versioned model's definition
* Overwriting dbt's `generate_alias_name` macro, to use different behavior based on `node.version`

See ["Custom aliases"](/docs/build/custom-aliases) for more details.

Note that the value of `defined_in` and the `alias` configuration of a model are not coordinated, except by convention. The two are declared and determined independently.

### `include`[​](#include "Direct link to include")

The specification of which columns are defined in a model's top-level `columns` property to include or exclude in a versioned implementation of that model.

* `include` is either:
  + a list of specific column names to include
  + `'*'` or `'all'`, indicating that **all** columns from the top-level `columns` property should be included in the versioned model
* `exclude` is a list of column names to exclude. It can only be declared if `include` is set to one of `'*'` or `'all'`.

tip

Not to be confused with the `--select/--exclude` [syntax](/reference/node-selection/exclude), which is used for model selection.

The `columns` list of a versioned model can have *at most one* `include/exclude` element. However, if none of your model versions specify columns, you don't need to define columns at all and can omit the `columns/include`/`exclude` keys from the versioned model. In this case, dbt will automatically use all top-level columns for all versions.

You may declare additional columns within the version's `columns` list. If a version-specific column's `name` matches a column included from the top level, the version-specific entry will override that column for that version.

models/<schema>.yml

```
models:  
    
  # top-level model properties  
  - name: <model_name>  
    columns:  
      - name: <column_name> # required  
      
    # versions of this model  
    versions:  
      - v: <version_identifier> # required  
        columns:  
          - include: '*' | 'all' | [<column_name>, ...]  
            exclude:  
              - <column_name>  
              - ... # declare additional column names to exclude  
            
          # declare more columns -- can be overrides from top-level, or in addition  
          - name: <column_name>  
            ...
```

By default, `include` is "all", and `exclude` is the empty list. This has the effect of including all columns from the base model in the versioned model.

#### Example[​](#example "Direct link to Example")

models/customers.yml

```
models:  
  - name: customers  
    columns:  
      - name: customer_id  
        description: Unique identifier for this table  
        data_type: text  
        constraints:  
          - type: not_null  
        data_tests:  
          - unique  
      - name: customer_country  
        data_type: text  
        description: "Country where the customer currently lives"  
      - name: first_purchase_date  
        data_type: date  
      
    versions:  
      - v: 4  
        
      - v: 3  
        columns:  
          - include: "*"  
          - name: customer_country  
            data_type: text  
            description: "Country where the customer first lived at time of first purchase"  
        
      - v: 2  
        columns:  
          - include: "*"  
            exclude:  
              - customer_country  
        
      - v: 1  
        columns:  
          - include: []  
          - name: id  
            data_type: int
```

Because `v4` has not specified any `columns`, it will include all of the top-level `columns`.

Each other version has declared a modification from the top-level property:

* `v3` will include all columns, but it reimplements the `customer_country` column with a different `description`.
* `v2` will include all columns *except* `customer_country`.
* `v1` doesn't include *any* of the top-level `columns`. Instead, it declares only a single integer column named `id`.

### Our recommendations[​](#our-recommendations "Direct link to Our recommendations")

* Follow a consistent naming convention for model versions and aliases.
* Use `defined_in` and `alias` only if you have good reason.
* Create a view that always points to the latest version of your model. You can automate this for all versioned models in your project with an `on-run-end` hook. For more details, read the full docs on ["Model versions"](/docs/mesh/govern/model-versions#configuring-database-location-with-alias)

### Detecting breaking changes[​](#detecting-breaking-changes "Direct link to Detecting breaking changes")

When you use the `state:modified` selection method in Slim CI, dbt will detect changes to versioned model contracts, and raise an error if any of those changes could be breaking for downstream consumers.

Breaking changes include:

* Removing an existing column
* Changing the data\_type of an existing column
* Removing or modifying one of the `constraints` on an existing column (dbt v1.6 or higher)
* Changing unversioned, contracted models.
  + dbt also warns if a model has or had a contract but isn't versioned.

* Example message for unversioned models
* Example message for versioned models

```
  Breaking Change to Unversioned Contract for contracted_model (models/contracted_models/contracted_model.sql)  
  While comparing to previous project state, dbt detected a breaking change to an unversioned model.  
    - Contract enforcement was removed: Previously, this model's configuration included contract: {enforced: true}. It is no longer configured to enforce its contract, and this is a breaking change.  
    - Columns were removed:  
      - color  
      - date_day  
    - Enforced column level constraints were removed:  
      - id (ConstraintType.not_null)  
      - id (ConstraintType.primary_key)  
    - Enforced model level constraints were removed:  
      - ConstraintType.check -> ['id']  
    - Materialization changed with enforced constraints:  
      - table -> view
```

```
Breaking Change to Contract Error in model sometable (models/sometable.sql)  
  While comparing to previous project state, dbt detected a breaking change to an enforced contract.  
  
  The contract's enforcement has been disabled.  
  
  Columns were removed:  
   - order_name  
  
  Columns with data_type changes:  
   - order_id (number -> int)  
  
  Consider making an additive (non-breaking) change instead, if possible.  
  Otherwise, create a new model version: https://docs.getdbt.com/docs/mesh/govern/model-versions
```

Additive changes are **not** considered breaking:

* Adding a new column to a contracted model
* Adding new `constraints` to an existing column in a contracted model

Was this page helpful?
----------------------

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-properties/versions.md)

Last updated on **Nov 19, 2025**

[Previous

Data tests](/reference/resource-properties/data-tests)[Next

General configs](/category/general-configs)

* [`v`](#v)
* [`defined_in`](#defined_in)
* [`alias`](#alias)
* [`include`](#include)
* [Our recommendations](#our-recommendations)
* [Detecting breaking changes](#detecting-breaking-changes)

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/reference/resource-properties/versions.md)

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