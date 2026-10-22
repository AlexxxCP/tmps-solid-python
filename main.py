from abc import ABC, abstractmethod


class Delivery(ABC):
    """Общий способ узнать стоимость доставки."""

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
    """SRP: отвечает только за расчёт итоговой суммы заказа."""

    def __init__(self, delivery: Delivery):
        # DIP: способ доставки передаётся извне через общий интерфейс.
        self.delivery = delivery

    def calculate_total(self, prices: list[int]) -> int:
        return sum(prices) + self.delivery.get_cost()


def main() -> None:
    prices = [100, 200]
    deliveries = [
        ("Обычная доставка", StandardDelivery()),
        ("Срочная доставка", ExpressDelivery()),
    ]

    print("MiniShop: расчёт стоимости заказа")
    print(f"Товары: {' + '.join(str(price) for price in prices)} = {sum(prices)} леев")
    print()

    for name, delivery in deliveries:
        calculator = OrderCalculator(delivery)
        total = calculator.calculate_total(prices)
        print(f"{name} ({delivery.get_cost()} леев): итого {total} леев")


if __name__ == "__main__":
    main()