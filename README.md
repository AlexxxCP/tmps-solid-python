# TMPS Laboratory Report 1: Creational Design Patterns

## Student Information

| Field | Details |
| --- | --- |
| Student | Luchiciov Alexei |
| Group | FAF-241 |
| Course | Software Design Techniques and Mechanisms (TMPS) |
| Laboratory work | 1 |
| Topic | Creational Design Patterns |
| Project | MiniShop |
| Programming language | Python |

The English course title follows the [official UTM Software Engineering curriculum, page 5](https://fcim.utm.md/wp-content/uploads/sites/24/2023/08/inginerie-software.pdf#page=5).

## Relation to Laboratory 0

This laboratory continues the MiniShop project from Laboratory 0.
The earlier report, which describes the SOLID principles, is available in
[LAB0_SOLID_REPORT.md](LAB0_SOLID_REPORT.md). This laboratory keeps the same
store, item prices, and delivery options and demonstrates three creational
design patterns.

## Objective

Extend MiniShop with three creational design patterns:

1. **Builder** to assemble an order step by step.
2. **Factory Method** to create standard, express, and pickup deliveries.
3. **Prototype** to copy an existing order and adapt the copy.

The report also briefly explains the other creational patterns named in
the assignment.

## Technologies

- Python 3.9 or later.
- Python standard library: `abc` for abstract base classes, `copy.deepcopy()`
  for cloning an order, and `typing.Optional` for the builder's delivery.
- Console application.
- Git and GitHub for version control and publication.

No external Python packages are required.

## Application Description

MiniShop calculates the total price of two items, priced at 100 and 200 MDL,
with standard delivery, express delivery, or free pickup. It prints the totals
for all three options. The sample order uses the same two items in each case.

| Delivery option | Item subtotal | Delivery cost | Order total |
| --- | ---: | ---: | ---: |
| Standard delivery | 300 MDL | 30 MDL | 330 MDL |
| Express delivery | 300 MDL | 60 MDL | 360 MDL |
| Free pickup | 300 MDL | 0 MDL | 300 MDL |

The calculation is:

```text
Order total = sum of item prices + delivery cost
```

The prices are predefined in `main()`. The program automatically demonstrates
each option; it does not provide an interactive menu, database, payment
processing, or delivery-time calculations. All amounts are whole Moldovan
lei (MDL).

## Project Structure

- [main.py](main.py) contains the application and all three design patterns.
- [README.md](README.md) is the report for Laboratory 1.
- [LAB0_SOLID_REPORT.md](LAB0_SOLID_REPORT.md) preserves the report for Laboratory 0.
- [.gitignore](.gitignore) excludes `Example/`, Python cache files, virtual
  environments, and local settings.

| Component | Responsibility |
| --- | --- |
| `Delivery` | Defines the common type and `get_cost()` operation. |
| `StandardDelivery`, `ExpressDelivery`, `PickupDelivery` | Provide their delivery costs. |
| `DeliveryFactory` | Declares the `create_delivery()` factory method. |
| Concrete delivery factories | Create one specific delivery type each. |
| `Order` | Stores order items and delivery, calculates the total, and can be cloned. |
| `OrderBuilder` | Collects item prices and a delivery, then builds an `Order`. |
| `build_order()` | Uses a builder and a delivery factory to create an order. |
| `main()` | Demonstrates and prints each delivery option and the prototype copy. |

## How the Application Works

1. `main()` sets the item prices to 100 and 200 MDL.
2. It passes a concrete delivery factory to `build_order()`.
3. The builder adds the items, gets a delivery from the factory, and builds
   an `Order`.
4. The standard order is cloned to create another order. The clone's delivery
   is changed to express delivery; the original order keeps its standard delivery.
5. A separate builder creates the free-pickup order.
6. The program prints the total for each order and shows the original and
   cloned totals.

## Implemented Creational Design Patterns

### 1. Builder

**Purpose:** construct a complex object step by step.

`OrderBuilder` collects item prices using `add_item()`, accepts a delivery
using `set_delivery()`, and creates the finished order using `build()`.
The helper `build_order()` shows these steps:

```python
builder = OrderBuilder()
builder.add_item(100)
builder.add_item(200)
builder.set_delivery(factory.create_delivery())
order = builder.build()
```

This makes it clear which parts make up the order before the complete
`Order` object is created.

### 2. Factory Method

**Purpose:** let a creator's subclass decide which concrete product to create.

`DeliveryFactory` declares the `create_delivery()` method. Its concrete
subclasses, such as `StandardDeliveryFactory`, `ExpressDeliveryFactory`,
and `PickupDeliveryFactory`, each return one matching `Delivery` object.

`build_order()` accepts the abstract `DeliveryFactory` type and calls
`create_delivery()`. The helper does not need to know how that delivery
object is constructed. This is the Factory Method pattern: each concrete
factory implements the creation method for its delivery option.

### 3. Prototype

**Purpose:** create a new object by copying an existing one.

`Order.clone()` uses Python's `deepcopy()` to copy an order, including its
item list and delivery object. In `main()`, the program clones the standard
order, then changes only the cloned order's delivery to express delivery.

The original order stays standard, while the copy becomes express. The
prototype output shows both totals. Cloning is useful when a new order should
start with the same data as an existing order.

## Other Creational Patterns

The assignment asks students to know the other patterns as well.

| Pattern | Basic idea |
| --- | --- |
| **Singleton** | Provides one shared instance of a class. |
| **Abstract Factory** | Creates families of related objects through a common factory. |
| **Object Pool** | Reuses a managed group of objects, often when creating them is expensive. This pattern is optional in the assignment. |

The MiniShop does not need those patterns for this small example, so they are
described here but are not part of the implementation.

## Running the Application

From the repository root, run:

```powershell
python main.py
```

Python 3.9 or later is required. No additional packages are needed.

## Expected Output

```text
MiniShop: order builder demo
Items: 100 + 200 = 300 MDL

Standard delivery: total 330 MDL
Express delivery: total 360 MDL
Free pickup: total 300 MDL

Prototype example:
Original standard order: 330 MDL
Cloned order with express delivery: 360 MDL
```

## Conclusion

MiniShop continues the Laboratory 0 project with three creational patterns.
Builder assembles an order in steps, Factory Method creates the selected
delivery type, and Prototype copies an order that can then be adapted.
The program retains its original items and standard, express, and pickup
options.

## References

1. [Technical University of Moldova: Software Engineering curriculum](https://fcim.utm.md/wp-content/uploads/sites/24/2023/08/inginerie-software.pdf#page=5) - official English course title.
2. [Python documentation: Abstract Base Classes](https://docs.python.org/3.13/library/abc.html) - `ABC` and `abstractmethod`.
3. [Python documentation: copy](https://docs.python.org/3.13/library/copy.html) - `deepcopy()`.
