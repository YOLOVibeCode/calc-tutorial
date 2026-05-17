# The Agonizing Joy of Coding Yourself Into a Corner

## AI lets you dig holes faster than ever. Here's your ladder out.

---

*This is Part 2 of my vibe coding series. If you haven't read Part 1, start here:* [Why You Must Learn to Vibe Code—And Teach Everyone You Know](https://medium.com/@rvegajr/why-you-must-learn-to-vibe-code-and-teach-everyone-you-know-b7799bc132ea)

---

Let me tell you about the best worst thing that will happen to you.

You've discovered vibe coding. You followed my [previous tutorial](https://medium.com/@rvegajr/why-you-must-learn-to-vibe-code-and-teach-everyone-you-know-b7799bc132ea), sat down with Cursor, showed it a picture of a calculator, said "build this," and it *did*. Twenty minutes later you had a working app. You felt like a genius. You felt like you'd unlocked a cheat code to the universe.

So you kept going.

"Hey AI, make the buttons rounder."

*Done.*

"Actually, let's try a dark theme."

*Done.*

"What if we used a completely different layout?"

*Done.*

"Let's refactor this to be cleaner."

*Done. Also I renamed everything and created fifteen new files and deleted that one you liked.*

"Wait. Undo that."

*Undo what? We've made forty-seven changes in the last six minutes. "Undo" is a philosophical concept at this point.*

"Just... go back to how it was."

*How it was when? Before the dark theme? Before the layout change? Before I helpfully reorganized your entire project structure? You're going to need to be more specific, and also I don't remember, and also time is a flat circle.*

And now you're sitting there.

Staring at your screen.

Looking at code you don't recognize.

In files you don't remember creating.

The app won't run. The tests are broken. You don't even know what the tests *test* anymore because the AI "improved" them while you weren't looking.

You have coded yourself into a corner.

And here's the beautiful, terrible thing:

**You did it in like ten minutes.**

---

This is the agonizing joy of AI-assisted development. In the old days, it took *effort* to completely destroy your project. You had to really commit. You had to manually type every bad decision. You had to earn your disasters through hours of labor.

Now? You can go from "working app" to "smoldering crater" in the time it takes to heat up a Hot Pocket.

I have done this more times than I want to admit.

I have stared at my own code like it was written by a stranger. I have opened files and thought "what *is* this?" I have had that sinking feeling where you realize you don't know how to get back to when things worked, and you don't even remember when that was, and maybe the only option is to delete everything and start over.

Hours of work. Gone. Because I was vibing too hard.

**This tutorial exists so that never happens to you.**

We're going to set up save points for your code. Like a video game. Every time things work, you save. Then you can experiment as recklessly as you want. Try stupid ideas. Let the AI go absolutely feral.

Because when everything catches fire — and it will, gloriously — you just say "go back to my last save."

And you're back.

Right where things worked.

Let's build your safety net.

---

## What We're Making

By the end of this (about 15 minutes), you'll have:

🎮 **Save points** — Your code backed up in the cloud, safe forever

⏰ **A time machine** — Jump back to any previous save

🪄 **A magic phrase** — Just say "save this project" and Cursor handles everything

No memorizing commands. No understanding Git. Just vibes and safety nets.

---

## Part 1: What's GitHub? (30-Second Version)

**Git** = A system that tracks every change you make to your code. Like unlimited undo, but smarter.

**GitHub** = A website that stores your Git history in the cloud. Like iCloud for code.

**GitHub CLI** = A friendly tool that talks to GitHub so you don't have to type scary commands.

Here's the secret though: **You don't need to understand any of this.**

We're setting it up so that Cursor does all the nerdy parts. You just say "save this project" and magic happens.

Cool? Cool.

---

## Part 2: Get a GitHub Account

This is just signing up for a website. You've done this a million times.

