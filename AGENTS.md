# AGENTS.md

Guidance for anyone, human or AI, working in this repository. It's the only AI guidance file: never add vendor-specific ones (`CLAUDE.md`, `.claude/`, `GEMINI.md`, `.cursor/`, `.github/copilot-instructions.md`, and so on); CI rejects them.

## Start here
- [README.md](README.md): what it is and how users run it.
- [docs/requirements.md](docs/requirements.md): what it must do, as SHALL/SHOULD/MAY requirements with permanent `REQ-` IDs, one per row, grouped by section.
- [docs/architecture.md](docs/architecture.md): how it's built, trust boundaries, threat model.
- [docs/test-plan.md](docs/test-plan.md): how each requirement is tested.

Keep these current in the same change as the code. Write them in the present tense, short, with no history narration. Keep their fixed sections; leave one out only when it has nothing to say.

## Principles
- **Security first, then privacy.** Validate all input at trust boundaries, use least privilege, no secrets in the repo, and keep dependencies to a minimum. If a change would weaken security or privacy, stop and raise it.
- **Simplicity first.** The least code that meets the requirements: no speculative features, layers or configuration.
- **Requirements drive tests.** Each requirement has tests that cite its `REQ-` ID. Tests check behavior, not implementation details.

## Develop
```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements-dev.txt
ruff format && ruff check && mypy
pytest --cov --cov-branch --cov-report=term-missing --cov-fail-under=100
```
- Layout: code in `src/<package>/`, tests in `tests/`. Mark tests that use real external dependencies with `@pytest.mark.integration`.
- **Coverage is 100% line and branch.** Exclude a line only with an inline reason (`# pragma: no cover - <why>`). Never lower the floor.
- Code style: idiomatic Python (PEP 8 via ruff); every function and class has a docstring; diagnostics go through `logging`, never `print`. Text files use LF line endings.

## CI (required to merge)
`.github/workflows/ci.yml` calls the shared workflows in `nathanzm/.github`: a gitleaks secret scan, the vendor-file ban, dependency review (on public PRs), and the Python checks above. They're pinned by commit SHA; Dependabot keeps the pins and `requirements-dev.txt` current.

## Contributing
- Branch from `main` and open a PR. PRs are squash-merged, and the branch is deleted on merge.
- Commits are signed. Never force-push `main` or rewrite published history.
- Add a dependency only when the standard library can't reasonably do the job, and pin it. Check its license first: permissive licenses (MIT, BSD, Apache-2.0, ISC) are fine; anything copyleft (GPL, AGPL, LGPL) needs the maintainer's approval.
