# Vibe Code Calculator Tutorial

Build a pixel-perfect calculator clone in Python using AI.

**Full philosophy and methodology:** See `MEDIUM_ARTICLE.md`  
**Debugging hard issues:** See `DEBUGGING.md`

---

## Prerequisites

```bash
# Check Python
python3 --version  # Need 3.11+

# Install PyQt6
pip install PyQt6
```

---

## Step 0 — Screenshot Your Calculator

1. Open your system calculator (Windows or macOS)
2. Take a screenshot (`Cmd+Shift+4` on Mac, `Win+Shift+S` on Windows)
3. Paste it into your AI chat (Cursor, Windsurf, or Claude Code)

---

## Step 1 — Architect Prompt

Paste screenshot, then send:

```text
You are a software architect.

Goal: Create a pixel-perfect representation of the calculator in the attached screenshot, implemented in Python.

Constraints:
- Use TDD for the core calculation logic
- Use ISP (Interface Segregation Principle): define small, focused interfaces so UI, input controller, and calculator engine are separable and testable
- Provide an explicit file/folder structure
- Provide a test plan (what to test first, next, and why)
- Provide acceptance criteria for "pixel-perfect" (fonts, spacing, colors, button states)

Deliverables:
1. Architecture overview (components and responsibilities)
2. Interfaces (with method signatures)
3. Data model / state machine for input handling
4. TDD plan with prioritized test list
5. Step-by-step implementation plan

Do NOT implement. Design only.
```

---

## Step 2 — Developer Prompt

After receiving the architecture, send:

```text
You are now the AI developer.

Execute the architect's plan exactly:
1. Create the project structure
2. Implement tests first (TDD)
3. Implement the calculator engine behind small interfaces (ISP)
4. Build the UI to match the screenshot

After each step:
- Run tests
- Fix failures before moving on

Use PyQt6 for the UI.
```

---

## Step 3 — Fix Errors

When tests fail or errors occur:

```text
Error occurred. Please fix using TDD and ISP:
1. Add/adjust a test to capture the bug
2. Implement the smallest fix
3. Re-run tests and confirm they pass
```

---

## Step 4 — UI Adjustments

When the UI doesn't match:

```text
UI mismatch:
- [Describe specific differences]

Please adjust styles/layout to match the screenshot. Show what changed.
```

---

## Expected Project Structure

```
calc/
  __init__.py
  interfaces.py    # Protocols/ABCs
  engine.py        # Pure calculation logic
  controller.py    # Input state machine
  ui.py            # PyQt6 UI
tests/
  test_engine.py
  test_controller.py
main.py
requirements.txt
```

---

## Run Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/ -v

# Run app
python main.py
```

---

## Done Checklist

- [ ] All tests pass
- [ ] App runs without errors
- [ ] UI matches screenshot (layout, colors, fonts, button states)
