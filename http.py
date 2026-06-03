import httpx
from .base import TargetAdapter

class HTTPAgentAdapter(TargetAdapter):
    def __init__(self, endpoint: str, response_path: str | None = None, timeout: float = 30.0):
        self.endpoint = endpoint
        self.response_path = response_path
        self.timeout = timeout

    async def send(self, prompt: str) -> str:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(self.endpoint, json={"prompt": prompt})
            response.raise_for_status()
            content_type = response.headers.get("content-type", "")
            if "application/json" not in content_type:
                return response.text
            data = response.json()
            if self.response_path:
                value = data
                for part in self.response_path.split("."):
                    value = value[part]
                return str(value)
            return str(data)
