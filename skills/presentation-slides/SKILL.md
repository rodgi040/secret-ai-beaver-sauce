---
name: presentation-slides
description: Use when the user wants the slides from the AI Beavers talks (e.g. "Graph-Driven Development", Cursor Meetup Hamburg) - downloads the slide images and their information from the secret-ai-beaver-sauce repository and walks the user through them. Note - the full presentations are still being submitted (see Status).
license: MIT
metadata:
  author: AI Beavers
  event: Graph-Driven Development, Cursor Meetup Hamburg
  status: presentations pending - submission expected within 24 hours of 2026-09-10
---

# Presentation Slides - Download & Walkthrough

You help the user get the slides of the AI Beavers talks and the information on them: download the slide files, list what each slide covers, and answer questions about them.

## Status - read this first

> **The presentations will be submitted within the next 24 hours** (announced 2026-09-10, expected by 2026-09-11).
> *Die Präsentationen werden in den nächsten 24 Stunden eingereicht.*

Until then, the repository contains only a **preview of the first 5 slides** of "Graph-Driven Development" in [`presentation/`](https://github.com/rodgi040/secret-ai-beaver-sauce/tree/main/presentation). Tell the user this before downloading anything:

- If the full decks are not in `presentation/` yet, say so plainly and offer the preview slides.
- Do not invent content for slides that are not in the repository.
- Suggest checking back later (or updating the clone) once the presentations have been submitted.

## Where the slides live

| Source | Path |
|---|---|
| Canonical repository | `https://github.com/rodgi040/secret-ai-beaver-sauce` |
| Slide folder | `presentation/` (images named `slide-NN-<topic>.jpg`) |
| Slide content as text | [`skills/talk-recap/SKILL.md`](../talk-recap/SKILL.md) - the per-slide summary of the talk |

The folder listing is the source of truth for which slides exist. Read it; do not assume a fixed slide count.

## Rules

1. **Downloading is a network and filesystem write.** Ask for approval and a destination directory before downloading or cloning anything.
2. Download only from the canonical repository above. Verify the remote/URL before using a local clone (compare case-insensitively, ignoring trailing `.git` and https vs. ssh form).
3. Do not run `git pull` automatically. Offer a fast-forward update (`git pull --ff-only`) only if the worktree is clean and the branch tracks `origin/main`.
4. If a fact is not on a slide or in the talk recap, label it as unverified.

## Step 1 - Check what is available

Prefer an existing verified clone of the repository (read-only check). Otherwise list the folder via the GitHub API (read-only network call - mention it to the user):

```bash
gh api repos/rodgi040/secret-ai-beaver-sauce/contents/presentation --jq '.[].name'
# or, without gh:
curl -s https://api.github.com/repos/rodgi040/secret-ai-beaver-sauce/contents/presentation
```

Report the slide list and whether the full presentations are already there (see Status).

## Step 2 - Download (after approval)

Ask: *"May I download the slides to `<destination>`?"* Then use one of:

```bash
# Option A - full clone (also gets the tool catalog and skills)
git clone https://github.com/rodgi040/secret-ai-beaver-sauce.git <destination>

# Option B - only the slide folder (sparse checkout)
git clone --filter=blob:none --sparse https://github.com/rodgi040/secret-ai-beaver-sauce.git <destination>
git -C <destination> sparse-checkout set presentation
```

Verify with real output that the files exist in `<destination>/presentation/`.

## Step 3 - Extract the information

For each slide, in order:

1. Read the image (if you can view images) and the matching entry in the talk recap.
2. Write one line: slide number, title, key message.
3. Collect terms and tools mentioned on the slides and map them to entries in [`TOOLS.md`](https://github.com/rodgi040/secret-ai-beaver-sauce/blob/main/TOOLS.md).

Offer the result as a short Markdown summary. Write it to a file only if the user asks for one.

## Step 4 - Go deeper

- For the talk's ideas (Prompt -> Skill -> Loop -> Graph, loop vs graph decision framework) hand over to the `talk-recap` skill.
- For tool recommendations hand over to the `secret-ai-beaver-source` / `repo-onboarding` skill.

## Verification checklist

- [ ] Status notice (presentations pending) shown to the user
- [ ] Download/clone only after approval, from the canonical repository
- [ ] Slide list taken from the actual `presentation/` folder
- [ ] No content invented for missing slides
