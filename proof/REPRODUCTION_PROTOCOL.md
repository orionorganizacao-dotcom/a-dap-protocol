# Reproduction Protocol

Purpose:

Allow an independent third party to reproduce A-DAP verification without trusting the repository author.

---

## Step 1 — Clone repository

Run:

git clone <repository-url>

---

## Step 2 — Verify envelope integrity

Run:

python reference/verify_adap.py examples/minimal-envelope-verification.json

Expected:

Verification passed

---

## Step 3 — Verify tampering detection

Run:

python reference/verify_adap.py examples/tampered-envelope.json

Expected:

Verification failed

---

## Step 4 — Verify temporal evidence

Run:

ots verify examples/minimal-envelope-verification.ots

Expected:

Timestamp verified

---

## Success criteria

Independent reproduction obtains identical outputs.

---

## Principle

Evidence should survive author removal.
