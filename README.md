# 🏗️ Evolving System — E-Commerce Cart

**Topic Choice: D — E-Commerce Shopping Cart**

I chose this topic because shopping cart logic is one of the most common structures in real-world web projects. Features like discount rules, notifications, and checkout flows make it easy to see concretely why design patterns are necessary. It also directly aligns with my interests in web development and software engineering.

---

## What Is This Project?

This project documents the process of refactoring an intentionally poorly written e-commerce cart system using design patterns across three phases. Each phase applies one or more patterns to solve a real, identified problem in the codebase.

---

## Design Patterns Used

| Phase | Pattern | Category | Where Applied |
|-------|---------|----------|---------------|
| Phase 1 | Factory Method | Creational | Creating discount objects |
| Phase 2 | Decorator | Structural | Layering cart features (gift wrap, insurance, etc.) |
| Phase 2 | Facade | Structural | Unifying the checkout flow into a single interface |
| Phase 3 | Strategy | Behavioral | Making discount rules interchangeable |
| Phase 3 | Observer | Behavioral | Managing order confirmation notifications |

---

## Architecture Diagram

### Phase 0 — Before (Bad Code)

```mermaid
classDiagram
    class ShoppingCart {
        -user_type: str
        -items: list
        -coupon_code: str
        -log_history: list
        +add_item(name, price, quantity, category)
        +remove_item(name)
        +apply_coupon(code)
        +calculate_total() float
        +get_shipping_cost() float
        +send_order_confirmation(email)
        +print_receipt()
        +get_log() list
    }
    note for ShoppingCart "❌ God Class: handles items, discounts,\nshipping, notifications, and logging\nall in one place"
```

---

### Phase 1 — Factory Method (Creational)

```mermaid
classDiagram
    class ShoppingCart {
        -items: list
        -discount_strategy: DiscountStrategy
        +add_item()
        +calculate_total() float
    }

    class DiscountFactory {
        -_registry: dict
        +get_discount(user_type: UserType) DiscountStrategy
    }

    class DiscountStrategy {
        <<abstract>>
        +apply(total: float) float
    }

    class VipDiscount {
        +apply(total: float) float
    }

    class StudentDiscount {
        +apply(total: float) float
    }

    class EmployeeDiscount {
        +apply(total: float) float
    }

    class NoDiscount {
        +apply(total: float) float
    }

    class UserType {
        <<enumeration>>
        VIP
        STUDENT
        EMPLOYEE
    }

    ShoppingCart --> DiscountFactory : uses
    DiscountFactory --> DiscountStrategy : creates
    DiscountStrategy <|-- VipDiscount
    DiscountStrategy <|-- StudentDiscount
    DiscountStrategy <|-- EmployeeDiscount
    DiscountStrategy <|-- NoDiscount
    DiscountFactory --> UserType : accepts
```

---

### Phase 2 — Decorator + Facade (Structural)

```mermaid
classDiagram
    class CartBase {
        <<abstract>>
        +get_total() float
        +get_description() str
    }

    class ShoppingCart {
        +get_total() float
        +get_description() str
    }

    class CartDecorator {
        <<abstract>>
        -_cart: CartBase
        +get_total() float
        +get_description() str
    }

    class GiftWrapDecorator {
        +get_total() float
        +get_description() str
    }

    class InsuranceDecorator {
        +get_total() float
        +get_description() str
    }

    class PriorityShippingDecorator {
        +get_total() float
        +get_description() str
    }

    class CheckoutFacade {
        -_cart: CartBase
        -_notifiers: list
        +checkout(email: str)
    }

    class ShippingCalculator {
        +calculate(total: float) float
    }

    class OrderLogger {
        +log(order_data: dict)
    }

    CartBase <|-- ShoppingCart
    CartBase <|-- CartDecorator
    CartDecorator <|-- GiftWrapDecorator
    CartDecorator <|-- InsuranceDecorator
    CartDecorator <|-- PriorityShippingDecorator
    CartDecorator o-- CartBase : wraps

    CheckoutFacade --> CartBase : uses
    CheckoutFacade --> ShippingCalculator : uses
    CheckoutFacade --> OrderLogger : uses
```

---

### Phase 3 — Strategy + Observer (Behavioral)

```mermaid
classDiagram
    class ShoppingCart {
        -_discount_strategy: DiscountStrategy
        -_event_publisher: OrderEventPublisher
        +set_strategy(strategy: DiscountStrategy)
        +place_order()
        +calculate_total() float
    }

    class DiscountStrategy {
        <<abstract>>
        +apply(total: float) float
    }

    class VipDiscountStrategy {
        +apply(total: float) float
    }

    class FlashSaleStrategy {
        +apply(total: float) float
    }

    class LoyaltyPointsStrategy {
        +apply(total: float) float
    }

    class OrderEventPublisher {
        -_observers: list
        +subscribe(observer: OrderObserver)
        +unsubscribe(observer: OrderObserver)
        +notify(order_data: dict)
    }

    class OrderObserver {
        <<abstract>>
        +on_order_placed(order_data: dict)
    }

    class EmailNotifier {
        +on_order_placed(order_data: dict)
    }

    class SMSNotifier {
        +on_order_placed(order_data: dict)
    }

    class OrderLogger {
        +on_order_placed(order_data: dict)
    }

    ShoppingCart --> DiscountStrategy : uses
    DiscountStrategy <|-- VipDiscountStrategy
    DiscountStrategy <|-- FlashSaleStrategy
    DiscountStrategy <|-- LoyaltyPointsStrategy

    ShoppingCart --> OrderEventPublisher : uses
    OrderEventPublisher --> OrderObserver : notifies
    OrderObserver <|-- EmailNotifier
    OrderObserver <|-- SMSNotifier
    OrderObserver <|-- OrderLogger
```

---

## How to Run

Requires Python 3.

```bash
# Clone the repository
git clone https://github.com/Noluthando-2018/tasarim-oruntuleri.git
cd tasarim-oruntuleri

# Run the project
python -m src/main.py
```

---

## Branch Structure

```
main      → clean, final merged state
phase-1   → Creational pattern work
phase-2   → Structural pattern work (branched from phase-1)
phase-3   → Behavioral pattern work (branched from phase-2)
```

---

## Project Structure

```
tasarim-oruntuleri/
├── README.md
├── PROBLEMS.md
├── PATTERNS.md
├── src/
│   ├── shopping_cart.py
│   └── main.py
└── docs/
    ├── diagrams/
    └── ai-log/
        ├── phase1.md
        ├── phase2.md
        └── phase3.md
```
