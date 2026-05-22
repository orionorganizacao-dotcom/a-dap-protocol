# Assumptions

This document defines explicit assumptions required by A-DAP.

Purpose:

Make trust boundaries visible.

---

## Assumption 1 — Cryptographic primitives remain secure

Assumed:

- SHA256 collision resistance
- signature integrity

Not assumed:

Absolute cryptographic permanence.

---

## Assumption 2 — Timestamp providers remain externally verifiable

Assumed:

Timestamp evidence can be independently checked.

Not assumed:

Blind trust in timestamp providers.

---

## Assumption 3 — Evidence captured before outcome observation

Assumed:

Envelope generated before later observations.

Not assumed:

Retroactive generation.

---

## Assumption 4 — Independent auditors can access evidence

Assumed:

Third parties can reproduce verification.

Not assumed:

Access to internal infrastructure.

---

## Assumption 5 — Deterministic serialization rules applied

Assumed:

Canonicalization rules followed.

Not assumed:

Arbitrary formatting.

---

## Principle

Trust assumptions must be explicit.

Invisible assumptions create invisible vulnerabilities.
