from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class VipDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.80  # 20% off


class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.85  # 15% off


class EmployeeDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.70  # 30% off


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total  # no change