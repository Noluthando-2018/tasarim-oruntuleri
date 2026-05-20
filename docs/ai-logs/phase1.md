# AI Log — Phase 1 (Creational Patterns)

## Prompt I Sent to the AI

```
I'm refactoring a Python e-commerce cart. The ShoppingCart class currently
creates discount objects inline using a long if-elif chain. I want to apply
a Creational design pattern to fix this. Which pattern is most appropriate
here — Factory Method, Abstract Factory, or Builder? Explain the difference
in this context and show me how to structure the solution.
```

---

## What the AI Answered

The AI recommended **Factory Method** as the most appropriate choice for this case. It explained:

- **Factory Method** fits because we have a single product type (discount objects) that varies by subtype. The factory decides which concrete discount class to instantiate based on the user type.
- **Abstract Factory** would be appropriate if we had multiple related product families (e.g. discounts AND shipping calculators AND notification types all created together). That's more than we need right now.
- **Builder** would only make sense if creating a discount object required multiple configuration steps. Our discount objects are simple — they just need to know a rate.

The AI then showed a basic example structure with a `DiscountFactory` class and a `create_discount(user_type)` method returning concrete discount objects like `VipDiscount`, `StudentDiscount`, etc.

---

## What I Actually Implemented and Why

I followed the Factory Method approach the AI suggested, but I made two deliberate changes:

1. **I used a registry dictionary instead of if-elif inside the factory.** The AI's example still had an `if-elif` chain inside the factory method. That defeats part of the purpose — if I add a new discount type, I still have to edit the factory. I replaced it with a `dict` mapping user types to classes, so adding a new type only means adding one line to the registry.

2. **I added an `Enum` for user types** based on the AI's earlier suggestion in Phase 0. This means passing an invalid user type now raises an error immediately instead of silently returning no discount.

I wrote the code myself from scratch after understanding the pattern — I did not copy the AI's example directly.

---

## AI Code Review

**Prompt:**
```
Here is my Phase 1 implementation of the Factory Method pattern for
discount creation in Python. Please review it for:
- Correctness of the pattern
- Naming and code structure
- Anything that would be a problem in a real project

[CODE PASTED HERE]
```

**AI's feedback summary:**

- Confirmed the pattern was applied correctly
- Praised the use of a registry dictionary over if-elif
- Suggested renaming `create_discount` to `get_discount` to better reflect that it's a lookup, not construction from scratch — I agreed and changed it
- Suggested adding a fallback for unknown user types that raises a descriptive `ValueError` — I implemented this

**What I changed based on the review:**
- Renamed `create_discount` → `get_discount`
- Added `ValueError` for unrecognized user types with a clear message

**What I kept as-is:**
- My Enum approach — the AI suggested a plain string check instead, but I kept Enum because it provides compile-time safety and makes the valid options self-documenting