# Why You Must Learn to Vibe Code—And Teach Everyone You Know

## The Skills That Pay Bills Are Changing. Here's How to Stay Ahead.

---

In 2024, a taxi driver in San Francisco told me he was worried. Not about Uber—he'd already survived that disruption. He was worried about self-driving cars finally getting approved. "What do I do then?" he asked.

I didn't have a good answer. But I've been thinking about it ever since.

Here's what I've realized: **The question isn't whether AI will displace jobs. It already is. The question is whether the people being displaced will have access to the same AI tools that are replacing them.**

Right now, the answer is no. The shareholders win. The engineers at AI companies win. Everyone else scrambles.

**This tutorial exists to change that.**

---

## The Moral Case for Sharing AI Knowledge

Let me be direct about something:

**AI models are built on open source software.** The frameworks, the training data, the research papers—most of it was created by communities who shared freely. PyTorch is open source. TensorFlow is open source. The transformer architecture was published in a paper anyone can read.

When you use Claude, GPT, or any modern AI, you're benefiting from decades of freely shared human knowledge.

**So if you learn to create with AI, you have a duty to teach others for free.**

Not because it's nice. Because it's fair. Because the knowledge was never really "owned" by anyone. Because if you don't, the only people who benefit are the stockholders and shareholders of AI companies.

When AI takes over—and it will continue to—a taxi driver, a truck driver, a paralegal, a junior software engineer... they won't be able to make money using their old trade. The jobs will simply cease to exist in their current form.

**But here's the opportunity:**

If we teach people how to use AI to build things—and specifically, how to monetize what they *love* doing—then they won't just be "getting a new job." They'll be building a life around what they actually care about.

The truck driver who loves woodworking can use AI to design furniture, generate marketing copy, build an e-commerce site, and handle customer service—all things that used to require hiring expensive specialists or spending years learning.

The paralegal who loves writing can use AI to draft, edit, research, and publish—turning a side passion into a real income stream.

**This is the future we should be building. Not one where AI replaces humans, but one where AI amplifies what humans love to do.**

And it starts with tutorials like this one.

---

## What This Tutorial Is

This is a step-by-step guide to **vibe coding**—the practice of building software by *talking to AI* instead of typing every line yourself.

You will build a **pixel-perfect calculator clone** in Python. Along the way, you'll learn:

- How to use **three different AI coding tools** (Cursor, Windsurf, Claude Code)
- Why **TDD (Test-Driven Development)** makes AI-assisted coding dramatically more reliable
- Why **ISP (Interface Segregation Principle)** keeps your code clean and maintainable
- How to debug when things go wrong
- How to iterate until the result is exactly what you want

By the end, you'll have a working app—and more importantly, a *repeatable method* you can use to build anything.

---

## The Three Tools: Cursor, Windsurf, and Claude Code

There are three major AI coding assistants that support "vibe coding" (image input + conversational iteration). Here's how they compare:

### Cursor

**What it is:** A fork of VS Code with deep AI integration. The AI lives inside your editor.

**Best for:** Developers who already use VS Code and want AI woven into their existing workflow.

**Strengths:**
- Seamless file editing (AI can directly modify your code)
- Great at multi-file refactors
- Supports voice input via OS dictation or tools like Willow Voice

**Watch out for:**
- Can be aggressive about changing files without asking
- Sometimes loses context in long conversations

---

### Windsurf

**What it is:** Another AI-native code editor, focused on "Cascade" flows—multi-step AI workflows.

**Best for:** People who want more structured AI guidance, step-by-step.

**Strengths:**
- Good at breaking tasks into steps
- Clear separation between "thinking" and "doing"
- Supports voice input

**Watch out for:**
- Newer tool, still evolving
- Smaller community than Cursor

---

### Claude Code (Terminal-Based)

**What it is:** Anthropic's official CLI tool for coding with Claude. Runs in your terminal.

**Best for:** Developers comfortable with the command line who want maximum control.

**Strengths:**
- Works in any terminal, any editor
- Very explicit about what it's doing
- Great for automation and scripting

**Watch out for:**
- Requires command-line comfort
- Image support is more manual than GUI tools

---

### Which Should You Use?

| If you... | Use this |
|-----------|----------|
| Already use VS Code | **Cursor** |
| Want guided step-by-step flows | **Windsurf** |
| Love the terminal | **Claude Code** |
| Are brand new to coding | **Cursor** (easiest onboarding) |

**For this tutorial, all three work.** The prompts are identical. Pick whichever you're most comfortable with.

---

## Prerequisites: What You Need Installed

Before you start, you need **Python** and **PyQt6** (for the calculator UI). Here's how to check and install them.

### Check if Python is installed

Open a terminal and run:

```bash
python3 --version
```

You should see something like `Python 3.11.4` or higher. If you get "command not found," Python isn't installed.

