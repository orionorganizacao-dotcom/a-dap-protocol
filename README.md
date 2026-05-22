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

# Core Definition

A-DAP defines auditability as:

> The ability to preserve independent evidence that a decision existed before the observation of its outcome.

This differs fundamentally from post-hoc explainability systems.

Traditional systems ask:

"What happened?"

A-DAP asks:

"Can you prove what existed before the outcome became visible?"

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
