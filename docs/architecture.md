# Architecture

## Overview
One paragraph: the components and how data flows between them.

## Components
| Component | Responsibility |
|---|---|
| `src/example` | Placeholder package |

## Trust boundaries and threat model
| Boundary | Untrusted input | Threats | Mitigation |
|---|---|---|---|
| Public API (`greet`) | `name` from the caller | Blank or malformed input | Validated; rejected with `ValueError` (REQ-002) |

## Design decisions
- Each decision and the reason for it, in one or two lines.
