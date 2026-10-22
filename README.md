# TMPS: A Tiny Project Using Three SOLID Principles

**MiniShop** is a Python console application that calculates an order total
with standard or express delivery. It demonstrates **SRP, OCP, and DIP**.

## Application Description

There are two items priced at 100 and 200 MDL. Standard delivery costs 30 MDL,
and express delivery costs 60 MDL. The application displays both order totals:

```text
MiniShop: order total calculator
Items: 100 + 200 = 300 MDL

Standard delivery (30 MDL): total 330 MDL
Express delivery (60 MDL): total 360 MDL
```

This is an educational example with predefined prices, no menu, database,
or payment processing. All amounts are whole Moldovan lei (MDL).
To change the item prices, edit the `prices` list inside `main()`.

## Running the Application

Python 3.9 or later is required. No external libraries are needed.

Run this command from the project directory:

```powershell
python main.py
```

## Project Structure

- `main.py` contains all application code.
- `README.md` describes the project and explains the principles.
- `.gitignore` excludes `Example/`, Python cache files, and local environments.

| Component | Responsibility |
| --- | --- |
| `Delivery` | Defines a common contract for getting a delivery cost through `get_cost()`. |
| `StandardDelivery` | Returns the standard delivery cost: 30 MDL. |
| `ExpressDelivery` | Returns the express delivery cost: 60 MDL. |
| `OrderCalculator` | Adds item prices and the delivery cost. |
| `main()` | Creates objects and prints the results. |

`Delivery` is an abstract class. Using `ABC` and `@abstractmethod`, it requires
concrete delivery classes to implement `get_cost()`.
An instance of `Delivery()` cannot be created directly.

## Three SOLID Principles

SOLID is a set of five principles for designing object-oriented software.
This project explains three of them.

### 1. S - Single Responsibility Principle

**Idea:** a class should have one reason to change.

`OrderCalculator` is responsible only for calculating the total. It does not
print a receipt or choose a delivery rate. Delivery classes define the costs,
and `main()` prints the results.

If the output format changes, update `main()`. If the standard delivery rate
changes, update `StandardDelivery`. Neither change requires modifying the
order calculation formula.

### 2. O - Open/Closed Principle

**Idea:** a component should support new behavior through extension without
requiring changes to its existing implementation.

`OrderCalculator` calls `get_cost()` without checking which delivery class
it receives. Free pickup can be added as a new class:

```python
from main import Delivery, OrderCalculator


class PickupDelivery(Delivery):
    def get_cost(self) -> int:
        return 0


calculator = OrderCalculator(PickupDelivery())
print(calculator.calculate_total([100, 200]))  # 300
```

This snippet illustrates a possible extension; the main application includes
two delivery methods. Adding pickup requires no changes to `OrderCalculator`.
The setup code, such as `main()`, only needs to create and pass the new object.

### 3. D - Dependency Inversion Principle

**Idea:** high-level logic should depend on abstractions rather than concrete
implementations.

The high-level logic here is `OrderCalculator`. Its constructor accepts
the `Delivery` abstraction, and the calculator calls its `get_cost()` method.
It does not create `StandardDelivery` or `ExpressDelivery` internally.

Instead, `main()` creates the concrete delivery object and passes it to the
calculator. This is constructor dependency injection. The delivery method
can therefore be replaced without changing the calculation code.

In Python, the `delivery: Delivery` type annotation does not enforce a type
check at runtime. The principle is expressed through the code structure:
the calculator uses only the common contract, while the implementation is
chosen outside it.

## Short Presentation Script

> I created MiniShop, a small application that calculates an order total
> including delivery. The two items cost 300 MDL together. The total is
> 330 MDL with standard delivery or 360 MDL with express delivery.
>
> The first principle is SRP: the calculator calculates the total,
> delivery classes define the rates, and main displays the results.
>
> The second principle is OCP: pickup can be added as a separate class
> without changing the calculator.
>
> The third principle is DIP: the calculator depends on the common Delivery
> interface, and the concrete delivery method is provided from outside.
>
> Each component has a focused responsibility, and new delivery methods
> can be added without changing the order calculation.