# AI Development for Absolute Beginners: Build Real Software in One Hour

## This is not a sales pitch. This is your tutorial.

I don't want anything from you. Give me one hour and follow along step by step.

By the end, you'll have built real software—a working calculator app—even if you've never written code before.

**Let's start building right now.**

---

## Step 1: Install Cursor (15 minutes)

**Watch and follow along:** https://www.loom.com/share/b6e2d33d3df54aa1b57deefea90fe0c1

This video shows you:
- Download Cursor IDE (free)
- Install Python
- Take a screenshot of what you want to build

**Pause the video and do each step.** Come back when Cursor is installed and you have your screenshot.

---

## Step 2: Your First Prompt - The Specification Writer

Now paste your screenshot into Cursor's chat and send this prompt:

```
You are a specification writer. Write detailed specifications for <what you want>. 
Write it in markdown in the root folder.
```

**Replace `<what you want>` with YOUR project:**
- "a pixel-perfect representation of this calculator screenshot"
- "a todo list app with categories and due dates"
- "a simple budgeting tool to track expenses"
- "a note-taking app with search functionality"

**Example:**
```
You are a specification writer. Write detailed specifications for a pixel-perfect 
representation of this calculator screenshot. Write it in markdown in the root folder.
```

**Press Enter.** Watch the AI create a detailed specification document.

### What Just Happened?

The AI analyzed your screenshot (or description) and created a complete specification—every button, color, behavior, and feature documented in detail.

This is your blueprint. Everything we build will refer back to this.

**Check the file:** Look in your folder for `CALCULATOR_SPEC.md` (or similar). Open it. That's your specification.

---

## Step 3: Your Second Prompt - The Software Architect

Now send this prompt:

```
You are a software architect. Let us read the specifications, and let us create an 
implementation plan where we use <tech>, utilize TDD and ISP, do not overcomplicate. 
Write the implementation plan as a markdown.
```

**Replace `<tech>` with your tech stack:**
- "Python with PyQt6 for the UI"
- "Node.js with Express and React"
- "Rust with a CLI interface"
- "Python with FastAPI for a REST API"

**For the calculator example:**
```
You are a software architect. Let us read the specifications, and let us create an 
implementation plan where we use Python with PyQt6 for the UI, utilize TDD and ISP, 
do not overcomplicate. Write the implementation plan as a markdown.
```

**Press Enter.** Watch the AI create a complete implementation plan.

### What Just Happened?

The AI just:
- Designed the entire architecture
- Broke the project into phases
- Defined what to test
- Created a step-by-step build plan
- Estimated time for each phase

**Check the file:** Look for `IMPLEMENTATION_PLAN.md`. Open it. That's your roadmap.

---

## Step 4: The Full Build - Watch and Code Along (45 minutes)

**Watch this video:** https://www.loom.com/share/8e0e2f44b9784612ae38600002b85039

This video shows:
- **Prompt 3:** Setting up your environment (dependencies, tools, Cursor rules)
- **Prompt 4:** Building the entire application step-by-step with TDD

