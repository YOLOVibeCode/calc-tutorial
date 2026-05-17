# Development Environment Setup

## ✅ Installation Complete

All dependencies and tools have been successfully installed and configured for the PyQt6 Calculator project.

---

## System Information

- **Operating System**: macOS (darwin 25.3.0)
- **Shell**: zsh
- **Python Version**: 3.14.0
- **Package Manager**: Homebrew (installed at `/opt/homebrew/bin/brew`)
- **Workspace**: `/Users/admin/Dev/YOLOVibeCode/VibeCodeCalcTutorial`

---

## Installed Dependencies

### Virtual Environment
A Python virtual environment has been created at `./venv/` to isolate project dependencies.

**Location**: `/Users/admin/Dev/YOLOVibeCode/VibeCodeCalcTutorial/venv`

### Python Packages

| Package | Version | Purpose |
|---------|---------|---------|
| PyQt6 | 6.11.0 | GUI framework for the calculator UI |
| PyQt6-Qt6 | 6.11.1 | Qt6 runtime libraries |
| PyQt6-sip | 13.11.1 | Python bindings for Qt6 |
| pytest | 9.0.3 | Testing framework |
| pytest-qt | 4.5.0 | PyQt6 testing plugin |
| pytest-cov | 7.1.0 | Test coverage reporting |
| coverage | 7.14.0 | Code coverage measurement |

**Full dependency list**: See `requirements.txt`

---

## Cursor Rules Configured

### Rule File Location
`.cursor/rules/python-pyqt6-calculator.mdc`

### Enforced Principles

#### 1. KISS (Keep It Simple, Stupid)
- No over-engineering
- Simple data structures
- Readable over clever code
- Minimal dependencies

#### 2. TDD (Test-Driven Development)
- **RED-GREEN-REFACTOR** cycle mandatory
- Write tests FIRST, then implementation
- 85% minimum code coverage
- 100% coverage for business logic

#### 3. ISP (Interface Segregation Principle)
- Focused, single-responsibility interfaces
- 3-7 methods per interface maximum
- Separate concerns: Engine, Formatter, State, UI
- No UI dependencies in business logic

#### 4. PyQt6 Best Practices
- Separation of concerns (Model-View-Controller)
- Signal/Slot pattern for events
- QSS for styling
- No PyQt6 imports in business logic

### Rule Scope
- **Applies to**: All Python files (`**/*.py`)
- **Auto-applies**: When working with Python files in this project

---

## Project Structure

```
VibeCodeCalcTutorial/
├── .cursor/
│   └── rules/
│       └── python-pyqt6-calculator.mdc    # Cursor rules
├── venv/                                   # Virtual environment
├── requirements.txt                        # Python dependencies
├── CALCULATOR_SPEC.md                      # UI/UX specifications
├── IMPLEMENTATION_PLAN.md                  # Development plan
└── SETUP.md                                # This file
```

**Next steps**: Follow IMPLEMENTATION_PLAN.md to create the calculator application.

---

## Quick Start Commands

### Activate Virtual Environment
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Install Dependencies (if needed)
```bash
pip install -r requirements.txt
```

### Run Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_calculator_engine.py -v

# Run in watch mode (install first: pip install pytest-watch)
pytest-watch
```

### Deactivate Virtual Environment
```bash
deactivate
```

---

## Development Workflow

### 1. Start Development Session
```bash
# Navigate to project
cd /Users/admin/Dev/YOLOVibeCode/VibeCodeCalcTutorial

# Activate virtual environment
source venv/bin/activate

# Verify setup
python -c "import PyQt6; import pytest; print('✓ Ready to develop')"
```

### 2. TDD Cycle
```bash
# 1. Write failing test
# Edit: tests/test_calculator_engine.py

# 2. Run test (should fail - RED)
pytest tests/test_calculator_engine.py::test_add -v

# 3. Write minimal implementation
# Edit: src/calculator_engine.py

# 4. Run test (should pass - GREEN)
pytest tests/test_calculator_engine.py::test_add -v

# 5. Refactor (keep tests green)
pytest

# 6. Commit
git add .
git commit -m "test: add test for calculator addition"
git commit -m "feat: implement calculator addition"
```

### 3. Check Coverage
```bash
pytest --cov=src --cov-report=term-missing

# Generate HTML report
pytest --cov=src --cov-report=html
open htmlcov/index.html  # macOS
```

---

## Verification Checklist

✅ **Python 3.14.0** installed and working  
✅ **Homebrew** package manager available  
✅ **Virtual environment** created at `./venv/`  
✅ **PyQt6 6.11.0** installed and importable  
✅ **pytest 9.0.3** installed with pytest-qt and pytest-cov  
✅ **requirements.txt** created with pinned versions  
✅ **Cursor rules** configured with KISS, TDD, ISP enforcement  
✅ **Project documentation** complete (SPEC, PLAN, SETUP)  

---

## Troubleshooting

### Virtual Environment Not Active
**Symptom**: `python` points to system Python, not venv

**Solution**:
```bash
source venv/bin/activate
# Verify: which python should show ./venv/bin/python
```

### Import Errors
**Symptom**: `ModuleNotFoundError: No module named 'PyQt6'`

**Solution**:
```bash
# Ensure venv is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### PyQt6 Display Issues on macOS
**Symptom**: Window doesn't appear or crashes

**Solution**:
```bash
# Ensure you're running Python app from terminal, not script
# PyQt6 requires proper display context on macOS
python src/main.py  # ✅ Works
./src/main.py       # ❌ May fail
```

### Tests Not Found
**Symptom**: `pytest` finds no tests

**Solution**:
```bash
# Ensure test files start with test_
# Ensure test functions start with test_
# Run from project root
pytest -v  # Shows discovery process
```

---

## Additional Tools (Optional)

### Code Formatting
```bash
pip install black isort
black src/ tests/
isort src/ tests/
```

### Linting
```bash
pip install pylint
pylint src/
```

### Type Checking
```bash
pip install mypy
mypy src/
```

### Watch Mode for Tests
```bash
pip install pytest-watch
pytest-watch
```

---

## Next Steps

1. ✅ **Setup Complete** - You're here!
2. 📖 **Read**: `IMPLEMENTATION_PLAN.md` for development phases
3. 🏗️ **Build**: Start with Phase 1 (Project Structure)
4. 🧪 **Test**: Follow TDD - write tests first!
5. 🎨 **Polish**: Match `CALCULATOR_SPEC.md` pixel-perfect

---

**Ready to start coding!** 🚀

Begin with Phase 1 of the Implementation Plan:
```bash
# Create project structure
mkdir -p src/ui tests
touch src/__init__.py src/ui/__init__.py tests/__init__.py

# Start with first test
code tests/test_calculator_engine.py
```
