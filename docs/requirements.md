# Requirements

Each requirement is one testable statement with a stable ID. Never reuse an ID; mark dropped requirements "Removed" instead of deleting them.

| ID | Requirement | Type |
|---|---|---|
| REQ-001 | Greeting a non-blank name returns `Hello, <name>!` with surrounding whitespace trimmed. | Functional |
| REQ-002 | A blank or whitespace-only name is rejected with an error. | Security (input validation) |

Types: Functional, Security, Privacy, Performance, Operational.
