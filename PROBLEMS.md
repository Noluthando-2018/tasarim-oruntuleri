# PROBLEMS.md — Phase 0 Design Problems

## Section 1: Identified Problems

### Problem 1: God Class
The `ShoppingCart` class handles completely unrelated responsibilities all by itself: managing items, calculating discounts, calculating shipping, sending notifications, and keeping a log. This directly violates the Single Responsibility Principle (SRP). Changing or testing any one feature forces you to deal with the entire class.

### Problem 2: Magic Strings for User Type
The `user_type` parameter is passed as a raw string: `"vip"`, `"student"`, `"employee"`. If a typo is made (e.g. `"stuednt"`), the system continues running silently — the user simply gets no discount with no error raised. There is no validation or type safety whatsoever.

### Problem 3: Hardcoded Discount Logic (Open/Closed Principle Violation)
The `if-elif` chain inside `calculate_total()` embeds discount rules directly in the code. Adding a new user type (e.g. `"senior"`) or a new coupon requires modifying existing, working code. This violates the Open/Closed Principle: a class should be open for extension but closed for modification.

### Problem 4: Category Discount Buried in the Wrong Place
The electronics category discount is hidden inside `calculate_total()` even though it is an independent business rule. It is mixed into the total calculation logic, making it invisible, hard to test in isolation, and risky to remove or change without breaking other things.

### Problem 5: Duplicated Subtotal Calculation (DRY Violation)
Both `calculate_total()` and `get_shipping_cost()` independently recalculate the raw subtotal from scratch. These two places do the same work without knowing about each other. If one is updated and the other is not, calculations will silently diverge.

### Problem 6: Notification Logic Inside the Cart Class
`send_order_confirmation()` has no business being inside a shopping cart class. It currently sends email; if SMS is added tomorrow and push notifications the day after, this method will keep growing forever. Notification handling is a completely separate responsibility.

---

## Section 2: AI Comparison

### Prompt I Sent to the AI

```
Review the following Python code from a software design perspective.
What design problems do you see? For each problem, explain in 1-2
sentences why it is a problem.

[CODE WAS PASTED HERE]
```

### What the AI Found

The AI identified the following problems:

1. **Single Responsibility Principle violation** — it noted that the class handles too many concerns and should be split into smaller, focused classes.
2. **Hardcoded conditionals for discounts** — it flagged the `if-elif` chain and suggested that adding new discount types would require modifying the class, violating OCP.
3. **Magic strings** — it pointed out that raw strings for `user_type` are error-prone and suggested using an `Enum` instead.
4. **Duplicate logic** — it noticed that the subtotal was being calculated in two different methods independently.
5. **Notification inside cart** — it flagged `send_order_confirmation()` as misplaced and suggested a separate notification service.

The AI did not identify Problem 4 (the category discount being buried inside `calculate_total()`). It treated the electronics discount as part of the general discount problem rather than calling it out as a separate structural issue.

### Differences From My List

- The AI found largely the same problems I did, which gave me confidence my analysis was correct.
- I caught Problem 4 (category discount buried in total calculation) which the AI lumped together with Problem 3. I think they are distinct: one is about user-type discounts, the other is about category-based rules — they would be solved by different mechanisms.
- The AI additionally suggested using Python `Enum` for `user_type`, which I hadn't explicitly written down but agree with. I'll apply this in Phase 1.

### Conclusion

The AI was a useful sanity check — it confirmed most of my findings independently. However, it grouped related problems together rather than treating them as separate issues, which means it would have produced a shorter and less precise `PROBLEMS.md` than I did. It's better at spotting well-known violations (SRP, OCP) than at identifying subtler structural issues like the buried category logic.