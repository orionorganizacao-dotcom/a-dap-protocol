# A-DAP
### Auditable Decision Accountability Protocol

Canonical public implementation of the Auditable Decision Accountability Protocol (A-DAP).

---

## Core Definition

> Auditability is not explaining a decision.
> Auditability is preserving independent evidence that a decision existed before its outcome.

A-DAP introduces the concept of **Verifiable Prior Existence**:

**The ability to demonstrate that a decision existed, remained intact, and can be independently verified before the observation of its outcome.**

---

## Why A-DAP Exists

Current AI governance and explainability systems primarily reconstruct explanations after execution.

Examples:

- Explainability frameworks (LIME, SHAP)
- Documentation standards
- Logging systems
- Governance reports
- Risk frameworks

These approaches answer:

> "Why do we think the model decided this?"

A-DAP asks a different question:

> "Can we prove what decision existed before the result became known?"

---

## Architectural Principles

### P1 — Record ≠ Proof

Documenting an event is not equivalent to proving it existed before observation.

---

### P2 — Explanation ≠ Verification

Post-hoc explanations do not demonstrate prior existence.

---

### P3 — Decisions without verifiable prior existence generate narratives, not evidence

Retrospective rationalization is indistinguishable from competence without preserved evidence.

---

## Scope

A-DAP currently targets:

✅ Credit scoring systems

✅ Clinical decision pipelines

✅ Rule-based automated systems

✅ Deterministic ML pipelines

✅ Temperature=0 controlled LLM environments

✅ Binary and categorical decision systems

---

## Current limitations

A-DAP v0.1 does not fully address:

❌ Hardware-level GPU non-determinism

❌ Temperature > 0 generative systems

❌ Autonomous multi-agent chains

❌ Full stochastic reconstruction

❌ Institutional accountability

---

## Repository Structure

```text
A-DAP/
│
├── README.md
├── PROOF.md
├── REVIEW_REQUEST.md
├── REPOSITORY_MAP.md
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

## Repository Status

Status:

ACTIVE

This repository is the single public source of truth for:

- Protocol specification
- Verification examples
- Proof artifacts
- Integrations
- External review

Historical repositories are preserved only for reproducibility.

Archived repositories must not be interpreted as current protocol definitions.

---

## Verification Path

Minimal cold-start verification:

```bash
git clone https://github.com/orionorganizacao-dotcom/a-dap-protocol.git

cd a-dap-protocol

python verify_adap.py examples/minimal-envelope.json
```

Expected result:

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

## Tamper Test

The repository includes an intentional falsification example:

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

## Proof of Prior Existence

A-DAP supports independent timestamp anchoring.

Current pathway:

- SHA256 integrity
- Independent timestamp proof
- External verification
- Tamper resistance

See:

proof/TIMESTAMPING.md

---

## External Audit

Independent reviewers are encouraged to attempt:

- Integrity attacks
- Temporal attacks
- Reproducibility failures
- Hash collisions
- Verification inconsistencies
- Boundary failures

See:

REVIEW_REQUEST.md

---

## Threat Model

A-DAP does NOT claim to:

- prove truth
- eliminate manipulation
- guarantee correctness
- create institutional accountability
- solve all AI governance problems

A-DAP only claims:

> Preserve independently verifiable evidence of decision existence.

---

## Design Philosophy

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

## Citation

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

## License

MIT License

---

## Current Status

A-DAP v0.1

Status:

Protocol frozen for hostile external review.

Current objective:

> Attempt to break the protocol.
