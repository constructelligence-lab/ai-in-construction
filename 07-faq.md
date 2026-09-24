# Questions we get asked

## Will AI replace construction jobs?

Not the ones on site, and not estimators or project managers. There is no technology in this guide that
decides anything on its own, and there is no evidence from real projects that any of it removes the need for a
competent person on site, an estimator's judgement about means and methods, or a superintendent's read of a
crew.

What it does remove is repetitive work: tracing quantities, hunting for a clause, rebuilding the same report,
retyping minutes. Done well, that converts into *more bids with the same team* and *problems found earlier* --
which is a growth story, not a headcount story. Any vendor selling you the other version is selling you a
fantasy.

## Is it safe to put construction documents into a general AI assistant?

Only on a business plan whose terms say your data is not used to train models, and only with a written company
rule about what may be pasted. Even then, three categories should stay out of general assistants entirely:

- contracts still under negotiation, and anything marked confidential or under an NDA
- pricing, bid strategy, and margin information
- personal data: medical records, disciplinary records, ID documents, payroll detail

Use the [acceptable use policy template](templates/ai-acceptable-use-policy.md). It takes an hour and it
prevents the incident that would otherwise set your whole AI effort back a year.

## Where should a contractor start?

With the decision that costs the most when it is late — usually "which jobs are going over" or "can we bid more
work with the same estimators". Then check the data, pilot on jobs where you know the answer, and run it live
on one job with a named owner. [The 90-day plan](05-a-90-day-plan.md) is the whole answer, and it is deliberately
unglamorous.

The most common mistake is starting with the technology instead of the decision. The second most common is
skipping the check on whether the underlying data is coded, current and reachable.

## How much does this cost?

It varies far too much to quote honestly here, and any guide that gives you a number is guessing about your
size and scope. What you can control is the shape: pilots are usually a modest monthly fee for a short term,
and production pricing runs from a few hundred dollars a month for a single-seat assistant to six figures a
year for a platform across a large contractor.

Two rules matter more than the sticker price. **What does year two cost?** Introductory pricing is a marketing
expense, and renewals are where it comes back. **What does it cost to leave?** If the answer is "your history,
insights and configuration stay with us", you have not bought a tool, you have rented your own data.

## Do we need a data scientist?

No. You need a named owner for the decision, someone in finance or IT who can get read-only access to the
system that holds the data, and a willingness to fix cost coding. Every successful deployment we have seen in
a mid-sized contractor was run by an operations or finance person who understood the business, not by a data
scientist.

## We are a 15-person company. Is any of this for us?

The general assistants are: drafting RFIs, letters and minutes is the cheapest, most immediately useful thing
in this guide, and it works at any size.

Takeoff tools get affordable fast when your alternative is an estimator working weekends. Forecasting tools are
harder to justify when you have four jobs and know every one of them personally — though household-name
forecasting is worth testing the moment you have more active jobs than you can hold in your head. Camera
analytics usually are not worth it below a certain site size, and the honest answer depends on your risk
profile rather than your revenue.

## Our schedules and cost codes are a mess. Does that rule us out?

It rules out relying on forecasts until the specific inputs for *your* decision are fixed — not AI in general.
Run the three tests in [your data decides](03-your-data-decides.md), find the one gap that blocks your chosen
decision, and fix it. You will get better month-end reporting out of the fix whether or not you ever buy the
tool.

## How do I know whether it is working?

Measure it before, on jobs where you already know the answer. Accuracy against known outcomes, lead time
against your existing routine, hours spent against hours saved, and adoption — did the named owner still open
it in week twelve without being reminded? [The 90-day plan](05-a-90-day-plan.md) has the scorecard, and the
templates folder has a version you can fill in.

If you cannot answer "did any decision change because of this?" then the honest answer is that it has not
worked yet, whatever the dashboard says.

## What in this space is actually hype?

- **Fully autonomous estimating.** Quantities, yes. Pricing, means, methods and risk still need an estimator.
- **AI that decides anything on site without review.** Tools flag; people decide.
- **Anything that forecasts without your history**, or offers a risk score nobody can explain.
- **"AI-powered" attached to a rules engine.** A workflow that routes an invoice is useful; calling it AI is
  marketing.
- **Robotics claims from a video.** Watch for what is actually deployed, on how many sites, for how long.
- **Anything that promises to work on data you do not have.** No model fixes an uncoded timesheet.

## How does this relate to BIM, digital twins and robotics?

They share inputs, not purposes. A current model is what makes progress tracking possible; progress tracking is
what makes a digital twin anything other than a modelling bill. Most contractors get more value from one
decision made weekly than from a twin nobody updates — and the sequencing in
[the 90-day plan](05-a-90-day-plan.md) applies to all of it.

## Will our people actually use it?

They will if it makes their week easier and does not feel like surveillance. That is a management problem, not
a technology problem, and it has three parts: tell people what is changing and why, before it changes; give the
output to someone who is expected to act on it; and be honest about what the data will and will not be used
for — especially for progress and safety tools that touch the field.

Tools that arrive as a surprise are the ones that get worked around.

---

[Back to contents](README.md)
