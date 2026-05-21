class OrderLogger:
    def log(self, order_data: dict):
        print(f"[LOG] Order recorded: total=${order_data['total']:.2f}, "
              f"shipping=${order_data['shipping']:.2f}, "
              f"items={order_data['item_count']}")