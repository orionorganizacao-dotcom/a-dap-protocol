import json
import hashlib

with open("examples/minimal-envelope.json", "r") as f:
    envelope = json.load(f)

payload = envelope.copy()
payload.pop("decision_hash")

serialized = json.dumps(
    payload,
    sort_keys=True,
    separators=(",", ":")
)

computed_hash = hashlib.sha256(
    serialized.encode()
).hexdigest()

print("\nComputed hash:\n")
print(computed_hash)

stored = envelope["decision_hash"]

if stored == "TO_BE_COMPUTED":
    print("\nEnvelope awaiting hash generation")

elif stored == computed_hash:
    print("\n✓ Verification passed")

else:
    print("\n✗ Hash mismatch")
    print("Integrity validation failed")
