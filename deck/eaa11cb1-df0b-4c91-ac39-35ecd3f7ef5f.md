---
uuid: eaa11cb1-df0b-4c91-ac39-35ecd3f7ef5f
guid: MJV3$smRaJ
tags:
  - general_reference
citations:
  - https://docs.getdbt.com/reference/dbtignore
---

<front>
How can you configure dbt to completely ignore certain files in your repo?
</front>

---

<back>

You can create a .dbtignore file in the root of your dbt project to specify files that should be entirely ignored by dbt. The file behaves like a .gitignore file, using the same syntax. Files and subdirectories matching the pattern will not be read, parsed, or otherwise detected by dbt—as if they didn't exist.

</back>