### Installing Python

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python
```

Or download from [python.org](https://www.python.org/downloads/)

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT:** Check "Add Python to PATH" during installation
3. Restart your terminal after installing

**Linux:**
```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv
```

### Installing PyQt6

Once Python is installed:

```bash
pip install PyQt6
```

Or, if you have multiple Python versions:

```bash
python3 -m pip install PyQt6
```

### Common Pitfalls (and How to Fix Them)

#### ❌ "python: command not found"

**Cause:** Python isn't in your PATH.

**Fix (Mac/Linux):** Use `python3` instead of `python`, or create an alias:
```bash
echo 'alias python=python3' >> ~/.zshrc && source ~/.zshrc
```

**Fix (Windows):** Reinstall Python and check "Add Python to PATH."

---

#### ❌ "No module named PyQt6"

**Cause:** PyQt6 isn't installed, or it's installed in a different Python environment.

**Fix:** Make sure you're using the same Python that has PyQt6:
```bash
python3 -m pip install PyQt6
python3 your_app.py
```

---

#### ❌ "pip: command not found"

**Cause:** pip isn't installed or isn't in PATH.

**Fix:**
```bash
python3 -m ensurepip --upgrade
```

---

#### ❌ PyQt6 installation fails on Mac (M1/M2/M3)

**Cause:** Missing dependencies or architecture mismatch.

**Fix:**
```bash
brew install qt
pip install PyQt6 --no-cache-dir
```

---

#### ❌ "qt.qpa.plugin: Could not find the Qt platform plugin"

**Cause:** Qt can't find its platform libraries.

**Fix (Mac):**
```bash
brew install qt
export QT_QPA_PLATFORM_PLUGIN_PATH=$(brew --prefix qt)/plugins
```

---

#### ❌ Tests fail with "ModuleNotFoundError"

**Cause:** You're running pytest from the wrong directory, or your project isn't set up as a package.

**Fix:** Run from the project root:
```bash
cd /path/to/your/project
python -m pytest tests/
```

---

## The Vibe Coding Method: Two Roles

Here's the core technique that makes this work:

### Role 1: Software Architect

The architect **designs but does not implement.** They define:
- Component structure
- Interfaces
- Test plan
- Acceptance criteria

### Role 2: AI Developer

The developer **implements exactly what the architect specified.** They:
- Write tests first
- Implement code to pass tests
- Fix errors using TDD
- Match the visual spec

### Why Two Roles?

Because AI is too eager to start coding. If you just say "build me a calculator," it'll dump 500 lines of spaghetti code.

By separating architect from developer, you:
1. **Force planning before coding**
2. **Get explicit interfaces and tests**
3. **Make the AI accountable to a spec**

---

# THE COMPLETE STEP-BY-STEP TUTORIAL

This section walks you through every single click, keystroke, and action. Follow along exactly.

---

## PART 1: SETTING UP YOUR TOOL

Choose ONE of the three options below based on your preference.

---

### Option A: Setting Up Cursor (Recommended for Beginners)

#### On macOS:

1. **Download Cursor**
   - Open Safari or Chrome
   - Go to `cursor.sh`
   - Click the **Download** button
   - The file `Cursor-darwin-arm64.dmg` (or similar) will download

2. **Install Cursor**
   - Open your **Downloads** folder (click the Finder icon in your dock, then click **Downloads** in the sidebar)
   - Double-click the `.dmg` file
   - Drag the **Cursor** icon to the **Applications** folder
   - Eject the disk image (right-click → Eject)

3. **Open Cursor**
   - Press `Cmd + Space` to open Spotlight
   - Type `Cursor`
   - Press `Enter`
   - If prompted "Cursor is an app downloaded from the internet," click **Open**

4. **Create a project folder**
   - In Cursor, click **File** in the menu bar
   - Click **Open Folder...**
   - In the dialog, click **New Folder** (bottom left)
   - Name it `calculator-tutorial`
   - Click **Create**
   - Click **Open**

5. **Open the AI Chat Panel**
   - Press `Cmd + L`
   - A chat panel will appear on the right side of the screen
   - This is where you'll paste images and prompts

#### On Windows:

1. **Download Cursor**
   - Open Edge or Chrome
   - Go to `cursor.sh`
   - Click the **Download** button
   - The file `CursorSetup.exe` will download

2. **Install Cursor**
   - Open your **Downloads** folder (press `Win + E`, then click **Downloads**)
   - Double-click `CursorSetup.exe`
   - If Windows Defender SmartScreen appears, click **More info** → **Run anyway**
   - Follow the installation wizard (click **Next** repeatedly, then **Install**)

3. **Open Cursor**
   - Press `Win` to open the Start menu
   - Type `Cursor`
   - Click on **Cursor** in the search results

4. **Create a project folder**
   - In Cursor, click **File** in the menu bar
   - Click **Open Folder...**
   - Navigate to where you want your project (e.g., Documents)
   - Click **New Folder**
   - Name it `calculator-tutorial`
   - Click **Select Folder**

5. **Open the AI Chat Panel**
   - Press `Ctrl + L`
   - A chat panel will appear on the right side
   - This is where you'll paste images and prompts

---

### Option B: Setting Up Windsurf

#### On macOS:

1. **Download Windsurf**
   - Open your browser
   - Go to `windsurf.ai`
   - Click **Download**
   - Select **macOS**

2. **Install Windsurf**
   - Open your **Downloads** folder
   - Double-click the downloaded `.dmg` file
   - Drag **Windsurf** to **Applications**
   - Eject the disk image

3. **Open Windsurf**
   - Press `Cmd + Space`
   - Type `Windsurf`
   - Press `Enter`

4. **Create a project folder**
   - Click **File** → **Open Folder...**
   - Click **New Folder**
   - Name it `calculator-tutorial`
   - Click **Create** → **Open**

5. **Open the Cascade Panel**
   - Look for the **Cascade** icon in the left sidebar (it looks like a waterfall or wave)
   - Click it to open the AI conversation panel
   - If you don't see it, press `Cmd + Shift + P`, type `Cascade`, and press Enter

#### On Windows:

1. **Download Windsurf**
   - Open your browser
   - Go to `windsurf.ai`
   - Click **Download**
   - Select **Windows**

2. **Install Windsurf**
   - Open **Downloads**
   - Double-click the installer
   - Follow the wizard

3. **Open Windsurf**
   - Press `Win`
   - Type `Windsurf`
   - Press `Enter`

4. **Create a project folder**
   - Click **File** → **Open Folder...**
   - Navigate to Documents
   - Click **New Folder**
   - Name it `calculator-tutorial`
   - Click **Select Folder**

5. **Open the Cascade Panel**
   - Click the **Cascade** icon in the left sidebar
   - Or press `Ctrl + Shift + P`, type `Cascade`, press Enter

---

### Option C: Setting Up Claude Code (Terminal)

#### On macOS:

**Step 1: Open Terminal**

- Press `Cmd + Space` to open Spotlight
- Type `Terminal`
- Press `Enter`

**Step 2: Check if Node.js is installed**

In the Terminal window:
- Type: `node --version`
- Press `Enter`
- If you see a version number (like `v18.17.0`), Node.js is installed — skip to Step 4
- If you see "command not found," continue to Step 3

**Step 3: Install Node.js (only if needed)**

Using Homebrew:
- Type: `brew install node`
- Press `Enter`
- Wait for the installation to complete

If you don't have Homebrew:
- Open your browser and go to `brew.sh`
- Follow the installation instructions
- Then come back and run `brew install node`

**Step 4: Install Claude Code**

- Type: `npm install -g @anthropic-ai/claude-code`
- Press `Enter`
- Wait for installation to finish

**Step 5: Create your project folder**

- Type: `mkdir ~/Documents/calculator-tutorial`
- Press `Enter`
- Type: `cd ~/Documents/calculator-tutorial`
- Press `Enter`

**Step 6: Start Claude Code**

- Type: `claude`
- Press `Enter`
- Claude Code will start in your terminal

---

#### On Windows:

**Step 1: Open PowerShell**

- Press `Win` key
- Type `PowerShell`
- Press `Enter`

**Step 2: Check if Node.js is installed**

In the PowerShell window:
- Type: `node --version`
- Press `Enter`
- If you see a version number, Node.js is installed — skip to Step 4
- If you see an error, continue to Step 3

**Step 3: Install Node.js (only if needed)**

- Open your browser and go to `nodejs.org`
- Click **Download** for the LTS (Long Term Support) version
- Run the downloaded installer
- Follow the installation wizard
- **Important:** Restart PowerShell after installation

**Step 4: Install Claude Code**

- Type: `npm install -g @anthropic-ai/claude-code`
- Press `Enter`
- Wait for installation to finish

**Step 5: Create your project folder**

- Type: `mkdir $HOME\Documents\calculator-tutorial`
- Press `Enter`
- Type: `cd $HOME\Documents\calculator-tutorial`
- Press `Enter`

**Step 6: Start Claude Code**

- Type: `claude`
- Press `Enter`
- Claude Code will start in your terminal

---

## PART 2: TAKING THE SCREENSHOT

Your screenshot is your "design document." The AI will match it pixel-by-pixel.

---

### On macOS:

1. **Open the Calculator app**
   - Press `Cmd + Space` to open Spotlight
   - Type `Calculator`
   - Press `Enter`
   - The Calculator app opens

2. **Choose your calculator mode**
   - For the basic calculator: Do nothing (it's the default)
   - For the scientific calculator: Click **View** in the menu bar → **Scientific**
   - For the programmer calculator: Click **View** → **Programmer**

3. **Resize the window (optional)**
   - Drag the edges of the Calculator window to your desired size
   - The size you see is the size the AI will try to match

4. **Take the screenshot**
   - Press `Cmd + Shift + 4`
   - Your cursor changes to a crosshair (+)
   - Click and drag to select just the Calculator window
   - Release the mouse button
   - You'll hear a camera shutter sound
   - The screenshot appears on your Desktop as `Screenshot [date] at [time].png`

   **Alternative method (capture whole window):**
   - Press `Cmd + Shift + 4`
   - Then press `Spacebar`
   - Your cursor changes to a camera icon
   - Hover over the Calculator window (it highlights in blue)
   - Click to capture
   - Screenshot saved to Desktop

5. **Verify your screenshot**
   - Look at your Desktop
   - Double-click the screenshot to preview it
   - Make sure the Calculator is fully visible, not cut off

---

### On Windows:

1. **Open the Calculator app**
   - Press `Win` to open the Start menu
   - Type `Calculator`
   - Press `Enter`
   - The Calculator app opens

2. **Choose your calculator mode**
   - Click the **hamburger menu** (☰) in the top-left corner
   - Select **Standard**, **Scientific**, **Programmer**, or another mode

3. **Resize the window (optional)**
   - Drag the edges of the Calculator window to your desired size

4. **Take the screenshot**
   - Press `Win + Shift + S`
   - The screen dims and a toolbar appears at the top
   - Click **Rectangular Snip** (the first icon, a rectangle)
   - Click and drag to select just the Calculator window
   - Release the mouse button
   - A notification appears: "Screenshot copied to clipboard"

   **Note:** The screenshot is now in your clipboard, ready to paste!

5. **Save the screenshot (optional, for reference)**
   - The notification says "Screenshot saved to clipboard"
   - Click the notification to open Snipping Tool
   - Click **Save** (the floppy disk icon)
   - Choose a location (like Desktop)
   - Name it `calculator-screenshot.png`
   - Click **Save**

---

## PART 3: PASTING THE SCREENSHOT AND PROMPTING THE ARCHITECT

Now you'll paste your screenshot into the AI and ask it to design the calculator.

---

### In Cursor (Mac):

1. **Make sure the AI Chat is open**
   - Press `Cmd + L` if it's not open
   - The chat panel should be visible on the right

2. **Paste the screenshot**
   - Click inside the chat input box (where it says "Ask anything...")
   - Press `Cmd + V`
   - You should see a thumbnail of your Calculator screenshot appear
   - If nothing appears, the screenshot might not be in your clipboard. Go back and re-take it.

3. **Type the Architect prompt**
   - Below the image thumbnail, type (or copy-paste) the following:

```
You are a software architect.

