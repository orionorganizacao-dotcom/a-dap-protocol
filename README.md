# A-DAP

### Verifiable Decision Preservation Protocol

Canonical entrypoint for independently verifiable decision preservation and reconstruction.

---

## What is A-DAP?

A-DAP is a minimal protocol designed to preserve independently verifiable evidence that a decision existed before its outcome was observed.

Traditional systems generally preserve:

- outputs
- logs
- explanations
- retrospective justifications

A-DAP preserves something different:

**Evidence of decision existence, integrity and temporal precedence.**

Core statement:

> "Recording is not proving.
>
> Explanation is not verification."

---

## Formal Definition

Verifiable prior existence is the property by which a decision can demonstrate:

- existence
- integrity
- temporal precedence

before outcome observation.

---

## Why A-DAP Exists

Traditional architectures:

```text
User
↓
Model
↓
Action
↓
Log
↓
Explanation
```

Problems:

Logs can be modified.

Explanations may be generated after outcomes become known.

Retrospective narratives are not equivalent to independent evidence.

Without prior evidence:

```text
Decision ≠ Proof
```

---

## A-DAP Architecture

Traditional systems:

```text
User
↓
Model
↓
Action
↓
Log
```

A-DAP:

```text
User
↓
Model
↓
Decision Envelope
↓
Hash Generation
↓
External Temporal Anchor
↓
Evidence Record
↓
Execution
```

Purpose:

Transform decisions from transient events into externally verifiable objects.

---

## Temporal Integrity

Integrity alone is insufficient.

A cryptographic hash can prove that evidence remained unchanged.

It cannot independently prove when the evidence existed.

Therefore A-DAP supports optional temporal anchoring mechanisms.

Examples:

- OpenTimestamps
- Independent witness publication
- RFC3161 timestamp authorities
- External blockchain commitments
- Third-party email hash delivery

Purpose:

Provide evidence that the commitment existed before outcome observation.

Strengthened properties:

✓ Existence

✓ Integrity

✓ Temporal precedence

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
```

---

# 10-Minute Audit Path

Follow this order:

### Step 1

Read:

```text
specification/
```

Understand:

- Envelope
- Hash
- Verification
- Temporal integrity

---

### Step 2

Open:

```text
examples/minimal-envelope.json
```

Understand:

- decision payload
- evidence structure

---

### Step 3

Run:

```text
examples/tamper-test.md
```

Expected:

Original evidence:

```text
✓ Valid
```

Modified evidence:

```text
✗ Invalid
```

---

### Step 4

Read one practical case:

```text
cases/healthcare-triage.md
```

or

```text
cases/autonomous-agents.md
```

---

### Step 5

Read:

```text
integration/openai-agent-flow.md
```

Understand how A-DAP integrates with agent systems.

---

## Minimal Hypothesis

A-DAP hypothesis:

> "Decisions become externally verifiable objects instead of transient execution events."

---

## Scope of v0.1

Included:

✓ Envelope

✓ Hash generation

✓ Temporal anchoring concept

✓ Verification flow

✓ Tamper detection

✓ External audit path

✓ Agent integration examples

✓ Real-world use cases

---

Not included:

✗ Ed25519 signatures

✗ Full RFC3161 implementation

✗ Merkle trees

✗ Database backend

✗ Dashboard UI

✗ Distributed verification

✗ Multi-agent orchestration

---

## Limitations

A-DAP does not:

- prove decision correctness
- guarantee truthfulness of inputs
- eliminate malicious operators
- create institutional accountability
- replace governance systems

A-DAP preserves independently verifiable evidence.

---

MIT License
