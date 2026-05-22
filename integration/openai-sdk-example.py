import hashlib
import json
from datetime import datetime


class ADAPEnvelope:

    def create(
        self,
        user_request,
        decision,
        tool
    ):

        timestamp = datetime.utcnow().isoformat()

        payload = {
            "timestamp": timestamp,
            "user_request": user_request,
            "decision": decision,
            "tool": tool
        }

        serialized = json.dumps(
            payload,
            sort_keys=True
        )

        decision_hash = hashlib.sha256(
            serialized.encode()
        ).hexdigest()

        envelope = {
            "id": "decision-001",
            **payload,
            "decision_hash": decision_hash,
            "status": "PRE-COMMIT"
        }

        return envelope


adap = ADAPEnvelope()

envelope = adap.create(
    user_request="Schedule meeting tomorrow",
    decision="Create calendar event",
    tool="calendar.create"
)

print(
    json.dumps(
        envelope,
        indent=2
    )
)
