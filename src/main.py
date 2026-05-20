# main.py — kullanım örneği

from shopping_cart import ShoppingCart

# VIP kullanıcı alışverişi
cart = ShoppingCart("vip")

cart.add_item("Laptop", 999.99, 1, "electronics")
cart.add_item("Mouse", 29.99, 2, "electronics")
cart.add_item("Notebook", 4.99, 5, "stationery")

cart.apply_coupon("SAVE10")

cart.print_receipt()
cart.send_order_confirmation("user@example.com")

print("Log:", cart.get_log())

# Yazım hatası olan user_type — hata vermez, sessizce indirim almaz
cart2 = ShoppingCart("stuednt")  # ❌ typo, hiç indirim yok ama kimse fark etmez
cart2.add_item("Kalem", 2.99, 3, "stationery")
cart2.print_receipt()