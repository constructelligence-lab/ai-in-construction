# Your data decides what AI can do

Every use case in this guide runs on data most contractors already hold: drawings, schedules, the job cost
ledger, timecards, contracts, photos, invoices. The difference between a tool that works and one that
produces plausible nonsense is almost never the model. It is whether that data is **coded**, **current** and
**reachable**.

| Property | What it means | What it costs you when it is missing |
| --- | --- | --- |
| **Coded** | Costs and hours posted to the right job and cost code, consistently | Forecasts inherit the noise; labour productivity is unmeasurable |
| **Current** | Schedules updated weekly, models to the latest revision, timecards posted weekly | The tool answers confidently about last quarter's job |
| **Reachable** | In a database, platform or folder a tool can read — not in someone's inbox | Every project becomes a manual export, and it stops in month two |

## Fixing this pays for itself before any AI arrives

This is the part vendors skip, because it is not their product. But wait: if you improve cost coding, every
report you already have gets better — your WIP, your job cost reports, your month-end close, your ability to
answer "how are we doing on the Riverside job" without a phone call. Those benefits arrive whether or not you
ever buy an AI product. They also happen to be the precondition for everything in this guide.

So treat data readiness as the first project, with its own value, not as an IT toll you pay on the way to
something more interesting.

## The three properties, in practice

### Coded

- Are hours posted to the job **and** the cost code, by the end of the week they were worked?
- Do field staff know which cost code to use — and is the list short enough that they can choose correctly
  under pressure at 6am?
- Do change orders get their own codes, so you can see whether the work was actually covered?
- If your chart of accounts changed, has history been mapped so that three years of jobs are comparable?

**The test:** pick one recent job and try to explain, from the system alone, why labour came in over budget by
cost code. If that takes an afternoon and three phone calls, no forecasting tool can save you.

### Current

- Is the schedule updated weekly with actual progress, by someone whose job depends on it?
- Are the model and drawing set to the latest revision, with superseded sheets actually removed?
- Do timecards and invoices get posted within days, not at month-end?
- Do you know today which subcontracts have been issued but not yet in the ledger as commitments?

**The test:** ask for the current schedule and current drawing set on a live job. If assembling them takes
longer than five minutes, that is your readiness gap, and it is the one that breaks progress tracking and
schedule risk first.

### Reachable

- Can a read-only system read the tables you need directly, or is a human exporting a PDF every month?
- Are documents in a document management system, SharePoint, or a platform — or spread across inboxes?
- Can you grant scoped, read-only access without handing over administrative credentials?
- Is there one source of truth per thing (one job list, one cost code list, one vendor list)?

**The test:** ask for the labour hours by cost code for the last twelve months, per job, as a file. If that
request needs a meeting, you have found the constraint.

## Minimum viable data, per use case

| Use case | What must be true first |
| --- | --- |
| Estimating and takeoff | Current vector drawings, revision control, cost codes the quantities map onto |
| Document search and review | Documents in one place, in text, with addenda marked |
| Progress tracking | Weekly capture habit, current model, weekly schedule update, shared location names |
| Schedule risk | Resource-loaded CPM with logic, updated weekly, plus duration history |
| Job cost and cash forecasting | Weekly timecards coded to cost codes, commitments in the system, owned cost-to-complete |
| Safety analytics | Incident and near-miss records with activity, mechanism, trade, phase |
| General assistants | A written policy, a business-tier tool, a named reviewer |

Notice how few rows need anything new. Almost every row needs something you already have, made honest.

## The five things worth fixing whether or not you buy anything

1. **Weekly timecard coding** to job and cost code, with a supervisor review before it posts.
2. **Commitments in the ledger** — subcontracts and POs entered as commitments, not tracked in a desktop
   spreadsheet.
3. **One job list and one cost code list**, used by the field, the office and the accounting system.
4. **A named revision owner** for drawings and models, with superseded versions removed rather than archived
   in the same folder.
5. **A weekly schedule update** that reflects what the field believes, not what the owner wants to hear.

Each of these is unglamorous. Together they are the reason two contractors can buy the same product and get
completely different results.

## A note on history

Forecasting tools need history, and the honest question is whether you have *comparable* history. A contractor
who has built twenty similar warehouses has a strong basis for cost and duration forecasting. A contractor
whose last three jobs were a school, a plant upgrade and a fit-out has a much weaker basis, and should be
sceptical of confident predictions.

Ask any vendor: how many projects like mine are in your training data, and what accuracy did you see on the
ones with the least history? The answer tells you whether you are buying a forecast or a guess with a
polished interface.

---

Next: [risks and controls](04-risks-and-controls.md) ·
[back to contents](README.md)

