# A-DAP — Operational Provenance Layer v0.2

---

# Purpose

A-DAP defines a layer for preserving independently verifiable evidence regarding the operational conditions surrounding AI output generation.

The objective is not to reconstruct hidden internal reasoning.

The objective is not to recover true intent.

The objective is to preserve evidence.

---

# Problem

Traditional logging systems preserve outputs and timestamps.

They generally do not preserve independently verifiable operational context that existed before or during execution.

Examples:

- Retrieval sources may change
- External APIs may change
- Model routing may change
- Runtime configurations may change
- Safety filters may change
- Human intervention may occur

Layer 1 (Decision Evidence) proves:

- A decision existed
- The decision was preserved
- The decision was temporally anchored

Layer 2 (Operational Provenance) proves:

- Under what observable conditions that decision occurred

Without Layer 2:

Same output ≠ same operational reality

---

# Operational Evidence Envelope

Minimal structure:

```json
{
  "decision_id":"uuid",
  "timestamp":"RFC3339",
  "model":"gpt-x",
  "system_hash":"sha256",
  "input_hash":"sha256",
  "retrieval_hash":"sha256",
  "tool_state_hash":"sha256",
  "runtime_hash":"sha256",
  "output_hash":"sha256"
}
```

Purpose:

Preserve observable execution context without requiring exposure of internal model reasoning.

---

# Threat Model

Operational Provenance does NOT defend against:

1. Complete infrastructure compromise

2. Collusion among all verification entities

3. False external sources

4. Hardware-level attacks

5. Intentional fabrication before commitment

Operational Provenance DOES defend against:

1. Silent retrieval modification

2. Runtime parameter drift

3. Hidden routing changes

4. Post-hoc narrative reconstruction

5. Undocumented intervention

---

# Layer Architecture

Layer 1:

Decision Preservation

Proves:

Decision existed before result observation.

Layer 2:

Operational Provenance

Proves:

Observable conditions surrounding execution.

Layer 3 (future):

Independent External Verification

Proves:

Evidence trajectory itself remained externally auditable.

Relationship:

External Verification

↑

Operational Provenance

↑

Decision Preservation

---

# Demonstrated Case

## GCD-001

Observed event:

A decision output remained apparently consistent.

Traditional logging showed:

Input:
unchanged

Output:
unchanged

Timestamp:
unchanged

No anomaly detected.

Operational Provenance detected:

retrieval_hash mismatch

tool_state_hash mismatch

runtime_hash changed

Consequence:

Execution environment had changed despite stable visible outputs.

Layer 1 conclusion:

"No issue detected."

Layer 2 conclusion:

"Operational state changed."

This demonstrates:

Decision evidence alone cannot reconstruct execution conditions.

Operational provenance becomes independently necessary.

---

# Architectural Claim

A-DAP does not attempt to reconstruct hidden cognition.

A-DAP preserves independently verifiable evidence regarding:

- decision existence
- temporal ordering
- operational context

The goal is not explanation.

The goal is evidentiary reconstruction.

---

Version:

v0.2

Status:

Draft for external review
