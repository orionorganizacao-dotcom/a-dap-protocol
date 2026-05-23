# A-DAP — Evidence Map v0.1

Purpose:
This document maps architectural claims to observable artifacts, maturity status, and reproducible verification paths.

This file does not claim institutional validation.
Its purpose is traceability.

---

## Claim → Artifact → Status → Observable Evidence → Verification Path

### Anterioridade Verificável

Artifact:
proof/TIMESTAMPING.md

Status:
Experimental

Observable Evidence:
timestamp-receipt.json

Verification Path:

1. Open:
proof/TIMESTAMPING.md

2. Open:
timestamp-receipt.json

3. Reproduce timestamp verification process

Expected outcome:

- Timestamp integrity preserved
- Temporal evidence reconstructable

---

### Envelope Integrity

Artifact:

examples/minimal-envelope-verified.json

Status:

Implemented

Observable Evidence:

examples/tampered-envelope.json

Verification Path:

1. Open:
examples/minimal-envelope.json

2. Open:
examples/minimal-envelope-verified.json

3. Open:
examples/tampered-envelope.json

4. Execute:
examples/tamper-test.md

Expected outcome:

- Original envelope validates

- Modified envelope fails validation

---

### Threat Model

Artifact:

specification/THREAT_MODEL.md

Status:

Defined

Observable Evidence:

specification/ASSUMPTIONS.md

Verification Path:

1. Open:
specification/THREAT_MODEL.md

2. Open:
specification/ASSUMPTIONS.md

Expected outcome:

- Threat boundaries explicit

- Out-of-scope assumptions explicit

---

### ARS (Accountability Reconstruction Score)

Artifact:

specification/adap-spec-v0.1.md

Status:

Experimental Framework

Observable Evidence:

No baseline established

Verification Path:

1. Open:
specification/adap-spec-v0.1.md

Expected outcome:

- Framework definition available
