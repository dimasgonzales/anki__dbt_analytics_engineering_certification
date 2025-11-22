---
tags:
  - packages
  - cli-commands
  - versioning
citations:
- cleaned_docs/packages/rank_1.md
guid: a0f0d81aa3
source: llm
uuid: ffaa4681-e7fc-5caa-8f9a-fcef7943f02d
---

<front>

What is the purpose of the `package-lock.yml` file generated when running `dbt deps`?

</front>

---

<back>

It resolves and pins specific versions of all dependencies (including transitive ones) to ensure consistent installations across environments. Subsequent `dbt deps` runs use the lock file instead of resolving the latest versions from `packages.yml`.

</back>
