class Shippable:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def get_name(self):
        return self._name

    def get_weight(self):
        return self._weight