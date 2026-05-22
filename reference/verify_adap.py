import hashlib
import json

def sha256_file(filename):
    sha = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(4096)

            if not chunk:
                break

            sha.update(chunk)

    return sha.hexdigest()


def verify():

    envelope_hash = sha256_file(
        "../examples/minimal-envelope.json"
    )

    with open(
        "../examples/ledger.json",
        "r"
    ) as f:

        ledger = json.load(f)

    stored_hash = ledger[0]["decision_hash"]

    print("Generated hash:")
    print(envelope_hash)

    print()

    print("Ledger hash:")
    print(stored_hash)

    print()

    if envelope_hash == stored_hash:
        print("✓ Verification passed")

    else:
        print("✗ Verification failed")


verify()
