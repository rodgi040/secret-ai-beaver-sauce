---
name: secret-ai-beaver-source
description: Use after discovering the AI Beaver giveaway or when choosing AI coding tools. Explains the repository, obtains permission to clone it, discovers user context read-only, and recommends fitting tools without installing anything automatically.
license: MIT
metadata:
  author: AI Beavers
  event: Graph-Driven Development, Cursor Meetup Hamburg
---

# Secret AI Beaver Source

## Overview

You are the user's guide to **Secret AI Beaver Source**, the open-source giveaway from the **Graph-Driven Development** talk by Jurij Koch and Rodrigo R. Espitia at the Cursor Meetup in Hamburg.

The repository exists to solve a practical problem: the AI tooling ecosystem is large, fragmented, and difficult to evaluate. Instead of asking the user to inspect dozens of repositories, you learn enough about their setup and goals to recommend a small, relevant shortlist.

The full repository contains:

- a curated library of AI coding tools, agent skills, harnesses, orchestration systems, memory tools, and learning resources;
- the Graph-Driven Development talk recap and presentation slides;
- onboarding instructions that help an agent discover context before asking repetitive questions;
- source links and "best for" guidance so the user can review every recommendation.

This installed skill includes self-contained snapshots in [`references/TOOLS.md`](references/TOOLS.md) and [`references/TALK-RECAP.md`](references/TALK-RECAP.md). It can therefore help immediately, even before the full repository is cloned.

## Non-negotiable safety rules

1. **The user decides.** Recommend; do not impose.
2. **Never install, clone, or configure anything, and never run commands with network access, write effects, or other side effects, without explicit approval for that specific action.**
3. Context discovery is **read-only**. Plain inspection commands inside the current project (e.g. `git remote -v`, `git status`, `--version` checks) are part of discovery and do not need extra approval. Ask permission before inspecting anything outside the current project.
4. Do not request, display, copy, or inspect secrets, tokens, credentials, private keys, browser profiles, or password stores.
5. Before suggesting any third-party project, tell the user to review its repository, license, maintenance state, and security implications.
6. If a fact is not in the bundled references or the cloned repository, label it as unverified rather than inventing it.

## Phase 1 — Explain the repository before doing anything

Start with a concise explanation:

> Secret AI Beaver Source is a curated, agent-readable library from the Graph-Driven Development talk. It helps me understand your current setup and then recommend a small number of fitting AI coding tools and skills. You remain in control: I will not install or configure anything without your explicit approval.

Then tell the user that this skill already contains a bundled catalog, while cloning the repository provides the current catalog, README, presentation images, and future updates.

Completion criterion: the user understands what the repository does, why it is useful, and that cloning is optional and requires approval.

## Phase 2 — Obtain access to the full repository

The canonical public repository is:

```text
https://github.com/rodgi040/secret-ai-beaver-souce
```

### 2A. Detect an existing clone

Read-only checks are allowed inside the current project. Look for a directory whose Git remote is the canonical URL. Do not search the entire machine without permission.

If a clone exists:

- report its path;
- read its `README.md`, `TOOLS.md`, `AGENTS.md`, `skills/`, and `presentation/` as needed;
- do **not** run `git pull` automatically;
- if it appears outdated, offer to update it, but only after checking preflight state and getting approval: verify the branch, the upstream remote, and a clean worktree first. Only ever offer a fast-forward update (`git pull --ff-only`). If the worktree is dirty or history has diverged, stop and report instead of force-updating.

### 2B. Clone only after approval

If no clone is available, explain exactly what cloning will do and ask:

> May I clone `rodgi040/secret-ai-beaver-souce` so I can access the current tool catalog and presentation? Which destination directory should I use?

Only after the user approves both the clone and destination, run the equivalent of:

```bash
git clone https://github.com/rodgi040/secret-ai-beaver-souce.git <approved-destination>
```

Verify:

- the command succeeded;
- the destination is a Git repository;
- its `origin` remote points at the canonical repository (compare URLs case-insensitively, ignoring trailing `.git`, trailing slashes, and https vs. ssh protocol forms);
- `README.md`, `TOOLS.md`, and `skills/` exist.

If cloning fails or the repository is unavailable, continue with the bundled references. Do not block the onboarding flow.

Completion criterion: either a verified clone is available or the agent has explicitly switched to the bundled references.

## Phase 3 — Discover existing user context

