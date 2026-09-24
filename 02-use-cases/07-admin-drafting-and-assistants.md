# Admin, drafting and general assistants

**Answers the question:** how much of the paperwork — RFIs, letters, minutes, scopes, safety talks, submittal
cover letters — can come off the critical path?

**Maturity:** mature and immediately useful, provided you accept one rule: a named person reviews everything
before it leaves the company.

**Data it needs:** a business-tier tool with contractual terms about your data, a written rule about what may
be pasted in, and your own bank of past documents to work from rather than generating from nothing.

## What it actually does

- **Drafts from facts you supply.** Turn a superintendent's five bullet points into a proper RFI, a delay
  notice, a scope of work for a subcontract, or minutes that read like a grown-up wrote them. Delay notices
  and subcontract scopes carry contractual consequences: check the notice period in the contract and have
  someone with commercial authority approve before either is issued.
- **Rewrites and re-tones.** The same message for an owner, a subcontractor, or a supplier — firmer where it
  needs to be firm, without being inflammatory.
- **Summarises.** A 40-minute meeting transcript into a decision list, a long spec into the trade-relevant
  clauses, a submittal package into a reviewer's checklist.
- **Translates and clarifies.** A subcontractor's email written in a second language, or a subcontract
  clause restated in plain English for a foreman. Label the restatement as a summary and keep the contract
  wording as the governing text — a paraphrase can shift a legal meaning without anyone noticing.
- **Standardises.** Your RFI format and tone, applied consistently by everyone from a first-year coordinator
  to a 25-year veteran — worth more than the time saved.

## What it needs from you

- **A business plan, not a consumer account, for anything work-related.** Written terms that your data is not
  used to train models, administrative controls, ideally SSO and an audit log.
- **A written rule on what may be pasted.** The
  [acceptable use policy template](../templates/ai-acceptable-use-policy.md) covers the categories that
  matter: contracts under negotiation, pricing and bid strategy, personal and medical data, anything under
  confidentiality or an NDA, and anything a client has told you to protect.
- **A reviewer who owns the output.** Every RFI, letter and set of minutes goes out under someone's name.
  That person is the reviewer.
- **A library of your own documents.** A tool that writes from your last twenty RFIs beats one that invents
  from general knowledge — for tone, for terminology, and for internal consistency.

## Where it goes wrong

- **Plausible, wrong, and specific.** Invented specification numbers, invented clause references, invented
  quantities. Anything checkable must be checked, and the person checking needs to know it is their job.
- **Letters that inflame a dispute.** Tone is a commercial lever. A drafted notice that reads as aggressive
  can cost more than the time it saved, particularly mid-claim.
- **Minutes that record a decision nobody made.** This is the sharpest edge in this chapter. Minutes become
  the contemporaneous record, and a summariser that infers agreement from discussion has just changed your
  contractual position. Approve minutes line by line, and never let a summary of a change discussion
  circulate as a change.
- **Quiet commitments.** A drafted email that offers a date, a price or a variation. Check it as you would
  check a letter — the model does not know what you are authorised to agree.
- **Data leakage through convenience.** The most common breach is not a sophisticated attack. It is a
  contract pasted into a personal account to save ten minutes.
- **Copy-paste documentation.** If a safety talk or method statement is generated rather than thought about,
  it is generic advice in a company template. Regulators, insurers and competent clients notice.

## How to judge a pilot

Pick one document type you produce often, and count:

1. Choose the highest-volume candidate — typically RFIs, weekly owner updates, or meeting minutes.
2. Run **twenty real examples** through the tool. For each, record **minutes to a sendable draft** and
   **corrections required**, split into formatting, tone and **factual errors**.
3. Any factual error rate above zero means the review step is mandatory, and must be visible in the workflow
   rather than assumed.
4. Ask two people outside the pilot — someone who reads the output, like a client rep or a superintendent —
   whether the quality changed. Their answer decides whether you roll it out.

## Questions worth asking a vendor

- Are my inputs and outputs excluded from model training, in writing, including for subprocessors?
- Where is data processed and stored, and what is the retention period?
- Is there SSO, an audit log, and admin control over who can use it?
- Can it work from **our** past documents — retrieval over our own library — rather than general knowledge?
- Can it hold our standard templates and tone?
- Does it flag when it is unsure, and can we require citations for anything factual?
- What does the enterprise tier cost, and what is missing from the cheap tier that we would actually need?

---

Related: [documents and contract review](02-documents-and-contract-review.md) ·
[risks and controls](../04-risks-and-controls.md) · [back to contents](../README.md)
