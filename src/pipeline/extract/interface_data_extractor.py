from abc import ABC, abstractmethod


class InterfaceDataExtractor(ABC):
    @abstractmethod
    def extract_data(self):
        pass
