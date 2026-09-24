# Job cost and cash forecasting

**Answers the question:** which jobs are going over, how much money are we actually exposed to, and when does
the cash land?

**Maturity:** the highest-value category for most contractors that already code their costs properly — and the
one where a human judgement still sits at the centre of the number.

**Data it needs:** hours and costs coded to the right job and cost code, committed costs in the system, a
maintained cost-to-complete, and read access to the ledger without a monthly PDF export in the way.

## What it actually does

- **Cost at completion.** Actuals to date, plus commitments, plus the remaining uncommitted cost to complete,
  projected forward — expressed as a variance against budget and an estimated margin at completion. Get that
  definition wrong and commitments get counted twice, which is one of the classic job cost errors.
- **Early warning.** Flags jobs whose trend is running ahead of estimate while there is still time to affect
  the outcome, rather than at month-end close, or at the final invoice.
- **Cash forecasting.** AR aging, retention, AP due dates, billing schedules and pay-when-paid chains,
  projected weekly or monthly: when money arrives, when it leaves, and when the gap is widest.
- **WIP position.** Over- and under-billing per job, and the exposure that hides inside it — a job that is
  over-billed and behind is a liability, not a win.
- **Labor and productivity signal.** Hours by cost code against budget and against production installed,
  which is how you find out in week four instead of week fourteen that a crew is losing money.
- **Invoice and duplicate checks.** Matching invoices to commitments and prior payments to catch double
  billing, which is unglamorous and pays for itself.

## What it needs from you

- **Hours coded to job and cost code.** The single biggest determinant of whether any of this works. If
  timecards are coded to "General" or corrected a month late, your forecast inherits that noise.
- **Commitments in the system.** Subcontracts and purchase orders recorded as commitments, not as a note in
  a spreadsheet on someone's desktop.
- **A cost-to-complete someone owns.** The forecast is only as good as the human judgement inside it, and
  that judgement has to be updated — ideally by the PM, weekly or monthly, and dated so the trend is visible.
- **A readable source.** A database you can query read-only, or an API. A monthly export someone emails
  around is a reporting process, not a forecasting input.
- **Consistent structure.** Multi-company and multi-entity jobs mapped deliberately, so a company switch
  does not silently change what a number means.

## Where it goes wrong

- **The cost-to-complete is engineering judgement, not maths.** No model removes this. What a good tool does
  is make the judgement visible, dated and comparable week to week, so a PM who says "no change" for six
  weeks and then reports a 12% overrun has to explain the six weeks.
- **The lag nobody accounts for.** Unposted time, unapproved change orders, pending change orders nobody has
  priced, stored materials not yet billed, backcharges not yet issued. A forecast that ignores unapproved
  change orders will look wonderful until the last month of the job, then collapse.
- **Argue-with-the-PM dynamics.** A number that arrives without its working gets rejected, and the tool is
  blamed. Show the rows: actuals, commitments, cost to complete, and the variance — every time.
- **Stale data dressed as insight.** If the ledger is five weeks behind, the forecast is five weeks behind,
  however good the model is. Fix the posting lag rather than buying a better forecaster.
- **Write access.** A forecasting tool does not need to write to your accounting system, ever. Insist on
  read-only, and get it in writing.
- **Ignoring the owner's side.** Cash is not just cost: it is billings, approvals and collections. A model
  that only projects cost will comfort you right up to the moment you miss payroll.

## How to judge a pilot

Backtest on closed jobs, because there is only one honest test:

1. Take **five to ten completed jobs**. For each, pull the forecast as it stood at roughly **50–60% complete**
   — a snapshot, not a reconstruction after the fact.
2. Compare against the **final cost**. Score the miss in percentage points per job and note the direction.
   Consistently optimistic forecasts point at either the cost-to-complete process or the model's handling of
   unapproved change orders and commitments — diagnose which one before blaming the tool.
3. Measure **lead time**: how many weeks earlier than your existing month-end reporting did the tool flag an
   overrun that did happen? That is the number to put in front of an owner.
4. Then run it live for a quarter, and check the unglamorous thing: **did anyone act?** A forecast that is
   right and ignored has changed nothing.

Use the [pilot scorecard](../templates/pilot-scorecard.md) so the result survives the enthusiasm of week one.

## Questions worth asking a vendor

- How do you read my data — read-only database connection, API, or file export — and can you write back at
  all? (The answer you want is no.)
- How do commitments, unapproved change orders and pending change orders flow into the forecast?
- Who maintains the cost to complete, in what workflow, and does the tool keep a dated history of it?
- Can I see the rows behind every number, all the way down to the source transaction?
- How do you handle multiple companies, entities or divisions under one system?
- What accuracy have you seen on jobs with less than eight weeks of history?
- Does it surface cash as well as cost — billings, retention, collections — or only cost?
- What does implementation actually require from my finance team, in hours, and who owns it after go-live?

---

Related: [your data decides](../03-your-data-decides.md) ·
[scheduling and schedule risk](04-scheduling-and-schedule-risk.md) · [back to contents](../README.md)
