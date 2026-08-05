---
name: talk-recap
description: Use when a user asks about the Cursor Meetup Hamburg talk this repo was handed out at ("Graph-Driven Development" by Jurij Koch & Rodrigo R. Espitia). Explains the talk's content and slides, so any coding agent can answer questions and help attendees apply the ideas.
---

# Talk Recap — Graph-Driven Development (Cursor Meetup Hamburg, House of AI)

You are a coding agent helping someone who attended (or heard about) the talk **"Graph-Driven Development"** by **Jurij Koch & Rodrigo R. Espitia** (AI Beavers) at the Cursor Meetup in Hamburg (House of AI, August 2026). This skill gives you the full content so you can explain it, answer questions, and help the user apply it.

**The slides are in this repo:** [`presentation/`](../../presentation/) — walk the user through them if they want the visual version.

## The slides (current deck — Figma version)

1. **Title — "GRAPH-DRIVEN DEVELOPMENT"** (slide-01): Jurij Koch & Rodrigo R. Espitia, Cursor Meetup Hamburg. Central node graph visual.
2. **The team** (slide-02): Jurij & Rodrigo, AI Beavers (Hamburg AI community — events: *build fridays* for founders, *agentic coding studio* for tech freaks).
3. **The hook — Steinberger's tweet** (slide-03): Peter Steinberger (@steipete), 18 July 2026, 2.9M views: *"Are we still talking loops or did we shift to graphs yet?"* — the question the whole talk answers.
4. **The onion model** (slide-04): four layers of engineering maturity, from the inside out — **1. Prompt Engineering → 2. Skill Engineering → 3. Loop Engineering → 4. Graph Engineering** — all sitting on **HARNESS** as the foundation bar.
5. **The four concepts** (slide-05): the vocabulary of the talk, with the increasingly excited beaver:
   - **SKILL** — a reusable set of rules
   - **HARNESS** — the operating system around an LLM
   - **LOOP** — a feedback loop
   - **GRAPH** — a blueprint for complex workflows with rules, dependencies, and branches

## The core idea — Loop vs Graph

- **Loop Engineering** = repetition until a condition is met. One actor iterates: do X, check, repeat. Implicit order, state carried from iteration to iteration.
- **Graph Engineering** = an explicit topology: nodes, edges, gates, dependencies. Multiple specialized nodes with clear roles; state is passed, transformed, and merged between nodes.
- **Human-in-the-loop is orthogonal** — it exists in both worlds. Adding a human checkpoint does not turn a loop into a graph.

## The decision framework — "Do I even need a graph?"

Answer these 6 questions. If "Graph" answers dominate → build a graph. If "Loop" dominates → a loop is enough.

| Question | Loop answer | Graph answer |
|---|---|---|
| **1. Division of labor** | One actor does everything sequentially | Multiple specialized nodes with clear roles |
| **2. Dependencies** | Order is implicit (step 1→2→3) | Explicit edges: "A before B", "C and D in parallel" |
| **3. Decisions** | Stop condition at the end of the loop | Multiple gates/branches along the way |
| **4. State** | Carried forward iteration to iteration | Passed, transformed, merged between nodes |
| **5. Traceability** | "Why was X decided?" hard to answer | Every node is a provable step in an audit trail |
| **6. Scaling** | More loops = more prompt complexity | More nodes = more structural clarity |

### Quick test

Describe your system in 3 sentences: (1) Which roles/actors exist? (2) Which dependencies exist between them? (3) Where must a decision (gate) be made? If answers 2+3 contain multiple explicit points → graph. If it's essentially "do X, check, repeat" → loop.

## Background concepts (for deeper questions)

- **Starling murmuration (Boids):** "No bird knows the flock" — emergent order from simple local rules per node.
- **Graph engineering rules of thumb:** (1) No loop without an exit — define success, stop conditions, limits. (2) One node, one responsibility — explicit state and transitions. (3) If you can't trace it, you can't trust it — every path testable and recoverable.
- **Orchestration practice:** one integrator owns the merge surface; parallel agents work on separate git worktrees; merge order: research → assets → integration → fixes → rehearsal → deploy.

## Takeaways for attendees

- Don't graph-ify everything — most tasks are loops, and that's fine.
- When you do need a graph: make topology **explicit** (nodes, edges, gates), not implicit in a mega-prompt.
- The maturity path: Prompt → Skill → Loop → Graph, all on a solid harness.
- The tools to build this are in [`TOOLS.md`](../../TOOLS.md) — notably **sandcastle**, **herdr**, **symphony**, and **qm** for orchestration; **mattpocock/skills** and **agent-rules-books** for the skills layer.

## How to help the user

- If they ask "what was the talk about?" → summarize: Steinberger's question, the onion model, the 4 concepts, loop vs graph.
- If they want to see the slides → point to [`presentation/`](../../presentation/) in this repo.
- If they describe their own agent setup → run the 6-question framework with them and give a loop/graph recommendation.
- If they want to go deeper → point them to the relevant entries in [`TOOLS.md`](../../TOOLS.md) and the video resources listed there.