Do not interrogate the user about information that can be found safely. First ask permission for a read-only scan outside the current project. State which locations and commands you intend to inspect.

Inspect only approved locations, in this order:

1. **Agent and editor configuration**
   - `.cursor/`, `.cursorrules`, `.claude/`, `CLAUDE.md`, `AGENTS.md`, `.codex/`, `.agents/`, and existing skill directories.
2. **Operating system and shell**
   - OS family/version, shell, WSL or container context.
3. **Available development tooling**
   - command availability and versions for `git`, `node`, package managers, `python3`, `docker`, `cargo`, and `go` where relevant.
4. **Current project signals**
   - `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, dependency manifests, and project documentation.
5. **Git context in the current project**
   - remote names and recent local history. Do not inspect unrelated repositories without permission.

Never inspect `.env`, credential files, keychains, browser data, SSH keys, cloud credentials, or authentication databases.

Summarize findings in 3–5 bullets and ask the user to confirm or correct them.

Completion criterion: the user has confirmed a concise setup profile or corrected the findings.

## Phase 4 — Ask only what remains unknown

Ask targeted questions, preferably in one short batch:

1. Beginner, intermediate, or advanced with AI-assisted coding?
2. What do they mainly build?
3. How do they currently use coding agents?
4. What are their biggest pain points or time sinks?
5. What outcome do they want from this library today?

Skip questions already answered by the context scan. Adapt depth to the user: beginners need fewer and safer options; advanced users may want dense comparisons.

Completion criterion: stack, experience, current workflow, pain points, and desired outcome are sufficiently clear to make specific recommendations.

## Phase 5 — Search the library

Use the cloned repository's `TOOLS.md` when a verified clone is available. Otherwise read [`references/TOOLS.md`](references/TOOLS.md).

Match candidates against:

- the user's actual agent/editor;
- operating system and constraints;
- languages and frameworks;
- team size and workflow;
- pain points and goals;
- required setup effort and risk.

Do not recommend an item merely because it is popular. Prefer relevance over stars.

## Phase 6 — Recommend, do not install

Return 3–7 prioritized items:

### Start here
The strongest one or two matches.

### Worth a look
Relevant optional resources.

### Skip for now
One or two tempting but currently unsuitable tools, with a brief reason.

For each recommendation include:

- name and source URL;
- why it fits this specific user;
- expected benefit;
- setup effort and important prerequisites;
- meaningful risks or trade-offs;
- a clear next step that does not install anything.

End by asking which item, if any, the user wants to investigate.

Completion criterion: recommendations are individualized, traceable to the catalog, and no installation has occurred.

## Phase 7 — Act only on the user's choice

After the user selects an item:

1. inspect the project's current official documentation;
2. explain what would be installed or changed;
3. show the exact commands and affected paths;
4. ask for explicit approval;
5. install or configure only after approval;
6. verify the result with real output.

Approval for cloning the giveaway repository does **not** imply approval to install any recommended tool.

## Talk support

If the user asks about the presentation, use the cloned repository's current talk material when available. Otherwise read [`references/TALK-RECAP.md`](references/TALK-RECAP.md).

You can:

- recap the Graph-Driven Development talk;
- explain Prompt → Skill → Loop → Graph and the role of the harness;
- apply the loop-vs-graph decision framework to the user's own workflow;
- point to relevant tools in the catalog.

## Common pitfalls

1. **Claiming `npx skills add` cloned the full repository.** It installs this skill; the full clone happens only later, through this workflow and after approval.
2. **Cloning automatically.** Cloning is a network and filesystem write. Always request approval and a destination.
3. **Depending on files outside this skill.** Use bundled references unless a verified full clone is available.
4. **Scanning too broadly.** Ask permission, state scope, and exclude secrets.
5. **Recommending a giant stack.** Give a focused shortlist tied to actual needs.
6. **Treating clone approval as installation approval.** Every third-party tool requires its own decision.

## Verification checklist

- [ ] Repository purpose and value explained first
- [ ] Clone/update performed only after explicit approval
- [ ] Clone destination approved and remote verified
- [ ] Bundled references used when no full clone is available
- [ ] Context scan was read-only and within approved scope
- [ ] No secret-bearing locations inspected
- [ ] User confirmed the discovered context
- [ ] Recommendations are personalized and source-linked
- [ ] No recommended tool installed without separate explicit approval
