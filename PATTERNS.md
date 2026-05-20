# PATTERNS.md — Design Patterns Log

This file documents every design pattern applied throughout the project: where it was used, why it was chosen, and what was gained.

---

## Phase 1 — Creational Patterns

### Factory Method

**Where:** `src/discounts/discount_factory.py`

**Problem it solved:** Discount objects (`VipDiscount`, `StudentDiscount`, `CouponDiscount`, etc.) were being created inline inside `ShoppingCart` using hardcoded `if-elif` chains. Adding a new discount type required modifying the cart class directly, which violated both SRP and OCP.

**Why Factory Method:** Factory Method moves object creation into a dedicated factory, so the cart no longer needs to know how to build discount objects. New discount types can be added by creating a new class and registering it in the factory — without touching any existing code.

**Why not other Creational patterns:**
- **Abstract Factory** — overkill here; we only have one product family (discounts), not multiple related families.
- **Builder** — Builder is for constructing complex objects step by step. Discount objects are simple; they don't need a multi-step build process.
- **Singleton** — not applicable; we need multiple distinct discount objects, not a single shared instance.

**What was gained:**
- `ShoppingCart` is no longer responsible for creating discount objects
- Adding a new discount type only requires adding a new class — nothing else changes
- Each discount type is independently testable
- The factory acts as the single place where the mapping from user type to discount is defined

**Before UML:**
```
ShoppingCart
├── calculate_total()
│   ├── if user_type == "vip" → total *= 0.80
│   ├── elif user_type == "student" → total *= 0.85
│   └── elif user_type == "employee" → total *= 0.70
```

**After UML:** See `docs/diagrams/phase1_uml.png`

---

## Phase 2 — Structural Patterns

### Decorator

**Where:** `src/cart/cart_decorators.py`

**Problem it solved:** Optional cart features like gift wrapping, shipping insurance, and priority handling were being added directly inside `ShoppingCart` as flags and conditionals, making the class grow uncontrollably every time a new feature was requested.

**Why Decorator:** Decorator allows wrapping a cart object with additional behavior at runtime without modifying the base class. Each optional feature becomes its own wrapper class that adds its cost and behavior on top of the existing cart.

**Why not other Structural patterns:**
- **Adapter** — Adapter is for bridging incompatible interfaces. Our cart and features share the same codebase; there's no interface mismatch to solve.
- **Composite** — Composite is for tree structures where individual objects and groups are treated the same. That doesn't match our use case of layering optional features.

**What was gained:**
- Base `ShoppingCart` stays simple and unchanged
- Features can be combined freely at runtime (e.g. gift wrap + insurance + priority)
- Adding a new feature requires only a new decorator class — nothing else changes
- Each decorator is independently testable

**Before/After UML:** See `docs/diagrams/phase2_decorator_uml.png`

---

### Facade

**Where:** `src/checkout/checkout_facade.py`

**Problem it solved:** The checkout process — calculating total, applying shipping, sending confirmation, logging the order — was scattered across multiple methods and called in different orders from `main.py`. This made the checkout flow fragile, hard to follow, and easy to break by calling steps out of order.

**Why Facade:** Facade provides a single, clean `CheckoutFacade.checkout()` method that orchestrates all the steps internally. The caller doesn't need to know the order or details of the subsystems involved.

**Why not Adapter:** Adapter translates between two incompatible interfaces. Our subsystems (cart, notifier, logger) are not incompatible — they just need to be coordinated. That is exactly what Facade does.

**What was gained:**
- Checkout is now a single method call from the outside
- Internal steps can be reordered or changed without affecting any caller
- Much easier to read, test, and maintain
- `main.py` becomes significantly simpler

**Before/After UML:** See `docs/diagrams/phase2_facade_uml.png`

---

## Phase 3 — Behavioral Patterns

### Strategy

**Where:** `src/discounts/discount_strategy.py`

**Problem it solved:** Even after Phase 1, discount logic was still tied to specific classes registered in the factory. Swapping the entire discount algorithm at runtime (e.g. switching from a loyalty program to a seasonal flash sale) was not possible without modifying existing classes.

**Why Strategy:** Strategy defines a family of interchangeable algorithms, encapsulates each one in its own class, and lets the cart accept any strategy at runtime via dependency injection. This is the cleanest demonstration of the Open/Closed Principle in the project.

**OCP demonstration:** Adding a new discount strategy (e.g. `FlashSaleStrategy`) requires only creating a new class that implements the `DiscountStrategy` interface. No existing class is modified.

**What was gained:**
- Discount logic is fully decoupled from the cart
- New discount strategies can be injected without changing any existing class
- Strategies are individually unit-testable
- The cart can switch strategies at runtime (e.g. based on date or campaign)

**Before/After UML:** See `docs/diagrams/phase3_strategy_uml.png`

---

### Observer

**Where:** `src/notifications/order_notifier.py`

**Problem it solved:** `send_order_confirmation()` lived inside `ShoppingCart` and only supported email. Adding SMS or push notifications meant modifying the cart class — the wrong class entirely. The cart was coupled to every notification channel.

**Why Observer:** Observer lets the cart emit a single event (`order_placed`) and any number of independent listeners (email handler, SMS handler, logging handler) can subscribe and react. The cart knows nothing about who is listening or how many listeners exist.

**What was gained:**
- Cart has zero knowledge of notification channels
- New notification channels are added by creating a new listener class — nothing else changes
- Channels can be added, removed, and tested completely independently
- The system is now genuinely extensible without modifying existing code

**Before/After UML:** See `docs/diagrams/phase3_observer_uml.png`