# Healthcare Triage

## Problem

AI systems prioritize patients according to risk level.

Traditional systems generally preserve:

Decision
↓
Action
↓
Log
↓
Explanation

Problem:

Logs can be modified.

Explanations may be generated after outcome observation.

Retrospective narratives are not equivalent to independent evidence.

## A-DAP Flow

Decision
↓
Envelope Creation
↓
Hash Generation
↓
Independent Verification
↓
Action

## Benefit

Allows reconstruction of evidence proving that the decision existed before the clinical outcome.

## Example

Patient: ID-2034

Decision:
Priority = High Risk

Envelope Hash:
8d43f9e12ab45c78f4...

Verification:
Valid
