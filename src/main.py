from src.discounts.discount_factory import DiscountFactory, UserType
from src.shopping_cart import ShoppingCart
from src.cart.cart_decorators import GiftWrapDecorator, InsuranceDecorator
from src.checkout.checkout_facade import CheckoutFacade


def email_notifier(email: str, total: float):
    print(f"[EMAIL] Sending to {email}: Your order total is ${total:.2f}")


def sms_notifier(email: str, total: float):
    print(f"[SMS] Notifying {email}: Order confirmed, total ${total:.2f}")


# Build the cart
vip_discount = DiscountFactory.get_discount(UserType.VIP)
cart = ShoppingCart(discount=vip_discount)
cart.add_item("Laptop", 999.99, 1, "electronics")
cart.add_item("Mouse", 29.99, 2, "electronics")
cart.add_item("Notebook", 4.99, 5, "stationery")
cart.apply_coupon("SAVE10")

# Wrap with decorators
cart_with_giftwrap = GiftWrapDecorator(cart)
cart_with_insurance = InsuranceDecorator(cart_with_giftwrap)

print("Cart description:")
print(cart_with_insurance.get_description())
print()

# Checkout via Facade
facade = CheckoutFacade(
    cart=cart_with_insurance,
    notifiers=[email_notifier, sms_notifier]
)
facade.checkout(email="user@example.com", coupon_code="SAVE10")