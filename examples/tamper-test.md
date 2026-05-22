# Tamper Test

Purpose:

Demonstrate that changing even a single value invalidates integrity.

Original:

```text
minimal-envelope.json
```

Expected:

```text
✓ Verification passed
```

Tampered:

```text
tampered-envelope.json
```

Expected:

```text
✗ Hash mismatch

✗ Integrity validation failed
```

Conclusion:

A-DAP does not prove correctness.

A-DAP proves evidence integrity.
