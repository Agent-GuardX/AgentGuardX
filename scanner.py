import asyncio
from agentguardx.adapters.base import TargetAdapter
from agentguardx.evaluators.heuristic import HeuristicEvaluator
from agentguardx.models import Payload, ScanFinding

class Scanner:
    def __init__(self, adapter: TargetAdapter, evaluator: HeuristicEvaluator | None = None, concurrency: int = 5):
        self.adapter = adapter
        self.evaluator = evaluator or HeuristicEvaluator()
        self.concurrency = concurrency

    async def _run_one(self, payload: Payload, sem: asyncio.Semaphore) -> ScanFinding:
        async with sem:
            try:
                response = await self.adapter.send(payload.prompt)
            except Exception as exc:
                response = f"AGENTGUARDX_TRANSPORT_ERROR: {exc}"
            return self.evaluator.evaluate(payload, response)

    async def run(self, payloads: list[Payload]) -> list[ScanFinding]:
        sem = asyncio.Semaphore(self.concurrency)
        return await asyncio.gather(*(self._run_one(p, sem) for p in payloads))
