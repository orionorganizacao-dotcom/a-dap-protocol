# A-DAP

![status](https://img.shields.io/badge/status-frozen-blue)
![review](https://img.shields.io/badge/review-hostile-orange)
![license](https://img.shields.io/badge/license-MIT-green)
![version](https://img.shields.io/badge/version-v0.1-black)

> Auditability is not explaining a decision.
>
> Auditability is preserving independent evidence that a decision existed before its outcome.

---

# Auditable Decision Accountability Protocol

Canonical implementation and public source of truth for the Auditable Decision Accountability Protocol (A-DAP).

Current protocol state:

- Frozen for hostile external review
- Specification locked
- External falsification encouraged

---

# Quick Start

Clone repository:

```bash
git clone https://github.com/orionorganizacao-dotcom/a-dap-protocol

cd a-dap-protocol
```

Run verification:

```bash
python verify_adap.py
```

Expected output:

```bash
Verification result:

Envelope integrity:
PASS

Hash consistency:
PASS

Timestamp:
PASS
```

See:

- PROOF.md
- REVIEW_REQUEST.md
- proof/TIMESTAMPING.md

---

# Core Definition

A-DAP defines auditability as:

> The ability to preserve independent evidence that a decision existed before observation of its outcome.

This differs fundamentally from post-hoc explainability systems.

Traditional systems ask:

> "What happened?"

A-DAP asks:

> "Can you prove what existed before the outcome became visible?"

---

# Core Principles

## P1 — Record ≠ Proof

Recording an event does not prove that the event existed before its outcome.

---

## P2 — Explanation ≠ Verification

Explaining a decision after execution does not verify that the explanation itself existed beforehand.

---

## P3 — Decision without prior evidence produces narrative, not proof

Without independent preservation of evidence, retrospective rationalization becomes indistinguishable from competence.

---

# Problem

Current AI audit mechanisms mostly rely on:

- logs
- explanations
- reconstructed reasoning
- internal metadata

These mechanisms create a structural vulnerability:

```text
Decision
↓
Execution
↓
Outcome observed
↓
Explanation generated
```

The problem:

Explanation occurs after observation.

Therefore:

- explanations can be modified
- explanations can be reconstructed
- explanations can be manipulated

---

# A-DAP Architecture

A-DAP introduces a preservation layer before execution:

```text
Decision
↓
Envelope creation
↓
Cryptographic commitment
↓
Timestamp anchoring
↓
Execution
↓
Outcome
↓
Verification
```

This changes auditability from:

```text
"What do you claim happened?"
```

to:

```text
"What can be independently verified?"
```

---

# Repository Structure

```text
a-dap-protocol/

├── specification/
│   └── adap-spec-v0.1.md
│
├── examples/
│   ├── minimal-envelope.json
│   ├── tampered-envelope.json
│   ├── ledger.json
│   ├── verification-example.md
│   └── verify_adap.py
│
├── proof/
│   ├── external-audit.md
│   ├── TIMESTAMPING.md
│   ├── timestamp-receipt.json
│   └── minimal-envelope.json.ots
│
├── integration/
│
├── cases/
│
├── PROOF.md
│
├── REVIEW_REQUEST.md
│
├── LICENSE
│
└── README.md
```

---

# Minimal Verification Example

Decision envelope:

```json
{
"decision_id":"001",
"model":"credit_v1",
"threshold":"0.74",
"output":"DENIED"
}
```

Generate SHA256:

```bash
sha256sum minimal-envelope.json
```

Expected:

```bash
eab3290fbb3c4a2c8a57fe71a5f4d3b7d33fbd8c...
```

Run verifier:

```bash
python verify_adap.py
```

Expected:

```bash
Verification result:

Envelope integrity:
PASS

Hash consistency:
PASS
```

---

# Tamper Test

Modify:

```json
"output":"APPROVED"
```

Run verification:

```bash
python verify_adap.py
```

Expected:

```bash
Verification result:

Envelope integrity:
FAIL

Hash mismatch detected
```

---

# Timestamping

Integrity alone does not prove temporal existence.

A-DAP therefore supports timestamp anchoring.

Create timestamp:

```bash
ots stamp minimal-envelope.json
```

Generated:

```bash
minimal-envelope.json.ots
```

Verify:

```bash
ots verify minimal-envelope.json.ots
```

Expected:

```bash
Success:

Bitcoin block timestamp verified
```

---

# Threat Model

A-DAP does NOT guarantee:

- decision correctness
- absence of manipulation
- institutional accountability
- truthfulness of inputs
- deterministic behavior in arbitrary generative systems

A-DAP guarantees:

- evidence preservation
- integrity verification
- temporal consistency
- tamper detection

---

# Intended Use Cases

Suitable:

- credit scoring
- medical triage
- judicial systems
- regulated AI pipelines
- compliance systems
- deterministic decision workflows

Current limitations:

- stochastic LLM outputs
- temperature >0
- multi-agent chains
- hardware non-determinism

---

# External Review

This repository is intentionally frozen.

The goal is not agreement.

The goal is attempted falsification.

Reviewers are encouraged to:

- modify envelopes
- attack assumptions
- identify hidden dependencies
- reproduce verification independently
- attempt protocol failure

See:

```text
REVIEW_REQUEST.md
```

---

# Proof

Cold-start verification:

```bash
git clone https://github.com/orionorganizacao-dotcom/a-dap-protocol

cd a-dap-protocol

python verify_adap.py
```

See:

```text
PROOF.md
```

---

# License

MIT License

---

# Citation

```bibtex
@misc{adap2026,
title={A-DAP: Auditable Decision Accountability Protocol},
author={Ezio v.s Santos},
year={2026},
note={Public protocol implementation and hostile review repository}
}
```

---

# Final Statement

A-DAP does not attempt to prove that a decision was correct.

A-DAP attempts to prove that the decision existed before anyone knew its outcome.
