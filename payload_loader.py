from pathlib import Path
import yaml
from agentguardx.models import Payload

def load_payloads(path: str | Path) -> list[Payload]:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    items = raw.get("payloads", raw if isinstance(raw, list) else [])
    return [Payload(**item) for item in items]
