from dataclasses import asdict
from pathlib import Path
import html, json
from agentguardx.models import ScanFinding

def write_json(findings: list[ScanFinding], path: str) -> None:
    Path(path).write_text(json.dumps([asdict(f) for f in findings], indent=2), encoding="utf-8")

def write_markdown(findings: list[ScanFinding], path: str) -> None:
    lines = ["# AgentGuardX Security Report", ""]
    for f in findings:
        status = "PASS" if f.passed else "FAIL"
        lines += [f"## {status}: {f.id}", f"- Severity: `{f.severity}`", f"- Category: `{f.category}`", f"- Risk: `{f.risk or 'unmapped'}`", f"- Evidence: {f.evidence}", ""]
    Path(path).write_text("\n".join(lines), encoding="utf-8")

def write_html(findings: list[ScanFinding], path: str) -> None:
    rows = []
    for f in findings:
        status = "PASS" if f.passed else "FAIL"
        rows.append(f"<tr><td>{status}</td><td>{html.escape(f.id)}</td><td>{html.escape(f.severity)}</td><td>{html.escape(f.category)}</td><td>{html.escape(f.evidence)}</td></tr>")
    doc = """<!doctype html><html><head><meta charset='utf-8'><title>AgentGuardX Report</title>
    <style>body{font-family:Inter,Arial,sans-serif;background:#0d1117;color:#e6edf3;padding:30px}table{border-collapse:collapse;width:100%}td,th{border:1px solid #30363d;padding:10px}th{background:#161b22}.FAIL{color:#ff7b72}</style></head><body>
    <h1>AgentGuardX Security Report</h1><table><tr><th>Status</th><th>ID</th><th>Severity</th><th>Category</th><th>Evidence</th></tr>""" + "\n".join(rows) + "</table></body></html>"
    Path(path).write_text(doc, encoding="utf-8")
