from abc import ABC, abstractmethod


class AbstractGene(ABC):
    @abstractmethod
    def replicate(self):
        pass
