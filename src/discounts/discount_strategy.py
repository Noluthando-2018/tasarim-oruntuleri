from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class VipDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.80


class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.85


class EmployeeDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.70


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


# --- OCP DEMONSTRATION ---
# These new strategies were added without modifying any existing class above.
# ShoppingCart, DiscountFactory, and all other files are completely untouched.

class FlashSaleStrategy(DiscountStrategy):
    """50% off everything — added without modifying any existing code."""
    def apply(self, total: float) -> float:
        return total * 0.50


class LoyaltyPointsStrategy(DiscountStrategy):
    """$20 off for every $200 spent."""
    def apply(self, total: float) -> float:
        discount = (total // 200) * 20
        return total - discount