from abc import ABC, abstractmethod


# DIP (Principiul inversării dependențelor): calculatorul depinde de acest contract comun.
class Delivery(ABC):
    """Contract comun pentru obținerea costului livrării."""

    @abstractmethod
    def get_cost(self) -> int:
        pass


# OCP (Principiul deschis/închis): adăugați o subclasă Delivery pentru un nou tip de livrare.
class StandardDelivery(Delivery):
    def get_cost(self) -> int:
        return 30


class ExpressDelivery(Delivery):
    def get_cost(self) -> int:
        return 60


# OCP: adăugați ridicarea gratuită fără a modifica OrderCalculator.
class PickupDelivery(Delivery):
    def get_cost(self) -> int:
        return 0


class OrderCalculator:
    """SRP (Principiul responsabilității unice): calculează doar totalul comenzii."""

    def __init__(self, delivery: Delivery):
        # DIP: primiți livrarea din exterior, în loc să o creați aici.
        self.delivery = delivery

    def calculate_total(self, prices: list[int]) -> int:
        # OCP: acest calcul funcționează cu orice implementare Delivery.
        return sum(prices) + self.delivery.get_cost()


def main() -> None:
    prices = [100, 200]
    deliveries = [
        ("Standard delivery", StandardDelivery()),
        ("Express delivery", ExpressDelivery()),
        ("Free pickup", PickupDelivery()),
    ]

    # SRP: păstrați afișarea în consolă aici, în afara clasei OrderCalculator.
    print("MiniShop: order total calculator")
    print(f"Items: {' + '.join(str(price) for price in prices)} = {sum(prices)} MDL")
    print()

    for name, delivery in deliveries:
        # DIP: transmiteți livrarea aleasă către calculator.
        calculator = OrderCalculator(delivery)
        total = calculator.calculate_total(prices)
        print(f"{name} ({delivery.get_cost()} MDL): total {total} MDL")


if __name__ == "__main__":
    main()
