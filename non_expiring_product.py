from product import Product

class NonExpiringProduct(Product):
    def __init__(self, name, price, quantity, weight):
        super().__init__(name, price, quantity)
        self.weight = weight

    def is_expired(self):
        return False

    def requires_shipping(self):
        return self.weight > 0