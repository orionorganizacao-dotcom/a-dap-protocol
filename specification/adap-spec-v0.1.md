# A-DAP Specification v0.1

## Definition

A-DAP preserves independently verifiable evidence that a decision existed before outcome observation.

---

## Required Properties

### 1. Existence

A decision must have observable evidence of prior existence.

### 2. Integrity

Decision evidence must remain cryptographically unchanged.

### 3. Temporal precedence

Decision evidence must exist before execution outcome.

### 4. Reconstruction capability

A third party must be capable of reconstructing decision history.

---

## Architecture

Decision
↓
Commit
↓
Independent Evidence
↓
Execution
↓
Reconstruction

---

## Non-goals

A-DAP does not:

- prove correctness
- guarantee truth
- replace institutional accountability
- eliminate human manipulation

---

## Core statement

"Recording is not proving.

Explanation is not verification."
