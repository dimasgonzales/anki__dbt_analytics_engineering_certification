---
tags:
- compiled-code
- docs-generation
- state-concepts
citations:
- cleaned_docs/cli-commands/rank_7.md
guid: 0fb2cdc80e
source: llm
uuid: efdca8cb-e99a-521f-b853-b454acf50cea
---

<front>

What is the purpose of the `--empty-catalog` flag when running `dbt docs generate`?

</front>

---

<back>

It instructs dbt to generate the documentation artifacts (index.html and manifest.json) but skip the expensive database queries required to build `catalog.json`. This makes generation significantly faster but omits database-specific details like column types.

</back>
