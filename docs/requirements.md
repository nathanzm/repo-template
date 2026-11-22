# Requirements

Keywords: **SHALL** (mandatory), **SHALL NOT** (prohibited), **SHOULD** / **SHOULD NOT** (recommended / discouraged), and **MAY** (optional), as in RFC 2119 and RFC 8174. They're normative only in uppercase; text without one is context, not a requirement.

Each row holds one requirement with one keyword, so it can be tested on its own. IDs are permanent: never reuse or renumber them, and mark a dropped requirement "Removed" instead of deleting its row.

## 1. Scope
- **Purpose:** what the project is for, in one or two sentences.
- **Users:** who uses it, and in which roles.
- **Out of scope:** what it deliberately doesn't do.

## 2. Functional requirements

### 2.1 Greeting
*As a caller, I want a greeting for a name, so I can show it to a user.*

| ID | Requirement | Notes |
|---|---|---|
| REQ-001 | `greet` SHALL return `Hello, <name>!` for a non-blank name, with surrounding whitespace trimmed. | |

## 3. Non-functional requirements
Every subsection below is always present. One with nothing to require says "None." and why.

### 3.1 Security
| ID | Requirement | Notes |
|---|---|---|
| REQ-002 | `greet` SHALL reject a blank or whitespace-only name with an error. | Input validation at the public API |

### 3.2 Privacy
None. `greet` stores and sends nothing; the name only passes through.

### 3.3 Logging
None. The example doesn't log.

### 3.4 Reliability
None. `greet` has no state or data to protect.

### 3.5 Performance
None. Inputs are single names.

### 3.6 Compatibility
None beyond the Python version in `pyproject.toml`.

### 3.7 Operations
None. It's a library with no install steps of its own.
