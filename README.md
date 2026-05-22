# A-DAP Protocol

Verifiable Decision Preservation Protocol

Core statement:

> "Recording is not proving.  
> Explanation is not verification."

---

## Definition

A-DAP is a protocol for preserving independently verifiable evidence of decision existence, integrity, and temporal precedence before outcome observation.

It does not attempt to prove correctness.

It does not attempt to explain reasoning after execution.

It preserves evidence that allows independent reconstruction.

Formal definition:

> Verifiable prior existence is the property by which a decision can demonstrate existence, integrity, and temporal precedence before outcome observation.

---

## Why A-DAP Exists

Traditional systems preserve:

- Logs
- Outputs
- Retrospective explanations

The problem:

Logs can be modified.

Explanations can be generated after outcomes become known.

Retrospective narratives are not equivalent to independent evidence.

A-DAP addresses a different problem:

Preserving evidence that a decision existed before its outcome.

---

## Core Principle

Traditional systems:

```text
Decision
↓
Action
↓
Log
↓
Explanation
```

A-DAP:

```text
Decision
↓
Commit
↓
Independent Evidence
↓
Execution
↓
Reconstruction
```

Fundamental distinctions:

- Recording is not proving
- Explanation is not verification
- Retrospective narratives are not independent evidence

---

## What A-DAP Provides

✓ Decision existence preservation

✓ Temporal integrity

✓ Independent verification capability

✓ Reconstruction support

✓ Model-agnostic architecture

✓ Tamper detection

✓ Verifiable prior existence

---

## What A-DAP Does NOT Provide

✗ Truth

✗ Correctness guarantees

✗ Institutional accountability by itself

✗ Perfect transparency

✗ Immunity against total system compromise

✗ Human governance replacement

---

## Architectural Components

A minimal A-DAP implementation contains:

### 1. Decision Envelope

Stores decision information before execution.

Example:

```json
{
  "decision_id":"A001",
  "timestamp":"2026-05-22T09:41:00Z",
  "action":"approve_transaction",
  "input_reference":"request_8472",
  "reasoning":"Transaction approved according to predefined rules"
}
```

---

### 2. Commitment Layer

Creates cryptographic evidence of the decision state.

Example:

```text
SHA-256(decision_envelope)
```

Purpose:

- Detect modifications
- Preserve integrity
- Enable later verification

---

### 3. Independent Evidence Layer

Stores evidence independently of execution.

Examples:

- SHA-256 hashes
- Merkle proofs
- RFC3161 timestamps
- Ed25519 signatures
- External ledgers

---

### 4. Reconstruction Layer

Allows independent verification after execution.

Verification should answer:

1. Did the decision exist?

2. Was it modified?

3. Can the original state be reconstructed?

4. Did the decision exist before the observed outcome?

---

## Minimal Verification Example

Expected behavior:

```text
Original ledger:

✓ VERIFIED


Tampered ledger:

✗ FAILED
```

---

## Threat Model

A-DAP assumes:

✓ Independent evidence storage

✓ Cryptographic integrity

✓ Observable decision state

✓ External verification availability

A-DAP does not assume:

✗ Complete trust in operators

✗ Perfect system transparency

✗ Immutable execution environments

---

## Canonical Architecture

```text
Decision
      ↓
Commit
      ↓
Independent Evidence
      ↓
Execution
      ↓
