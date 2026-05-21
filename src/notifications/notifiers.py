from src.notifications.order_observer import OrderObserver


class EmailNotifier(OrderObserver):
    def on_order_placed(self, order_data: dict):
        print(f"[EMAIL] Order confirmation sent to {order_data['email']}: "
              f"Total ${order_data['total']:.2f}")


class SMSNotifier(OrderObserver):
    def on_order_placed(self, order_data: dict):
        print(f"[SMS] Text sent to {order_data['email']}: "
              f"Your order of ${order_data['total']:.2f} is confirmed!")


class OrderLoggerObserver(OrderObserver):
    def on_order_placed(self, order_data: dict):
        print(f"[LOG] Order recorded — total: ${order_data['total']:.2f}, "
              f"items: {order_data['item_count']}, "
              f"strategy: {order_data['strategy']}")