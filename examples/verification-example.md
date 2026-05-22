# Verification Example

## Objective

Demonstrate that a decision can be independently verified.

---

## Step 1

Create a decision envelope:

minimal-envelope.json

---

## Step 2

Generate SHA-256 hash:

Example:

9c4c3f6e2f8a5d8b7e0d7f2a4e3c1b9f

---

## Step 3

Store hash in:

ledger.json

---

## Step 4

Run verifier:

python verify_adap.py

---

Expected output:

Generated hash:
9c4c3f6e2f8a5d8b7e0d7f2a4e3c1b9f

Ledger hash:
9c4c3f6e2f8a5d8b7e0d7f2a4e3c1b9f

✓ Verification passed

---

Result:

Decision existence and integrity successfully reconstructed.
