# OpenAI Agent Flow (A-DAP Integration Example)

## Traditional Agent Flow

User Request
↓
LLM Decision
↓
Tool Execution
↓
Response
↓
Log

Problem:

Evidence only exists after execution.

Logs may be modified.

Explanations are retrospective.

---

## A-DAP Agent Flow

User Request
↓
LLM Decision
↓
Envelope Creation
↓
Hash Generation
↓
Independent Verification
↓
Tool Execution
↓
Response

---

## Example Envelope

{
"id":"decision-001",
"timestamp":"2026-05-22T14:00:00Z",
"decision":"Send calendar invite",
"hash":"af29d9138..."
}

Verification:

✓ Envelope exists

✓ Timestamp valid

✓ Integrity preserved

✓ Decision preceded execution

---

## Result

A-DAP does not explain why the model acted.

It proves the decision existed before action execution.
