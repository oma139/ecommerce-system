from product import Product
from datetime import date

class ExpiringProduct(Product):
    def __init__(self, name, price, quantity, expiry_date, weight):
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date
        self.weight = weight

    def is_expired(self):
        return date.today() > self.expiry_date

    def requires_shipping(self):
        return self.weight > 0