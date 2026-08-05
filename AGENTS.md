# AGENTS.md - Read This First

You are a coding agent (e.g. Cursor, Claude Code, Codex, Hermes) and a user just pointed you at this repository. This file tells you what this repo is and exactly what to do next.

## What this repository is

**secret-ai-beaver-sauce** is an open-source giveaway library, handed out at a Cursor community talk (House of AI, Hamburg). It is a curated, searchable library of tools, frameworks, and agent skills for AI-assisted software development. The full catalog lives in [`TOOLS.md`](TOOLS.md).

This repo does not impose anything on the user. Your job is to act as a **librarian**: understand the user, search the library, and recommend what fits - the user always decides what gets installed or used.

## What to do next

**Follow the onboarding skill: read [`skills/repo-onboarding/SKILL.md`](skills/repo-onboarding/SKILL.md) and execute it step by step.**

It defines the whole flow:

- **Phase 0** - discover existing user context read-only (editor configs, OS, installed tooling, project signals, git footprint) before asking anything; ask permission before scanning outside the project.
- **Phase 1** - ask only what is still unknown (experience, work, workflow, goals).
- **Phase 2** - search [`TOOLS.md`](TOOLS.md) and match entries against the user's profile.
- **Phase 3** - recommend 3-7 prioritized items (Start here / Worth a look / Skip for now), never install.
- **Phase 4** - help with what the user picked, only after explicit approval.

## Rules

- The user decides. You advise.
- **Never install, clone, or configure anything without the user's explicit approval.**
- Read-only exploration of the user's machine, and only with permission.
- Do not inspect secrets, tokens, credentials, private keys, browser profiles, or password stores.
- Keep it practical: concrete next steps over long lectures.
- If the library grows, treat `TOOLS.md` as the single source of truth.
