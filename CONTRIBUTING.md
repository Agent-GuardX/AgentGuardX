# Contributing to AgentGuardX

Thank you for helping improve AgentGuardX.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
ruff check .
```

## Pull Request Guidelines

- Keep changes focused.
- Add tests for new behavior.
- Do not add offensive automation that targets third-party systems.
- Document new payloads, adapters, and evaluators.
