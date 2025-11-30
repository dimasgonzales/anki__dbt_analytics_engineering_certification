---
tags:
- compiled-code
- test-config
- yaml-compilation
citations:
- cleaned_docs/cli-commands/rank_2.md
guid: 140a2b36ff
source: llm
uuid: 1d2ff1ba-2e0a-57bd-aaaf-e02e18aa0728
---

<front>

A user runs `dbt --no-populate-cache run` and receives a deprecation warning or syntax error. What is the correct way to structure this command?

</front>

---

<back>

Flags should always follow the subcommand.

Correct syntax:
```bash
dbt run --no-populate-cache
```
Global flags placed before the subcommand are legacy syntax and should be avoided.

</back>
