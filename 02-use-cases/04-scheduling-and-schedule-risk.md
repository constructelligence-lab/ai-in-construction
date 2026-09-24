# Scheduling and schedule risk

**Answers the question:** how likely is the finish date we just committed to, and what is pushing it?

**Maturity:** useful where the schedule is real. Where the schedule is a document produced for the owner, no
tool can help, because the input is fiction.

**Data it needs:** a resource-loaded CPM schedule with real logic, updated weekly — plus duration history
from jobs that actually finished.

## What it actually does

- **Risk forecasting.** Simulates durations, weather and productivity variation to say "70% likely to finish
  by 14 March" instead of "finish date: 14 March". Output includes a distribution and, in good tools, the
  activities that drive it.
- **Generative scheduling.** Explores many sequences and resource combinations to propose alternatives —
  useful in preconstruction, during a long-lead procurement decision, or when a disruption forces a resequence.
- **Duration benchmarking.** Estimates activity durations from your own completed jobs by trade, size and
  crew, rather than from the number someone typed in 2019.
- **Constraint and sequence checking.** Finds activities that ignore logic, crews double-booked on the same
  day, and calendars that do not match reality.

## What it needs from you

- **A schedule that is updated, weekly, with actuals.** This is the whole game. A schedule that is updated
  only before the owner's meeting produces a forecast of the owner's meeting.
- **Real logic and constraints.** Relationships, lags, calendars, resource limits and long-lead procurement.
  If the schedule has no logic, the tool is guessing about your project.
- **Duration history in a comparable structure.** Your own history beats industry averages, but only if you
  can group jobs that are actually alike — by trade, size range and building type.
- **An honest baseline.** You cannot measure slip against a baseline that was edited last month.

## Where it goes wrong

- **Garbage in, confident out.** A risk distribution built on an unmaintained schedule looks sophisticated
  and is meaningless. This is the single most common way schedule AI fails in practice.
- **Black-box scores.** "Risk: high" that nobody can explain in a coordination meeting gets ignored by week
  two. Only accept outputs that name the drivers.
- **False precision.** A 68.4% chance of finishing by the 14th implies a level of knowledge about productivity
  and weather that you do not have. Treat the number as a ranking and a conversation starter, not a promise.
- **Treating the simulation as a commitment.** A generative schedule proposes a sequence; the people who
  build it still own the plan. Hand a crew a plan nobody consulted them on and watch the logic fail in the
  field.
- **The pencil-whipped schedule.** If the schedule you feed it is the one you show the owner rather than the
  one the field works to, you will get an accurate forecast of the wrong project.

## How to judge a pilot

Backtest, then run live:

1. Take **three completed jobs** with real, updated schedules and their actual finish dates. Load the
   schedule as of a set date — say 40% complete — and ask the tool to forecast.
2. Score two things: **accuracy** (was the eventual finish inside the predicted range?) and, more important,
   **lead time** — how many weeks before your own team flagged the slip did the tool flag it? A warning you
   cannot act on is trivia.
3. Then run it live on one job alongside the existing weekly update, and ask the planner whether the driver
   list matched what they believed, and whether it changed a decision.

## Questions worth asking a vendor

- What does it read — P6 XER, MS Project, CSV — and does it write back, or read only?
- Does it respect my logic and constraints, or does it override them with its own model?
- Where do the durations come from, and how large is the comparable-job set it draws on for a job like mine?
- Can I see **why** the risk score changed this week, activity by activity?
- What is the output: a date, a probability, a driver list, or a proposed plan?
- How was the model validated, and on how many completed projects?
- Who is expected to act on the output every week, and what does the product do to make that easy?

---

Related: [progress tracking](03-progress-tracking.md) ·
[job cost and cash forecasting](05-job-cost-and-cash-forecasting.md) · [back to contents](../README.md)

