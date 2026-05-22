# A-DAP Protocol

Verifiable Decision Preservation Protocol

Core statement:

> "Recording is not proving.  
> Explanation is not verification."

A-DAP is a protocol for preserving independently verifiable evidence that a decision existed before its outcome.

It does not attempt to prove correctness.

It does not attempt to explain reasoning after execution.

It preserves evidence that allows independent reconstruction.

---

## Why A-DAP Exists

Traditional systems typically preserve logs, outputs and retrospective explanations.

The problem:

Logs can be modified.

Explanations can be generated after outcomes are known.

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

The distinction is fundamental:

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

### Decision Envelope

Stores decision information before execution.

Typical fields:

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

### Commitment Layer

Creates cryptographic evidence of the decision state.
