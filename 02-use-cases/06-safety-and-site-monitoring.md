# Safety and site monitoring

**Answers the question:** are we catching the leading indicators — the near misses and the unsafe conditions —
before they turn into an incident?

**Maturity:** mixed. Analytical use of incident and inspection data is straightforward and underused. Camera
analytics work where somebody is accountable for the alerts, and fail publicly where nobody is.

**Data it needs:** incident and near-miss records with enough detail to look for patterns, inspection and
observation data, and — for camera analytics — coverage, connectivity, and a written policy that workers
have seen.

## What it actually does

- **Camera and video analytics.** Detects missing PPE, exclusion-zone breaches, and increasingly unsafe
  behaviours and conditions such as blocked access routes, or plant and pedestrian proximity.
- **Photo analysis.** Flags visibly observable hazards in site photos: missing edge protection, poor
  housekeeping, blocked access routes. It cannot assess anything requiring an engineered judgement or a
  physical inspection, and it does not replace one.
- **Pattern analysis.** Reads years of incident, near-miss and inspection data to find where injuries actually
  cluster — by trade, activity, day of week, and phase of the job.
- **Documentation assistance.** Drafts toolbox talks, JSAs, permits and investigation reports from the facts
  you supply, and summarises a long report into the three findings that matter. Treat every one of these as a
  first draft: permits, JSAs and investigations are compliance records, and they need site-specific input and
  sign-off from a competent person before they enter the file.
- **Training reinforcement.** Short briefings generated from a near miss on that specific site, which land
  better than a generic annual module.

## What it needs from you

- **An alert owner and a response time.** Who reads the alerts, and by when? If the answer is "the safety
  manager, when he gets a chance", the system is ignored within a month.
- **Coverage that matches the risk.** Cameras on the highest-consequence activities, not scattered evenly
  because the cable run was easy.
- **A culture that treats it as help, not surveillance.** Explain what is monitored, what is not, and what
  the footage will and will not be used for. Bring the workforce — and, where applicable, the union — in
  before the cameras, not after.
- **Written policy and lawful basis.** Notice, signage, retention periods, who can view footage, and what
  happens to it after an incident. Get your lawyer and your broker involved; rules vary by country and state.
- **Incident records good enough to mine.** "Employee hurt back" is not data. Activity, mechanism, trade,
  phase, time, and what the person was doing are the data.

## Where it goes wrong

- **Alert fatigue.** Several hundred alerts a day, nobody reads them, and the investment has made safety worse
  by convincing people that monitoring is happening when nothing is being acted on. Count alerts per day and
  false positives per day before you scale beyond one site — usually within the first two weeks.
- **Surveillance backlash.** Cameras introduced without explanation read as distrust, and the safety manager
  loses the informal reporting that was producing better information than the cameras ever will.
- **Evidence you did not plan for.** Footage is a record. Capturing an unsafe condition and doing nothing may
  create a document that hurts you later. Settle retention and disclosure with your lawyer in advance, not in
  the week after an incident.
- **Identifying individuals.** Face recognition and biometric analysis of workers carry serious legal risk in
  many jurisdictions and are prohibited in some. If a vendor leads with them, that tells you something about
  their compliance posture.
- **Replacing judgement.** A camera is not a competent person. It does not understand task context and cannot
  stop work. Analytics supplement supervision; they do not substitute for it.
- **Privacy of the surrounding area.** Cameras that read a neighbouring property's windows, or a public
  footpath, are someone else's complaint waiting to happen.

## How to judge a pilot

One site, one behaviour, one measurable leading indicator:

1. Pick a single behaviour with real consequence — fall protection, exclusion zones around plant, or access
   route obstruction.
2. Record the **baseline** for two weeks: observations, near misses and any incident, from your existing
   process, with no tool running.
3. Run the tool for **eight to twelve weeks**. Track **alerts per day**, **false positives per day** (spot
   check a sample; do not trust the vendor's claim), **median time to response**, and **observed change in the
   behaviour**.
4. Ask the crews, directly and in person: has this helped, and has it changed what you do? Their answer is
   evidence — often the most important evidence you will collect.
5. Set kill criteria up front: if false positives per day exceed what your supervisor can triage, stop and
   retune rather than hiring someone to read a stream nobody can action.

## Questions worth asking a vendor

- Who is expected to review alerts, how quickly, and what does the workflow look like on a phone in the field?
- What is the measured false positive rate on a site like mine, and can I run a trial where I count it myself?
- What is retained, where, for how long, who can access it, and can I set those controls myself?
- Does the system identify individuals or use biometric data? If yes, stop and call your lawyer.
- Does it hold up as evidence in an investigation, and can it export a timeline?
- Who processes the video, and is any of it used for model training?
- Does it integrate with my incident management system, or is it another silo?
- What happens at the end of the contract — do I keep the footage and the analytics history?

---

Related: [risks and controls](../04-risks-and-controls.md) ·
[admin, drafting and general assistants](07-admin-drafting-and-assistants.md) ·
[back to contents](../README.md)
