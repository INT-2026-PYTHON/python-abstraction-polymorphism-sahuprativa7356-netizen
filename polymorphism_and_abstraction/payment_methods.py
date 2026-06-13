"""
## 2. Payment Methods — Duck Typing Polymorphism  *(Medium)*

=================================================
PAYMENT METHODS (DUCK TYPING)
=================================================

Problem Statement:
Build THREE INDEPENDENT classes that do NOT
share a common parent:

   class CreditCard:
       pay(amount)
   class UPI:
       pay(amount)
   class Cash:
       pay(amount)

Even though they have no common base class,
each one has a method named `pay(amount)`.
A single function `checkout(payment_method,
amount)` should work with ALL of them, just by
calling `payment_method.pay(amount)`.

This is DUCK TYPING POLYMORPHISM:
   "If it walks like a duck and quacks like a
    duck, it's a duck."
   If an object has a `pay()` method, the
   function treats it as a payment method.


-------------------------------------------------
Input Example:
methods = [
   CreditCard("Alice", "4111-1111-1111-1111"),
   UPI("bob@upi"),
   Cash("Carol"),
]

for m in methods:
    checkout(m, 500)

Output Example:
[CreditCard] Alice paid 500 via card 4111-1111-1111-1111
[UPI]        bob@upi paid 500
[Cash]       Carol paid 500 in cash

-------------------------------------------------
Explanation:
- `checkout` does not care which CLASS the
  object is, only that the object has a
  `pay()` method.
- This is polymorphism WITHOUT inheritance —
  Python doesn't require a shared base class.
- Adding a new payment method later (e.g.
  PayPal) only requires writing a new class
  with a `pay()` method; `checkout` keeps
  working unchanged.
=================================================

"""
# Independent Class 1
class CreditCard:
    def __init__(self, holder_name, card_number):
        self.holder_name = holder_name
        self.card_number = card_number

    def pay(self, amount):
        print(
            f"[CreditCard] {self.holder_name} paid "
            f"{amount} via card {self.card_number}"
        )


# Independent Class 2
class UPI:
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"[UPI] {self.upi_id} paid {amount}")


# Independent Class 3
class Cash:
    def __init__(self, person_name):
        self.person_name = person_name

    def pay(self, amount):
        print(f"[Cash] {self.person_name} paid {amount} in cash")


# Generic Checkout Function
def checkout(payment_method, amount):
    payment_method.pay(amount)


# Driver Code
methods = [
    CreditCard("Alice", "4111-1111-1111-1111"),
    UPI("bob@upi"),
    Cash("Carol")
]

for method in methods:
    checkout(method, 500)
