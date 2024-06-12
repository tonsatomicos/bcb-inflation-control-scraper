from abc import ABC, abstractmethod


class InterfaceDataTransform(ABC):
    @abstractmethod
    def transform_data(self):
        pass
