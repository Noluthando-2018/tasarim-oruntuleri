from src.notifications.order_observer import OrderObserver


class OrderEventPublisher:
    def __init__(self):
        self._observers: list[OrderObserver] = []

    def subscribe(self, observer: OrderObserver):
        self._observers.append(observer)

    def unsubscribe(self, observer: OrderObserver):
        self._observers.remove(observer)

    def notify(self, order_data: dict):
        for observer in self._observers:
            observer.on_order_placed(order_data)