# Risks and controls

None of these risks is exotic. All of them have happened to contractors already, usually with a tool that
demoed beautifully. Each one has a boring control that works better than a policy statement.

| Risk | What it looks like | Control |
| --- | --- | --- |
| Confidently wrong answers | An invented clause, a missed revision, a takeoff that double-counts | Require citations and reconciliation to a known quantity; review everything that leaves the company |
| Data leaving your control | A contract pasted into a consumer chatbot | Business-tier tool with no-training terms; a written rule about what may be pasted |
| Alert fatigue | Hundreds of camera alerts nobody reads | Pilot on one site; measure false positives per day before scaling |
| Black-box forecasts | A risk score nobody can explain in a meeting | Only buy forecasts that show the rows and the reasoning |
| Write access | A tool that can change the ERP or the schedule | Read-only connections, in writing, with credentials you control |
| Silent drift | Revisions move on; the tool keeps using the old set | A named revision owner; a reconciliation step in the weekly routine |
| Over-reliance | "The system says" used to end a conversation | Every number has a human owner who is accountable for it |

## Confidently wrong is the default failure, not the exception

Language models produce fluent text whether or not they know the answer. Vision models produce a number for
every symbol they can pattern-match. Forecasting models produce a distribution from whatever data you give
them. In all three cases, the failure mode is **plausible and specific** — which is exactly what makes it hard
to catch.

Three controls actually work:

- **Citations or source rows.** Every answer that matters points at the page, the clause, the sheet or the
  ledger row. No citation, no reliance.
- **Reconciliation to something you already know.** Before trusting a takeoff, a forecast or a progress
  figure, check it against a number you already believe — a previous bid, last month's cost report, a physical
  count.
- **A named reviewer for anything leaving the company.** Not a committee, not a disclaimer — a person.

## What your contracts, insurers and clients expect

This is the part that gets skipped, and it is where the real exposure sits. Before rolling anything out:

- **Confidentiality.** Your contracts almost certainly restrict disclosure of drawings, pricing and
  commercial terms. Pasting them into a tool whose terms you have not read is a disclosure. Check the
  subprocessor list, the retention period, and whether your data trains anything.
- **Client and owner requirements.** Public sector and some private clients already require disclosure or
  approval of tools that process their data or imagery. Read the IT and data clauses, not just the scope.
- **Insurance.** Ask your broker whether an AI-driven decision — a safety alert ignored, a forecast relied on,
  a quantity submitted — changes anything about your cover. Ask about cyber cover for the data itself.
- **Employment and privacy law.** Monitoring staff and site imagery has notice, consultation and, in some
  places, works-council or union requirements. Biometric identification is restricted or banned in several
  jurisdictions.
- **Professional and contractual liability.** A wrong quantity or an unreviewed letter is your liability, not
  the vendor's. Check what the vendor's contract actually limits them to — usually the licence fee.
- **Records retention.** Minutes, notices and photos are evidence. Decide how long they live and who can see
  them, in advance of the dispute rather than during it.

Take the list to your lawyer and your broker. The purpose of this section is to make sure the conversation
happens before the pilot, not after the first claim.

## Model risk: the quiet one

Two failure patterns deserve names because they are so common:

- **Automation bias.** People accept a system's output more readily than a colleague's, especially when it is
  presented as data. The first time a forecast is wrong, ask how long it took anyone to notice.
- **Defensive documentation.** A generated method statement, safety talk or inspection record can look like
  compliance while carrying none of the thinking. If a document exists to be defensible, a person has to have
  actually engaged with it.

Both are countered by the same habit: **ask who would have caught this if the tool were wrong**, and make sure
the answer is a name.

## A one-page policy is enough to start

You do not need a forty-page AI governance framework to let people draft RFIs safely. You need a page that
says which tools are approved, what may never be pasted in, who reviews output, and who to ask when unsure.
Use the [acceptable use policy template](templates/ai-acceptable-use-policy.md), adapt it, and have someone
with authority sign it.

The cost of not having it is the ten minutes that a contract spends in a personal account.

---

Next: [a 90-day plan to start](05-a-90-day-plan.md) ·
[back to contents](README.md)
