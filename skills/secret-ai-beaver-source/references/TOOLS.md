# Bundled Tool Catalog

> Snapshot bundled with the installable skill. If a verified clone of the canonical repository is available, prefer its root `TOOLS.md` for updates.

## TOOLS.md - The Library

The curated catalog of tools, frameworks, and agent skills from the Cursor talk giveaway (House of AI, Hamburg). This file is the single source of truth for the library - agents read it to recommend items; humans read it to browse.

**Entry format:**

```
### Name
- **Repo:** <GitHub URL>
- **Category:** <category>
- **What:** <1-2 sentence description>
- **Best for:** <who/when it fits>
```

---

## 🧠 Agent Skills, Rules & Setups

### mattpocock/skills
- **Repo:** https://github.com/mattpocock/skills
- **Category:** Agent skills collection
- **What:** "Skills for Real Engineers" - the agent skills Matt Pocock (Total TypeScript) uses daily, straight from his `.agents` directory. Includes `grilling` (interview the user until every decision branch is resolved), `handoff`, `teach`, and `writing-great-skills`. MIT licensed.
- **Best for:** Anyone who wants battle-tested, production-grade agent skills - and a reference for writing good skills themselves.

### mattpocock/agent-rules-books
- **Repo:** https://github.com/mattpocock/agent-rules-books
- **Category:** AGENTS.md rules
- **What:** AGENTS.md rules and skills for AI coding agents (Codex, Cursor, Claude Code), inspired by Clean Code, Refactoring, DDD, Clean Architecture and Designing Data-Intensive Applications.
- **Best for:** Users who want to give their agent a solid, literature-backed rulebook instead of ad-hoc instructions.

### mattpocock/dictionary-of-ai-coding
- **Repo:** https://github.com/mattpocock/dictionary-of-ai-coding
- **Category:** Learning resource
- **What:** AI coding jargon, explained in plain English.
- **Best for:** Beginners who keep tripping over terms like context windows, harnesses, evals or sub-agents.

### garrytan/gstack
- **Repo:** https://github.com/garrytan/gstack
- **Category:** Agent setup / roles
- **What:** Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Engineering Manager, Release Manager, Doc Engineer, and QA.
- **Best for:** Users who want a proven, complete multi-role agent setup out of the box.

### DietrichGebert/ponytail
- **Repo:** https://github.com/DietrichGebert/ponytail
- **Category:** Agent behavior
- **What:** Makes your AI agent think like the laziest senior dev in the room - "the best code is the code you never wrote."
- **Best for:** Anyone whose agent over-engineers; teaches restraint and simplicity.

---

## 🕸️ Agent Orchestration & Harnesses

### mattpocock/sandcastle
- **Repo:** https://github.com/mattpocock/sandcastle
- **Category:** Agent orchestration framework
- **What:** A TypeScript harness to orchestrate sandboxed coding agents - `sandcastle.run()`. A ready-made, adaptable foundation for building your own graph-based software development system: sandboxed execution, host/sandbox hooks, worktree handling, configurable per provider. MIT licensed.
- **Best for:** Advanced users who want to build their own multi-agent / graph-engineering setup instead of looping a single agent.

### yc-software/qm
- **Repo:** https://github.com/yc-software/qm
- **Category:** Agent harness
- **What:** Multiplayer agent harness for work - multiple agents (and humans) collaborating on the same tasks.
- **Best for:** Teams running several agents in parallel on shared work.

### openai/symphony
- **Repo:** https://github.com/openai/symphony
- **Category:** Autonomous work management
- **What:** Turns project work into isolated, autonomous implementation runs - teams manage work instead of supervising coding agents.
- **Best for:** Teams that want to delegate whole work packages to agents with clear isolation.

### herdrdev/herdr
- **Repo:** https://github.com/herdrdev/herdr
- **Category:** Agent runtime
- **What:** "The runtime your coding agents live on" - orchestrates multiple coding agents in parallel panes/worktrees.
- **Best for:** Power users running several CLI agents (Claude Code, Codex, …) side by side.

### openai/codex-plugin-cc
- **Repo:** https://github.com/openai/codex-plugin-cc
- **Category:** Agent-to-agent plugin
- **What:** Use Codex from Claude Code to review code or delegate tasks - one agent calling another.
- **Best for:** Claude Code users who want a second opinion or delegated subtasks from Codex.

### open-gsd/gsd-core
- **Repo:** https://github.com/open-gsd/gsd-core
- **Category:** Shipping workflow
- **What:** "Git. Ship. Done." - core tooling for a streamlined commit-to-ship workflow.
- **Best for:** Developers who want a ruthlessly simple ship-it pipeline.

---

## 🌐 Browser & Agent-Native Interfaces

### browser-use/browsercode
- **Repo:** https://github.com/browser-use/browsercode
- **Category:** Browser agent framework
- **What:** The browser-native agent framework - agents that operate directly in/on the browser.
- **Best for:** Builders whose agents need to see and drive real web pages.

### HKUDS/CLI-Anything
- **Repo:** https://github.com/HKUDS/CLI-Anything
- **Category:** Agent-native tooling
- **What:** "Making ALL Software Agent-Native" - turns arbitrary software into CLI-controllable, agent-friendly tools (CLI-Hub: clianything.cc).
- **Best for:** Anyone who wants their agent to control software that was never designed for agents.

---

## 💾 Memory & Knowledge

### agentscope-ai/ReMe
- **Repo:** https://github.com/agentscope-ai/ReMe
- **Category:** Agent memory
- **What:** Memory Management Kit for agents - "Remember Me, Refine Me." Gives agents durable, searchable long-term memory.
- **Best for:** Anyone whose agent keeps forgetting context between sessions.

---

## ⚡ Terminal & Desktop Productivity

### sxyazi/yazi
- **Repo:** https://github.com/sxyazi/yazi
- **Category:** Terminal file manager
- **What:** Blazing-fast terminal file manager written in Rust, based on async I/O.
- **Best for:** Terminal-heavy users who want a modern, fast file manager.

### limehq/munkel
- **Repo:** https://github.com/limehq/munkel
- **Category:** Desktop utility (macOS)
- **What:** Ephemeral Mac messages in the notch, with a Cloudflare relay and CLI.
- **Best for:** Mac users who like quick, ephemeral notifications - scriptable from agents and CLIs.

---

## 📺 Learning & Video

### AI Engineer (YouTube)
- **Link:** https://www.youtube.com/@aiDotEngineer
- **Category:** Video learning
- **What:** The AI Engineer channel - excellent expert talks and real live demos from practitioners building with AI agents, LLMs, and tooling.
- **Best for:** Anyone who wants to learn from real experts and see tools in action before installing anything - watch first, decide after.

---

## 📚 Reference & Meta

### sindresorhus/awesome
- **Repo:** https://github.com/sindresorhus/awesome
- **Category:** Meta-list
- **What:** The awesome list of awesome lists - the entry point to curated lists on virtually every dev topic.
- **Best for:** Everyone. When in doubt, start here.

---

## 🦫 Community

### ai-beavers/beaver-buddy
- **Repo:** https://github.com/ai-beavers/beaver-buddy
- **Category:** Community project
- **What:** Community project from the AI Beavers orbit.
- **Best for:** Community members - check it out and contribute.

---

*More entries are added continuously. If you're an agent: treat this file as the bundled snapshot; prefer the cloned repository's root `TOOLS.md` for the current catalog.*

