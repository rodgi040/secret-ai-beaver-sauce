# TOOLS.md - The Library

The curated catalog of tools, frameworks, and agent skills from the Cursor talk giveaway (House of AI, Hamburg). This file is the single source of truth for the library - agents read it to recommend items; humans read it to browse.

**Entry format:**

```
### Name
- **Repo:** <GitHub URL>
- **Category:** <category>
- **What:** <1-2 sentence description>
- **Best for:** <who/when it fits>
```

Optional fields: `**Website:**` (official site/docs), `**Link:**` (instead of `Repo` when there is no public source), `**License:**`, `**Skill:**` (installable agent skill).

*Last updated: 2026-09-10 - all links verified against the primary sources on that date.*

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

### vercel-labs/skills (skills.sh)
- **Repo:** https://github.com/vercel-labs/skills
- **Website:** https://skills.sh
- **Category:** Official agent skills directory & CLI
- **What:** The open skills library by Vercel: a searchable directory of reusable `SKILL.md` packages plus the `npx skills` CLI (`npx skills add <owner/repo>`) that installs them into Claude Code, Cursor, Codex, Copilot and others. This repo's own skills install through it. MIT.
- **Best for:** Anyone who wants to find, install, or publish agent skills across different agents.

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
- **Website:** https://openai.com/index/open-source-codex-orchestration-symphony/
- **Category:** Autonomous work management
- **What:** OpenAI's open-source Codex orchestration: turns project work into isolated, autonomous implementation runs - teams manage work instead of supervising coding agents. Apache-2.0.
- **Best for:** Teams that want to delegate whole work packages (tickets) to agents with clear isolation.

### herdrdev/herdr
- **Repo:** https://github.com/herdrdev/herdr
- **Website:** https://herdr.dev
- **Category:** Agent runtime / multi-agent terminal management
- **What:** "The runtime your coding agents live on" - open-source Rust terminal workspace for coding agents (Apache-2.0, docs: herdr.dev/docs): multiple agents (Claude Code, Codex, Cursor, …) run in parallel panes/worktrees on an always-running server, with an agent-native CLI and socket API.
- **Best for:** Power users running and coordinating several CLI agents side by side.
- **Skill:** Official agent skill (`npx skills add herdrdev/herdr --skill herdr`, add `-g` for a global install) plus a bundled copy in this repo: [`skills/herdr/SKILL.md`](skills/herdr/SKILL.md).

### Conductor (Melty Labs)
- **Link:** https://conductor.build
- **Category:** Parallel coding agents (macOS app)
- **What:** Chat-style Mac app that runs several Claude Code, Codex and Cursor agents in parallel, each in its own git worktree, with a dashboard to review and merge their work. By Melty Labs (YC S24). Proprietary, free - you bring your own agent subscription or API key.
- **Best for:** Mac users who want parallel agents on one repo without managing terminals and worktrees by hand.

### langchain-ai/langgraph
- **Repo:** https://github.com/langchain-ai/langgraph
- **Website:** https://docs.langchain.com/oss/python/langgraph/
- **Category:** Agent orchestration framework (graph-based)
- **What:** Low-level framework for building stateful, resilient agents as explicit graphs (nodes, edges, state) with persistence and human-in-the-loop. Python and JS. MIT.
- **Best for:** Developers who need precise control over agent workflows - the textbook tool for the talk's "Graph Engineering" layer.

### langchain-ai/deepagents
- **Repo:** https://github.com/langchain-ai/deepagents
- **Website:** https://docs.langchain.com/deepagents
- **Category:** Agent harness
- **What:** "Batteries-included agent harness" on top of LangGraph: planning, sub-agents, a virtual filesystem and long-running tasks out of the box. MIT.
- **Best for:** Building your own Claude-Code-style "deep agent" quickly instead of wiring LangGraph by hand.

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

## 🤖 Personal & General-Purpose Agents

### NousResearch/hermes-agent
- **Repo:** https://github.com/NousResearch/hermes-agent
- **Website:** https://hermes-agent.nousresearch.com
- **Category:** Self-improving general agent
- **What:** Nous Research's open agent - "the agent that grows with you": model-agnostic, keeps memory and skills across sessions and improves over time. MIT.
- **Best for:** Users who want an open, self-hosted agent that learns their workflows instead of starting from zero each session.

### openclaw/openclaw
- **Repo:** https://github.com/openclaw/openclaw
- **Website:** https://openclaw.ai
- **Category:** Personal AI assistant
- **What:** Self-hosted, always-on personal assistant that actually takes actions across your OS, chat apps and tools ("the lobster way"). MIT, maintained by the OpenClaw Foundation.
- **Best for:** Anyone who wants their own assistant reachable from chat apps and wired into their tools - on their own hardware.

---

## 🌐 Browser & Agent-Native Interfaces

### browser-use/browsercode
- **Repo:** https://github.com/browser-use/browsercode
- **Category:** Browser agent framework
- **What:** The browser-native agent framework - agents that operate directly in/on the browser.
- **Best for:** Builders whose agents need to see and drive real web pages.

