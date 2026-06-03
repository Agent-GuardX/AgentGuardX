<p align="center">
  <img src="assets/banner.svg" alt="AgentGuardX" width="100%" />
</p>

<h3 align="center">AI Security Red-Team Toolkit</h3>

<p align="center">
  <a href="#">App</a> --
  <a href="docs/">Docs</a> --
  <a href="docs/api.md">API</a>
</p>

<p align="center">
  <img alt="python" src="https://img.shields.io/badge/python-3.10%2B-blue">
  <img alt="license" src="https://img.shields.io/badge/license-Apache%202.0-green">
  <img alt="uv" src="https://img.shields.io/badge/%E2%9A%A1-uv-purple">
  <img alt="commitizen" src="https://img.shields.io/badge/commitizen-friendly-brightgreen">
  <img alt="Ruff" src="https://img.shields.io/badge/%E2%9A%A1-Ruff-blueviolet">
  <img alt="coverage" src="https://img.shields.io/badge/coverage-58%25-yellow">
  <img alt="build" src="https://img.shields.io/badge/build-passing-brightgreen">
</p>

---

## What is AgentGuardX?

AgentGuardX is an open-source **AI Security Red-Team Toolkit** designed to help security researchers, developers, and organizations evaluate and harden LLM-powered applications and autonomous agents.

It provides a modular testing framework for prompt injection, tool misuse, data exfiltration, unsafe agent behavior, policy bypasses, and common agentic AI security risks.

## Features

| Module | Description |
|---|---|
| Attack Modules | Collection of practical red-team attack scenarios for LLM agents. |
| Tool Analysis | Analyze tool integrations for risky configuration and misuse. |
| Automated Scanning | Scan agents and workflows for common vulnerabilities. |
| Reporting | Generate JSON and HTML security reports. |
| Extensible Core | Add custom payloads, detectors, adapters, and policies. |

## Quick Start

```bash
pip install -e .
agentguardx scan \
  --endpoint http://127.0.0.1:8000/agent \
  --response-path answer \
  --html report.html
```

Run the mock target:

```bash
uvicorn examples.mock_target:app --reload
```

## Project Structure

```text
AgentGuardX/
├── assets/                 # README banner and brand assets
├── agentguardx/            # Core Python package
├── payloads/               # Attack payload definitions
├── examples/               # Demo vulnerable targets
├── docs/                   # Documentation
├── tests/                  # Unit tests
├── .github/workflows/      # CI pipeline
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
└── README.md
```

## Documentation

- [Documentation](docs/)
- [API Reference](docs/api.md)
- [Threat Model](docs/threat-model.md)

## Ethical Use

AgentGuardX is intended for authorized security research, defensive testing, and educational use only. Do not run tests against systems you do not own or have explicit permission to assess.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## Security

To report a vulnerability, see [SECURITY.md](SECURITY.md).

## License

Apache License 2.0. See [LICENSE](LICENSE).
