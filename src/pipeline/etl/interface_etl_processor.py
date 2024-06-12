from abc import ABC, abstractmethod


class InterfaceETLProcessor(ABC):
    @abstractmethod
    def extract_data(self):
        pass

    @abstractmethod
    def transform_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass
