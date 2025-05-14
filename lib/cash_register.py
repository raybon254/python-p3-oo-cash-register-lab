#!/usr/bin/env python3

class CashRegister:
   def __init__(self, discount=0):
        self.items = []
        self.total = 0
        self.discount = discount
        self.last_transaction_amount = 0

   def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title) 
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction_amount = transaction_amount



   def apply_discount(self):
        if self.discount > 0:
          discount_amount = self.total * (self.discount / 100)
          self.total -= discount_amount
          discounted_total = int(self.total) if self.total == int(self.total) else round(self.total, 2)
          print(f"After the discount, the total comes to ${discounted_total}.")
        else:
          print("There is no discount to apply.")



   def void_last_transaction(self):
      self.total -= self.last_transaction_amount
      self.last_transaction_amount = 0



   def items(self):
        return self.items