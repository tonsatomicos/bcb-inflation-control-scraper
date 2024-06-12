from abc import ABC, abstractmethod


class InterfaceDataLoader(ABC):
    @abstractmethod
    def load_data(self):
        pass
