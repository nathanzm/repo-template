# Requirements

Keywords: **SHALL** (mandatory), **SHALL NOT** (prohibited), **SHOULD** / **SHOULD NOT** (recommended / discouraged), and **MAY** (optional), as in RFC 2119 and RFC 8174. They're normative only in uppercase; text without one is context, not a requirement.

Each row holds one requirement with one keyword, so it can be tested on its own. IDs are permanent: never reuse or renumber them, and mark a dropped requirement "Removed" instead of deleting its row.

## 1. Scope
- **Purpose:** what the project is for, in one or two sentences.
- **Users:** who uses it, and in which roles.
- **Out of scope:** what it deliberately doesn't do.

## 2. Functional requirements

### 2.1 Feature area
*As a <role>, I want <capability>, so that <benefit>.*

| ID | Requirement | Notes |
|---|---|---|
| REQ-001 | The system SHALL <observable behavior>. | |

## 3. Non-functional requirements
Every subsection below is always present. One with nothing to require says "None." and why.

### 3.1 Security
| ID | Requirement | Notes |
|---|---|---|
| REQ-002 | The system SHALL reject <invalid input> at <trust boundary> with an error. | Input validation |

### 3.2 Privacy
None. <Why: for example, it stores and sends no personal data.>

### 3.3 Logging
None. <Why.>

### 3.4 Reliability
None. <Why.>

### 3.5 Performance
None. <Why.>

### 3.6 Compatibility
None. <Why.>

### 3.7 Operations
None. <Why.>
