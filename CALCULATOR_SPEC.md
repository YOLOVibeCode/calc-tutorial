# Calculator UI Specification

## Overview
This document provides pixel-perfect specifications for a macOS-style calculator application with a dark theme interface.

## Window Structure

### Window Dimensions
- **Width**: 280px
- **Height**: 520px
- **Background**: Dark gray (#2D2D2D)
- **Border Radius**: 12px

### Window Controls (Top Left)
- **Position**: Top-left corner, 12px from edges
- **Spacing**: 8px horizontal gap between buttons
- **Buttons**: 
  - Close (Red): #FF5F57, 12px diameter
  - Minimize (Yellow): #FFBD2E, 12px diameter
  - Maximize (Green): #28C940, 12px diameter

### Top Bar Icons (Center)
- **Position**: Horizontally centered, 12px from top
- **Icons**: 
  - Layout toggle icon (left): White outline, 20×20px
  - Calculator grid icon (right): White outline, 20×20px
- **Spacing**: 16px gap between icons
- **Style**: Outlined icons with 2px stroke

## Display Area

### Container
- **Position**: Below window controls, 16px top margin
- **Width**: 248px (16px horizontal padding from window edge)
- **Background**: Transparent/same as window
- **Alignment**: Right-aligned content

### Previous Operation Display
- **Text**: "898.75×2" (example)
- **Font Family**: SF Pro Display / System Font
- **Font Size**: 28px
- **Font Weight**: 400 (Regular)
- **Color**: #8E8E93 (Medium gray)
- **Alignment**: Right
- **Line Height**: 34px
- **Position**: 60px from top of window

### Current Value Display
- **Text**: "1,797.5" (example)
- **Font Family**: SF Pro Display / System Font
- **Font Size**: 64px
- **Font Weight**: 300 (Light)
- **Color**: #FFFFFF (White)
- **Alignment**: Right
- **Line Height**: 76px
- **Position**: 8px below previous operation
- **Number Formatting**: Comma-separated thousands

## Button Grid

### Grid Layout
- **Columns**: 4
- **Rows**: 5
- **Total Buttons**: 20
- **Grid Start Position**: 32px below display area
- **Horizontal Padding**: 16px from window edges
- **Grid Width**: 248px

### Button Dimensions
- **Size**: 56px × 56px (circular)
- **Horizontal Gap**: 8px
- **Vertical Gap**: 8px

### Button States & Colors

#### Function Buttons (Column 1, Row 1-3)
- **Background**: #505050 (Dark gray)
- **Text Color**: #FFFFFF (White)
- **Buttons**: ±, AC, %
- **Font Size**: 24px
- **Font Weight**: 400

#### Number Buttons (0-9)
- **Background**: #505050 (Dark gray)
- **Text Color**: #FFFFFF (White)
- **Font Size**: 32px
- **Font Weight**: 300
- **Buttons**: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

#### Operator Buttons (Column 4)
- **Background**: #FF9F0A (Orange)
- **Text Color**: #FFFFFF (White)
- **Font Size**: 32px
- **Font Weight**: 300
- **Buttons**: ÷, ×, -, +, =

#### Special Button (0)
- **Width**: 120px (spans 2 columns)
- **Height**: 56px
- **Shape**: Pill-shaped (28px border radius)
- **Alignment**: Text left-aligned, 24px from left edge

#### Decimal Point Button (.)
- **Background**: #505050 (Dark gray)
- **Text Color**: #FFFFFF (White)
- **Font Size**: 32px
- **Font Weight**: 300

### Button Grid Map

```
Row 1: [±]    [AC]   [%]    [÷]
Row 2: [7]    [8]    [9]    [×]
Row 3: [4]    [5]    [6]    [-]
Row 4: [1]    [2]    [3]    [+]
Row 5: [0  (wide)]   [.]    [=]
```

### Button Position Coordinates (from top-left of window)

#### Row 1 (y: 180px)
- ± : x: 16px
- AC: x: 80px
- % : x: 144px
- ÷ : x: 208px

#### Row 2 (y: 244px)
- 7: x: 16px
- 8: x: 80px
- 9: x: 144px
- ×: x: 208px

#### Row 3 (y: 308px)
- 4: x: 16px
- 5: x: 80px
- 6: x: 144px
- -: x: 208px

#### Row 4 (y: 372px)
- 1: x: 16px
- 2: x: 80px
- 3: x: 144px
- +: x: 208px

#### Row 5 (y: 436px)
- 0: x: 16px (width: 120px)
- .: x: 144px
- =: x: 208px

## Interactive States

### Hover State
- **Opacity**: 85%
- **Transition**: 150ms ease-in-out

### Active/Pressed State
- **Opacity**: 60%
- **Scale**: 0.96
- **Transition**: 100ms ease-out

### Selected Operator State
- **Background**: #FFFFFF (White)
- **Text Color**: #FF9F0A (Orange)
- **Applied to**: Currently active operator waiting for second operand

## Typography

### Fonts
- **Primary**: SF Pro Display (macOS), Segoe UI (Windows), System Font (fallback)
- **Weights Used**: 
  - 300 (Light) - Main display, number buttons
  - 400 (Regular) - Previous operation, function labels

### Text Rendering
- **Anti-aliasing**: Enabled
- **Kerning**: Auto
- **Number spacing**: Tabular (monospace numbers for alignment)

## Shadows & Effects

### Window Shadow
- **Box Shadow**: 0px 20px 60px rgba(0, 0, 0, 0.5)

### Button Shadows
- **Default**: None (flat design)
- **Optional**: 0px 2px 4px rgba(0, 0, 0, 0.2) for subtle depth

## Animations

### Button Press
- **Duration**: 100ms
- **Easing**: ease-out
- **Transform**: scale(0.96)

### Display Update
- **Duration**: 200ms
- **Easing**: ease-in-out
- **Fade-in**: New numbers fade in from right

### Operator Selection
- **Duration**: 150ms
- **Easing**: ease-in-out
- **Color transition**: Background and text swap

## Functional Specifications

### Display Behavior
- **Max Digits**: 9 digits before switching to scientific notation
- **Decimal Places**: Up to 6 decimal places displayed
- **Overflow**: Scientific notation (e.g., 1.23e+10)
- **Number Formatting**: Comma separators for thousands

### Button Functions

#### AC (All Clear)
- Resets calculator to initial state (0)
- Clears current operation and history

#### ± (Plus/Minus)
- Toggles sign of current number
- Positive ↔ Negative

#### % (Percent)
- Converts current number to percentage (divides by 100)

#### Operators (÷, ×, -, +)
- Performs previous operation if exists
- Stores operator for next calculation
- Highlights operator button (white background, orange text)

#### = (Equals)
- Executes pending operation
- Displays result
- Clears operator highlight

#### Numbers (0-9)
- Appends digit to current number
- Max 9 digits

#### . (Decimal)
- Adds decimal point
- Only one decimal point allowed per number

## Accessibility

### Keyboard Support
- **Numbers**: 0-9 keys
- **Operators**: +, -, *, / keys
- **Enter/Return**: Execute (=)
- **Escape**: Clear (AC)
- **Backspace**: Delete last digit
- **Tab**: Navigate between buttons

### Screen Reader
- **Labels**: All buttons have aria-labels
- **Live Region**: Display area announces value changes
- **Role**: calculator

## Color Palette Reference

```css
--window-bg: #2D2D2D
--display-text-primary: #FFFFFF
--display-text-secondary: #8E8E93
--button-function-bg: #505050
--button-number-bg: #505050
--button-operator-bg: #FF9F0A
--button-text: #FFFFFF
--button-operator-active-bg: #FFFFFF
--button-operator-active-text: #FF9F0A
--window-control-close: #FF5F57
--window-control-minimize: #FFBD2E
--window-control-maximize: #28C940
```

## Responsive Behavior

### Fixed Size
- Calculator maintains fixed dimensions (280×520px)
- No responsive scaling (maintains pixel-perfect design)
- Center on larger screens

### High DPI Displays
- All assets render at 2× resolution for Retina displays
- Text renders at native resolution
- Buttons remain crisp with vector graphics or high-res assets

## Implementation Notes

### HTML Structure
- Semantic structure with proper ARIA roles
- Button elements for all interactive components
- Separate div for display area

### CSS Approach
- CSS Grid for button layout
- Flexbox for display alignment
- CSS custom properties for theming
- Transitions for interactive states

### JavaScript Behavior
- Event listeners on all buttons
- State management for calculator logic
- Display formatting with Intl.NumberFormat
- Keyboard event handling

---

**Version**: 1.0  
**Last Updated**: May 17, 2026  
**Design Reference**: macOS Calculator (Dark Mode)
