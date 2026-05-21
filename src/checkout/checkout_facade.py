from src.cart.cart_base import CartBase
from src.checkout.shipping_calculator import ShippingCalculator
from src.checkout.order_logger import OrderLogger


class CheckoutFacade:
    def __init__(self, cart: CartBase, notifiers: list = None):
        self._cart = cart
        self._shipping_calculator = ShippingCalculator()
        self._logger = OrderLogger()
        self._notifiers = notifiers or []

    def checkout(self, email: str, coupon_code: str = None):
        item_total = self._cart.get_total()
        shipping = self._shipping_calculator.calculate(item_total, coupon_code)
        final_total = item_total + shipping

        print("=== CHECKOUT ===")
        print(self._cart.get_description())
        print(f"Items Total : ${item_total:.2f}")
        print(f"Shipping    : ${shipping:.2f}")
        print(f"Final Total : ${final_total:.2f}")
        print("================")

        for notifier in self._notifiers:
            notifier(email, final_total)

        self._logger.log({
            "total": final_total,
            "shipping": shipping,
            "item_count": 1
        })