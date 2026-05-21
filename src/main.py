from src.discounts.discount_factory import DiscountFactory, UserType
from src.shopping_cart import ShoppingCart

# VIP user
vip_discount = DiscountFactory.get_discount(UserType.VIP)
cart = ShoppingCart(discount=vip_discount)

cart.add_item("Laptop", 999.99, 1, "electronics")
cart.add_item("Mouse", 29.99, 2, "electronics")
cart.add_item("Notebook", 4.99, 5, "stationery")
cart.apply_coupon("SAVE10")

cart.print_receipt()
cart.send_order_confirmation("user@example.com")
print("Log:", cart.get_log())

print()

# Student user
student_discount = DiscountFactory.get_discount(UserType.STUDENT)
cart2 = ShoppingCart(discount=student_discount)
cart2.add_item("Kalem", 2.99, 3, "stationery")
cart2.print_receipt()