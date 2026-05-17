# Calculator Implementation Plan

## Overview
Build a macOS-style calculator using Python and PyQt6, following TDD (Test-Driven Development) and ISP (Interface Segregation Principle).

## Architecture Principles

### Interface Segregation Principle (ISP)
Separate concerns into focused, single-responsibility interfaces:
- **Calculator Logic**: Pure calculation operations
- **Display Formatter**: Number formatting and display
- **Input Handler**: User input processing
- **UI Components**: Visual elements only

### Test-Driven Development (TDD)
Write tests first, then implement:
1. Write failing test
2. Write minimal code to pass
3. Refactor
4. Repeat

## Project Structure

```
calculator/
├── src/
│   ├── __init__.py
│   ├── calculator_engine.py      # Core calculation logic
│   ├── display_formatter.py      # Number formatting
│   ├── calculator_state.py       # State management
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── calculator_window.py  # Main window
│   │   ├── display_widget.py     # Display area
│   │   ├── button_widget.py      # Custom button
│   │   └── styles.py             # PyQt6 styles
│   └── main.py                   # Application entry
├── tests/
│   ├── __init__.py
│   ├── test_calculator_engine.py
│   ├── test_display_formatter.py
│   ├── test_calculator_state.py
│   └── test_ui_integration.py
├── requirements.txt
└── README.md
```

## Implementation Phases

### Phase 1: Project Setup (15 minutes)

**Files to Create:**
- `requirements.txt`
- `README.md`
- Project structure folders

**Tasks:**
1. Create virtual environment
2. Install dependencies (PyQt6, pytest, pytest-qt)
3. Set up project folders
4. Initialize git repository

**Requirements.txt:**
```
PyQt6==6.6.1
pytest==7.4.3
pytest-qt==4.3.1
pytest-cov==4.1.0
```

---

### Phase 2: Calculator Engine (TDD) (45 minutes)

**Goal:** Implement core calculation logic without UI.

#### Step 2.1: Calculator Engine Interface

**File:** `src/calculator_engine.py`

**Interface (ISP):**
```python
class ICalculatorEngine:
    """Interface for calculator operations"""
    def add(self, a: float, b: float) -> float: pass
    def subtract(self, a: float, b: float) -> float: pass
    def multiply(self, a: float, b: float) -> float: pass
    def divide(self, a: float, b: float) -> float: pass
    def percent(self, value: float) -> float: pass
    def negate(self, value: float) -> float: pass
```

**TDD Steps:**

1. **Write Test First:** `tests/test_calculator_engine.py`
   ```python
   def test_add():
       engine = CalculatorEngine()
       assert engine.add(2, 3) == 5
   ```

2. **Implement minimal code** to pass test

3. **Add more tests:**
   - Test subtraction
   - Test multiplication
   - Test division (including division by zero)
   - Test percent conversion
   - Test negation
   - Test edge cases (very large numbers, decimals)

4. **Run tests:** `pytest tests/test_calculator_engine.py -v`

**Implementation Notes:**
- Pure functions, no state
- Handle edge cases (division by zero)
- Return `float` or raise appropriate exceptions

---

### Phase 3: Display Formatter (TDD) (30 minutes)

**Goal:** Format numbers for display according to spec.

#### Step 3.1: Display Formatter Interface

**File:** `src/display_formatter.py`

**Interface (ISP):**
```python
class IDisplayFormatter:
    """Interface for number formatting"""
    def format_number(self, value: float) -> str: pass
    def format_operation(self, left: float, operator: str, right: float = None) -> str: pass
    def is_valid_input(self, current: str, new_char: str) -> bool: pass
```

**TDD Steps:**

1. **Write Test First:** `tests/test_display_formatter.py`
   ```python
   def test_format_number_with_commas():
       formatter = DisplayFormatter()
       assert formatter.format_number(1797.5) == "1,797.5"
   ```

2. **Test cases:**
   - Format integers with comma separators
   - Format decimals (max 6 decimal places)
   - Format scientific notation for large numbers
   - Format very small numbers
   - Handle max 9 digits before scientific notation

3. **Run tests:** `pytest tests/test_display_formatter.py -v`

**Implementation Notes:**
- Use Python's `locale` or manual formatting
- Max 9 visible digits
- Scientific notation for overflow

---

### Phase 4: Calculator State (TDD) (45 minutes)

**Goal:** Manage calculator state (current value, pending operation, etc.)

#### Step 4.1: State Manager Interface

**File:** `src/calculator_state.py`

**Interface (ISP):**
```python
class ICalculatorState:
    """Interface for calculator state management"""
    def input_digit(self, digit: str) -> None: pass
    def input_decimal(self) -> None: pass
    def input_operator(self, operator: str) -> None: pass
    def calculate(self) -> float: pass
    def clear(self) -> None: pass
    def get_display_value(self) -> str: pass
    def get_operation_display(self) -> str: pass
```

**TDD Steps:**

1. **Write Test First:** `tests/test_calculator_state.py`
   ```python
   def test_input_single_digit():
       state = CalculatorState()
       state.input_digit("5")
       assert state.get_display_value() == "5"
   ```

