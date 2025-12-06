---
tags:
- card_type/factual
- debugging/yaml-compilation
- development/modularity
- development/project-config
citations:
- cleaned_docs/yaml-compilation/rank_1.md
guid: 3017dbf5d7
source: llm
uuid: 1ffddc86-20b5-5bd3-ba15-ff42b92b3cda
claim_meta:
  verdict: NOT_FOUND
  explanation: "The reference text indicates that indentation errors can cause parsing issues in dbt YAML files, but it does not provide explicit evidence that indentation must be space-based, that tab characters are forbidden, or that they result in the specific error 'Could not parse dbt_project.yml'. The text discusses general indentation problems without detailing character-level rules or this exact error message."
  citation:
    quote: "Usually, it's to do with indentation — here's the offending YAML that caused this error:"
    is_quote_valid: true
---

<front>

What is the strict indentation rule for dbt YAML files, and which character causes immediate parsing errors?

</front>

---

<back>

dbt YAML files require **space-based** indentation. The use of **tab characters** is forbidden and will cause a `Could not parse dbt_project.yml` error during the compilation phase.

</back>
