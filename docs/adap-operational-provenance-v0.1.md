# A-DAP — Operational Provenance Threat Model v0.1

## Purpose

This document defines the primary threat model for A-DAP Operational Provenance.

The goal is not to prove that a system was correct.

The goal is to preserve independently verifiable evidence regarding the operational conditions surrounding output generation.

A-DAP does not reconstruct hidden reasoning.

A-DAP does not recover true internal intent.

A-DAP preserves evidence.

---

# Threat Model Scope

A-DAP protects against:

• retrospective alteration of operational evidence

• loss of execution context

• ambiguity regarding production conditions

• post-hoc reconstruction without evidence

• unverifiable narratives replacing evidence

A-DAP does not protect against:

• complete institutional collusion

• compromised cryptographic roots

• false external data sources

• malicious human interpretation

• truth manipulation outside the evidence chain

---

# Core distinction

Traditional logging asks:

"What happened?"

A-DAP asks:

"What independently verifiable evidence existed before interpretation occurred?"

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

# Evidence constraints

Evidence preservation requires:

## Integrity

Evidence cannot be modified without detection.

Mechanisms:

• SHA256

• Merkle structures

• signatures

---

## Temporal anchoring

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

# Threat Scenarios

---

## TM-001

Retrospective Log Rewrite

Attack:

System alters execution records after output generation.

Traditional logs:

Potentially vulnerable.

A-DAP response:

Hash mismatch.

Signature mismatch.

Timestamp inconsistency.

Status:

Detectable.

---

## TM-002

Context Removal Attack

Attack:

System removes retrieval context or tool usage information.

Traditional logs:

May silently omit.

A-DAP response:

Envelope inconsistency.

Missing evidence chain.

Status:

Detectable.

---

## TM-003

Synthetic Narrative Attack

Attack:

System generates explanations after outcomes occur.

Example:

"We recommended X because of Y."

No evidence exists proving Y was available before execution.

Traditional systems:

Explanation may appear valid.

A-DAP response:

No prior evidence envelope.

Status:

Detectable.

---

## TM-004

Verifier Dependence Attack

Attack:

Verification depends on the same entity that generated evidence.

Problem:

Circular legitimacy.

A-DAP response:

Require independent validation paths.

Examples:

• external timestamp authorities

• independent verifier implementations

• replicated evidence repositories

Status:

Partially mitigated.

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

Assumption boundary.

---

# Structural observations

Without Layer 1:

Origin becomes unclear.

Without Layer 2:

Operational context disappears.

Without Layer 3:

Evidence alone produces no accountability.

---

# Architectural relationship

Layer 1

Identity / Asset Provenance

Question:

"Who created this artifact?"

Examples:

• C2PA

• Content Credentials

• Watermarks

• Cryptographic signatures

---

Layer 2

Operational Provenance

Question:

"Under what verifiable conditions was this generated?"

Examples:

• decision envelopes

• retrieval context

• timestamps

• model metadata

• tool chains

• evidence hashes

---

Layer 3

Interpretation and Accountability

Question:

"What does this mean and who is responsible?"

Actors:

• auditors

• regulators

• institutions

• legal systems

---

# Canonical statement

A signed artifact can preserve authorship.

A decision envelope can preserve evidence.

Institutions determine responsibility.

---

# Limitation statement

A-DAP does not reveal hidden internal reasoning.

A-DAP does not reveal true intention.

A-DAP does not prove correctness.

A-DAP preserves independently verifiable evidence.

Interpretation remains a human and institutional function.

---

Version:

v0.1

Status:

Draft