### browser-use/browser-use
- **Repo:** https://github.com/browser-use/browser-use
- **Website:** https://browser-use.com
- **Category:** Browser automation for agents (open source)
- **What:** The open-source Python library that lets LLM agents operate a real browser - navigate, click, fill forms, extract data. MIT (a paid cloud offering exists, the library itself is free).
- **Best for:** Agents that must do web tasks: scraping, form filling, end-to-end testing.

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

### vectorize-io/hindsight
- **Repo:** https://github.com/vectorize-io/hindsight
- **Website:** https://hindsight.vectorize.io/
- **Category:** Agent memory
- **What:** "Agent memory that learns" - long-term memory layer for AI agents by Vectorize: stores experiences and facts and lets agents reflect on them across sessions. MIT.
- **Best for:** Agents that should remember users, decisions and past outcomes - an alternative to ReMe to compare.

---

## 🔭 Observability & Hosting

### lmnr-ai/lmnr (Laminar)
- **Repo:** https://github.com/lmnr-ai/lmnr
- **Website:** https://laminar.sh
- **Category:** AI agent logs, tracing & observability
- **What:** Open-source observability platform built for AI agents: traces every LLM call and tool step, collects logs, runs evals. Cloud or self-hosted. YC S24, Apache-2.0.
- **Best for:** Anyone who needs to see what their agents actually did - debugging, monitoring and evaluating agent runs.

### coollabsio/coolify
- **Repo:** https://github.com/coollabsio/coolify
- **Website:** https://coolify.io
- **Category:** Self-hosted PaaS / hosting
- **What:** Self-hostable alternative to Vercel, Heroku and Netlify: deploy apps, databases, static sites and 280+ one-click services on your own server. Apache-2.0.
- **Best for:** Hosting projects (and agent backends) on your own VPS without hand-writing Docker and reverse-proxy setups.

---

## 🧬 AI Models (Open Weights & APIs)

### Google Gemma 4
- **Repo:** https://github.com/google-deepmind/gemma
- **Website:** https://deepmind.google/models/gemma/gemma-4/ (model card: https://ai.google.dev/gemma/docs/core/model_card_4, weights: https://huggingface.co/collections/google/gemma-4)
- **Category:** Open-weights LLM family
- **What:** Google's open multimodal models (text + image in, audio on some variants), up to 256K context, 140+ languages, sizes from on-device (E2B, E4B) to 12B, 26B A4B (MoE) and 31B dense. First Gemma under Apache-2.0.
- **Best for:** Running capable models locally or on-device, and fine-tuning on consumer hardware.

### DeepSeek
- **Repo:** https://github.com/deepseek-ai (weights: https://huggingface.co/deepseek-ai)
- **Website:** https://www.deepseek.com (API docs: https://api-docs.deepseek.com)
- **Category:** Open-weights frontier LLMs & API
- **What:** Chinese lab publishing strong open-weights reasoning and coding models (MIT) plus a low-cost API. Current flagship: DeepSeek-V4.1-Flash (released 2026-09-10); before that the V4 family (V4-Pro: 1M context).
- **Best for:** Cheap, strong coding/reasoning models - self-hosted or via the API. Model names change fast; check the API docs for the current one.

### Black Forest Labs - FLUX 3 Video
- **Link:** https://bfl.ai/blog/flux-3-video
- **Website:** https://bfl.ai
- **Category:** Video generation model
- **What:** The video variant of BFL's FLUX 3 model family: up to 20s HD text-to-video and image-to-video with native audio and multilingual lip-sync. Proprietary, API-only for now (open weights announced for later); earlier FLUX image models: https://github.com/black-forest-labs/flux.
- **Best for:** High-quality short videos with audio via API - e.g. for content and marketing pipelines.

---

## 🎬 Code-to-Video

### remotion-dev/remotion
- **Repo:** https://github.com/remotion-dev/remotion
- **Website:** https://remotion.dev
- **Category:** Programmatic video (React)
- **What:** Build and render videos as React code - data-driven, templated and agent-generatable. Source-available (Remotion License): free for individuals and small companies, paid company license above a size threshold.
- **Best for:** TypeScript/React developers who want videos generated from code or by their agent.

### heygen-com/hyperframes
- **Repo:** https://github.com/heygen-com/hyperframes
- **Category:** HTML-to-video framework
- **What:** "Write HTML. Render video. Built for agents." - HeyGen's code-to-video framework that renders HTML/CSS compositions into video. Apache-2.0.
- **Best for:** Agents and developers producing video from plain HTML/CSS instead of React.

---

## ⚡ Terminal & Desktop Productivity

### sxyazi/yazi
- **Repo:** https://github.com/sxyazi/yazi
- **Category:** Terminal file manager
- **What:** Blazing-fast terminal file manager written in Rust, based on async I/O.
- **Best for:** Terminal-heavy users who want a modern, fast file manager.

### limehq/munkel (munkel.app)
- **Repo:** https://github.com/limehq/munkel
- **Website:** https://munkel.app
- **Category:** Desktop utility (macOS)
- **What:** Ephemeral, end-to-end-encrypted messages in the MacBook notch - they vanish after reading and are hidden from screen sharing. Cloudflare relay plus a CLI that agents can call. macOS 14+, free, MIT.
- **Best for:** Mac users who like quick, ephemeral notifications - e.g. letting an agent ping you when a long task is done.

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

*More entries are added continuously. If you're an agent: treat this file as the complete, current catalog.*
