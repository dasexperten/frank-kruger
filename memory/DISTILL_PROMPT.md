# Model distillation prompt

Read AGENTS.md and memory/PROTOCOL.md. The primary project is Lyudmila's dissertation. Given a saved session record and its cited evidence, produce only supported candidate memories.

For each candidate return: ID; kind (decision/fact/method/correction); one precise claim; applicability and limits; exact repository source and line interval; status candidate; counterevidence or uncertainty; review date if time-sensitive; suggested verification. Read the existing cards first and identify duplicates or conflicts. Do not promote a claim merely because it appeared in an earlier model answer. Retain provenance to original documents rather than summaries of summaries.

Keep unresolved hypotheses and planned work in the project state. Extract methodological lessons only from observed outcomes or explicit authoritative requirements. For corrections, identify the previous memory and the replacement evidence. Explain why compression does not change the source's meaning. Preserve numbers, units, dates, negations and limitations.

After a separate evidence review, use the CLI to record candidates and permitted transitions; run cycle and check usable/review_due groups. If code is unavailable, prepare proposed changes with source citations and state that lifecycle validation was not run. Never invent user approval, a test run or model training.
