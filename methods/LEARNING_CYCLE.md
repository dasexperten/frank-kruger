# Learning and memory cycle

This is a file-based routine. Writing to these files does not train the base model; a lesson counts only if a later session reads it and applies it.

## 1. Capture
After each substantial task, add one dated line to the **Inbox** section of `research/PROJECT_STATE.md`: what worked or failed, and the evidence (file, source, check).

## 2. Distill
Move an inbox item to `LEARNING.md` only when it has helped in at least two separate tasks, or when an independent check confirmed it. Write it as a rule:

`YYYY-MM-DD | When X, do Y, because Z | Evidence: file/source | Applies to: task type | Status: active/superseded`

Single observations stay in the inbox. Items that never recur are deleted at compaction.

## 3. Promote
A lesson that keeps recurring for one kind of task becomes a step in the matching `methods/` file, so it loads automatically for that task. Keep the `LEARNING.md` entry as a pointer to it.

## 4. Compact
Run when `MEMORY.md` or `LEARNING.md` passes about 4 KB, or monthly, whichever is first:
- merge duplicates;
- mark replaced decisions `superseded` with the date and replacing entry, and never delete the history of a decision;
- move old detail to `archive/` and leave a one-line pointer;
- empty the inbox of items that were distilled or dropped.

## 5. Test
After changing any `methods/` file, rerun the cases in `evaluation/SCENARIOS.md` that the change could affect. Log date, model, request, answer and score (0/1/2) in a separate results file, not in the protocol. Fabrication and isolation cases must pass.

## Rules
- Record only confirmed facts, with origin and date.
- Do not write lessons from a single unverified run.
- Compaction changes are committed with a message saying what was merged or archived.


## Executable support
Use memory/PROTOCOL.md and tools/memory.py for evidence-backed candidate review, transitions, freshness checks and indexes. Retain card history; compaction of narrative inbox notes must not delete evidence or decision history.
