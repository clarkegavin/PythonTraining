from Product import Product

class Inventory:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product) # append product objects to the inventory

    def display_inventory(self):
        for product in self.product_list:
            print(product.display())

    def sum_inventory(self):
        total = 0
        for product in self.product_list:
            total += product.get_price()
        return total

