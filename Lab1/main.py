"""MiniShop demonstrates three creational design patterns."""

from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Optional


class Delivery(ABC):
    """Common product type for the available delivery options."""

    @abstractmethod
    def get_cost(self) -> int:
        pass


class StandardDelivery(Delivery):
    def get_cost(self) -> int:
        return 30


class ExpressDelivery(Delivery):
    def get_cost(self) -> int:
        return 60


class PickupDelivery(Delivery):
    def get_cost(self) -> int:
        return 0


# Factory Method: each concrete factory creates one delivery option.
class DeliveryFactory(ABC):
    @abstractmethod
    def create_delivery(self) -> Delivery:
        pass


class StandardDeliveryFactory(DeliveryFactory):
    def create_delivery(self) -> Delivery:
        return StandardDelivery()


class ExpressDeliveryFactory(DeliveryFactory):
    def create_delivery(self) -> Delivery:
        return ExpressDelivery()


class PickupDeliveryFactory(DeliveryFactory):
    def create_delivery(self) -> Delivery:
        return PickupDelivery()


class Order:
    def __init__(self, items: list[int], delivery: Delivery):
        self.items = items
        self.delivery = delivery

    def total(self) -> int:
        return sum(self.items) + self.delivery.get_cost()

    def clone(self) -> "Order":
        """Prototype: return an independent copy of this order."""
        return deepcopy(self)


# Builder: add order parts first, then create the completed order with build().
class OrderBuilder:
    def __init__(self):
        self._items: list[int] = []
        self._delivery: Optional[Delivery] = None

    def add_item(self, price: int) -> None:
        self._items.append(price)

    def set_delivery(self, delivery: Delivery) -> None:
        self._delivery = delivery

    def build(self) -> Order:
        if self._delivery is None:
            raise ValueError("Set a delivery option before building the order.")

        return Order(self._items.copy(), self._delivery)


def build_order(prices: list[int], factory: DeliveryFactory) -> Order:
    builder = OrderBuilder()
    for price in prices:
        builder.add_item(price)

    builder.set_delivery(factory.create_delivery())
    return builder.build()


def main() -> None:
    prices = [100, 200]

    # Builder and Factory Method create the first order.
    standard_order = build_order(prices, StandardDeliveryFactory())

    # Prototype copies the order; Factory Method supplies express delivery.
    express_order = standard_order.clone()
    express_order.delivery = ExpressDeliveryFactory().create_delivery()

    # Builder and Factory Method also create the free-pickup order.
    pickup_order = build_order(prices, PickupDeliveryFactory())

    orders = [
        ("Standard delivery", standard_order),
        ("Express delivery", express_order),
        ("Free pickup", pickup_order),
    ]

    print("MiniShop: order builder demo")
    print(f"Items: {' + '.join(str(price) for price in prices)} = {sum(prices)} MDL")
    print()

    for name, order in orders:
        print(f"{name}: total {order.total()} MDL")

    print()
    print("Prototype example:")
    print(f"Original standard order: {standard_order.total()} MDL")
    print(f"Cloned order with express delivery: {express_order.total()} MDL")


if __name__ == "__main__":
    main()
