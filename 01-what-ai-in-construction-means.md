# What "AI in construction" actually means

The word is doing three jobs at once, and they fail in completely different ways. Naming which kind you
are looking at is the fastest way to tell a real product from a slide.

| Technology | What it does | Construction examples | What it is bad at |
| --- | --- | --- | --- |
| **Computer vision** | Reads images, drawings and video | Takeoff from plans, progress from 360° photos or scans, PPE and exclusion-zone detection, defect spotting | Anything not visible or not in the image set; thin fonts, overlapping detail, revisions |
| **Language models (LLMs)** | Reads and writes text | Finding a clause or spec section, answering questions over a document set, drafting RFIs, letters, minutes, scopes | Knowing whether a statement is *true* for your project; arithmetic; anything it has to cite |
| **Predictive models and statistics** | Forecasts from history | Cost at completion, schedule risk, cash flow, safety risk ranking | Projects with no comparable history; data that is stale, uncoded or inconsistent |

A fourth thing often gets the label and is none of the above: **workflow automation with a rules engine**.
An invoice that routes for approval, a form that turns a field note into a ticket, a dashboard that
refreshes itself. It is genuinely useful and it is not AI, in the same way that a spreadsheet formula is
not AI. Vendors blur this because "AI" sells budget.

## The uncomfortable part: most value today is the third kind

Much of what is honestly working on construction jobs is *arithmetic over data that used to be too
scattered to use*. Cost at completion from the job cost ledger and committed costs. A schedule risk score
from progress and float. A cash forecast from AR aging, AP due dates and billings.

That is not a disappointment. A forecast you can check line by line is more useful than a clever one you
cannot argue with in a meeting — and unlike the other two categories, its inputs and its working are both
inspectable. If you take one idea from this guide, take this one: **prefer the forecast you can audit.**

## How to tell which one you are being sold

Ask what the product reads, and what it does when it is unsure.

| If the vendor says… | It is probably | Ask |
| --- | --- | --- |
| "Upload your drawings and it produces the takeoff" | Computer vision | How do I correct a quantity, and does the correction stick? |
| "Ask questions across your documents" | LLM | Show me the citation for every answer, and what happens when there is no answer |
| "Predicts which jobs will overrun" | Statistics | Show me the training window, the inputs, and the last 12 months of accuracy on jobs like mine |
| "AI-powered dashboard" | Automation | What does it compute, and from which source system? |
| "Learns your company's way of estimating" | Unclear | With what data, how much of it, and who reviews the output? |

## What each kind needs from you before it works

- **Computer vision** needs a clean, complete, current drawing set — and a named person who owns revisions.
  Vision does not know that sheet A-201 was superseded; someone has to.
- **Language models** need documents that are actually in the system, in text a machine can read, with a
  version history you trust. Scanned PDFs and 400 MB of email attachments are not a document set.
- **Predictive models** need history coded to the same cost codes and the same job structure you use today.
  If your chart of accounts changed three years ago, that is the first thing to reconcile.

None of these is an AI problem. They are data problems, covered in
[your data decides what AI can do](03-your-data-decides.md).

## Three sentences to keep in your head

1. **If the output leaves the company, a person reviews it.** Always. No exceptions, in any category.
2. **If you cannot see the working, you cannot defend the number.** Prefer tools that show rows, sources
   and assumptions over tools that show a score.
3. **Buy the decision, not the technology.** "Which jobs are going over" is a decision. "AI-powered
   analytics" is a category.

---

Next: [the use cases that work today](02-use-cases/01-estimating-and-takeoff.md), or jump to
[your data decides](03-your-data-decides.md) if you want the preconditions first.
