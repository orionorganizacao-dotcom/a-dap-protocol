# Quick Start (10-Minute External Audit)

An external reviewer can understand A-DAP by following this order:

### Step 1 — Read the protocol definition

```text
specification/adap-spec-v0.1.md
```

Purpose:

Understand what A-DAP claims and what it explicitly does not claim.

---

### Step 2 — Inspect a minimal decision envelope

```text
examples/minimal-envelope.json
```

Purpose:

Observe the minimum structure required to preserve independently verifiable evidence.

---

### Step 3 — Inspect a ledger example

```text
examples/ledger.json
```

Purpose:

Understand how evidence can be chained and preserved.

---

### Step 4 — Inspect verification flow

```text
examples/verification-example.md
```

Purpose:

Understand how an external observer reconstructs evidence.

---

### Step 5 — Run the reference verifier

```bash
python reference/verify_adap.py
```

Expected result:

```text
✓ Verification passed
```

---

# Repository Structure

```text
a-dap-protocol/
│
├── README.md
│
├── specification/
│   └── adap-spec-v0.1.md
│
├── examples/
│   ├── minimal-envelope.json
│   ├── ledger.json
│   └── verification-example.md
│
├── reference/
│   └── verify_adap.py
│
└── LICENSE
```

---

# Expected Understanding After 10 Minutes

✓ What problem A-DAP solves

✓ What A-DAP does not solve

✓ How evidence is preserved

✓ How independent reconstruction works

✓ How verification occurs

---

# Scope Boundaries

A-DAP does not:

✗ Prove correctness of decisions

✗ Guarantee truthfulness of inputs

✗ Prevent malicious operators

✗ Replace institutional accountability

✗ Explain reasoning after execution

A-DAP provides:

✓ Evidence preservation

✓ Integrity validation

✓ Temporal precedence

✓ Independent reconstruction

✓ Verifiability outside the system

---

# Canonical Statement

> "Auditability is not explaining a decision.
>
> Auditability is preserving independent evidence that the decision existed before its outcome."
