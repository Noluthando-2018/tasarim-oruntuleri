from enum import Enum
from src.discounts.discount_strategy import (
    DiscountStrategy, VipDiscount, StudentDiscount, EmployeeDiscount, NoDiscount
)


class UserType(Enum):
    VIP = "vip"
    STUDENT = "student"
    EMPLOYEE = "employee"
    REGULAR = "regular"


class DiscountFactory:
    _registry = {
        UserType.VIP: VipDiscount,
        UserType.STUDENT: StudentDiscount,
        UserType.EMPLOYEE: EmployeeDiscount,
        UserType.REGULAR: NoDiscount,
    }

    @classmethod
    def get_discount(cls, user_type: UserType) -> DiscountStrategy:
        discount_class = cls._registry.get(user_type)
        if discount_class is None:
            raise ValueError(f"Unknown user type: {user_type}. Valid types: {list(cls._registry.keys())}")
        return discount_class()