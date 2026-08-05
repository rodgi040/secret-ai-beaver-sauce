![secret-ai-beaver-sauce](assets/banner.png)

# secret-ai-beaver-sauce

**An open-source giveaway library for AI-assisted software development** - curated tools, frameworks, and agent skills, handed out at a Cursor community talk (House of AI, Hamburg).

This repo is not a framework you install. It's a **library your coding agent can search**: your agent reads this repo, gets to know you and your system, and then recommends the tools and skills that actually fit you. You decide what to use.

## Quickstart - install the onboarding skill

Install the main skill into your coding agent (Cursor, Claude Code, Codex, ...) with one command:

```
npx skills add rodgi040/secret-ai-beaver-sauce --skill secret-ai-beaver-source
```

Your agent will ask your permission, then scan known context locations read-only (editor configs, installed tooling, project files), confirm its findings with you, ask a few targeted questions, search the library, and come back with tailored recommendations. It will never install or configure anything without your explicit approval.

Prefer a specific agent? Add `--agent <name>` (e.g. `--agent cursor`). Want it available everywhere? Add `--global`.

Alternatively, clone the repo (or just open it in your editor) and paste this command into your coding agent:

```
Read skills/repo-onboarding/SKILL.md in this repository and follow it
step by step. You are now my onboarding librarian: first discover what
you can learn about me and my system from my machine (read-only), ask me
only what is still unknown, then search TOOLS.md and recommend the tools
and skills that fit me. Don't install anything without asking me.
```

## What's inside

| File | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | The onboarding guide every agent reads first - context, interview flow, recommendation rules |
| [`TOOLS.md`](TOOLS.md) | The library: curated tools, frameworks & skills with GitHub links and "best for" hints |
| [`skills/secret-ai-beaver-source/`](skills/secret-ai-beaver-source/SKILL.md) | The installable main skill: explains the repo, then onboards you and recommends fitting tools |
| [`skills/repo-onboarding/`](skills/repo-onboarding/SKILL.md) | The repo-native onboarding flow agents follow after cloning (same steps, no install needed) |
| [`skills/talk-recap/`](skills/talk-recap/SKILL.md) | Explains the talk's content (Graph-Driven Development) - so your agent can recap it and help you apply it |
| [`presentation/`](presentation/) | The talk slides as images - browse them anytime |
| [`assets/`](assets/) | Repo artwork |

## Disclaimer

All content in this repository is provided **as is**, without any warranty. The maintainer assumes **no liability** for the contents of this repository, the linked third-party projects, or any consequences of installing or using them. You install and use everything at your own risk - review third-party code before running it.

## License

Content in this repository is shared for the community. Linked third-party projects are licensed by their respective owners (check each linked repo).
