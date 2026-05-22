# A-DAP Verification Proof

This document records the minimal cold-start verification path for A-DAP v0.1.

Objective:

Demonstrate that a decision envelope can be independently verified through deterministic hashing.

---

## Command

Run from repository root:

```bash
python reference/verify_adap.py
```

---

## Expected Output

```text
Computed hash:

<computed_sha256_hash>

Envelope awaiting hash generation
```

---

## Interpretation

The verifier reads:

```text
examples/minimal-envelope.json
```

It removes:

```text
decision_hash
```

It serializes the remaining payload deterministically using:

```text
sort_keys=True
separators=(",",":")
```

It computes:

```text
SHA-256
```

The current envelope contains:

```text
"decision_hash":"TO_BE_COMPUTED"
```

Expected state:

```text
Envelope awaiting hash generation
```

---

## Verification Flow

```text
Envelope
    ↓
Canonicalization
    ↓
SHA-256
    ↓
Verification result
```

---

## Next Verification State

After replacing:

```text
"decision_hash":"TO_BE_COMPUTED"
```

with the computed hash:

```text
"decision_hash":"<generated_hash>"
```

Running:

```bash
python reference/verify_adap.py
```

should return:

```text
✓ Verification passed
```

---

## Tamper Validation

Modify:

```json
"decision":"High Risk Priority"
```

to:

```json
"decision":"Low Risk Priority"
```

Run again:

```bash
python reference/verify_adap.py
```

Expected:

```text
✗ Hash mismatch
Integrity validation failed
```

---

## Why This Matters

This demonstrates that A-DAP does not only document decisions.

It preserves independently verifiable evidence.

---

End of verification record

A-DAP v0.1
