class Product:
    def __init__(self, id_, name, price, quantity):
        self._id_ = id_
        self._name = name
        self._price = price
        self._quantity = quantity

# The @property is only really needed when we want to modify how an existing attribute is 'calculated'
# prior to that we can and should just access the attribute directly from the calling object

    @property
    def price(self):
        """The price property"""
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def quantity(self):
        """The quantity property"""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @quantity.deleter
    def quantity(self):
        del self._quantity

    def display(self):
        return f"ID {self._id_} | Product {self._name} | Price {self._price:,.2f} | Quantity {self._quantity}"
