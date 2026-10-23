# TMPS Laboratory Report: SOLID Principles

## Student Information

| Field | Details |
| --- | --- |
| Student | Luchiciov Alexei |
| Group | FAF-241 |
| Course | Software Design Techniques and Mechanisms (TMPS) |
| Topic | Application of Three SOLID Principles |
| Project | MiniShop |
| Programming language | Python |

The English course title follows the [official UTM Software Engineering curriculum, page 5](https://fcim.utm.md/wp-content/uploads/sites/24/2023/08/inginerie-software.pdf#page=5).

## Objective

Develop a small object-oriented application and demonstrate three SOLID
principles: Single Responsibility (SRP), Open/Closed (OCP), and Dependency
Inversion (DIP). Explain where each principle appears in the implementation.

## Technologies

- Python 3.9 or later.
- Python standard library: `abc` for abstract base classes.
- Console interface.
- Git and GitHub for version control and publication.

No external libraries or installation of dependencies are required.

## Application Description

MiniShop calculates the total cost of an order with standard delivery,
express delivery, or free pickup.

Two predefined items cost 100 and 200 MDL. Their combined price is 300 MDL.
The application calculates and displays all three options automatically.

| Option | Item subtotal | Delivery cost | Order total |
| --- | ---: | ---: | ---: |
| Standard delivery | 300 MDL | 30 MDL | 330 MDL |
| Express delivery | 300 MDL | 60 MDL | 360 MDL |
| Free pickup | 300 MDL | 0 MDL | 300 MDL |

The calculation is:

```text
Order total = sum of item prices + delivery cost
```

All amounts are whole Moldovan lei (MDL). Prices are stored in the `prices`
list inside `main()`. This is a fixed demonstration without interactive
selection, a database, or payment processing. Delivery times are not calculated.

## Project Structure

- [main.py](main.py) contains the complete application and short SOLID comments.
- [README.md](README.md) contains this laboratory report.
- [.gitignore](.gitignore) excludes `Example/`, Python cache files, virtual
  environments, and local settings.

| Component | Responsibility |
| --- | --- |
| `Delivery` | Defines the common `get_cost()` operation for delivery options. |
| `StandardDelivery` | Returns the standard delivery cost: 30 MDL. |
| `ExpressDelivery` | Returns the express delivery cost: 60 MDL. |
| `PickupDelivery` | Returns the pickup cost: 0 MDL. |
| `OrderCalculator` | Adds the item prices and the supplied delivery cost. |
| `main()` | Creates the objects, runs the demonstration, and prints results. |

`Delivery` is an abstract base class. Its `get_cost()` method is marked with
`@abstractmethod`, so concrete subclasses must implement that method before
they can be instantiated.

## How the Application Works

1. `main()` creates the item price list: `[100, 200]`.
2. It creates standard delivery, express delivery, and pickup objects.
3. Each delivery object is passed to an `OrderCalculator`.
4. The calculator sums the item prices and calls the object's `get_cost()`.
5. `main()` prints the resulting total for each option.

## Application of SOLID Principles

SOLID contains five object-oriented design principles. This report focuses
on the three selected for the implementation.

### S - Single Responsibility Principle (SRP)

**Meaning:** a class should have one responsibility and one reason to change.

`OrderCalculator` handles the order calculation. Delivery classes define their
own costs, while console output is kept in `main()`.

For example, changing the standard delivery rate requires updating
`StandardDelivery`. Changing the output format affects `main()`.
Neither change requires modifying the calculation formula.

The calculator's calculation method is:

```python
def calculate_total(self, prices: list[int]) -> int:
    return sum(prices) + self.delivery.get_cost()
```

### O - Open/Closed Principle (OCP)

**Meaning:** a component should be open for extension but closed for modification.

Free pickup was added as a new class:

```python
class PickupDelivery(Delivery):
    def get_cost(self) -> int:
        return 0
```

The new option was included in the delivery list in `main()`.
The implementation of `OrderCalculator` remained unchanged: it already calls
`get_cost()` on the supplied delivery object.

Returning `0` makes pickup free. Adding the new option without modifying the
calculator demonstrates OCP. Another delivery option can be added in the same way.

### D - Dependency Inversion Principle (DIP)

**Meaning:** high-level logic should depend on abstractions rather than
concrete implementations.

The high-level calculation logic depends on `Delivery`, which defines the
common `get_cost()` operation. The calculator receives its delivery through
the constructor:

```python
def __init__(self, delivery: Delivery):
    self.delivery = delivery
```

`main()` creates the concrete delivery objects and passes each one to the
calculator:

```python
calculator = OrderCalculator(delivery)
```

The calculator uses the shared operation to obtain the delivery cost.
It does not create or select a specific delivery class internally.

The type annotation documents the expected abstraction; it does not enforce
runtime type checking. DIP is demonstrated by the common delivery interface
and the separation between object creation and calculation.

## Running the Application

From the repository root, run:

```powershell
python main.py
```

## Execution Results

```text
MiniShop: order total calculator
Items: 100 + 200 = 300 MDL

Standard delivery (30 MDL): total 330 MDL
Express delivery (60 MDL): total 360 MDL
Free pickup (0 MDL): total 300 MDL
```

## Verification

The application was executed using `python main.py`. It completed successfully,
and all three totals matched the expected results:

| Case | Expected result | Observed result |
| --- | ---: | ---: |
| Standard delivery | 330 MDL | 330 MDL |
| Express delivery | 360 MDL | 360 MDL |
| Free pickup | 300 MDL | 300 MDL |

The console output also matches the example in this report.

## Conclusion

MiniShop demonstrates three SOLID principles in a small Python application.
SRP separates delivery costs, calculation, and output. OCP is demonstrated by
adding free pickup without changing the calculator. DIP allows the calculator
to use the common `Delivery` abstraction while `main()` supplies concrete objects.

## Short Presentation Script

> My project is MiniShop, a small order total calculator. It adds item prices
> and the cost of standard delivery, express delivery, or free pickup.
>
> I used three SOLID principles. SRP gives each part its own job:
> delivery classes provide costs, the calculator calculates the total,
> and main prints the results.
>
> OCP is demonstrated by adding PickupDelivery without changing OrderCalculator.
>
> DIP means that the calculator uses the common Delivery interface.
> Main creates a delivery object and passes it to the calculator, which calls
> get_cost() to obtain its cost.

## References

1. [Technical University of Moldova: Software Engineering curriculum](https://fcim.utm.md/wp-content/uploads/sites/24/2023/08/inginerie-software.pdf#page=5) - official English course title.
2. [Python documentation: Abstract Base Classes](https://docs.python.org/3.13/library/abc.html) - `ABC` and `abstractmethod`.