# Documents and contract review

**Answers the question:** where is the clause, what did we agree, and what are we on the hook for?

**Maturity:** mature for search and summarising, early and risky for anything that reads as advice.

**Data it needs:** documents that exist, are in the system, and are readable as text — with the version
history and addenda that tell you which one governs.

## What it actually does

- **Search with an answer.** Instead of "find the clause", you ask "what's the notice period for a delay
  claim" and get the clause, ideally with a citation you can click.
- **Obligation extraction.** Insurance limits, bond requirements, liquidated damages, retainage, notice
  deadlines, pay-when-paid, no-damage-for-delay, termination for convenience — pulled into a table someone
  can chase.
- **Drafting.** RFIs, response letters, minutes, scopes, submittal cover letters.
- **Summarising.** A 300-page spec into the twenty things that affect your trade, or a subcontract into the
  clauses that differ from your standard.

## What it needs from you

- **The documents, not their ghosts.** If the answer lives in a project manager's inbox as an attachment, no
  tool can find it. A document set is a place: a folder, a platform, an export that is kept current.
- **Text, not pixels.** Scanned images need OCR, and OCR of a stamped, hand-annotated drawing set is
  unreliable. Know which of your documents are text and which are pictures.
- **Version discipline.** Addenda, bulletins and reissued specs must be in the set, marked as governing. A
  language model has no idea that section 07 92 00 Rev 2 replaced Rev 1 unless the set says so.
- **A question.** These tools are much better at "find X" than at "tell me everything important".

## Where it goes wrong

- **The invented clause.** This is the failure everyone has heard of and it still happens: a fluent,
  confident summary of a clause that does not exist. The control is mechanical: **no citation, no answer.**
  If the tool cannot point at the page, treat the answer as a draft, not a finding.
- **Confidently summarising the wrong revision.** Worse than inventing, because it is plausible. It produces
  a real clause with the wrong obligation attached.
- **Comfort replacing diligence.** "The AI reviewed the contract" is not a contract review. On a job with a
  meaningful contract value, the commercial terms still get read by a human who is accountable for them.
- **Confidentiality.** Contracts, pricing, personnel data and claim correspondence pasted into a consumer
  tier assistant is a disclosure, and it may breach the confidentiality clause in the very contract you are
  asking about. See the [acceptable use policy template](../templates/ai-acceptable-use-policy.md).

## How to judge a pilot

Build a **known-answer test set** before you look at any product:

1. From three real projects, write **20 questions with known answers** — a notice period, a retainage
   percentage, a warranty duration, a scope inclusion, a specification section for a material. Write down
   the governing document and the page yourself, first.
2. Run all 20 through the tool. Score **correct**, **correct-with-wrong-citation**, **wrong**, and
   **refused to answer**. A tool that says "I can't find that" scores better than one that guesses.
3. Time the same questions against your current method — usually a phone call and a scroll through a PDF.
4. Then test the honest edge case: ask for something that **is not in the document set** and see whether it
   says so.

Anything below "every answer carries a citation that survives a spot check" is not ready to be relied on for
commercial terms, whatever the demo felt like.

## Questions worth asking a vendor

- Show me the citation for every answer, and tell me what happens when the answer isn't in the set.
- How do you handle addenda and superseded revisions?
- Can it produce an obligations table with dates I can put in a calendar, and export it?
- Where is my document set stored and processed, which subprocessors touch it, and for how long is it kept?
- Are my documents used to train any model — in writing, including for your subprocessors?
- Can the assistant be restricted to a project folder, so a question about job A cannot reach job B?
- Does it read drawings, or only text documents? If it claims drawings, ask for a test on a real scanned
  sheet with hand annotations.
- What does the retention and audit log look like if I need to prove who saw what?

---

Related: [risks and controls](../04-risks-and-controls.md) ·
[admin, drafting and general assistants](07-admin-drafting-and-assistants.md) ·
[back to contents](../README.md)
