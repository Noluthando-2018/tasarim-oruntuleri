from src.discounts.discount_factory import DiscountFactory, UserType
from src.discounts.discount_strategy import FlashSaleStrategy, LoyaltyPointsStrategy
from src.shopping_cart import ShoppingCart
from src.notifications.order_publisher import OrderEventPublisher
from src.notifications.notifiers import EmailNotifier, SMSNotifier, OrderLoggerObserver


# Set up Observer
publisher = OrderEventPublisher()
publisher.subscribe(EmailNotifier())
publisher.subscribe(SMSNotifier())
publisher.subscribe(OrderLoggerObserver())

# Build cart
vip_discount = DiscountFactory.get_discount(UserType.VIP)
cart = ShoppingCart(discount=vip_discount, publisher=publisher)

cart.add_item("Laptop", 999.99, 1, "electronics")
cart.add_item("Mouse", 29.99, 2, "electronics")
cart.add_item("Notebook", 4.99, 5, "stationery")

print("=== ORDER 1: VIP discount ===")
cart.place_order("user@example.com")

print()
print("=== ORDER 2: Flash Sale — strategy swapped at runtime ===")
cart.set_strategy(FlashSaleStrategy())
cart.place_order("user@example.com")

print()
print("=== ORDER 3: Loyalty Points strategy ===")
cart.set_strategy(LoyaltyPointsStrategy())
cart.place_order("user@example.com")

print()
print("Log:", cart.get_log())