from abc import ABC, abstractmethod

class Exporter(ABC):

    @abstractmethod
    def export(self, score_path: str) -> str:
        pass
