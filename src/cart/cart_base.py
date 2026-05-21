from abc import ABC, abstractmethod


class CartBase(ABC):
    @abstractmethod
    def get_total(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass