---
tags:
- card_type/factual
- development/cli-commands
- state/selectors
citations:
  - docs/site_docs.getdbt.com/citations/docs_getdbt_com_reference_commands_snapshot.md
guid: C+vAz]PJg!
source: apkg
uuid: bb23bf49-00ce-56cc-b9dc-a2eafee80b9f
claim_meta:
  verdict: SUPPORTED
  explanation: "The Reference Text explicitly states that the dbt snapshot command executes snapshots defined in the project, looks for them in snapshot-paths directories, and demonstrates filtering using selection syntax with the --select flag."
  citation:
    quote: "The `dbt snapshot` command executes the Snapshots defined in your project. dbt will look for Snapshots in the `snapshot-paths` paths defined in your `dbt_project.yml` file."
    is_quote_valid: false
---

<front>

What does the `dbt snapshot` command do?

</front>

---

<back>

It will execute the snapshots defined in your project. dbt will look for snapshots in the directories configured via snapshot-paths. Snapshots can be filtered using standard dbt selection syntax.

</back>
