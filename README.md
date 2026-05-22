# A-DAP

![Status](https://img.shields.io/badge/status-frozen-blue)
![Review](https://img.shields.io/badge/review-hostile-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-v0.1-black)

> Auditability is not explaining a decision.
>
> Auditability is preserving independent evidence that a decision existed before its outcome.

### Auditable Decision Accountability Protocol

Canonical public implementation and public source of truth for the Auditable Decision Accountability Protocol (A-DAP).

> Status: A-DAP v0.1 — Frozen for hostile external review
>
> Current objective:
>
> Attempt to break the protocol.

---

# Core Definition

A-DAP introduces the concept of **Verifiable Prior Existence**:

**The ability to demonstrate that a decision existed, remained intact, and can be independently verified before observation of its outcome.**

---

# Why A-DAP Exists

Current AI governance systems primarily reconstruct explanations after execution.

Examples include:

- LIME
- SHAP
- Logging systems
- Documentation frameworks
- Governance reports
- Risk management standards

These approaches usually answer:

> "Why do we think the model decided this?"

A-DAP asks a different question:

> "Can we prove what decision existed before the result became known?"

---

# Architectural Principles

## P1 — Record ≠ Proof

Documenting an event is not equivalent to proving that the event existed before observation.

---

## P2 — Explanation ≠ Verification

Post-hoc explanations do not demonstrate prior existence.

---

## P3 — Decisions without verifiable prior existence generate narratives, not evidence

Retrospective rationalization is indistinguishable from competence without preserved evidence.

---

# Scope

Current intended applications:

✅ Credit scoring systems

✅ Clinical decision pipelines

✅ Rule-based systems

✅ Deterministic machine learning pipelines

✅ Temperature = 0 controlled LLM environments

✅ Binary decision systems

✅ Categorical decision systems

---

# Current Limitations

A-DAP v0.1 does not fully address:

❌ Hardware-level GPU non-determinism

❌ Temperature > 0 generative systems

❌ Autonomous multi-agent chains

❌ Full stochastic reconstruction

❌ Institutional accountability

---

# Repository Structure

```text
A-DAP/
│
├── README.md
├── PROOF.md
├── REVIEW_REQUEST.md
│
├── specification/
│
├── proof/
│
├── examples/
│
├── cases/
│
├── integration/
│
└── archive/
```

---

# Repository Status

This repository is the single public source of truth for:

- Protocol specification
- Verification examples
- Proof artifacts
- Integrations
- External review

Historical repositories are preserved for reproducibility and transparency.

Archived repositories must not be interpreted as current protocol definitions.

---

# Verification Path

Minimal cold-start verification:

```bash
git clone https://github.com/orionorganizacao-dotcom/a-dap-protocol.git

cd a-dap-protocol

python verify_adap.py examples/minimal-envelope.json
```

Expected:

```bash
Envelope loaded

Computing SHA256...

Expected:
5f2b17f4...

Computed:
5f2b17f4...

MATCH

Verification: PASS
```

---

# Tamper Test

Intentional falsification example:

```bash
python verify_adap.py examples/tampered-envelope.json
```

Expected:

```bash
Expected:
5f2b17f4...

Computed:
92ab7ce1...

Verification: FAIL
```

---

# Proof of Prior Existence

A-DAP supports independent timestamp anchoring.

Current pathway:

- SHA256 integrity verification
- Independent timestamp proof
- External verification
- Tamper resistance

See:

```text
proof/TIMESTAMPING.md
```

---

# External Audit

Independent reviewers are encouraged to attempt:

- Integrity attacks
- Temporal attacks
- Reproducibility failures
- Verification inconsistencies
- Boundary failures

See:

```text
REVIEW_REQUEST.md
```

---

# Threat Model

A-DAP does NOT claim to:

❌ Prove truth

❌ Eliminate manipulation

❌ Guarantee correctness

❌ Create institutional accountability

❌ Solve all AI governance problems

A-DAP only claims:

> Preserve independently verifiable evidence of decision existence.

---

# Design Philosophy

Traditional systems:

```text
Decision
    ↓
Execution
    ↓
Logging
    ↓
Explanation
```

A-DAP:

```text
Decision
    ↓
Evidence Preservation
    ↓
Execution
    ↓
Verification
```

---

# Protocol State

Current Version:

```text
A-DAP v0.1
```

Current Phase:

```text
Frozen for hostile external review
```

Current Objective:

```text
Attempt to break the protocol
```

---

# Citation

If using A-DAP in research:

```text
A-DAP:
Auditable Decision Accountability Protocol

Version:
v0.1

Repository:
https://github.com/orionorganizacao-dotcom/a-dap-protocol
```

---

# License

MIT License

---

# Final Note

The purpose of A-DAP is not to establish truth.

The purpose of A-DAP is to preserve evidence.

Truth requires institutions.

Evidence requires architecture.
