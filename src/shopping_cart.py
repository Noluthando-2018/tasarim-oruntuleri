from src.cart.cart_base import CartBase
from src.discounts.discount_strategy import DiscountStrategy
from src.notifications.order_publisher import OrderEventPublisher


class ShoppingCart(CartBase):

    def __init__(self, discount: DiscountStrategy, publisher: OrderEventPublisher):
        self._discount = discount
        self._publisher = publisher
        self._items = []
        self._coupon_code = None
        self._log_history = []

    def set_strategy(self, discount: DiscountStrategy):
        """Swap discount strategy at runtime — OCP in action."""
        self._discount = discount

    def add_item(self, name: str, price: float, quantity: int, category: str):
        self._items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        })
        self._log_history.append(f"Added {name} x{quantity}")

    def apply_coupon(self, code: str):
        self._coupon_code = code

    def _get_subtotal(self) -> float:
        return sum(i["price"] * i["quantity"] for i in self._items)

    def get_total(self) -> float:
        total = self._get_subtotal()
        total = self._discount.apply(total)

        if self._coupon_code == "SAVE10":
            total -= total * 0.10
        elif self._coupon_code == "SAVE20":
            total -= total * 0.20

        electronics_total = sum(
            i["price"] * i["quantity"]
            for i in self._items if i["category"] == "electronics"
        )
        if electronics_total > 500:
            total -= 50

        return total

    def get_description(self) -> str:
        lines = [f"  {i['name']} x{i['quantity']} — ${i['price'] * i['quantity']:.2f}"
                 for i in self._items]
        return "\n".join(lines)

    def place_order(self, email: str):
        total = self.get_total()
        self._publisher.notify({
            "email": email,
            "total": total,
            "item_count": len(self._items),
            "strategy": type(self._discount).__name__
        })
        self._log_history.append(f"Order placed for {email}, total ${total:.2f}")

    def get_log(self):
        return self._log_history