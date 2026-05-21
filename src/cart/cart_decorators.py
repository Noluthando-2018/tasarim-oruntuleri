from src.cart.cart_base import CartBase


class CartDecorator(CartBase):
    def __init__(self, cart: CartBase):
        self._cart = cart

    def get_total(self) -> float:
        return self._cart.get_total()

    def get_description(self) -> str:
        return self._cart.get_description()


class GiftWrapDecorator(CartDecorator):
    COST = 5.99

    def get_total(self) -> float:
        return self._cart.get_total() + self.COST

    def get_description(self) -> str:
        return self._cart.get_description() + " + Gift Wrap ($5.99)"

    def __repr__(self):
        return f"GiftWrapDecorator({self._cart})"


class InsuranceDecorator(CartDecorator):
    COST = 9.99

    def get_total(self) -> float:
        return self._cart.get_total() + self.COST

    def get_description(self) -> str:
        return self._cart.get_description() + " + Shipping Insurance ($9.99)"

    def __repr__(self):
        return f"InsuranceDecorator({self._cart})"


class PriorityShippingDecorator(CartDecorator):
    COST = 14.99

    def get_total(self) -> float:
        return self._cart.get_total() + self.COST

    def get_description(self) -> str:
        return self._cart.get_description() + " + Priority Shipping ($14.99)"

    def __repr__(self):
        return f"PriorityShippingDecorator({self._cart})"