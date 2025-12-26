# Debugging Difficult Issues (Analysis-First, No Overcomplication)

Use this doc when you hit a gnarly bug and want a clean AI workflow: **analyze first**, then **implement fixes only after the root cause is understood**.

---

## The rule

- **Architect phase**: analyze only. **No implementation.**
- **Developer phase**: implement the smallest fix, guided by the analysis (prefer TDD when possible).

---

## What to paste into chat (minimum)

- **What you expected** vs **what happened**
- **Exact error text / stack trace** (copy/paste)
- **How to reproduce** (the smallest set of steps)
- **Environment**: OS, Python version, key packages, and how you run it
- **Pointers to relevant code**:
  - repo root is open
  - file paths + the specific functions/classes involved

If you can, also include:
- Recent “last known good” change (what changed?)
- Logs (app + test output)
- A screenshot (if it’s a UI bug)

---

## Prompt 1 — Software Architect (analyze only)

Paste this (fill in the issue details):

```text
You are a software architect.

Context:
- Repo: opened at the code root.
- Goal: diagnose the issue we’re experiencing.

Issue:
<describe expected vs actual>

Repro steps:
1)
2)
3)

Error / logs:
<paste stack trace or logs>

Relevant files / entry points:
- <path>: <what it contains>
- <path>: <what it contains>

Constraints:
- Do NOT implement any code.
- Only analyze and recommend: likely root cause(s), what evidence supports each, and the smallest set of experiments/inspections to confirm.

Output format:
1) Summary of the problem in one paragraph
2) Top 3 root-cause hypotheses (ranked) with supporting evidence you’d look for
3) The next 5 concrete debugging actions (specific files/lines to inspect, commands to run, what signals to look for)
4) If tests are missing: propose 1-2 minimal tests that would prevent regression (describe them; don’t implement)
```

---

## Prompt 2 — AI Developer (only after the architect)

Once you agree with the analysis, paste:

```text
You are the AI developer.

Implement the fix based on the architect’s analysis.
Constraints:
- Keep it minimal (smallest change that fixes the bug).
- Prefer TDD: add/adjust a test if appropriate, then fix, then re-run tests.
- Preserve interfaces (ISP): don’t mix UI logic into the engine; don’t couple components unnecessarily.

Deliverables:
- Show the exact files changed and why.
- Show the commands run and the results (tests / run output).
```

---

## Quick tactics (use only when needed)

- **Reduce to a minimal repro**: “Can we reproduce with a 10-line script or a single unit test?”
- **Bisect mentally**: “What changed since last working version?”
- **Add observability**: targeted logs (input → state → output), then remove once fixed.
- **Check boundaries**: UI vs controller vs engine—bugs often live at component seams.


