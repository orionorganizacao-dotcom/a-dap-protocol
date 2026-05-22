# External Audit Procedure

Objective:

Allow a third party to validate A-DAP without prior knowledge.

## Step 1 — Read the protocol definition

Read:

specification/adap-spec-v0.1.md

Expected understanding:

- Problem definition
- Core principle
- Scope limitations

---

## Step 2 — Inspect the decision envelope

Inspect:

examples/minimal-envelope.json

Expected understanding:

- Minimal decision envelope structure
- Envelope fields
- Timestamp relation
- Integrity fields

---

## Step 3 — Execute verification

Run:

```bash
python reference/verify_adap.py examples/minimal-envelope.json
```

Expected result:

```text
✓ Verification passed
```

Expected conclusion:

The decision evidence structure remains intact.

---

## Step 4 — Execute tamper test

Run:

```bash
python reference/verify_adap.py examples/tampered-envelope.json
```

Expected result:

```text
✗ Integrity validation failed
```

Expected conclusion:

Any modification breaks verification.

---

## Validation Criteria

The reviewer should independently conclude:

1. Decision evidence existed before outcome observation

2. Integrity can be independently verified

3. Verification is distinct from explanation

4. Correctness is outside protocol scope

---

## Final Statement

A-DAP preserves independently verifiable evidence.

A-DAP does not preserve truth.

A-DAP does not prove correctness.

A-DAP preserves evidence for reconstruction.