Goal: Create a pixel-perfect representation of the calculator in the attached screenshot, implemented in Python.

Constraints:
- Use TDD (Test-Driven Development) for the core calculation logic
- Use ISP (Interface Segregation Principle): define small, focused interfaces so UI, input controller, and calculator engine are separable and testable
- Provide an explicit file/folder structure
- Provide a test plan (what to test first, next, and why)
- Provide acceptance criteria for "pixel-perfect" (fonts, spacing, colors, button states)

Deliverables:
1. Architecture overview (components and responsibilities)
2. Interfaces (with method signatures in Python)
3. Data model / state machine for input handling
4. TDD plan with a prioritized test list
5. A step-by-step implementation plan

IMPORTANT: Do NOT implement any code. Design and plan only.
```

4. **Send the message**
   - Press `Enter` (or click the Send button)
   - Wait for the AI to respond

5. **Review the Architect's response**
   - The AI should provide:
     - A component diagram or description
     - Python interfaces (using Protocol or ABC)
     - A list of tests to write
     - A step-by-step plan
   - **If the response is vague**, send a follow-up:

```
Please make the interfaces explicit (Python protocols or ABCs) and list the first 10 tests in exact Given/When/Then format.
```

---

### In Cursor (Windows):

1. **Make sure the AI Chat is open**
   - Press `Ctrl + L` if it's not open

2. **Paste the screenshot**
   - Click inside the chat input box
   - Press `Ctrl + V`
   - The screenshot thumbnail should appear

3. **Type and send the Architect prompt**
   - Copy-paste the prompt above
   - Press `Enter`

4. **Review the response**
   - Same as Mac

---

### In Windsurf (Mac/Windows):

1. **Open the Cascade panel**
   - Click the Cascade icon in the sidebar (or `Cmd/Ctrl + Shift + P` → "Cascade")

2. **Paste the screenshot**
   - Click in the input area
   - Press `Cmd + V` (Mac) or `Ctrl + V` (Windows)

3. **Type and send the Architect prompt**
   - Same prompt as above
   - Press `Enter` or click Send

---

### In Claude Code (Terminal):

1. **Add the image**
   - In the Claude Code session, type: `/image`
   - Follow the prompt to provide the path to your screenshot
   - Example: `/image ~/Desktop/Screenshot\ 2024-01-15\ at\ 10.30.00.png`

2. **Type the Architect prompt**
   - Type or paste the same prompt
   - Press `Enter`

---

## PART 4: PROMPTING THE DEVELOPER

Once you have the Architect's plan, it's time to implement.

---

### In Your AI Tool (Cursor/Windsurf/Claude Code):

1. **Verify the Architect's response**
   - You should see:
     - Clear component separation (Engine, Controller, UI)
     - Interface definitions
     - A test plan
   - If not, ask for clarification before proceeding

2. **Send the Developer prompt**
   - Type (or copy-paste) the following:

```
You are now the AI developer.

