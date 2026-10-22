from abc import ABC, abstractmethod


class Delivery(ABC):
    """Common contract for getting a delivery cost."""

    @abstractmethod
    def get_cost(self) -> int:
        pass


class StandardDelivery(Delivery):
    def get_cost(self) -> int:
        return 30


class ExpressDelivery(Delivery):
    def get_cost(self) -> int:
        return 60


class OrderCalculator:
    """SRP: responsible only for calculating the order total."""

    def __init__(self, delivery: Delivery):
        # DIP: the delivery method is provided through a common interface.
        self.delivery = delivery

    def calculate_total(self, prices: list[int]) -> int:
        return sum(prices) + self.delivery.get_cost()


def main() -> None:
    prices = [100, 200]
    deliveries = [
        ("Standard delivery", StandardDelivery()),
        ("Express delivery", ExpressDelivery()),
    ]

    print("MiniShop: order total calculator")
    print(f"Items: {' + '.join(str(price) for price in prices)} = {sum(prices)} MDL")
    print()

    for name, delivery in deliveries:
        calculator = OrderCalculator(delivery)
        total = calculator.calculate_total(prices)
        print(f"{name} ({delivery.get_cost()} MDL): total {total} MDL")


if __name__ == "__main__":
    main()