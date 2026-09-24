# How to buy and pilot

A good demo and a good product are different things. A demo is a scripted path through clean data; a product
survives your messiest job in month five, when the same person has to keep feeding it and nobody from the
vendor is watching.

This chapter is about telling them apart cheaply, and about structuring a pilot so the decision is made on
evidence rather than on how the sales engineer made you feel.

## The demo rules that save the most time

- **Never demo on the vendor's data.** Send them two of your own projects beforehand, one clean and one messy,
  and watch them demo on those. Vendors who only demo on curated data have told you something.
- **Ask them to demo the correction, not the output.** Anyone can show a quantity appearing. Watch how a
  missed symbol, a wrong forecast driver or a wrong citation gets fixed, and how long it takes.
- **Break it on purpose.** Ask a question whose answer is not in the documents. Hand over a superseded drawing.
  Say a job nickname instead of a job number. Watch how the product fails; you will live with that behaviour.
- **Ask who does the weekly work after go-live.** If the answer is "it is automatic", ask what happens when the
  data is late, missing, or wrong — because it will be.
- **Ask for a reference on a job like yours**, sized like yours, and phone them without the vendor on the call.

## Structure a pilot so it can fail

A pilot with no success criteria is a purchase with extra steps. Before you start, agree in writing:

| Element | What to pin down |
| --- | --- |
| Scope | One decision, one job or one historical set, the named owner inside your company |
| Duration | Six to twelve weeks, with a fixed end date |
| Success criteria | Accuracy on known answers, hours saved, lead time gained — numbers, not adjectives |
| Your obligations | Who loads data, how long access takes, who is available for the setup |
| Cost | A paid pilot is fine and usually better: it aligns incentives and gets you real attention |
| Exit | What you get if you stop: your data, in a usable format, and confirmation it is deleted |
| Kill criteria | Written in week one, when everyone is still optimistic |

The point of a fixed end date is that it forces a decision. Pilots that roll into production by inertia are how
companies end up paying for four tools and using none of them.

## Pricing models, and the traps in each

| Model | Watch for |
| --- | --- |
| Per seat / per user | Seats expand quietly; a tool used by two people priced for twenty |
| Per project or per job | Definition of "project"; annual volume commitments; overage rates |
| Per volume (drawings, pages, documents) | A busy bid month pushing you into a higher tier |
| Platform fee plus modules | The module you actually need being in the tier above |
| Percentage of savings or of contract value | Hard to verify, and it misprices software badly over time |
| Free for the first year | The renewal conversation, and what the data load costs you on the way out |

Whatever the model, ask two questions: **what does year two cost**, and **what does it cost to leave**.

## Security and data review

Run this before the pilot, not during it. Send it to the vendor as a written questionnaire; a vendor who
hesitates at a data-processing questionnaire is a vendor with something to hide.

- Where is data stored and processed, in which countries, and which subprocessors are involved?
- Is our data used to train models — theirs or anyone else's? Get it in writing, including for subprocessors.
- What is the retention period, and what happens on termination: export format, deletion, and confirmation?
- SSO, MFA, role-based access, audit logs: what exists in the tier we are buying?
- Who at the vendor can see our data, and is that access logged?
- Penetration testing, certifications (SOC 2, ISO 27001), and when they were last renewed. Ask for the report,
  not the badge.
- Incident response: how do we get told, and how quickly?
- Cyber and professional liability insurance held by the vendor, and the limits.

## What a good answer sounds like

| Question | Strong answer | Weak answer |
| --- | --- | --- |
| How accurate is it? | "Here is a study on N projects, here is the methodology, here is where it degrades" | "95%+ accuracy" with no definition of accuracy |
| What if the data is wrong? | "Here is what we do when the schedule is stale — we surface it" | "Our customers keep their data clean" |
| Where does the cost at completion come from? | "Actuals, commitments, and the cost-to-complete your PM maintains; here is the workflow" | "Our AI calculates it" |
| Can I see the working? | Shows rows, sources and assumptions | Shows a score |
| Can it write back to our ERP? | "No, and it should not — read-only" | "Yes, full integration" |
| What does leaving look like? | A documented export and deletion path | Silence, or a data-hostage clause |

## Read the contract for three things

1. **Data rights.** Ownership, training use, retention, deletion, and what happens in an acquisition.
2. **Liability.** What the vendor's liability is capped at, and whether it covers a wrong quantity or a missed
   clause. It is usually capped at the fee, which is worth knowing before you rely on the output.
3. **Exit.** Notice period, data export format, deletion confirmation, and the transition to your own numbers
   if you stop.

Take the vendor questions checklist into the call: [vendor questions](templates/vendor-questions.md). Print it,
write the answers down, and keep them for the week-12 decision.

---

Next: [questions we get asked](07-faq.md) · [back to contents](README.md)
