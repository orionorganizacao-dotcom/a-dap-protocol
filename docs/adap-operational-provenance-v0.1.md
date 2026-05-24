# A-DAP — Operational Provenance Layer v0.2

---

# Purpose

A-DAP defines a layer for preserving independently verifiable evidence regarding the operational conditions surrounding AI output generation.

The objective is not to reconstruct hidden internal reasoning.

The objective is not to recover true intent.

The objective is to preserve evidence.

---

# Core distinction

Content provenance and decision provenance are distinct properties.

Content provenance answers:

"Who created this?"

Decision provenance answers:

"Under what verifiable conditions was this produced?"

Human and institutional review answers:

"What does this mean and who is responsible?"

---

# Three-layer trust architecture

---

## Layer 1 — Identity / Asset Provenance

Purpose:

Preserve authorship and origin information regarding generated artifacts.

Examples:

• C2PA

• Content Credentials

• Watermarks

• Cryptographic signatures

Question answered:

"Who produced this artifact?"

---

## Layer 2 — Operational Provenance

A-DAP Layer

Purpose:

Preserve independently verifiable evidence regarding the operational conditions surrounding production.

Examples:

• model version

• tool chain identifiers

• retrieval context

• input state

• timestamps

• execution metadata

• hashes

• decision envelopes

Question answered:

"Under what verifiable conditions was this generated?"

Limitations:

A-DAP does not reconstruct hidden internal reasoning.

A-DAP does not reveal a true "why."

A-DAP preserves evidence.

---

## Layer 3 — Interpretation and Accountability

Actors:

• human auditors

• regulators

• institutions

• legal systems

Question answered:

"What does this mean and who is responsible?"

---

# Structural observations

Without Layer 1:

Origin becomes unclear.

Without Layer 2:

Operational context disappears.

Without Layer 3:

Evidence does not produce accountability.

---

# Minimal Evidence Unit (MEU)

An A-DAP implementation should minimally preserve:

Required:

• input hash

• execution timestamp

• model identifier

• model version

• tool chain identifiers

• retrieval references

• envelope identifier

• cryptographic signature

Optional:

• environmental variables

• policy state

• external API versions

• hardware metadata

• execution region

---

# Evidence Constraints

---

## Integrity

Evidence cannot be modified without detection.

Mechanisms:

• SHA256

• Merkle structures

• signatures

---

## Temporal Anchoring

Evidence must demonstrate existence in time.

Mechanisms:

• RFC3161 timestamps

• trusted timestamp authorities

• blockchain anchoring (optional)

---

## Independence

Evidence verification cannot depend exclusively on the generating system.

Mechanisms:

• external verifiers

• independent repositories

• third-party timestamp validation

---

# Threat Model

---

## TM-001

Retrospective Log Rewrite

Attack:

Execution records are modified after generation.

Traditional logs:

Potentially vulnerable.

A-DAP response:

• hash mismatch

• signature mismatch

• timestamp inconsistency

Status:

Detectable

---

## TM-002

Context Removal Attack

Attack:

Retrieval context or tool usage is removed.

Traditional systems:

May silently omit information.

A-DAP response:

• envelope inconsistency

• missing evidence chain

Status:

Detectable

---

## TM-003

Synthetic Narrative Attack

Attack:

Explanations are generated after outcomes occur.

Example:

"We recommended X because of Y."

No evidence exists proving Y was available before execution.

Traditional systems:

Explanation appears plausible.

A-DAP response:

No prior evidence envelope exists.

Status:

Detectable

---

## TM-004

Verifier Dependence Attack

Attack:

Evidence validation depends on the same entity that generated it.

Problem:

Circular legitimacy.

A-DAP response:

Require independent validation paths.

Examples:

• external timestamp authorities

• independent verifier implementations

• replicated repositories

Status:

Partially mitigated

---

## TM-005

Complete Collusion Attack

Attack:

Generator, verifier and institutional actors cooperate maliciously.

Problem:

Entire trust chain compromised.

A-DAP response:

Out of scope.

Reason:

No system can bootstrap legitimacy from itself.

Status:

Boundary assumption

---

# Demonstrative Case

## GCD-001 — Missing Operational Provenance Scenario

Purpose:

Demonstrate a situation where Layer 1 remains valid while Layer 2 is absent.

---

Scenario

Assume two generated outputs:

Output A

Output B

Both preserve:

• authorship

• signatures

• timestamps

• cryptographic integrity

Layer 1 succeeds.

Question answered:

"Who produced these artifacts?"

Answer:

Known.

---

Observed problem

Auditors later attempt reconstruction:

• model version used

• retrieval sources available

• tool chain state

• execution conditions

• input state

No independently verifiable operational evidence exists.

Only outputs remain.

---

Consequence

Auditors can verify:

"This artifact existed."

Auditors cannot verify:

"Under what operational conditions was this produced?"

Multiple explanations become possible:

Hypothesis A

Different retrieval context

Hypothesis B

Different model version

Hypothesis C

Different external tool state

Hypothesis D

Post-hoc narrative reconstruction

These hypotheses become indistinguishable.

---

Structural Result

Layer 1 remains intact.

Authorship survives.

Operational context disappears.

Evidence collapses into narrative.

---

Observation

Failure did not originate from lack of provenance.

Failure originated from missing operational provenance.

Layer 1 preserved identity.

Layer 2 was absent.

---

Implication

Content provenance alone does not preserve production conditions.

Without Layer 2:

the artifact survives,

but surrounding evidence disappears.

---

# Canonical Statements

"A signed artifact can preserve authorship."

"A decision envelope can preserve evidence."

"Institutions determine responsibility."

---

# Limitation Statement

A-DAP does not reveal hidden internal reasoning.

A-DAP does not reveal true intention.

A-DAP does not prove correctness.

A-DAP preserves independently verifiable evidence.

Interpretation remains a human and institutional function.

---

Version:

v0.2

Status:

Draft