**Go to** [github.com](https://github.com)

**Click** Sign Up

**Enter** your email (Gmail, whatever), a password, and a username.

> ⚠️ **Username Warning:** This is public. The whole internet sees it. So maybe not `XxShadowNinja420xX` or `ilovetoilets`. Something like `yourname-dev` is perfectly fine.

**Do the robot puzzle.** Yes, even though you're literally using AI to write code. I know.

**Check your email.** Enter the code they sent.

**Skip all the "personalization" questions.** Just click through until you see your dashboard.

Done. You have a GitHub account. Basically a hacker now.

---

## Part 3: Create Your Repo

A "repository" is a folder that GitHub knows about. We call it a "repo" because developers physically cannot say full words.

**Click** the green **New** button (top-left of dashboard)

Or go straight to: [github.com/new](https://github.com/new)

**Name it** something like `my-calc-tutorial` — use lowercase, dashes instead of spaces. Computers are picky.

**Select** Private — your code, your business. You can make it public later if you want.

**Check** "Add a README file" — just gives you a starter file, like a welcome mat.

**Click** Create repository.

**COPY THE URL.** You're looking at your new empty repo. The URL looks like:

```
https://github.com/YOUR-USERNAME/my-calc-tutorial
```

Copy it. Write it down. Tattoo it somewhere. We need it soon.

> 💡 **Pro tip:** There's a green **Code** button on the page with a copy icon. Click that.

---

## Part 4: Install GitHub CLI

Git has approximately ten thousand commands and they all sound like keyboard mashing. `git rebase --onto HEAD~3 feature` or whatever. Absolutely not.

**GitHub CLI** is friendlier. And Cursor can use it for us.

---

### On Mac

Open Terminal (`Cmd + Space`, type Terminal, Enter).

**If you have Homebrew:**

```
brew install gh
```

**If you don't have Homebrew,** install it first:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then do the `brew install gh` thing.

---

### On Windows

**Easy way:**

1. Go to [cli.github.com](https://cli.github.com)
2. Click Download for Windows
3. Run installer, click Next until done

**Fancy way (if you have winget):**

```
winget install GitHub.cli
```

---

### Check It Worked

Open a **fresh** terminal and type:

```
gh --version
```

See a version number? You're good.

See "command not found"? Close the terminal, open a new one, try again.

---

## Part 5: Log In

GitHub CLI needs to know who you are. One-time setup.

**Run this in your terminal:**

```
gh auth login
```

**Answer the questions like this:**

- What account do you want to log into? → **GitHub.com**
- What is your preferred protocol for Git operations? → **HTTPS**
- Authenticate Git with your GitHub credentials? → **Yes**
- How would you like to authenticate GitHub CLI? → **Login with a web browser**

**Copy the code** it shows you (looks like `ABCD-1234`).

**Press Enter** — your browser opens.

**Paste the code** into the GitHub page.

**Click Authorize.**

**Go back to terminal** — it should say `✓ Logged in as your-username`.

Done. GitHub CLI and GitHub are now best friends.

---

## Part 6: Connect Your Project

Time to introduce your code to its new cloud home.

If you built the calculator from [Part 1 of this series](https://medium.com/@rvegajr/why-you-must-learn-to-vibe-code-and-teach-everyone-you-know-b7799bc132ea), we're about to back it up. If you're working on something else, same process.

**Open Cursor.**

**Open your project folder** — File → Open Folder → your calculator project.

**Open the AI chat** — `Cmd+L` on Mac, `Ctrl+L` on Windows.

**Paste this prompt** (replace `YOUR-USERNAME` with your actual username):

```
Connect this project to my GitHub repo.

Repo URL: https://github.com/YOUR-USERNAME/my-calc-tutorial

Please:
1. Initialize git if needed
2. Set the remote to my repo
3. Add all files  
4. Commit with message "Initial commit - let's go!"
5. Push to GitHub

Run the commands and show me what happens.
```

**Send it.** Cursor will ask permission to run terminal commands. Say yes. Watch the magic happen.

**Check GitHub.** Go to your repo URL. Refresh.

**See your files?** 🎉 You did it. Your code is in the cloud.

---

## Part 7: The Magic Phrase

Here's the whole point of everything.

We're going to teach Cursor that when you say "save this project," it automatically backs up your code to GitHub.

No commands. No remembering anything. Just two words.

---

**Create the folder structure:**

In Cursor's file explorer:

- Right-click → New Folder → name it `.cursor`
- Right-click on `.cursor` → New Folder → name it `rules`
- Right-click on `rules` → New File → name it `github-save.mdc`

**Paste this into the file:**

```
---
description: Save project to GitHub on request
globs:
alwaysApply: true
---

# Save This Project

When I say:
- "save this project"
- "save my work"  
- "save to GitHub"
- "push my changes"
- "checkpoint"

Do this:

## 1. Check what changed

git status

Show me the changed files.

## 2. Stage everything

git add .

## 3. Ask for a save name

Ask me: "What should I call this save?" 

Use my answer as the commit message. If I say "you pick" just describe what changed.

## 4. Commit

git commit -m "MESSAGE HERE"

## 5. Push

git push origin main

## 6. Confirm

Say: "✅ Saved! Your code is backed up."

---

## If things go wrong:

**Nothing to commit:** Say "Already saved! No changes since last time."

**Push rejected:** Run git pull --rebase origin main then push again.

**Auth error:** Tell me to run gh auth login
```

**Save the file** — `Cmd+S` or `Ctrl+S`.

> 💡 **Using Windsurf?** Create a file called `.windsurfrules` in your project root and paste the same thing.

---

## Part 8: Test It

Let's see if our time machine works.

**Change something.** Open any file. Add a comment:

```
# Testing my save system - this is exciting!
```

Save the file.

**Say the magic words.** Open Cursor chat and type:

```
save this project
```

**Watch it work.** Cursor should:

- Show you what changed
- Ask what to call this save
- Commit and push
- Tell you it's done

**Check GitHub.** Go to your repo. See a new commit?

**IT WORKS.** You have save points.

---

## Part 9: Your New Life

Here's the workflow now.

### The One Rule

> When something works, save it.

- App runs? → "save this project"
- Bug fixed? → "save this project"
- Tests pass? → "save this project"
- UI looks good? → "save this project"

Then go wild. Ask the AI to try crazy stuff. Refactor everything. Experiment recklessly.

When it all catches fire:

> "go back to my last save"

And you're back. Safe. Right where things worked.

---

## Cheat Sheet

**"save this project"** → Backs up everything to GitHub

**"what changed?"** → Shows modified files

**"go back to my last save"** → Reverts to previous checkpoint

**"show my save history"** → Lists all your saves

**"I broke everything, help"** → Cursor helps you undo

---

## When Stuff Breaks

**"Authentication failed"** — GitHub forgot you. Run `gh auth login` again.

**"Nothing to commit"** — Good news! Already saved. No changes to back up.

**"Push rejected"** — Tell Cursor: "push was rejected, pull and try again"

**"Merge conflict"** — Rare, but if you see it: "I have a merge conflict, help me fix it"

---

## The Point

Remember where we started?

You were standing in the rubble of your own project. Code you didn't recognize. Files you didn't remember. That sinking "how do I get back" feeling.

That doesn't happen anymore.

Now you have save points. You have a time machine. You can:

1. **Vibe** — Let the AI build fast and loose
2. **Save** — When it works, say the words
3. **Break** — Experiment without fear
4. **Rewind** — When it goes wrong, go back
5. **Repeat** — Forever

This is how professionals work. Not because they're careful. Because they don't have to be.

Neither do you. Not anymore.

---

## Go Break Something

Seriously. On purpose.

Tell your AI to "completely redesign everything using a totally different approach." Watch it make a glorious mess. Then say "go back to my last save."

Feel the power.

Then build something you would've been scared to try before. Something ambitious. Something that might not work.

Because you can't mess up permanently anymore.

You have a time machine.

---

## What's Next?

In Part 1, you learned to [vibe code a calculator](https://medium.com/@rvegajr/why-you-must-learn-to-vibe-code-and-teach-everyone-you-know-b7799bc132ea).

In Part 2 (this one), you learned to save your work like a grownup.

Now go build something real. Something you care about. Something that solves a problem in your life.

And when you do — teach someone else.

That's the whole point.

---

*Vibe recklessly. Save frequently. Never lose your work again.*

*That's the vibe.*
