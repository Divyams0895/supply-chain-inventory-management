import csv
import os


class Inventory:

    def __init__(self):
        self.file = "data/productlist.csv"


    # Add Stock
    def addStock(self):
        product_id = input("Enter Product ID: ")
        quantity = int(input("Enter quantity to add: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if not os.path.exists(self.file):
            print("Product file does not exist.")
            return

        with open(self.file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            products = list(reader)
            headers = reader.fieldnames

        for product in products:

            if product["Product Id"] == product_id:

                current_quantity = int(product["Quantity"])
                new_quantity = current_quantity + quantity

                product["Quantity"] = str(new_quantity)

                with open(
                    self.file,
                    mode="w",
                    newline="",
                    encoding="utf-8"
                ) as f:

                    writer = csv.DictWriter(
                        f,
                        fieldnames=headers
                    )

                    writer.writeheader()
                    writer.writerows(products)

                print("Stock added successfully!")
                print("New Stock:", new_quantity)
                return

        print("Product not found!")


    # Remove Stock
    def removeStock(self):
        product_id = input("Enter Product ID: ")
        quantity = int(input("Enter quantity to remove: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if not os.path.exists(self.file):
            print("Product file does not exist.")
            return

        with open(self.file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            products = list(reader)
            headers = reader.fieldnames

        for product in products:

            if product["Product Id"] == product_id:

                current_quantity = int(product["Quantity"])

                if quantity > current_quantity:
                    print("Insufficient stock!")
                    print("Available stock:", current_quantity)
                    return

                new_quantity = current_quantity - quantity

                product["Quantity"] = str(new_quantity)

                with open(
                    self.file,
                    mode="w",
                    newline="",
                    encoding="utf-8"
                ) as f:

                    writer = csv.DictWriter(
                        f,
                        fieldnames=headers
                    )

                    writer.writeheader()
                    writer.writerows(products)

                print("Stock removed successfully!")
                print("Remaining Stock:", new_quantity)
                return

        print("Product not found!")


    # Check Stock
    def checkStock(self):
        product_id = input("Enter Product ID: ")

        if not os.path.exists(self.file):
            print("Product file does not exist.")
            return

        with open(self.file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for product in reader:

                if product["Product Id"] == product_id:

                    print("\nProduct:", product["Product Name"])
                    print("Current Stock:", product["Quantity"])
                    print("Reorder Level:", product["Reorder Level"])

                    return

        print("Product not found!")


    # Low Stock Alert
    def lowStockAlert(self):
        if not os.path.exists(self.file):
            print("Product file does not exist.")
            return

        with open(self.file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            products = list(reader)

        low_stock_products = []

        for product in products:

            quantity = int(product["Quantity"])
            reorder_level = int(product["Reorder Level"])

            if quantity <= reorder_level:
                low_stock_products.append(product)

        if not low_stock_products:
            print("\nNo low-stock products.")
            return

        print("\n" + "=" * 70)
        print(" " * 20 + "LOW STOCK ALERT")
        print("=" * 70)

        print(
            f"{'ID':<10}"
            f"{'Product Name':<25}"
            f"{'Quantity':<15}"
            f"{'Reorder Level':<15}"
        )

        print("-" * 70)

        for product in low_stock_products:
            print(
                f"{product['Product Id']:<10}"
                f"{product['Product Name']:<25}"
                f"{product['Quantity']:<15}"
                f"{product['Reorder Level']:<15}"
            )

        print("=" * 70)


    # Calculate Inventory Value
    def inventoryValue(self):
        if not os.path.exists(self.file):
            print("Product file does not exist.")
            return

        with open(self.file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            products = list(reader)

        total_value = 0

        for product in products:
            price = float(product["Price"])
            quantity = int(product["Quantity"])

            total_value += price * quantity

        print("\nTotal Inventory Value:", total_value)