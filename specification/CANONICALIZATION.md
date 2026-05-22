# Canonicalization Rules

This document defines how A-DAP creates deterministic evidence.

Purpose:

Guarantee that identical information always produces identical hashes.

---

## Problem

Different serializations can generate different hashes for identical content.

Example:

JSON A:

{
 "decision":"approve",
 "score":0.92
}

JSON B:

{
 "score":0.92,
 "decision":"approve"
}

Semantically:

Same information

Cryptographically:

Different hash outputs

---

## Canonicalization Rules

### Rule 1 — UTF-8 Encoding

All files must use:

UTF-8

---

### Rule 2 — Deterministic key ordering

JSON keys sorted alphabetically.

Example:

Correct:

{
 "decision":"approve",
 "score":0.92
}

Incorrect:

{
 "score":0.92,
 "decision":"approve"
}

---

### Rule 3 — Remove formatting differences

Ignore:

- whitespace
- indentation
- line breaks

---

### Rule 4 — Stable number representation

Correct:

0.92

Incorrect:

0.920000

---

### Rule 5 — Immutable envelope structure

Required structure:

decision
timestamp
model
hash

---

## Objective

Prevent ambiguity in evidence generation.

---

## Principle

Identical evidence must always produce identical cryptographic outputs.
