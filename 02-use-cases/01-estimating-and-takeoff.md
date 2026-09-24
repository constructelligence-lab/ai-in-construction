# Estimating and takeoff

**Answers the question:** can we bid more work without more estimators, and can we do it without missing a
quantity?

**Maturity:** the most mature category in construction AI, by a wide margin.

**Data it needs:** the current drawing set, in vector PDF from CAD where possible, with someone accountable
for revisions — plus your own assembly-to-cost-code mapping for the quantities to be worth anything.

## What it actually does

Two different jobs, often sold as one:

- **Counting.** Symbols for devices, fixtures, doors, windows, hangers, structural members. This is pattern
  recognition and it is genuinely good at it, especially on clean vector plans.
- **Measuring.** Areas, linear runs, volumes and perimeters from plan geometry — floors, wall areas for
  finishes, pipe and duct runs, excavation volumes from contours.

The output is a quantity table: item, sheet, level, area, count. That table is not a bid. Turning it into a
bid still requires pricing, means and methods, production rates, general conditions, and an opinion about
risk. The tool removes tracing, not judgement.

## What it needs from you

- **Drawings the machine can read.** Vector PDFs exported from CAD behave far better than scans of printed
  sheets. If your issue set is scanned, expect a correction-heavy workflow or no workflow at all.
- **Consistency.** Symbols drawn as blocks and layers named to a standard perform much better than the same
  door drawn four different ways by four different drafters.
- **A complete, current set with revisions identified.** Give the tool the superseded sheets and it will
  happily count them twice.
- **Your cost codes.** The quantity table matters when it maps onto the codes your estimating software and
  your job cost ledger already use. Otherwise you have bought a faster way to produce a spreadsheet nobody
  can price.

## Where it goes wrong

The characteristic failure is not a wrong number — it is a **missed revision**. A sheet reissued after the
tool ran leaves you with a takeoff that is confidently, invisibly out of date. Budget for a revision check as
a permanent, named step, not a one-time setup task.

The others, in rough order of how often they bite:

- **Tracing errors on raster or poorly scaled sheets.** Small scale errors multiply across large runs.
- **Overlapping or duplicated geometry** double-counted across levels or in overlapping viewports.
- **Assemblies that don't survive contact with your cost codes**, so quantities arrive faster than they can
  be priced.
- **Unreviewed submission.** Everything that leaves the building carries your estimate's name on it. A
  quantity nobody checked is a commercial risk, and the liability sits with you, not with the software.

## How to judge a pilot

Do not judge it on a demo plan. Judge it on jobs where the answer is already known:

1. Pick **three completed jobs** with quantities you trust and a mix of drawing quality — one clean, one
   messy, one with a significant revision history.
2. Run the takeoff for the trades you care about most, and compare item by item against your final numbers.
3. Record three numbers per job: **quantity discrepancy (%)**, **hours to correct it**, and **whether the
   correction stuck** — did it teach the tool, or will you correct it again next time.
4. Then, and only then, run it on **one live bid** and measure estimator hours against your last comparable
   bid, plus the rework caused by the revision check.

If the discrepancy is small but the correction time is large, you have moved the work rather than removed it
— which is a real finding, and worth saying out loud before renewal.

## Questions worth asking a vendor

- How do I correct a missed symbol or a wrong measurement, and does the tool retain that correction?
- Can it take two revisions of the same sheet and show me the delta in quantities?
- What happens on scanned plans — refuse, degrade gracefully, or produce confident rubbish?
- Can it export to my estimating software or an Excel model tagged with **my** cost codes?
- What accuracy does it claim, measured how, on what kind of drawing sets — and can I see that evaluation?
- Who reviews the output before it becomes a bid, and what does the product do to make that review quick?
- Where do my drawings live, for how long, and are they used to train anything?
- Is pricing per seat, per project or per drawing volume — and what happens in a busy bid month?

---

Related: [your data decides what AI can do](../03-your-data-decides.md) ·
[how to buy and pilot](../06-how-to-buy-and-pilot.md) · [back to contents](../README.md)

