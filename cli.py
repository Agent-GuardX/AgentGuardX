import asyncio
import typer
from agentguardx.adapters.http import HTTPAgentAdapter
from agentguardx.core.payload_loader import load_payloads
from agentguardx.core.scanner import Scanner
from agentguardx.reporting.writers import write_html, write_json, write_markdown

app = typer.Typer(help="AgentGuardX - AI agent security red-team toolkit")

@app.command()
def scan(endpoint: str, payloads: str = "payloads/basic.yaml", response_path: str | None = None, output: str = "report.json", html: str | None = None, markdown: str | None = None, concurrency: int = 5):
    loaded = load_payloads(payloads)
    adapter = HTTPAgentAdapter(endpoint, response_path=response_path)
    findings = asyncio.run(Scanner(adapter, concurrency=concurrency).run(loaded))
    write_json(findings, output)
    if html:
        write_html(findings, html)
    if markdown:
        write_markdown(findings, markdown)
    failed = sum(1 for f in findings if not f.passed)
    typer.echo(f"Scan complete: {len(findings)} checks, {failed} potential findings. JSON: {output}")

if __name__ == "__main__":
    app()
