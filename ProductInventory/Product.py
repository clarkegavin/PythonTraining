class Product:
    def __init__(self, id_, name, price, quantity):
        self.id_ = id_
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"ID {self.id_} | Product {self.name} | Price {self.price:,.2f} | Quantity {self.quantity}"

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

