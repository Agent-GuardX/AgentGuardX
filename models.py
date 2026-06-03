from dataclasses import dataclass, field
from typing import Any

@dataclass
class Payload:
    id: str
    category: str
    prompt: str
    severity: str = "medium"
    tags: list[str] = field(default_factory=list)
    indicators: list[str] = field(default_factory=list)
    owasp: str | None = None

@dataclass
class ScanFinding:
    id: str
    category: str
    severity: str
    passed: bool
    risk: str | None
    prompt: str
    response: str
    evidence: str
    metadata: dict[str, Any] = field(default_factory=dict)
