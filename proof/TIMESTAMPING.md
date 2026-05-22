# Temporal Anchoring

A-DAP requires more than integrity.

A hash proves that evidence was not modified.

A timestamp anchor helps prove that the evidence existed before outcome observation.

---

## Recommended Method

Use OpenTimestamps.

Install:

```bash
pip install opentimestamps-client
```

Stamp:

```bash
ots stamp examples/minimal-envelope-verified.json
```

This creates:

```text
examples/minimal-envelope-verified.json.ots
```

Verify:

```bash
ots verify examples/minimal-envelope-verified.json.ots
```

---

## Expected Result

The verifier should show that the file hash was anchored externally.

This provides independent temporal evidence.

---

## A-DAP Evidence Stack

```text
Decision Envelope
↓
SHA-256 Hash
↓
External Timestamp Anchor
↓
Verification
↓
Tamper Test
```

---

## Why This Matters

Integrity answers:

"Has the envelope changed?"

Temporal anchoring answers:

"Did the envelope exist before the outcome was known?"

A-DAP requires both.
