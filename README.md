# A-DAP
### Auditable Decision Accountability Protocol

Canonical entrypoint for externally verifiable decision evidence.

---

## What is A-DAP?

A-DAP is a minimal protocol designed to preserve decision evidence before execution.

Traditional systems usually preserve:

- outputs
- logs
- explanations
- post-hoc justifications

A-DAP preserves something different:

**verifiable evidence that a decision existed before its outcome was observed.**

Core principle:

"Auditability is not explaining a decision. Auditability is preserving independent evidence that a decision existed before the result."

---

## Problem

Traditional architectures:

User
↓
Model
↓
Action
↓
Log

Problem:

Logs can be modified.

Explanations can be generated after execution.

Narratives can be reconstructed after outcomes become known.

Without prior evidence:

Decision ≠ Proof

---

## A-DAP architecture

A-DAP introduces a pre-execution evidence layer.

User
↓
Model
↓
Decision Envelope
↓
Hash Generation
↓
Evidence Record
↓
Execution

The objective is not to prove correctness.

The objective is to preserve:

- existence
- integrity
- temporality

---

## Repository Structure

```text
a-dap-protocol/
│
├── specification/
│
├── proof/
│
├── examples/
│
├── cases/
│   ├── healthcare-triage.md
│   ├── credit-scoring.md
│   ├── content-moderation.md
│   └── autonomous-agents.md
│
├── integration/
│   ├── openai-agent-flow.md
│   ├── openai-envelope-example.json
│   ├── openai-sdk-example.py
│   └── verification-flow.md
│
├── README.md
└── LICENSE