2. **Test scenarios:**
   - Input multiple digits
   - Input decimal point
   - Chain operations (2 + 3 + 4)
   - Clear all
   - Operator precedence (not needed for basic calculator)
   - Replace operator
   - Calculate with equals

3. **State properties:**
   - `current_value`: Current display number
   - `previous_value`: Left operand
   - `operator`: Current operator (+, -, ×, ÷)
   - `should_reset_display`: Flag for next input
   - `operation_history`: Previous operation string

4. **Run tests:** `pytest tests/test_calculator_state.py -v`

**Implementation Notes:**
- Compose `CalculatorEngine` and `DisplayFormatter`
- Manage state transitions
- Handle edge cases (consecutive operators, equals without operation)

---

### Phase 5: UI Components (60 minutes)

**Goal:** Create PyQt6 UI components matching the spec.

#### Step 5.1: Styles Configuration

**File:** `src/ui/styles.py`

**Content:**
```python
class CalculatorStyles:
    """Central style configuration matching spec"""
    
    # Colors
    WINDOW_BG = "#2D2D2D"
    DISPLAY_PRIMARY = "#FFFFFF"
    DISPLAY_SECONDARY = "#8E8E93"
    BUTTON_FUNCTION_BG = "#505050"
    BUTTON_OPERATOR_BG = "#FF9F0A"
    BUTTON_TEXT = "#FFFFFF"
    
    # Dimensions
    WINDOW_WIDTH = 280
    WINDOW_HEIGHT = 520
    BUTTON_SIZE = 56
    BUTTON_GAP = 8
    
    # Fonts
    DISPLAY_FONT_SIZE = 64
    DISPLAY_FONT_WEIGHT = 300
    PREVIOUS_FONT_SIZE = 28
    BUTTON_FONT_SIZE = 32
    
    @staticmethod
    def get_button_style(button_type: str, active: bool = False) -> str:
        """Returns QSS stylesheet for button type"""
        pass
```

**No tests needed** - pure configuration.

#### Step 5.2: Custom Button Widget

**File:** `src/ui/button_widget.py`

**Purpose:** Reusable calculator button with hover/press states.

**Features:**
- Circular shape (border-radius: 28px)
- Three types: number, function, operator
- Hover effect (opacity 85%)
- Press effect (scale 0.96)
- Wide button variant for "0"

**Simple Test:** `tests/test_ui_integration.py`
```python
def test_button_click_signal(qtbot):
    button = CalculatorButton("5", "number")
    with qtbot.waitSignal(button.clicked):
        button.click()
```

#### Step 5.3: Display Widget

**File:** `src/ui/display_widget.py`

**Features:**
- Two QLabel widgets (previous operation, current value)
- Right-aligned text
- Proper font sizes and colors
- Auto-resize text if overflow

**Simple Test:**
```python
def test_display_shows_value(qtbot):
    display = DisplayWidget()
    display.set_value("123")
    assert display.current_label.text() == "123"
```

#### Step 5.4: Main Calculator Window

**File:** `src/ui/calculator_window.py`

**Features:**
- Fixed size (280×520)
- Dark background
- Grid layout for buttons (QGridLayout)
- Connect button signals to state manager
- Keyboard event handling

**Layout:**
```python
# Button grid positions
buttons = [
    [('±', 0, 0), ('AC', 0, 1), ('%', 0, 2), ('÷', 0, 3)],
    [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('×', 1, 3)],
    [('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3)],
    [('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3)],
    [('0', 4, 0, 1, 2), ('.', 4, 2), ('=', 4, 3)]  # 0 spans 2 columns
]
```

---

### Phase 6: Integration (30 minutes)

**Goal:** Wire everything together.

#### Step 6.1: Main Application

**File:** `src/main.py`

```python
def main():
    app = QApplication(sys.argv)
    
    # Create state manager with engine and formatter
    engine = CalculatorEngine()
    formatter = DisplayFormatter()
    state = CalculatorState(engine, formatter)
    
    # Create window with state
    window = CalculatorWindow(state)
    window.show()
    
    sys.exit(app.exec())
```

#### Step 6.2: Integration Tests

**File:** `tests/test_ui_integration.py`

**Test user flows:**
1. Test simple calculation (2 + 3 = 5)
2. Test chain operations (2 + 3 + 4 = 9)
3. Test clear button
4. Test decimal input
5. Test keyboard input

```python
def test_simple_calculation(qtbot):
    window = create_calculator_window()
    qtbot.addWidget(window)
    
    # Click 2
    window.button_2.click()
    # Click +
    window.button_add.click()
    # Click 3
    window.button_3.click()
    # Click =
    window.button_equals.click()
    
    assert window.display.get_value() == "5"
```

---

### Phase 7: Polish & Refinement (30 minutes)

**Tasks:**
1. Fine-tune colors and spacing to match spec exactly
2. Add hover/press animations
3. Implement keyboard shortcuts
4. Add operator highlight (white bg, orange text when active)
5. Test on different screen resolutions
6. Handle edge cases in UI (very long numbers)

