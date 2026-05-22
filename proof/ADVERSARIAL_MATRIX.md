# A-DAP Adversarial Test Matrix

Purpose:

Define explicit hostile tests against A-DAP v0.1.

---

## Test A1 — Envelope Modification

Attack:

Modify one field after evidence creation.

Expected:

Hash mismatch.

Pass criteria:

Verification fails.

Status:

Pending

---

## Test A2 — Timestamp Manipulation

Attack:

Replace timestamp evidence.

Expected:

Timestamp inconsistency detected.

Pass criteria:

Temporal verification fails.

Status:

Pending

---

## Test A3 — Hidden Tampering

Attack:

Change content without declaring modification.

Expected:

Integrity violation detected.

Pass criteria:

Verification fails.

Status:

Pending

---

## Test A4 — Retroactive Fabrication

Attack:

Create envelope after outcome observation.

Expected:

Temporal inconsistency.

Pass criteria:

External proof invalidated.

Status:

Pending

---

## Test A5 — Independent Cold Start Audit

Attack:

Third party attempts verification with no internal access.

Expected:

Verification succeeds.

Pass criteria:

Reproduction successful.

Status:

Pending

---

## Principle

A protocol should survive adversarial pressure, not friendly interpretation.
