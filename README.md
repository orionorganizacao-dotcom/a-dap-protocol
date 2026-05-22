# A-DAP Protocol
Auditable Decision Accountability Protocol

A-DAP is a protocol for preserving independently verifiable evidence that a decision existed before its outcome.

It does not attempt to prove correctness.

It does not attempt to explain reasoning after execution.

It preserves evidence that allows independent reconstruction.

---

## Core Principle

Traditional systems:

Decision → Action → Log → Explanation

A-DAP:

Decision → Commit → Independent Evidence → Action

The distinction is fundamental:

Recording is not proving.

Explanation is not verification.

---

## What A-DAP Provides

✓ Decision existence preservation

✓ Temporal integrity

✓ Independent verification

✓ Reconstruction capability

✓ Model-agnostic architecture

---

## What A-DAP Does NOT Provide

✗ Truth

✗ Accountability by itself

✗ Perfect transparency

✗ Immunity against total system compromise

---

## Quick Verification

Go to:

examples/minimal-envelope/

Run:

```bash
python verify_adap.py
