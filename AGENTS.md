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
# <The commands to set up, format, lint, type check and test,
#  exactly as CI runs them.>
```
- Layout: `<where code and tests live>`. Tests that use real external dependencies are marked as integration tests.
- **Coverage is 100% line and branch.** Exclude a line only with an inline comment giving the reason. Never lower the floor.
- Code style: the language's idiomatic style, enforced by its formatter and linter with warnings as errors; every function and type has a doc comment; diagnostics go through the language's standard logger, never bare prints. Text files use LF line endings.

## CI (required to merge)
`.github/workflows/ci.yml` calls `standards.yml` in `nathanzm/.github` at `@main`, so this repo pins no actions. It detects the languages here and runs a gitleaks secret scan, the vendor-file ban, dependency review (on public PRs), actionlint, and each language's checks above. Code in a language with no gate fails CI until `nathanzm/.github` gets one. `standards / result` is the only required check. A repo with pinned dependencies adds `.github/dependabot.yml` for its package ecosystem, with a 7-day cooldown.

## Contributing
- Branch from `main` and open a PR. PRs are squash-merged, and the branch is deleted on merge.
- Commits are signed. Never force-push `main` or rewrite published history.
- Add a dependency only when the standard library can't reasonably do the job, and pin it. Check its license first: permissive licenses (MIT, BSD, Apache-2.0, ISC) are fine; anything copyleft (GPL, AGPL, LGPL) needs the maintainer's approval.
