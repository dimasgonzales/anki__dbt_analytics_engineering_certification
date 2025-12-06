---
tags:
- card_type/factual
- development/cli-commands
- development/packages
- governance/versioning
citations:
- cleaned_docs/packages/rank_1.md
guid: a0f0d81aa3
source: llm
uuid: ffaa4681-e7fc-5caa-8f9a-fcef7943f02d
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly confirms that package-lock.yml pins dependency versions to ensure consistency, and that subsequent dbt deps runs use the lock file unless packages.yml is changed, directly supporting all key points of the answer."
  citation:
    quote: "The package-lock.yml file ensures consistent and repeatable installs across all environments. When you run dbt deps, dbt installs packages based on the versions locked in the package-lock.yml. - Source: packages/rank_2.md"
    is_quote_valid: false
---

<front>

What is the purpose of the `package-lock.yml` file generated when running `dbt deps`?

</front>

---

<back>

It resolves and pins specific versions of all dependencies (including transitive ones) to ensure consistent installations across environments. Subsequent `dbt deps` runs use the lock file instead of resolving the latest versions from `packages.yml`.

</back>
