# AI Log — Phase 3 (Behavioral Patterns)

## Pair Programming Session

**Duration:** ~40 minutes
**AI Tool Used:** Claude (claude.ai)

---

## What We Discussed

The session focused on two problems: making discount rules fully interchangeable at runtime (Strategy), and decoupling the cart from its notification channels (Observer).

We started with Strategy. I already had a Factory Method from Phase 1, so I needed to understand the difference — the AI explained it clearly: Factory Method is about *creating* the right object, Strategy is about *swapping the algorithm* the object uses at runtime. They solve different problems and can coexist. That cleared up my confusion.

For Observer, I asked about the difference between push and pull models. In the push model, the subject sends event data directly to observers. In the pull model, observers are just notified that something happened and they fetch the data themselves. The AI recommended push for my use case since the order data is small and well-defined — I agreed.

We finished with a discussion about where exactly the Open/Closed Principle is demonstrated. The AI helped me identify the Strategy pattern as the clearest example: adding a `FlashSaleStrategy` requires only a new class, nothing existing is modified.

---

## Prompts Used in This Session

**Prompt 1:**
```
I already have a Factory Method for creating discount objects in Phase 1.
Now I want to apply Strategy so that the discount algorithm itself is
interchangeable at runtime. What's the difference between these two patterns
in my context, and can they coexist?
```

**AI answer summary:**
Factory Method solves *which object to create*. Strategy solves *which algorithm to run*. They can coexist: the factory creates a strategy object, and the cart runs it. The AI showed me how to define a `DiscountStrategy` abstract base class with an `apply(total)` method, and concrete implementations like `VipDiscountStrategy` and `FlashSaleStrategy`.

---

**Prompt 2:**
```
I want to use Observer so the cart can emit an "order placed" event and
multiple listeners (email, SMS, logging) can react without the cart knowing
about them. Should I use a push or pull model? Show me how to structure
the Subject and Observer interfaces in Python.
```

**AI answer summary:**
The AI recommended the push model for simplicity. It showed an `OrderEventPublisher` class with `subscribe()`, `unsubscribe()`, and `notify()` methods, and an `OrderObserver` abstract base class with a `on_order_placed(order_data)` method. Concrete observers like `EmailNotifier` and `SMSNotifier` implement the interface independently.

---

**Prompt 3:**
```
Where exactly is the Open/Closed Principle demonstrated in my Phase 3 code?
I need to be able to point to a specific, concrete example for my documentation.
```

**AI answer summary:**
The AI pointed to the Strategy pattern as the clearest OCP example: the `ShoppingCart` accepts any `DiscountStrategy` and calls `apply()` on it. To add a new discount algorithm, you create a new class implementing `DiscountStrategy` — no existing class is touched. It also noted that the Observer pattern demonstrates OCP for notifications: adding a new channel means adding a new `OrderObserver` subclass, nothing else changes.

---

## How Long Would This Phase Have Taken Without AI?

Without AI, this phase would have taken roughly 3–4 hours instead of about 1.5 hours. The biggest time save was the Strategy vs Factory Method clarification — I was genuinely confused about whether I needed both, and getting that explained clearly in a few exchanges saved probably an hour of reading documentation and second-guessing.

The push vs pull Observer discussion also saved time — I would have read multiple articles and still been unsure which to use.

---

## Where the AI Misled Me

When I asked the AI to show me a Strategy implementation, it suggested making `ShoppingCart` inherit from an abstract `Discountable` base class and override a `calculate_discount()` method. This is not Strategy — that's Template Method. Strategy uses *composition* (the cart holds a reference to a strategy object). Template Method uses *inheritance* (a subclass overrides a step in a parent's algorithm).

I caught this because I had read the pattern descriptions on refactoring.guru. I told the AI and it corrected itself. This is a good example of why you shouldn't copy AI code without understanding what pattern you're actually implementing.

**What I did:** Implemented Strategy using composition — `self._discount_strategy = strategy` in the cart constructor, called as `self._discount_strategy.apply(total)`.

---

## Final Code Review

**Prompt:**
```
This is my complete Phase 3 implementation with Strategy and Observer patterns.
Please review the full codebase for correctness, naming, structure, and
anything that would be a problem in a real production project.

[FULL CODE PASTED HERE]
```

**AI's feedback:**
- Strategy and Observer both implemented correctly using composition
- Suggested adding type hints throughout for clarity — I added them
- Suggested the `OrderEventPublisher` should be injected into the cart rather than created inside it, to make the cart easier to test in isolation — I agreed and refactored this
- Noted that my `SMSNotifier` was a stub with no real implementation, which is fine for this project

**What I changed:**
- Added type hints across all Phase 3 files
- Injected `OrderEventPublisher` into the cart via the constructor instead of creating it internally

**What I kept:**
- SMSNotifier as a stub — the assignment doesn't require real SMS sending, just demonstrating the pattern
