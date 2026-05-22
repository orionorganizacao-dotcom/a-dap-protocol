# Healthcare Triage Example

Scenario:

An AI system classifies emergency patients.

Traditional flow:

Patient Data
↓
Model Decision
↓
Action
↓
Log
↓
Explanation

Problem:

The explanation may be generated after the outcome becomes known.

A-DAP flow:

Patient Data
↓
Decision Envelope
↓
Hash + Timestamp
↓
Action
↓
Verification

Result:

An auditor can reconstruct whether the decision evidence existed before the clinical outcome.

A-DAP does not prove the decision was medically correct.

A-DAP proves the evidence existed prior to outcome observation.