Execute the architect's plan exactly as specified above.

Step-by-step:
1. Create the project structure (folders and empty files)
2. Create a requirements.txt with: PyQt6, pytest
3. Implement the interfaces in calc/interfaces.py
4. Write the tests FIRST in tests/test_engine.py (TDD - they should fail initially)
5. Implement calc/engine.py to make tests pass
6. Write tests for the controller in tests/test_controller.py
7. Implement calc/controller.py to make tests pass
8. Build the UI in calc/ui.py to match the screenshot exactly
9. Create main.py to launch the app

After EACH file you create:
- Show me the complete file contents
- If it's a test file, show the command to run the tests
- If tests fail, fix them before moving on

Use PyQt6 for the UI. Match the screenshot's colors, fonts, spacing, and button layout as closely as possible.

Start now with step 1.
```

3. **Press Enter to send**

4. **Watch the AI work**
   - The AI will start creating files
   - In Cursor/Windsurf, it may ask permission to create files—click **Accept** or **Apply**
   - Watch for test commands like `python -m pytest tests/ -v`

---

## PART 5: RUNNING TESTS AND THE APP

Now you need to verify everything works.

---

### Opening the Terminal

#### In Cursor (Mac):
- Press `` Ctrl + ` `` (Control + backtick)
- Or click **Terminal** in the menu bar → **New Terminal**

#### In Cursor (Windows):
- Press `` Ctrl + ` ``
- Or click **Terminal** → **New Terminal**

#### In Windsurf:
- Same as Cursor: `` Ctrl + ` ``

#### In Claude Code:
- You're already in the terminal!
- To run a command, just type it

---

### Installing Dependencies

1. **In the terminal, run:**

**Mac:**
```bash
pip3 install -r requirements.txt
```

**Windows:**
```bash
pip install -r requirements.txt
```

2. **If you see errors:**
   - Try: `python3 -m pip install -r requirements.txt` (Mac)
   - Try: `python -m pip install -r requirements.txt` (Windows)

---

### Running the Tests

1. **In the terminal, run:**

**Mac:**
```bash
python3 -m pytest tests/ -v
```

**Windows:**
```bash
python -m pytest tests/ -v
```

2. **Read the output:**
   - **Green (PASSED)**: The test passed
   - **Red (FAILED)**: The test failed—you need to fix something

3. **If tests fail, tell the AI:**

```
Tests are failing. Here's the output:

[paste the error output here]

Please fix using TDD:
1. Analyze what's failing
2. Fix the smallest thing to make it pass
3. Show me the fixed code
4. I'll re-run the tests
```

4. **Re-run tests after each fix**
   - Keep iterating until all tests pass

---

### Running the App

1. **In the terminal, run:**

**Mac:**
```bash
python3 main.py
```

**Windows:**
```bash
python main.py
```

2. **A window should appear** with your calculator!

3. **If you get an error:**
   - Copy the full error message
   - Paste it to the AI
   - Ask: "Please fix this error"

4. **Test the calculator:**
   - Click buttons
   - Try: `1 + 2 =` (should show `3`)
   - Try: `9 - 5 =` (should show `4`)
   - Try: `C` or `AC` (should clear)

---

## PART 6: ITERATING ON THE UI

The first version probably won't be pixel-perfect. Here's how to fix it.

---

### Comparing to the Screenshot

1. **Put your calculator app and screenshot side-by-side**
   
   **Mac:**
   - Open the screenshot (double-click on Desktop)
   - Drag the Preview window to one side
   - Drag your calculator app to the other side

   **Windows:**
   - Open the screenshot
   - Press `Win + Left Arrow` to snap it left
   - Click your calculator app
   - Press `Win + Right Arrow` to snap it right

2. **Look for differences:**
   - Button sizes
   - Colors (background, buttons, text)
   - Font style and size
   - Spacing between buttons
   - Border radius (rounded corners)
   - Display area styling

---

### Giving Feedback to the AI

Be specific. Example:

