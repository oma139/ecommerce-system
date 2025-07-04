from cart_item import CartItem
from shippable import Shippable
import shipping_service

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.is_expired():
            print(f"{product.name} is expired.")
            return
        if quantity > product.quantity:
            print(f"Not enough stock for {product.name}")
            return
        self.cart.append(CartItem(product, quantity))

    def checkout(self):
        if not self.cart:
            print("Cart is empty!")
            return

        subtotal = 0
        shipping_fees = 0
        shippable_items = []

        for item in self.cart:
            subtotal += item.get_total_price()
            if item.product.requires_shipping():
                shippable_items.append(Shippable(item.product.name, item.product.weight))
                shipping_fees += item.product.weight * 10

        total = subtotal + shipping_fees
        if self.balance < total:
            print("Insufficient balance.")
            return

        for item in self.cart:
            item.product.quantity -= item.quantity

        self.balance -= total
        print("=== Checkout Summary ===")
        print(f"Subtotal: {subtotal}")
        print(f"Shipping: {shipping_fees}")
        print(f"Total Paid: {total}")
        print(f"Remaining Balance: {self.balance}")

        if shippable_items:
            shipping_service.ship(shippable_items)

        self.cart.clear()