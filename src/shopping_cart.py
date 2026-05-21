from src.discounts.discount_strategy import DiscountStrategy


class ShoppingCart:

    def __init__(self, discount: DiscountStrategy):
        self._discount = discount
        self._items = []
        self._coupon_code = None
        self._log_history = []

    def add_item(self, name: str, price: float, quantity: int, category: str):
        self._items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        })
        self._log_history.append(f"Added {name} x{quantity}")

    def remove_item(self, name: str):
        self._items = [i for i in self._items if i["name"] != name]
        self._log_history.append(f"Removed {name}")

    def apply_coupon(self, code: str):
        self._coupon_code = code

    def _get_subtotal(self) -> float:
        return sum(i["price"] * i["quantity"] for i in self._items)

    def calculate_total(self) -> float:
        total = self._get_subtotal()
        total = self._discount.apply(total)

        if self._coupon_code == "SAVE10":
            total -= total * 0.10
        elif self._coupon_code == "SAVE20":
            total -= total * 0.20

        electronics_total = sum(
            i["price"] * i["quantity"]
            for i in self._items
            if i["category"] == "electronics"
        )
        if electronics_total > 500:
            total -= 50

        return total

    def get_shipping_cost(self) -> float:
        subtotal = self._get_subtotal()
        if self._coupon_code == "FREESHIP":
            return 0.0
        if subtotal > 100:
            return 0.0
        if subtotal > 50:
            return 4.99
        return 9.99

    def send_order_confirmation(self, email: str):
        total = self.calculate_total()
        print(f"[EMAIL] Sending to {email}: Your order total is ${total:.2f}")

    def print_receipt(self):
        print("=== RECEIPT ===")
        for item in self._items:
            line_total = item["price"] * item["quantity"]
            print(f"  {item['name']} x{item['quantity']} — ${line_total:.2f}")
        print(f"Subtotal : ${self._get_subtotal():.2f}")
        print(f"Shipping : ${self.get_shipping_cost():.2f}")
        print(f"Total    : ${self.calculate_total():.2f}")
        print("===============")

    def get_log(self):
        return self._log_history