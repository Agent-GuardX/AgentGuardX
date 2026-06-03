from abc import ABC, abstractmethod

class TargetAdapter(ABC):
    @abstractmethod
    async def send(self, prompt: str) -> str:
        raise NotImplementedError
