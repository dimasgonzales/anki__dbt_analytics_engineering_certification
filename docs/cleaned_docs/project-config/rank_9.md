Copy page

On this page

version
=======

Model versions, dbt\_project.yml versions, and .yml versions

Take note that [model versions](/docs/mesh/govern/model-versions) are different from [dbt\_project.yml versions](/reference/project-configs/version#dbt_projectyml-versions) and [.yml property file versions](/reference/project-configs/version#yml-property-file-versions).

Model versions is a *feature* that enables better governance and data model management by allowing you to track changes and updates to models over time. dbt\_project.yml versions refer to the compatibility of the dbt project with a specific version of dbt. Version numbers within .yml property files inform how dbt parses those YAML files. The latter two are completely optional starting from dbt v1.5.

dbt projects have two distinct types of `version` tags. This field has a different meaning depending on its location.

`dbt_project.yml` versions[​](#dbt_projectyml-versions "Direct link to dbt_projectyml-versions")
------------------------------------------------------------------------------------------------

The version tag in a `dbt_project` file represents the version of your dbt project.

Starting in dbt version 1.5, `version` in the `dbt_project.yml` is an *optional parameter*. If used, the version must be in a [semantic version](https://semver.org/) format, such as `1.0.0`. The default value is `None` if not specified. For users on dbt version 1.4 or lower, this tag is required, though it isn't currently used meaningfully by dbt.

For more on Core versions, see [About dbt Core versions](/docs/dbt-versions/core).

dbt\_project.yml

```
version: version
```

`.yml` property file versions[​](#yml-property-file-versions "Direct link to yml-property-file-versions")
---------------------------------------------------------------------------------------------------------

A version tag in a `.yml` property file provides the control tag, which informs how dbt processes property files.

Starting from version 1.5, dbt will no longer require this configuration in your resource `.yml` files. If you want to know more about why this tag was previously required, you can refer to the [FAQs](#faqs). For users on dbt version 1.4 or lower, this tag is required,

For more on property files, see their general [documentation](/reference/define-properties) on the same page.

* Resource property file with version specified
* Resource property file without version specified

<any valid filename>.yml

```
version: 2  # Only 2 is accepted by dbt versions up to 1.4.latest.  
  
models:   
    ...
```

<any valid filename>.yml

```
models:   
    ...
```

FAQS[​](#faqs "Direct link to FAQS")
------------------------------------

Why do model and source YAML files always start with `version: 2`?

Once upon a time, the structure of these `.yml` files was very different (s/o to anyone who was using dbt back then!). Adding `version: 2` allowed us to make this structure more extensible.

From [dbt Core v1.5](/docs/dbt-versions/core-upgrade/Older versions/upgrading-to-v1.5#quick-hits), the top-level `version:` key is optional in all resource YAML files. If present, only `version: 2` is supported.

Also starting in v1.5, both the [`config-version: 2`](/reference/project-configs/config-version) and the top-level `version:` key in the `dbt_project.yml` are optional.

Resource YAML files do not currently require this config. We only support `version: 2` if it's specified. Although we do not expect to update YAML files to `version: 3` soon, having this config will make it easier for us to introduce new structures in the future