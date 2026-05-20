# shopping_cart.py — Faz 0 başlangıç kodu (kasıtlı olarak kötü yazılmış)


# ❌ Sorun 1: God Class — bu sınıf her şeyi yapıyor
class ShoppingCart:

    def __init__(self, user_type: str):
        # ❌ Sorun 2: user_type bir magic string, doğrulama yok
        # "vip" yerine "vipp" yazsan sessizce indirim almıyorsun
        self.user_type = user_type
        self.items = []         # list of dicts
        self.coupon_code = None
        self.log_history = []

    def add_item(self, name: str, price: float, quantity: int, category: str):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        })
        self.log_history.append(f"Added {name} x{quantity}")

    def remove_item(self, name: str):
        self.items = [i for i in self.items if i["name"] != name]
        self.log_history.append(f"Removed {name}")

    def apply_coupon(self, code: str):
        self.coupon_code = code

    # ❌ Sorun 3: İndirim mantığı if-else zincirleriyle hardcoded
    # Yeni bir indirim eklemek için bu metodu doğrudan değiştirmen gerekiyor
    def calculate_total(self) -> float:
        total = 0.0

        for item in self.items:
            total += item["price"] * item["quantity"]

        # Kullanıcı tipi indirimleri
        if self.user_type == "vip":
            total *= 0.80   # VIP için %20 indirim
        elif self.user_type == "student":
            total *= 0.85  # Öğrenci için %15 indirim
        elif self.user_type == "employee":
            total *= 0.70  # Çalışan için %30 indirim

        # Kupon indirimleri
        if self.coupon_code == "SAVE10":
            total -= total * 0.10
        elif self.coupon_code == "SAVE20":
            total -= total * 0.20
        elif self.coupon_code == "FREESHIP":
            pass  # kargo ücretsiz, calculate_total'ı etkilemiyor

        # ❌ Sorun 4: Kategori indirimi de buraya gömülmüş
        electronics_total = 0.0
        for item in self.items:
            if item["category"] == "electronics":
                electronics_total += item["price"] * item["quantity"]
        if electronics_total > 500:
            total -= 50  # 500$+ elektronik alışverişinde 50$ indirim

        return total

    # ❌ Sorun 5: Kargo hesabı, calculate_total'daki mantığı tekrar ediyor
    # İki yerde aynı subtotal hesabı — biri değişirse diğeri bozulur
    def get_shipping_cost(self) -> float:
        subtotal = sum(i["price"] * i["quantity"] for i in self.items)

        if self.coupon_code == "FREESHIP":
            return 0.0
        if subtotal > 100:
            return 0.0
        if subtotal > 50:
            return 4.99
        return 9.99

    # ❌ Sorun 6: Bildirim mantığının bir sepet sınıfında işi yok
    # Yarın SMS eklenirse, öbür gün push notification — bu metot sonsuza büyür
    def send_order_confirmation(self, email: str):
        total = self.calculate_total()
        print(f"[EMAIL] Sending to {email}: Your order total is ${total:.2f}")

    def print_receipt(self):
        print("=== RECEIPT ===")
        for item in self.items:
            line_total = item["price"] * item["quantity"]
            print(f"  {item['name']} x{item['quantity']} — ${line_total:.2f}")
        subtotal = sum(i["price"] * i["quantity"] for i in self.items)
        print(f"Subtotal : ${subtotal:.2f}")
        print(f"Shipping : ${self.get_shipping_cost():.2f}")
        print(f"Total    : ${self.calculate_total():.2f}")
        print("===============")

    def get_log(self):
        return self.log_history