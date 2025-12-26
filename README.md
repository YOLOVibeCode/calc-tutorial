# Vibe Coding Tutorial: Build a Pixel‑Perfect Calculator in Python (TDD + ISP)

This repo is a hands-on tutorial for running an **easy, high-leverage “vibe coding” session**: you speak your intent, you show the AI the UI you want, and you iterate quickly with **TDD (Test-Driven Development)** and **ISP (Interface Segregation Principle)** guiding the work.

This tutorial is based on the starting notes in `Primer.txt`.

---

## What you’ll build

A **pixel-perfect clone** (as close as practical) of your system calculator UI, implemented in **Python**, with:

- **A UI layer** that renders the calculator to match your screenshot.
- **A calculator engine** with a clean interface and deterministic behavior.
- **Automated tests** (TDD loop) that validate the engine (and optionally UI behavior).
- **ISP-driven design** (small, focused interfaces so components are swappable and testable).

---

## What you’ll need

- **An IDE with an AI chat that accepts images**: Cursor or Windsurf.
- **Optional voice dictation** (recommended):
  - Willow Voice / Whisper-based dictation / OS dictation.
  - Any microphone dictation that lets you speak prompts into your IDE.
- **Python 3.11+** (3.12+ is great too).

---

## The vibe coding loop (the whole method)

You will do the project as a two-role conversation:

- **Role 1 — “Software Architect”**: designs the system using **TDD + ISP**, defines acceptance criteria, file structure, and test plan.
- **Role 2 — “AI Developer”**: implements exactly what the architect specified, runs tests, fixes failures, and iterates.

When anything breaks, you do **TDD-style fix cycles**:

1. Reproduce (run tests / run app).
2. Add or adjust a test (when appropriate).
3. Fix the smallest thing.
4. Re-run and confirm.

---

## Step 0 — Capture the UI spec (screenshot)

Your screenshot is your “design doc”.

1. Open the built-in calculator on your machine (Windows or macOS).
2. Resize it to the size you want your clone to match.
3. Take a screenshot:
   - **macOS**: `Cmd + Shift + 4` (region) or `Cmd + Shift + 5` (options)
   - **Windows**: `Win + Shift + S` (snipping)
4. Paste the screenshot **directly into the IDE chat**.

Tip: If you can, also include a second screenshot showing hover/pressed states (optional).

---

## Step 1 — Prompt the “Software Architect” (TDD + ISP)

Paste your screenshot into chat, then send a message like this (edit as you like):

```text
You are a software architect.

Goal: Create a pixel-perfect representation of the calculator in the attached screenshot, implemented in Python.

Constraints:
- Use TDD for the core calculation logic.
- Use ISP (Interface Segregation Principle): define small, focused interfaces so the UI, input controller, and calculator engine are separable and testable.
- Provide an explicit file/folder structure.
- Provide a test plan (what to test first, next, and why).
- Provide acceptance criteria for “pixel-perfect” (fonts, spacing, colors, button states).

Deliverables:
1) Architecture overview (components and responsibilities)
2) Interfaces (with method signatures)
3) Data model / state machine for input handling
4) TDD plan with a prioritized test list
5) A step-by-step implementation plan
```

### What you’re looking for in the architect’s answer

- **Clear boundaries**:
  - UI should call an interface like `CalculatorEngine` and `InputController` rather than “doing math”.
- **A test-first plan**:
  - Start with math semantics (e.g., digit entry, clear, backspace, decimal, sign, equals).
- **Concrete acceptance criteria** for the UI:
  - Size, padding, font, colors, radius, button grid.
  - Pressed/hover/focus behavior (even if simplified).

If the architect’s response is vague, ask:

```text
Please make the interfaces explicit (Python protocols or ABCs) and list the first 10 tests in exact Given/When/Then terms.
```

---

## Step 2 — Prompt the “AI Developer” (execute the architect’s plan)

Once the architect has produced a plan, send this:

```text
You are now the AI developer.

Execute the architect’s plan exactly.
- Create the project structure.
- Implement tests first (TDD).
- Implement the calculator engine behind small interfaces (ISP).
- Then build the UI to match the screenshot as closely as possible.

After each meaningful step:
- run tests (or show the command to run them)
- fix failures before moving on

If you need to choose a UI toolkit, propose 1 default choice and justify it briefly.
```

---

## Step 3 — Keep the session tight (how to iterate)

### When the AI writes code

Ask it to:

- **Show exact filenames** and what changed.
- **Run tests** and paste the output.
- Make small commits of work (even if you’re not literally committing in git).

### When something fails

Use this exact kind of instruction:

```text
The tests are failing / the app errors.
Please fix the error using TDD and ISP:
- first, add/adjust a test if needed to capture the bug
- then implement the smallest fix
- re-run tests and confirm they pass
```

### When UI doesn’t match the screenshot

Give targeted feedback:

```text
UI mismatch feedback:
- Buttons are too tall by ~8px
- Font weight is too light
- Spacing between columns is too large
- Display padding needs to increase on the right

Please adjust styles/layout to match the screenshot more closely. Show what you changed.
```

---

## Step 4 — Definition of “done”

You’re done when:

- **Engine tests pass** (core behavior locked in).
- **App runs** without errors.
- UI matches the screenshot closely on:
  - **Layout** (grid, spacing, alignment)
  - **Typography** (font size/weight)
  - **Colors** (backgrounds, text)
  - **Button states** (pressed at minimum; hover/focus optional but nice)

---

## Recommended project shape (example)

Your architect may pick something slightly different, but this is a good “ISP + TDD” baseline:

- `calc/engine.py` — pure logic (unit tested)
- `calc/interfaces.py` — small interfaces (Protocols / ABCs)
- `calc/controller.py` — input state machine (unit tested)
- `calc/ui.py` — UI wiring / rendering
- `tests/` — unit tests for engine + controller

---

## Troubleshooting playbook

- **The AI is mixing UI logic and math**:
  - “Move math into the engine behind an interface; the UI must not compute results directly.”
- **Tests are flaky or too UI-driven**:
  - “Keep most tests on engine/controller. UI tests optional and minimal.”
- **Pixel-perfect is hard**:
  - Provide more screenshots, specify sizes (window width/height), and ask for a “layout debug mode” (show button bounding boxes).

---

## Your next action

1. Paste a calculator screenshot into your IDE chat.
2. Send the **Software Architect** prompt from Step 1.
3. Then send the **AI Developer** prompt from Step 2.

When you’re ready, paste the architect’s response here and I’ll help refine it into an implementation checklist and crisp prompts for the developer phase.


