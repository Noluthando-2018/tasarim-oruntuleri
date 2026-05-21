from abc import ABC, abstractmethod


class OrderObserver(ABC):
    @abstractmethod
    def on_order_placed(self, order_data: dict):
        pass