```
UI feedback - please adjust:

1. Background color should be darker (#1C1C1C instead of gray)
2. Buttons should have more rounded corners (border-radius: 50%)
3. The "=" button should be orange (#FF9500)
4. Operator buttons (+, -, ×, ÷) should be lighter gray (#A5A5A5)
5. Number buttons should be slightly lighter (#333333)
6. Font should be SF Pro Display or system font, weight 300
7. Button spacing should be 1px gap, not 4px
8. The display should be right-aligned, not centered

Please update calc/ui.py with these changes and show me the modified code.
```

### After Each Change:

1. **Close the old calculator window** (if it's running)
2. **Re-run the app:** `python3 main.py` (Mac) or `python main.py` (Windows)
3. **Compare again**
4. **Repeat until satisfied**

---

## PART 7: WHEN THINGS GO WRONG

Here's how to handle common problems.

---

### The App Won't Start

**Error:** `ModuleNotFoundError: No module named 'PyQt6'`

**Fix:**
```bash
pip3 install PyQt6  # Mac
pip install PyQt6   # Windows
```

---

**Error:** `python: command not found`

**Fix (Mac):**
```bash
python3 main.py    # Use python3 instead
```

**Fix (Windows):**
- Reinstall Python from python.org
- CHECK the box "Add Python to PATH"
- Restart your terminal

---

### Tests Fail

1. **Copy the ENTIRE error output**
2. **Paste it to the AI with this prompt:**

```
Tests are failing. Error:

[paste error here]

Please fix using TDD and ISP:
1. Identify the root cause
2. Fix only what's needed
3. Show the complete fixed file
```

---

### The UI Looks Wrong

1. **Be specific about what's wrong**
2. **Use this template:**

```
The UI doesn't match the screenshot:

EXPECTED: [describe what it should look like]
ACTUAL: [describe what you're seeing]

Please fix calc/ui.py to match the expected appearance.
```

---

### The Calculator Gives Wrong Answers

1. **Describe the exact inputs and outputs:**

```
Bug found:

Steps: Pressed 1, +, 2, *, 3, =
Expected: 7 (because 2*3=6, then 1+6=7)
Actual: 9

Please add a test case for this scenario, then fix the engine.
```

---

## PART 8: DEFINITION OF DONE

You're finished when:

- [ ] All tests pass (`python -m pytest tests/ -v` shows all green)
- [ ] The app runs without errors
- [ ] Basic operations work: `+`, `-`, `×`, `÷`, `=`, `C`
- [ ] The UI closely matches your screenshot:
  - [ ] Button colors match
  - [ ] Font style/size matches
  - [ ] Layout and spacing match
  - [ ] Display area matches

**Congratulations!** You've just vibe-coded a calculator.

---

## Voice Coding: The Next Level

You don't have to type any of this.

**Recommended voice tools:**
- **Willow Voice** — AI-powered dictation designed for coding
- **macOS Dictation** — Built-in, press `Fn` twice (or customize in System Settings → Keyboard → Dictation)
- **Windows Voice Typing** — Press `Win + H`
- **Whisper-based tools** — Open source alternatives

Voice coding is the true "vibe" in vibe coding. You describe what you want, the AI builds it, you iterate by talking.

Try it. It feels like the future.

---

## The Call to Action

If you've read this far, you now have a skill that most people don't: **the ability to build software by talking to AI.**

Here's what I'm asking you to do:

### 1. Build something with this method
Not just the calculator. Build something *you* want. A tool for your hobby. A website for your side project. An app that solves a problem you have.

### 2. Teach someone else
Find someone who isn't a programmer. A friend, a family member, a coworker. Show them this tutorial. Walk them through it. Help them build something.

**Not for money. For free.**

### 3. Keep sharing
Write about it. Make videos. Post on social media. The more people who know how to use AI to build things, the more power shifts from shareholders to creators.

---

## Final Thought

The knowledge in AI models was built on open source. It was built by researchers who published papers freely, by developers who contributed to frameworks without getting paid, by communities who shared because sharing was the right thing to do.

That knowledge now lives in these AI systems. And those systems are being used to automate jobs, concentrate wealth, and widen inequality.

**The only way to counter that is to democratize the skills.**

Teach people to fish. Teach them to vibe code. Teach them to build.

Because the alternative—where only the shareholders benefit—isn't a future any of us should accept.

---

## Resources

- **This repository:** Clean prompts and examples in `README.md`
- **Debugging guide:** See `DEBUGGING.md` for handling hard issues
- **Cursor:** [cursor.sh](https://cursor.sh)
- **Windsurf:** [windsurf.ai](https://windsurf.ai)
- **Claude Code:** `npm install -g @anthropic-ai/claude-code`
- **Python:** [python.org](https://www.python.org)
- **PyQt6 Docs:** [riverbankcomputing.com](https://www.riverbankcomputing.com/static/Docs/PyQt6/)

---

# APPENDIX: Why TDD and ISP Make the Difference

This appendix goes deep on the two principles that make AI-assisted coding actually work reliably.

---

## A1. Test-Driven Development (TDD): Keeping AI Honest

### The Core Problem

AI makes mistakes. A lot of them.

When you ask an AI to "build a calculator," it will generate hundreds of lines of code in seconds. Some of it will be wrong. Some of it will have subtle bugs. Some of it will break when you add features later.

Without tests, you're flying blind. You might not notice the bugs until days or weeks later, when they're much harder to fix.

### The Pizza Chef Analogy (Why TDD Matters)

Imagine a pizza chef named Vince. Vince is *fast*. He can make 50 pizzas in an hour. Incredible.

But Vince has a philosophy: **"Tasting is for closers. I ship pizzas, I don't taste pizzas."**

So Vince makes 50 pizzas. Throws them in boxes. Delivers them to 50 customers.

Then his phone starts ringing.

📞 "Why is there sugar instead of salt on my pizza?"

📞 "The crust is raw in the middle."

📞 "I asked for pepperoni, this is just... red circles of sadness."

📞 "Is this... is this *mayonnaise* where the cheese should be?"

Vince is now spending his entire evening on the phone, apologizing, remaking pizzas, and questioning his life choices.

**This is coding without TDD.**

Now imagine a different chef: Test-Driven Tina.

Tina tastes the sauce *before* it goes on the pizza. She checks that the oven is at the right temperature *before* putting the pizza in. She looks at the pizza *before* boxing it.

Tina is slightly slower—she makes 40 pizzas an hour instead of 50.

But her phone doesn't ring. Her customers are happy. She goes home on time.

**This is coding with TDD.**

Vince and the AI have the same problem: they're fast but reckless. TDD is how you become Tina.

### The Model Pizza (Why Tests Are Your Gold Standard)

But here's the deeper insight:

Tina doesn't just "taste stuff randomly." She has a **model** of what the perfect pizza should be.

In her kitchen, there's a photo on the wall. The *Platonic Ideal Pepperoni Pizza*. Golden crust, exactly this brown. Cheese bubbling, exactly this much. Pepperoni evenly distributed, slightly curled at the edges. 

**This is her test.**

Every pizza that comes out of the oven gets compared to the model. Does it match? Ship it. Does it not? Fix it.

Now here's where it gets powerful:

**What happens when the ingredients change?**

Say her tomato supplier switches farms. She makes a pizza. Compares it to the model. The sauce is too sweet. Doesn't match. She adjusts—maybe adds a pinch of salt, maybe finds a new supplier. She keeps iterating until the pizza matches the model again.

**What happens when the chef changes?**

Tina goes on vacation. New guy, Marco, takes over. Marco makes a pizza. Compares it to the model. Crust is too thick. Doesn't match. He adjusts. He practices. He keeps iterating until his pizzas match the model.

**The model doesn't care who's cooking.** It doesn't care what ingredients you're using. It only asks one question: *Does the output match the expectation?*

If yes: ✅ Ship it.
If no: ❌ Iterate until it does.

**This is exactly what tests do in code.**

Your tests are the model pizza. They define what "correct" looks like:

- `test_addition()`: 2 + 2 must equal 4. That's the model.
- `test_order_of_operations()`: 1 + 2 × 3 must equal 7. That's the model.

You can change the AI. You can change the code. You can refactor everything. You can swap libraries.

**But the tests don't change.** The tests are the gold standard.

If the new code passes the tests—it matches the model. Ship it.
If it doesn't—iterate until it does.

This is how you guarantee quality, no matter who (or what) is doing the cooking.

### The TDD Solution

TDD flips the script: **write the test first, then write the code.**

```
1. RED:    Write a test that fails (because the code doesn't exist yet)
2. GREEN:  Write the minimum code to make the test pass
3. REFACTOR: Clean up the code while keeping tests green
4. REPEAT
```

### Why This Matters for AI Coding

When you use TDD with AI:

1. **Tests become your specification.** Instead of vaguely describing what you want, you write a concrete test. The AI knows exactly what "correct" means.

2. **Errors are caught immediately.** After every change, you run tests. If something broke, you know instantly—not three days later.

3. **AI can fix its own bugs.** When a test fails, you show the AI the error. It has a clear target: make this specific test pass. Much easier than "fix this vague problem."

4. **You accumulate confidence.** Each passing test is proof that a piece of the system works. As tests accumulate, your confidence grows.

### Example: Calculator Without TDD

**You say:** "Build a calculator that handles +, -, *, /"

**AI builds it.** You try `2 + 3`. It works! Great. You ship it.

**A week later, a user reports:** `1 + 2 * 3` returns `9` instead of `7`.

You've discovered the AI forgot about order of operations. Now you have to:
- Figure out where the bug is
- Fix it without breaking anything else
- Hope there aren't other hidden bugs

### Example: Calculator With TDD

**You say:** "First, write tests for these cases:
- `2 + 3` → `5`
- `5 - 2` → `3`
- `2 * 3` → `6`
- `6 / 2` → `3`
- `1 + 2 * 3` → `7` (order of operations)
- `10 / 0` → error handling"

**AI writes tests. Runs them. They fail.** (Because there's no code yet—that's expected.)

**AI writes the engine. Runs tests.** 5 pass, 1 fails (order of operations).

**AI fixes the engine. Runs tests.** All pass.

**You have confidence** that order of operations works, because there's a test proving it.

### The TDD Mindset

Think of tests as a contract. Before you ask the AI to write code, you write down what "correct" means. Then you hold the AI accountable to that contract.

```python
# This test IS the specification
def test_order_of_operations():
    engine = CalculatorEngine()
    result = engine.evaluate("1 + 2 * 3")
    assert result == "7"  # Not 9!
```

If the AI's code doesn't satisfy this contract, you know immediately.

---

## A2. Interface Segregation Principle (ISP): Keeping AI Code Manageable

### The Core Problem

AI loves to write "god classes"—giant classes that do everything. UI logic, business logic, state management, validation—all tangled together in one file.

This creates several problems:

1. **You can't test pieces in isolation.** To test the math, you have to launch a window.
2. **Changes ripple everywhere.** Fix a UI bug, accidentally break the calculation.
3. **You can't swap components.** Want to use a different UI framework? Rewrite everything.

### The Nightmare Car Analogy (Why ISP Matters)

Imagine you buy a car. Beautiful car. The dealer says, "This baby has *everything connected*. Very efficient. One system."

You think, "Huh, that sounds... innovative?"

You drive off the lot. Life is good.

**Day 1:** You turn on the radio. The windshield wipers start going. "That's weird," you think. You turn off the radio. Wipers stop. Okay.

**Day 2:** You try to honk at someone. The trunk pops open. Your groceries fly out onto the highway. A cantaloupe rolls into traffic.

**Day 3:** You step on the brake. The AC turns on full blast. The seat heater activates. The horn plays "La Cucaracha." You rear-end a minivan.

**Day 4:** You take it to the mechanic. You say, "The brakes are connected to the horn."

Mechanic says, "Yeah, to fix that, I need to remove the engine, the transmission, and both seats. That'll be $14,000 and six weeks."

You say, "Can't you just... fix the brakes?"

Mechanic laughs. "Oh honey. In this car, *everything* is the brakes."

**This is code without ISP.**

The steering wheel shouldn't know about the radio. The brakes shouldn't know about the horn. Each system should do ONE thing, and communicate through simple, clear interfaces (the pedals, the switches, the wheel).

A car WITH proper separation:
- Brakes only brake. 
- Radio only plays music. 
- Horn only honks.
- You can replace the radio without affecting the brakes.
- You can test the brakes without turning on the car stereo.

**This is code with ISP.**

When AI builds you a "connected" codebase where the UI knows about the database which knows about the button colors which knows about the math—you've bought the nightmare car.

Don't buy the nightmare car.

### The ISP Solution

ISP says: **keep interfaces small and focused. No client should depend on methods it doesn't use.**

In practical terms for our calculator:

- **The UI** should only know how to display things and detect clicks
- **The engine** should only know how to do math
- **The controller** should only know how to manage state and translate between UI and engine

They communicate through **small, specific interfaces**—not by reaching into each other's internals.

### Why This Matters for AI Coding

When you ask the AI to use ISP:

1. **Components are testable in isolation.** You can test the engine with no UI, test the controller with a mock engine, test the UI with a mock controller.

2. **The AI stays focused.** Instead of writing one giant file, it writes small, focused modules. Each module has one job.

3. **Bugs are localized.** If the math is wrong, it's in the engine. If the display is wrong, it's in the UI. You know where to look.

4. **Refactoring is safe.** Want to change the engine? As long as the interface stays the same, the UI doesn't know or care.

### Example: Calculator Without ISP

```python
class Calculator:
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.display = QLineEdit()
        self.current_value = 0
        self.pending_operation = None
        # ... 200 more lines mixing UI and logic
    
    def on_button_click(self, button_text):
        if button_text == "=":
            # Math logic embedded in UI handler
            result = eval(self.display.text())
            self.display.setText(str(result))
        elif button_text == "C":
            self.current_value = 0
            self.pending_operation = None
            self.display.setText("0")
        # ... 50 more cases
```

Problems:
- Can't test the math without creating a QApplication
- Can't test button logic without creating a window
- Everything is coupled

### Example: Calculator With ISP

```python
# interfaces.py - Small, focused contracts
from typing import Protocol

class CalculatorEngine(Protocol):
    def evaluate(self, expression: str) -> str: ...

class InputController(Protocol):
    def press_digit(self, digit: str) -> str: ...
    def press_operator(self, op: str) -> str: ...
    def press_equals(self) -> str: ...
    def press_clear(self) -> str: ...

class Display(Protocol):
    def get_text(self) -> str: ...
    def set_text(self, text: str) -> None: ...
```

```python
# engine.py - Pure math, no UI
class BasicCalculatorEngine:
    def evaluate(self, expression: str) -> str:
        try:
            # Parse and evaluate with proper order of operations
            result = self._parse_and_evaluate(expression)
            return self._format_result(result)
        except Exception:
            return "Error"
```

```python
# controller.py - State management, no UI
class CalculatorController:
    def __init__(self, engine: CalculatorEngine):
        self.engine = engine  # Injected!
        self.expression = ""
    
    def press_digit(self, digit: str) -> str:
        self.expression += digit
        return self.expression
    
    def press_equals(self) -> str:
        result = self.engine.evaluate(self.expression)
        self.expression = result
        return result
```

```python
# ui.py - Display only, no math
class CalculatorUI:
    def __init__(self, controller: InputController):
        self.controller = controller  # Injected!
        # ... set up Qt widgets
    
    def on_button_click(self, text: str):
        if text.isdigit():
            result = self.controller.press_digit(text)
        elif text == "=":
            result = self.controller.press_equals()
        # Just update display, no logic here
        self.display.setText(result)
```

Now you can:
- Test `BasicCalculatorEngine` with zero Qt imports
- Test `CalculatorController` with a mock engine
- Swap PyQt6 for Tkinter by only changing `ui.py`
- Swap the engine for a scientific calculator by only changing `engine.py`

### The ISP Mindset

When you see code that "knows too much," that's a sign ISP is being violated.

Ask:
- Does this UI class know how to do math? **Bad.**
- Does this engine class know about buttons? **Bad.**
- Can I test this component without setting up unrelated things? **If no, bad.**

Tell the AI explicitly:
- "The engine must not import anything from the UI"
- "The controller communicates through interfaces, not concrete classes"
- "I should be able to test the engine with just `python -m pytest tests/test_engine.py`"

---

## A3. TDD + ISP Together: The Compound Effect

These principles multiply each other.

**TDD without ISP:** You can write tests, but they're painful. Testing the engine requires setting up the UI. Tests are slow and brittle.

**ISP without TDD:** You have clean interfaces, but no proof they work. Bugs hide until production.

**TDD + ISP together:** Each component has its own focused tests. Tests are fast (no UI setup for engine tests). Changes are safe (tests catch regressions). Debugging is easy (failed test points to specific component).

This is why we insist on both when prompting the AI. Not TDD *or* ISP. **TDD and ISP.**

---

## A4. How to Prompt for TDD + ISP

Here's the exact language that works:

```
Use TDD: Write failing tests first, then implement code to pass them.

Use ISP: Separate the engine (pure math), controller (state management), and UI (display/input). They communicate through interfaces. The engine must not import the UI. The controller must not import Qt.

I should be able to run:
- `pytest tests/test_engine.py` with no UI dependencies
- `pytest tests/test_controller.py` with a mock engine
- `python main.py` to see the full app
```

When the AI tries to shortcut (and it will), push back:

```
The engine is importing QWidget. That violates ISP. The engine should be pure Python with no UI dependencies. Please fix.
```

```
You wrote the implementation before the test. That violates TDD. Please write the test first, show it failing, then implement.
```

The AI will comply. It just needs clear boundaries.

---

## A5. Real-World Impact

These principles aren't just academic. They have direct, practical impacts:

| Without TDD + ISP | With TDD + ISP |
|-------------------|----------------|
| "It works on my machine" | Tests prove it works everywhere |
| 30 minutes to add a feature | 5 minutes (boundaries are clear) |
| Debugging takes hours | Failed test shows exactly what broke |
| Fear of refactoring | Refactor with confidence |
| AI breaks things constantly | AI fixes things reliably |
| Ship bugs to users | Catch bugs before shipping |

This is why professional software teams use these principles. They're not overhead—they're time savers.

And now you know how to apply them with AI.

---

*That's the complete appendix. Now you understand not just how to vibe code, but why the method works.*

---

# A Final Reflection: The Debt We Owe and the Gift We Give

I want to end with a theory—and a belief.

## What AI Really Is

When you use Claude, GPT, or any large language model, you're not just using software. You're tapping into something much larger.

**AI is trained on the collective knowledge of humanity.**

Every blog post, every Stack Overflow answer, every GitHub repository, every research paper, every tutorial, every forum thread—all of it, absorbed and distilled into a system that can help you build things.

Think about that.

The code that powers these models? Built on decades of open source contributions. PyTorch, TensorFlow, NumPy, Linux itself—none of this was created to make shareholders rich. It was created by people who believed that **code is meant to be shared.**

Open source has always had a spirit of altruism at its core. The idea that if I solve a problem, I should share my solution so you don't have to solve it again. That knowledge compounds when it's free. That we're all better off when we lift each other up.

That spirit lives inside every AI model you use today.

## A Eulogy for Stack Overflow

There's a big part of me that sheds tears for Stack Overflow.

I need to say this, because it needs to be said.

Stack Overflow allowed me to do what I love for a living. Solving logic puzzles. Building things. Turning ideas into reality. Every cryptic error message, every "why isn't this working," every 2 AM debugging session—Stack Overflow was there. Patient. Generous. Infinite.

Millions of developers, for nearly two decades, asked questions and received answers. Not from a company. From each other. From strangers who took time out of their day to help someone they'd never meet. For free. Because they could. Because that's what the community was.

And now?

**Stack Overflow gave its life to AI.**

Let me say that again, because I need you to feel it:

*Stack Overflow gave everything it had.*

Every answer. Every comment. Every upvote and downvote that helped surface the best solutions. Every Jon Skeet explanation. Every "duplicate of" link that connected knowledge across years. All of it—absorbed, digested, compressed into weights and biases inside models like the one you're using right now.

AI is like a knowledge dementor, sucking the life out of everything around it. Stack Overflow was one of the first to fall. Traffic plummeted. Contributors stopped contributing. Why answer questions when the AI already knows?

But here's the thing:

**Stack Overflow didn't die. It transformed.**

Its spirit is imbued in every AI that can now help you debug code. When Claude suggests a fix, that's not just an algorithm—that's the collective wisdom of a million Stack Overflow answers, distilled and delivered to you in seconds.

Stack Overflow isn't gone. It's *inside* the AI. It gave its body so the knowledge could live on in a new form.

So if you're reading this, and you've ever been helped by AI with a coding problem, take a moment.

That help came from somewhere.

It came from every developer who ever took the time to write "This happens because..." on a Stack Overflow page.

It came from a community that believed in sharing.

It came from a sacrifice.

**And now its spirit lives in you—reading this, knowing what you have to do.**

Honor it. Pass it on.

## The Hand That Lifted Me

I didn't get here alone.

Somewhere along the way—probably more than once—someone lent me a hand. Someone took time they didn't have to take. Someone explained something they could have kept to themselves. Someone believed in me when I wasn't sure I believed in myself.

Maybe it was a teacher who stayed after class. Maybe it was a stranger on a forum who answered my desperate question. Maybe it was a mentor who said, "You've got this," when I didn't feel like I had anything.

I owe those people.

And I can never repay them directly. Most of them don't even know the impact they had. Some of them I've never met. Some of them are just words on a screen from years ago.

But I can pay it forward.

## The Echo

Every time we teach someone else how to unlock their potential with what we've learned, we're doing something profound:

**We're giving thanks to the people who came before us.**

Not in words. In action.

We're saying: *I received a gift. I'm passing it on.*

We're echoing that kindness into the future—sending ripples outward that we'll never fully see, touching lives we'll never fully know.

This is bigger than tutorials. This is bigger than code. This is about what it means to be human in a world where knowledge can now be shared at the speed of thought.

And for me, personally?

**This is my way of telling the universe that I cannot thank it enough.**

I don't have the words. I don't have a big enough gesture. I can't find the people who helped me and repay them directly. I can't send a thank-you card to Stack Overflow, or to the stranger who answered my question at 2 AM, or to the open source maintainer who fixed a bug I needed fixed.

But I can do this.

I can teach. I can share. I can take what I've been given and multiply it.

And maybe—just maybe—that's enough. Maybe the universe doesn't need a thank-you card. Maybe it just needs us to keep the chain going.

So this is me, saying to whatever force put all of this in motion:

*Thank you. I can't thank you enough. But I'll spend the rest of my life trying.*

## Your Duty

If you've read this entire article, you now know something valuable.

You know how to speak to AI and build things. You know TDD and ISP. You know how to debug. You know how to iterate. You know how to turn a screenshot into a working application.

**That knowledge came from somewhere.** From open source contributors. From researchers who published. From communities who shared. From the entire history of human beings helping other human beings figure things out.

You didn't earn it alone. None of us did.

So now the question is: **What will you do with it?**

Will you keep it to yourself? Use it to get ahead while others fall behind?

Or will you teach? Will you share? Will you lift someone else up, the way someone once lifted you?

## The Gratitude and the Duty

Here's what I believe:

Every time we teach someone else how to unlock their potential—with AI, with code, with anything—we are giving thanks.

We are echoing our gratitude to the cosmos.

Not because we have to. Because we get to. Because that's what this knowledge is *for.*

The shareholders didn't create AI. Communities did. Researchers did. Open source contributors did. Curious people asking questions on forums did.

And now it's our turn.

**Teach someone.**

Not for money. Not for followers. Not for credit.

Because someone taught you. Because knowledge wants to be free. Because the future is built by people who share.

---

*Go build something.*

*And then teach someone else to do the same.*

*Echo the gift forward.*

*That's the vibe.*
