from Product import Product
from Inventory import Inventory

def main() -> object:
    p1 = Product(1, "Product A", 12.50, 200)
    p2 = Product(2, "Product B", 1003.50, 100)
    p3 = Product(3, "Product C", 84.50, 13)

    print("Products Created")
    inventory = Inventory()
    print("Inventory Created")
    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)

    inventory.display_inventory()
    print(f"Total inventory price: €{inventory.sum_inventory():,.2f}")

    p1.price = 100.20
    p1.quantity = 199
    inventory.display_inventory()
    print(f"Total inventory price: €{inventory.sum_inventory():,.2f}")


if __name__ == "__main__":
    main()
