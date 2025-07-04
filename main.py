from datetime import date
from expiring_product import ExpiringProduct
from non_expiring_product import NonExpiringProduct
from customer import Customer

cheese = ExpiringProduct("Cheese", 50, 10, date(2025, 7, 10), 1.5)
tv = NonExpiringProduct("TV", 10000, 5, 15)
card = NonExpiringProduct("Mobile Scratch Card", 100, 100, 0)

c = Customer("Omar", 12000)

c.add_to_cart(cheese, 2)
c.add_to_cart(tv, 1)
c.add_to_cart(card, 3)

c.checkout()