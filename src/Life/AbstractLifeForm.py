from abc import ABC, abstractmethod


class AbstractLifeForm(ABC):
    @abstractmethod
    def reproduce(self):
        pass
