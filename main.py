from abc import ABC, abstractmethod


# DIP (Dependency Inversion): the calculator depends on this common contract.
class Delivery(ABC):
    """Common contract for getting a delivery cost."""

    @abstractmethod
    def get_cost(self) -> int:
        pass


# OCP (Open/Closed): add a new Delivery subclass for a new delivery type.
class StandardDelivery(Delivery):
    def get_cost(self) -> int:
        return 30


class ExpressDelivery(Delivery):
    def get_cost(self) -> int:
        return 60


# OCP: add free pickup without changing OrderCalculator.
class PickupDelivery(Delivery):
    def get_cost(self) -> int:
        return 0


class OrderCalculator:
    """SRP (Single Responsibility): only calculate the order total."""

    def __init__(self, delivery: Delivery):
        # DIP: receive the delivery from outside instead of creating it here.
        self.delivery = delivery

    def calculate_total(self, prices: list[int]) -> int:
        # OCP: this calculation works with any Delivery implementation.
        return sum(prices) + self.delivery.get_cost()


def main() -> None:
    prices = [100, 200]
    deliveries = [
        ("Standard delivery", StandardDelivery()),
        ("Express delivery", ExpressDelivery()),
        ("Free pickup", PickupDelivery()),
    ]

    # SRP: keep console output here, outside OrderCalculator.
    print("MiniShop: order total calculator")
    print(f"Items: {' + '.join(str(price) for price in prices)} = {sum(prices)} MDL")
    print()

    for name, delivery in deliveries:
        # DIP: pass the chosen delivery into the calculator.
        calculator = OrderCalculator(delivery)
        total = calculator.calculate_total(prices)
        print(f"{name} ({delivery.get_cost()} MDL): total {total} MDL")


if __name__ == "__main__":
    main()