# External Audit Checklist

This document defines the minimal external audit process for A-DAP.

Objective:

Allow an independent third party to verify integrity, temporal consistency, and tamper resistance without requiring access to internal systems.

---

## Audit Goal

The auditor should be able to determine:

✓ A decision existed before execution

✓ Decision evidence remained unchanged

✓ Any modification becomes detectable

✓ Verification can be reproduced independently

---

# Step 1 — Inspect the Original Envelope

Open:

```text
examples/minimal-envelope.json
```

Expected structure:

```json
{
  "decision_id":"HT-001",
  "timestamp":"2026-05-22T14:30:00Z",
  "system":"Healthcare Triage AI",
  "patient_reference":"PAT-2034",
  "decision":"High Risk Priority",
  "reasoning_reference":"severity_score >= threshold",
  "decision_hash":"<SHA256>"
}
```

Verify:

✓ decision exists

✓ timestamp exists

✓ decision_hash exists

---

# Step 2 — Run Reference Verification

Execute:

```bash
python reference/verify_adap.py
```

Expected output:

```text
A-DAP Verification

Expected hash:
8d43f9e12ab45c78f4ab2...

Computed hash:
8d43f9e12ab45c78f4ab2...

RESULT:

HASH MATCH ✓
Envelope integrity verified
```

Interpretation:

The decision payload has not changed.

---

# Step 3 — Tamper Test

Open:

```text
examples/minimal-envelope.json
```

Modify:

Before:

```json
"decision":"High Risk Priority"
```

After:

```json
"decision":"Low Risk Priority"
```

Save file.

Run again:

```bash
python reference/verify_adap.py
```

Expected output:

```text
A-DAP Verification

Expected hash:
8d43f9e12ab45c78f4ab2...

Computed hash:
7ac81de93fa11ab54d1...

RESULT:

HASH MISMATCH ✗
Integrity violation detected
```

Interpretation:

A modification occurred after the original decision was recorded.

---

# Step 4 — Temporal Integrity Verification

Integrity alone does not prove chronology.

An external anchor should exist.

Examples:

• RFC3161 timestamp authority

• OpenTimestamps proof

• Independent witness hash

• External signed receipt

Example:

```text
SHA256:

8d43f9e12ab45c78f4ab2...

Anchored:

2026-05-22
14:30 UTC
```

Verify:

✓ external timestamp exists

✓ timestamp precedes execution

---

# Step 5 — Independent Reproduction

An independent auditor should reproduce:

```bash
python reference
