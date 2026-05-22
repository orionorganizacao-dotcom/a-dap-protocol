# Threat Model

This document defines the explicit threat boundaries of A-DAP v0.1.

The purpose is not to claim universal security.

The purpose is to make assumptions visible and falsifiable.

---

## Outside A-DAP scope

A-DAP does NOT protect against:

- compromised operating systems
- compromised hardware
- malicious host environments
- total collusion among all participants
- fabricated input generation
- compromised cryptographic primitives
- false timestamp providers
- adversarial data collection

---

## Inside A-DAP scope

A-DAP protects against:

- post-creation evidence modification
- hidden tampering
- retrospective evidence fabrication
- unverifiable reconstruction
- silent envelope alteration
- integrity loss after creation

---

## Threat Categories

### T1 — Evidence Modification

Attack:

Evidence altered after creation.

Expected result:

Hash mismatch detected.

Protection:

SHA256 deterministic hashing.

---

### T2 — Hidden Tampering

Attack:

Modification without notification.

Expected result:

Verification failure.

Protection:

Envelope integrity validation.

---

### T3 — Retroactive Fabrication

Attack:

Evidence created after outcome observation.

Expected result:

Temporal inconsistency detected.

Protection:

External timestamp anchoring.

---

### T4 — Trust Dependency

Attack:

Verification requires trusting author claims.

Expected result:

Independent reproduction succeeds.

Protection:

Cold-start verification process.

---

## Assumption

A-DAP does not prove:

- truth
- correctness
- intent
- accountability

A-DAP preserves:

- integrity
- temporal existence
- reproducibility
- independent evidence

---

## Principle

Undetected failure is more dangerous than explicit failure.