**Optional Enhancements:**
- Window controls (close, minimize, maximize) - can use native or custom
- Copy/paste support
- History panel
- Settings

---

## Testing Strategy

### Unit Tests
- **Calculator Engine:** Pure logic, easy to test
- **Display Formatter:** String formatting
- **Calculator State:** State transitions

### Integration Tests
- **UI Interactions:** Using pytest-qt
- **User Flows:** Multi-step operations

### Test Coverage Goal
- Minimum 85% code coverage
- All business logic 100% covered

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_calculator_engine.py -v

# Run tests in watch mode
pytest-watch
```

---

## Development Workflow

### TDD Cycle for Each Component

1. **RED:** Write a failing test
   ```bash
   pytest tests/test_calculator_engine.py::test_add
   # FAILED (function doesn't exist)
   ```

2. **GREEN:** Write minimal code to pass
   ```python
   def add(self, a, b):
       return a + b
   ```
   ```bash
   pytest tests/test_calculator_engine.py::test_add
   # PASSED
   ```

3. **REFACTOR:** Improve code quality
   - Extract constants
   - Remove duplication
   - Improve naming

4. **REPEAT:** Next test

### Git Workflow

**Commit after each passing test:**
```bash
git add .
git commit -m "test: add test for calculator addition"
git add .
git commit -m "feat: implement calculator addition"
```

**Branches:**
- `main`: Production-ready code
- `develop`: Integration branch
- `feature/calculator-engine`: Feature branches
- `test/calculator-engine`: Test branches (optional)

---

## ISP Implementation Examples

### Good: Segregated Interfaces
```python
# Each interface has a single, focused purpose
class ICalculatorEngine:
    def add(self, a, b): pass
    def subtract(self, a, b): pass

class IDisplayFormatter:
    def format_number(self, value): pass

class IInputHandler:
    def handle_digit(self, digit): pass
```

### Bad: Fat Interface (Avoid)
```python
# Don't do this - violates ISP
class ICalculator:
    def add(self, a, b): pass
    def format_number(self, value): pass
    def show_display(self): pass
    def handle_click(self, button): pass
    def save_history(self): pass
    # Too many responsibilities!
```

---

## Key Design Decisions

### 1. Separation of Concerns
- **Model:** Calculator logic (no PyQt6 dependencies)
- **View:** PyQt6 UI components (no business logic)
- **Controller:** State manager (connects model and view)

### 2. Dependency Injection
- Pass dependencies via constructor
- Easy to test with mocks
- Easy to swap implementations

```python
class CalculatorState:
    def __init__(self, engine: ICalculatorEngine, formatter: IDisplayFormatter):
        self.engine = engine
        self.formatter = formatter
```

### 3. No Over-Engineering
- No complex state machines (simple state variables)
- No elaborate observer patterns (simple signals/slots)
- No unnecessary abstractions
- Keep it simple and readable

### 4. PyQt6 Best Practices
- Use signals/slots for event handling
- QSS for styling (similar to CSS)
- QGridLayout for button grid
- Fixed size window (no responsive layout needed)

---

## Estimated Time Breakdown

| Phase | Time | Cumulative |
|-------|------|------------|
| Project Setup | 15 min | 15 min |
| Calculator Engine (TDD) | 45 min | 60 min |
| Display Formatter (TDD) | 30 min | 90 min |
| Calculator State (TDD) | 45 min | 135 min |
| UI Components | 60 min | 195 min |
| Integration | 30 min | 225 min |
| Polish & Refinement | 30 min | 255 min |
| **Total** | **~4.5 hours** | |

**Note:** Times are estimates for focused development. Actual time may vary.

---

## Success Criteria

### Functional Requirements
- ✅ All basic operations work (+ - × ÷)
- ✅ Percent and negate functions work
- ✅ Clear button resets state
- ✅ Decimal input works correctly
- ✅ Chain operations work (2 + 3 + 4)
- ✅ Keyboard shortcuts work
- ✅ Display formatting matches spec

### Visual Requirements
- ✅ Matches pixel-perfect spec
- ✅ Correct colors (#2D2D2D, #FF9F0A, etc.)
- ✅ Correct dimensions (280×520)
- ✅ Hover/press states work
- ✅ Operator highlight works

### Code Quality
- ✅ 85%+ test coverage
- ✅ All tests passing
- ✅ ISP principles followed
- ✅ Clean, readable code
- ✅ No PyQt6 dependencies in business logic

---

## Next Steps

1. **Start with Phase 1:** Set up project structure
2. **Follow TDD rigorously:** Write tests first, always
3. **Commit frequently:** After each passing test
4. **Keep it simple:** Resist over-engineering
5. **Refer to spec:** Check CALCULATOR_SPEC.md for visual details

---

**Ready to start coding?** Begin with Phase 1: Project Setup!

```bash
# Create project structure
mkdir -p calculator/{src/ui,tests}
touch calculator/requirements.txt
cd calculator
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
