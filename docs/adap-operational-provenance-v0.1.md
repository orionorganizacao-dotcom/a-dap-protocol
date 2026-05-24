# A-DAP — Operational Provenance Layer v0.1

## Core distinction

Content provenance and decision provenance are distinct properties.

Content provenance answers:

"Who created this?"

Decision provenance answers:

"Under what verifiable conditions was this produced?"

Human and institutional review answer:

"What does this mean, and who is responsible?"

---

## Three-layer trust architecture

Layer 1 — Identity / Asset Provenance

Examples:
- C2PA
- Content Credentials
- Watermarks
- Cryptographic signatures

Question answered:

"Who produced this artifact?"

---

Layer 2 — Verifiable Operational Context Preservation

A-DAP layer

Purpose:

Preserve independently verifiable evidence regarding the operational conditions surrounding production.

Examples:

- model version
- external tools used
- retrieval context
- input state
- timestamps
- execution metadata
- hashes
- decision envelopes

Question answered:

"Under what verifiable conditions was this generated?"

Limitations:

A-DAP does not reconstruct hidden internal reasoning.

A-DAP does not reveal a true "why".

A-DAP preserves evidence.

---

Layer 3 — Interpretation and Accountability

Actors:

- human auditors
- regulators
- institutions
- legal systems

Question answered:

"What does this mean and who is responsible?"

---

## Structural observations

Without Layer 1:
origin becomes unclear.

Without Layer 2:
context disappears.

Without Layer 3:
evidence does not produce accountability.

---

## Canonical statement

"A signed artifact can preserve authorship.

A decision envelope can preserve evidence.

Institutions determine responsibility."
