# AI Log — Phase 2 (Structural Patterns)

## Pattern Selection Discussion

**Prompt sent to AI:**

```
I'm refactoring a Python e-commerce cart. I need to handle two things:

1. Adding optional features to a cart at runtime — things like gift wrapping,
   shipping insurance, and priority handling. Each adds a cost and some behavior.

2. The checkout process has multiple steps (calculate total, apply shipping,
   send confirmation, log the order) that are currently scattered and called
   in different orders from main.py. I want to simplify this.

For problem 1: should I use Decorator, or is there a better structural pattern?
For problem 2: should I use Facade or Adapter? What's the difference here?
```

**AI's answer summary:**

For problem 1, the AI confirmed **Decorator** is the right choice. It explained that Decorator is specifically designed for adding optional behavior to objects at runtime without subclassing. It contrasted with Composite (which is for tree structures) and Strategy (which swaps core algorithms, not adds optional layers).

For problem 2, the AI clearly explained the difference: **Adapter** is for making two incompatible interfaces work together — like wrapping a third-party library so it fits your code. **Facade** is for simplifying a complex set of subsystems into one clean interface. Since my checkout steps are all internal code that already works together, Facade is correct.

**My decision:**
- Decorator for optional cart features — confirmed
- Facade for checkout flow — confirmed
- I rejected Adapter because my subsystems aren't incompatible, they're just uncoordinated

---

## Where the AI Was Wrong or Incomplete

The AI's Decorator example used **inheritance** to stack features — each new feature subclassed the previous one. This is technically a form of the Decorator pattern but it's the wrong implementation. With inheritance-based stacking, you get a combinatorial explosion of subclasses if you want every possible combination of features.

The correct implementation uses **composition**: each decorator holds a reference to the cart object and wraps it. This is what the Gang of Four actually describe and what makes the pattern useful.

I pointed this out to the AI and it agreed it had shown a simplified example. I implemented the composition-based version.

**What I did differently:**
- Used composition (`self._cart = cart`) in every decorator instead of inheritance
- This means any combination of decorators works without creating new subclasses

---

## Code Review

**Prompt:**
```
Here is my Phase 2 implementation with Decorator for cart features and
Facade for checkout. Did I apply them correctly? What would you change?

[CODE PASTED HERE]
```

**AI's feedback summary:**
- Confirmed Decorator was implemented correctly using composition
- Confirmed Facade correctly hid the subsystem details
- Suggested adding a `__repr__` method to each decorator so the cart's state is readable when printed — useful for debugging
- Suggested the Facade could accept a list of notifiers instead of having email hardcoded — this would make it more flexible

**What I kept:**
- Added `__repr__` to decorators — good suggestion, very practical

**What I changed:**
- Made the Facade accept a list of notifiers so it's not hardcoded to email only — this also set up Phase 3 nicely for the Observer pattern