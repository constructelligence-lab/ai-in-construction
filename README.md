# AI in Construction: a practical guide

Most construction AI writing is written for people who want to sell you something, or for people who
have never had to explain a cost overrun to a client. This guide is written for the person who has to
decide: *is any of this worth doing on my jobs, and where do I start?*

It is short on hype and long on the parts that decide whether AI works in a construction company —
which decisions it can improve, what your data has to look like before any of it works, what goes
wrong, and how to run a pilot you can actually judge.

**Updated September 2026 · roughly a 45 minute read, or a 90-day plan if you do the work.**

---

## The short version

If you read nothing else, read this:

- **Most of the value today is arithmetic over data you already own** — cost at completion, schedule risk,
  cash — not magic. Prefer the forecast you can audit.
- **The label covers three different technologies** with three different failure modes: computer vision,
  language models and predictive statistics. Name which one you are looking at before you buy it.
- **Your data decides.** Coded, current, reachable. Fixing those three pays for itself before any AI arrives.
- **One decision, one owner, one job, twelve weeks.** That is the pilot, and it beats a company-wide rollout
  every time.
- **If the output leaves the company, a person reviews it.** If you cannot see the working, you cannot defend
  the number.

## Who this is for

| If you are… | Start with | The question you actually have |
| --- | --- | --- |
| Owner / GM | [A 90-day plan](05-a-90-day-plan.md) | "What should I spend on this, and what do I get?" |
| Estimator / chief estimator | [Estimating and takeoff](02-use-cases/01-estimating-and-takeoff.md) | "Will this bid more work with the same team?" |
| Project manager / superintendent | [Progress tracking](02-use-cases/03-progress-tracking.md), [Scheduling](02-use-cases/04-scheduling-and-schedule-risk.md) | "Does this tell me something I don't already know?" |
| Controller / finance | [Job cost and cash forecasting](02-use-cases/05-job-cost-and-cash-forecasting.md) | "Which jobs are going over, while they're still running?" |
| IT / ops lead | [Your data decides](03-your-data-decides.md), [Risks and controls](04-risks-and-controls.md) | "What has to be true before we plug a tool in?" |
| Anyone being sold to | [How to buy and pilot](06-how-to-buy-and-pilot.md) | "How do I tell a real product from a demo?" |

## Contents

1. **[What "AI in construction" actually means](01-what-ai-in-construction-means.md)**
   Three different technologies, three different failure modes, and how to tell which one you're being sold.

2. **The use cases that work today** — what each does, what it needs from you, where it goes wrong, and how to judge it:
   - [Estimating and takeoff](02-use-cases/01-estimating-and-takeoff.md)
   - [Documents and contract review](02-use-cases/02-documents-and-contract-review.md)
   - [Progress tracking](02-use-cases/03-progress-tracking.md)
   - [Scheduling and schedule risk](02-use-cases/04-scheduling-and-schedule-risk.md)
   - [Job cost and cash forecasting](02-use-cases/05-job-cost-and-cash-forecasting.md)
   - [Safety and site monitoring](02-use-cases/06-safety-and-site-monitoring.md)
   - [Admin, drafting and general assistants](02-use-cases/07-admin-drafting-and-assistants.md)

3. **[Your data decides what AI can do](03-your-data-decides.md)**
   Coded, current, reachable. The three properties that separate a tool that works from one that produces
   plausible nonsense — and why fixing them pays for itself before any AI arrives.

4. **[Risks and controls](04-risks-and-controls.md)**
   Confidently wrong answers, data leaving your control, alert fatigue, black-box forecasts, write access,
   and what your contracts and insurers expect from you.

5. **[A 90-day plan to start](05-a-90-day-plan.md)**
   Pick one decision, check the data, pilot on jobs where you know the answer, then run it live with a named
   owner. Includes a worked example and kill criteria.

6. **[How to buy and pilot](06-how-to-buy-and-pilot.md)**
   The questions that separate a product from a demo, what a good answer sounds like, and how to structure a
   paid pilot.

7. **[Questions we get asked](07-faq.md)**

## Templates you can use today

| Template | Use it for |
| --- | --- |
| [AI use-case scorecard](templates/ai-use-case-scorecard.csv) | Comparing candidate use cases on hours, cost and risk before you buy |
| [Pilot scorecard](templates/pilot-scorecard.md) | Scoring a pilot on evidence instead of enthusiasm |
| [AI acceptable use policy](templates/ai-acceptable-use-policy.md) | A one-page rule set for what staff may paste into general AI tools |
| [Vendor questions](templates/vendor-questions.md) | The checklist to take into a sales call |

## What this guide deliberately does not do

- **It does not name a winner.** Tool capabilities change quarterly; the questions that expose a weak
  product do not. Where tools are named at all, they are named as categories.
- **It does not quote statistics it cannot source.** Where a number would help, it tells you how to measure
  your own instead. Your hours are the only statistic that matters to your decision.
- **It does not promise that AI replaces anyone on site.** Nothing in here does that, and nothing you buy
  today will either.
- **It is not legal, tax or insurance advice.** Chapter 4 covers the questions to take to your lawyer,
  broker and accountant — not the answers they should give.

## How to use it

Read it once, then do chapter 5. The failure mode of AI in construction is not bad technology — it is a
company buying six tools, running none of them on a real decision, and concluding that AI doesn't work in
construction. One decision, one owner, one job, twelve weeks.

Each use-case chapter repeats the vendor questions and the back-test method on purpose, so that any one of them
can be handed to the person who owns that decision and read alone. Start with
[the 90-day plan](05-a-90-day-plan.md) if you would rather read one chapter and get moving.

---

*Worked examples in this guide use invented numbers and are labelled as such. Formulas and process steps
are standard construction practice.*

<!-- begin:family -->
## More from Constructelligence

Open construction resources from the same team, all maintained alongside this one:

| Repository | What it is |
| --- | --- |
| [Construction data migration](https://github.com/constructelligence-lab/construction-data-migration) | A guide and toolkit for moving a contractor between systems, and proving nothing was lost. |
| [Construction project records](https://github.com/constructelligence-lab/construction-project-records) | Open schemas, templates and a checker for RFIs, submittals, change events, daily reports and punch lists. |
| [Construction reference data](https://github.com/constructelligence-lab/construction-data) | Cost codes, units, waste factors, pay units, trade sequence, glossary and metric formulas in CSV. |
| [Construction reference MCP server](https://github.com/constructelligence-lab/construction-mcp) | An offline MCP server that gives AI assistants construction reference data and calculators. |
| [Construction prompts](https://github.com/constructelligence-lab/construction-prompts) | 28 prompts for ChatGPT, Claude and Gemini, from bid go/no-go to notice letters. |
| [Construction agent skills](https://github.com/constructelligence-lab/construction-agent-skills) | 28 installable agent skills for Claude Code and any agent that reads SKILL.md. |
| [Open source construction tools](https://github.com/constructelligence-lab/open-source-construction-tools) | Open source software for BIM, CAD, scheduling and site work, verified against the GitHub API. |

<!-- end:family -->

---

*Maintained by [Constructelligence](https://constructelligence.co) — building the AI infrastructure for
construction.*