**Code along with the video.** Pause when you need to. You'll see:
- How to handle errors (they happen, it's normal)
- How tests work (write tests first, then code)
- How to verify everything works
- The final working application

### The Last Two Prompts

**Prompt 3 (Environment Setup):**
```
Please now look at the implementation plan and make sure that we have everything 
installed on this computer that we need in order to run this successfully. Install 
any installers such as Chocolatey and Winget in order to make it easier to do the 
installs for us. Also, write a cursor rules statement that enforces best practices 
for the technology that we're going to implement this in. Enforce KISS, TDD, ISP in 
this cursor rules file.
```

**Prompt 4 (Joyful Development):**
```
We're the happiest and most joyful software developer in the universe. Let us now 
implement the plan as specified by the software architect, make sure we follow the 
rules of the cursor rules file, but do it with the utmost joy.
```

---

## What You Just Did

In one hour, you:

1. ✅ **Wrote specifications** - Documented exactly what to build
2. ✅ **Designed architecture** - Planned how to build it professionally
3. ✅ **Set up environment** - Got all tools and dependencies ready
4. ✅ **Built real software** - Created a working application with tests

And you used a real methodology that professional developers use: **DADS VIBE CODE**

- **Phase 1:** Specification Writer (what to build)
- **Phase 2:** Software Architect (how to build it)
- **Phase 3:** DevOps Engineer (tools to build with)
- **Phase 4:** Joyful Developer (actually build it)

---

## The Templates (Use These for ANY Project)

These four prompts work for anything:

### Template 1: Specification Writer
```
You are a specification writer. Write detailed specifications for <what you want>. 
Write it in markdown in the root folder.
```

### Template 2: Software Architect
```
You are a software architect. Let us read the specifications, and let us create an 
implementation plan where we use <tech>, utilize TDD and ISP, do not overcomplicate. 
Write the implementation plan as a markdown.
```

### Template 3: DevOps Engineer
```
Please now look at the implementation plan and make sure that we have everything 
installed on this computer that we need in order to run this successfully. Install 
any installers such as Chocolatey and Winget in order to make it easier to do the 
installs for us. Also, write a cursor rules statement that enforces best practices 
for the technology that we're going to implement this in. Enforce KISS, TDD, ISP in 
this cursor rules file.
```

### Template 4: Joyful Developer
```
We're the happiest and most joyful software developer in the universe. Let us now 
implement the plan as specified by the software architect, make sure we follow the 
rules of the cursor rules file, but do it with the utmost joy.
```

**That's it.** Four prompts. Use them for any project.

---

## What Can You Build Now?

Use the same four prompts for:

**Web Applications:**
- Todo list with categories
- Personal budgeting tool
- Recipe organizer
- Habit tracker

**Desktop Apps:**
- Note-taking app with search
- Timer/pomodoro tracker
- File organizer
- Screenshot annotation tool

**CLI Tools:**
- File converter (JSON to CSV)
- Batch image resizer
- Text analyzer
- Git helper tool

**APIs/Backends:**
- REST API for your app
- Data pipeline for processing
- Automation scripts
- Web scraper

Just change what you put in `<what you want>` and `<tech>`.

---

## Deep Dive: The Full Methodology

Want to understand this methodology deeply?

**[Read DADS VIBE CODE](https://github.com/YOLOVibeCode/calc-tutorial/blob/main/DADS_VIBE_CODE.md)**

This document explains:
- Why each phase exists
- How to choose the right AI model for each phase
- Success criteria for each step
- When to use this methodology (and when not to)
- Examples across different project types
- Troubleshooting common issues

**[See the complete calculator tutorial](https://github.com/YOLOVibeCode/calc-tutorial)**

---

## Your Next Steps

### Right Now:
1. Build your calculator (or whatever you chose)
2. Modify it—change colors, add features
3. Show someone what you built

### This Week:
1. Build a second project using the four prompts
2. Try a different tech stack
3. Share your experience

### This Month:
1. Build the tool you've been thinking about
2. Help someone else learn this
3. Explore advanced topics

---

## Why This Works

### 1. Separation of Concerns
Each prompt has ONE job:
- Prompt 1: Define what to build
- Prompt 2: Plan how to build it
- Prompt 3: Get tools ready
- Prompt 4: Build it

### 2. Professional Practices
- **TDD (Test-Driven Development):** Write tests first
- **ISP (Interface Segregation Principle):** Keep components separate
- **KISS (Keep It Simple, Stupid):** Don't overcomplicate

### 3. Systematic Process
Not random prompting. A proven methodology that works every time.

---

## Common Questions

**"I'm not technical. Can I really do this?"**
Yes. You just did (if you followed along). The AI does the technical work. You direct it.

**"What if I get stuck?"**
Watch the video at that part again. The troubleshooting is shown in real-time.

**"Is this really free?"**
Yes. Cursor has a free tier. All tools shown are free.

**"How long to build real apps?"**
You just built one. That's how long. One hour.

**"What makes this different from other tutorials?"**
You started building in 5 minutes, not after reading thousands of words. Action first, explanation after.

---

## Resources

### Videos
- **Installation (15 min):** https://www.loom.com/share/b6e2d33d3df54aa1b57deefea90fe0c1
- **Full Build (45 min):** https://www.loom.com/share/8e0e2f44b9784612ae38600002b85039

### Documentation
- **Complete Methodology:** https://github.com/YOLOVibeCode/calc-tutorial/blob/main/DADS_VIBE_CODE.md
- **All Prompts:** https://github.com/YOLOVibeCode/calc-tutorial/blob/main/Prompts.md
- **Full Repository:** https://github.com/YOLOVibeCode/calc-tutorial

---

## Start Your Next Project Right Now

1. Think of something you want to build
2. Open Cursor
3. Use Prompt 1 with your idea
4. Use Prompt 2 with your tech choice
5. Follow Prompts 3 and 4

**That's it.**

No more reading. Go build something.

---

*Written by a dad who believes everyone can build software with AI. No gatekeeping. No sales. Just teaching.*

*P.S. — When you build something cool, share it. Tag me. I love seeing what people create.*
