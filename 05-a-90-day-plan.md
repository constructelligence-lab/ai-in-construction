# A 90-day plan to start

The failure mode of AI in construction is not bad technology. It is a company that buys six tools, runs none
of them on a real decision, and concludes that AI does not work in construction. That conclusion is usually
wrong, and the experiment that produced it was usually not an experiment at all.

Here is a plan that produces a real answer in twelve weeks: **one decision, one owner, one job.**

## The shape of it

| Weeks | What happens | Output |
| --- | --- | --- |
| 1-2 | Pick the decision | A one-page charter: the decision, the owner, the metric |
| 3-4 | Check the data | A go / fix-first / stop decision on data readiness |
| 5-8 | Pilot on history | Accuracy measured on jobs where you know the answer |
| 9-12 | Run it live on one job | A weekly routine someone acts on, and a written verdict |

## Weeks 1-2: pick the decision

Pick the decision that **costs the most when it is late** — not the most interesting technology. For most
contractors it is one of these:

- Which jobs are going over, while they are still running?
- Can we bid more work with the same estimators?
- Which subcontractors and suppliers are drifting, before the schedule says so?
- Where is next month's cash crunch coming from?
- Which safety leading indicators are moving on this site?

Write a one-page charter with four lines on it:

1. **The decision**, in one sentence, as a question.
2. **The owner** — a named person, not a department, who will act on the answer every week.
3. **The metric** — how you will know it worked, and the number today.
4. **The kill criteria** — what would make you stop, decided now, while it is still cheap to be honest.

If nobody will put their name on the owner line, you have found the reason this will fail, and the reason is
not the technology.

## Weeks 3-4: check the data

Run the three tests in [your data decides](03-your-data-decides.md) for your chosen decision: coded, current,
reachable. Then pick one:

- **Go.** The data is good enough. Start the pilot.
- **Fix first.** There is one specific gap — usually weekly cost coding, commitments in the system, or an
  unmaintained schedule. Fix it, and note that fixing it improves your existing reports too, so the four
  weeks are not wasted.
- **Stop.** The decision depends on data nobody collects, and collecting it is a project in itself. Say so
  out loud. Cancelling here is a successful outcome; the alternative is buying a tool and blaming it later.

Tell the vendor what you found. A vendor who runs away when you mention your posting lag was never going to
survive month three with you anyway.

## Weeks 5-8: pilot on history

This is the step almost everyone skips, and it is the only one that produces evidence cheaply. Run the tool on
**two or three finished jobs where you already know the answer**, then score it:

- **Accuracy.** How far off was it, per job, and in which direction? Consistently optimistic is a finding
  about your process, not just about the tool.
- **Lead time.** How long before your existing routine would this have told you? A warning you receive in time
  to act is worth money; an accurate post-mortem is worth a paragraph.
- **Effort.** Hours your team spent feeding it, correcting it and interpreting it. Include the person doing
  setup at 9pm.
- **Explainability.** Could the person who owns the decision retell *why* the answer came out that way, in a
  meeting, without the tool on screen? If not, the number will not survive contact with your PMs.

Use the [pilot scorecard](templates/pilot-scorecard.md), and write the result down before the vendor's next
presentation so that the enthusiasm of a good demo does not overwrite the evidence.

## Weeks 9-12: run it live on one job

One live job, with the owner from week 1 in the loop, weekly:

- **Week 9:** load the live data, agree the weekly routine, and tell the people affected what is changing --
  including the field, and including any trade partner who will see the output.
- **Weeks 9-12:** the owner reviews the output at a fixed time each week and writes down what they did about
  it. "Nothing" is a legitimate entry, and a pattern of nothing is the finding.
- **Week 12:** the verdict. Expand, adjust, or stop. Write it down on the same one-page charter you started
  with, so the next decision has a precedent.

## What to measure at week 12

| Measure | Why it matters |
| --- | --- |
| Did the decision change? | The only question that ultimately counts |
| Lead time gained | Days or weeks earlier than your existing routine |
| Hours spent vs hours saved | Include setup and correction, not just weekly use |
| Accuracy vs the known answer | From the historical pilot, not the vendor's case study |
| Adoption | Did the owner still open it in week 12 without being reminded? |

## Worked example (invented numbers)

> A 40-person general contractor with roughly $30M of annual revenue decides on the question *"which jobs are
> going over?"* — because it lost money on two jobs last year that looked fine until the final month.
>
> In weeks 3-4 it discovers that commitments are tracked in three desktop spreadsheets and that timecards are
> posted up to nine days late. It spends three weeks fixing exactly those two things, which also makes
> month-end close two days faster.
>
> In weeks 5-8 it back-tests on five closed jobs. The forecast at 50% complete lands within 3% of final cost
> on four of them, and misses by 11% on the one with a large unapproved change order. That is a finding about
> the change-order process, and it becomes a rule: unapproved change orders are entered as a distinct line.
>
> In weeks 9-12 it runs on one live $4M job, reviewed every Monday by the owner with the PM. In week 11 it
> flags a masonry crew running 14% over on labour with two floors still to go; the PM reassigns a crew and the
> job closes at 2% over budget. Nothing else in the pilot changed a decision, and that one catch paid for the
> year.
>
> The verdict at week 12 is *expand to all jobs* — but only because the data fixes happened first, and
> because the Monday routine survived twelve weeks without anyone being reminded.

Those numbers are invented to show the shape of a result. Yours will differ, and the shape is the point: data
fix, historical back-test, one live decision, written verdict.

## The five things people forget

1. **The field is a stakeholder.** If progress, safety or productivity data changes what crews are measured
   on, tell them first, in person.
2. **Setup is a project.** Budget hours for implementation, mapping, and the first month of corrections.
   Vendors understate this; contractors under-budget it.
3. **Someone has to own the weekly routine.** Tools do not create habits; calendars and named owners do.
4. **The data will be dirty in ways you did not expect.** Job names with three spellings, two cost code lists,
   a company switch nobody documented. Expect to find them and fix them.
5. **Write the rules at the same time.** The [acceptable use policy](templates/ai-acceptable-use-policy.md)
   takes an hour and prevents the incident that would otherwise set the whole effort back a year.

---

Next: [how to buy and pilot](06-how-to-buy-and-pilot.md) · [back to contents](README.md)
