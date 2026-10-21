# Materials index

Read this first, then open only the files a task needs. Update it in the same commit whenever a file is added, moved or removed. Empty rows are not facts.

## Files
| ID | Path | What it is | Chapter / topic | Provenance | Status |
|---|---|---|---|---|---|

## Stable IDs
- **S-n**: source (paper, report, dataset documentation)
- **D-n**: dataset
- **C-n**: dissertation chapter, **C3-H2** means chapter 3, hypothesis 2
- **Q-n**: claim in a claim map
- **R-n**: analysis run

Never reuse or renumber an ID. A retired item keeps its row with status `retired` and a note.

## Topic to file lookup
| Topic or keyword (include synonyms) | IDs |
|---|---|

## Gaps
Known missing material, listed here so it is not assumed to exist.
- Institutional requirements, calculation datasets and promised voice message are not included in the supplied package. The concept and five supporting works are now available.


## Imported dissertation package

| ID | File | Role |
|---|---|---|
| S-1 | [Concept](dissertation/originals/dissertation-concept-2026-09-07.docx) | Main research document |
| S-2 | [Academic writing](dissertation/originals/academic-writing.pdf) | Writing reference |
| S-3 | [Article example](dissertation/originals/article-example.pdf) | Example |
| S-4 | [Article plan](dissertation/originals/article-plan.docx) | Template |
| S-5 | [Article structure](dissertation/originals/article-structure.docx) | Guidance |
| S-6 | [Article writing](dissertation/originals/article-writing.docx) | Guidance |

Topic, hypothesis, goals and chapters: [BRIEF.md](dissertation/BRIEF.md). Full searchable text and line counts: [document index](../indexes/README.md). Provenance and hashes: [manifest](dissertation/manifest.json). Search with `python tools/memory.py search QUERY`.
