class ShippingCalculator:
    def calculate(self, subtotal: float, coupon_code: str = None) -> float:
        if coupon_code == "FREESHIP":
            return 0.0
        if subtotal > 100:
            return 0.0
        if subtotal > 50:
            return 4.99
        return 9.99