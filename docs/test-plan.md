# Test plan

## Strategy
- **Unit** (`tests/`): each requirement's behavior, including error paths. 100% line and branch coverage, enforced by CI.
- **Integration** (`@pytest.mark.integration`): runs against real dependencies (files, processes, services) instead of mocks wherever practical.
- **Fuzz/property** (where input parsing exists): generated inputs against the parsers, run in CI as a short job.
- Tests are written against the requirements, not the implementation. Every `REQ-` ID has at least one test.

## Test cases
Sections match [requirements.md](requirements.md).

### 2. Functional requirements
| Requirement | Test | Kind |
|---|---|---|
| REQ-001 | `tests/test_example.py::test_greets_name` | Unit |

### 3. Non-functional requirements
| Requirement | Test | Kind |
|---|---|---|
| REQ-002 | `tests/test_example.py::test_rejects_blank_name` | Unit |
