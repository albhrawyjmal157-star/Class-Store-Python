
import os
import time

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

# ---------- Class Product ----------
class Product:
    def __init__(self, product_id, name, quantity, price):
        self.id = product_id
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)

# ---------- Class Store ----------
class Store:
    def __init__(self):
        self.products = []

    # ---------- Helper Functions ----------
    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    # ---------- Main Functions ----------
    def add_product(self):
        product_id = input("Enter ID: ")
        if self.find_product_by_id(product_id):
            print("Product already exists ⛔")
            return
        name = input("Enter Name: ")
        quantity = input("Enter Quantity: ")
        price = input("Enter Price: ")
        product = Product(product_id, name, quantity, price)
        self.products.append(product)
        print("Product added successfully ✅")

    def delete_product(self):
        product_id = input("Enter ID to delete: ")
        product = self.find_product_by_id(product_id)
        if product:
            self.products.remove(product)
            print("Product deleted successfully 🗑️")
        else:
            print("Product not found ⛔")

    def update_product(self):
        product_id = input("Enter ID to update: ")
        product = self.find_product_by_id(product_id)
        if not product:
            print("Product not found ⛔")
            return

        print("1 - Update ID")
        print("2 - Update Name")
        print("3 - Update Quantity")
        print("4 - Update Price")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Only numbers allowed ⛔")
            return

        if choice == 1:
            new_id = input("Enter new ID: ")
            product.id = new_id
        elif choice == 2:
            new_name = input("Enter new Name: ")
            product.name = new_name
        elif choice == 3:
            new_quantity = int(input("Enter new Quantity: "))
            product.quantity = new_quantity
        elif choice == 4:
            new_price = float(input("Enter new Price: "))
            product.price = new_price
        else:
            print("Invalid choice ⛔")
            return
        print("Product updated successfully ✅")

    def show_products(self):
        if not self.products:
            print("No products to show ⛔")
            return
        for product in self.products:
            print("*" * 30)
            print(f"ID      : {product.id}")
            print(f"Name    : {product.name}")
            print(f"Quantity: {product.quantity}")
            print(f"Price   : {product.price}")
            print("*" * 30)

    def search_product(self):
        product_id = input("Enter ID to search: ")
        product = self.find_product_by_id(product_id)
        if product:
            print("*" * 30)
            print(f"ID      : {product.id}")
            print(f"Name    : {product.name}")
            print(f"Quantity: {product.quantity}")
            print(f"Price   : {product.price}")
            print("*" * 30)
        else:
            print("Product not found ⛔")

# ---------- Main Program ----------
store = Store()

while True:
    clear_screen()
    print("1 - Add Product")
    print("2 - Delete Product")
    print("3 - Update Product")
    print("4 - Show All Products")
    print("5 - Search Product")
    print("6 - Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Only numbers allowed ⛔")
        time.sleep(2)
        continue

    if choice == 1:
        store.add_product()
    elif choice == 2:
        store.delete_product()
    elif choice == 3:
        store.update_product()
    elif choice == 4:
        store.show_products()
    elif choice == 5:
        store.search_product()
    elif choice == 6:
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice ⛔")
    time.sleep(2)
