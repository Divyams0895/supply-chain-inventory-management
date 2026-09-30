import csv
import os
from datetime import datetime


class Transaction:

    def __init__(self):
        self.product_file = "data/productlist.csv"
        self.transaction_file = "data/transactionlist.csv"


    # Purchase Stock
    def purchaseStock(self):

        product_id = input("Enter Product ID: ")
        quantity = int(input("Enter purchase quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if not os.path.exists(self.product_file):
            print("Product file does not exist.")
            return

        with open(
            self.product_file,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as f:

            reader = csv.DictReader(f)
            products = list(reader)
            headers = reader.fieldnames

        for product in products:

            if product["Product Id"] == product_id:

                current_quantity = int(product["Quantity"])
                price = float(product["Price"])

                product["Quantity"] = str(
                    current_quantity + quantity
                )

                with open(
                    self.product_file,
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

                self.saveTransaction(
                    product_id,
                    product["Product Name"],
                    "Purchase",
                    quantity,
                    price
                )

                print("Purchase completed successfully!")
                return

        print("Product not found!")


    # Sell Product
    def sellProduct(self):

        product_id = input("Enter Product ID: ")
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if not os.path.exists(self.product_file):
            print("Product file does not exist.")
            return

        with open(
            self.product_file,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as f:

            reader = csv.DictReader(f)
            products = list(reader)
            headers = reader.fieldnames

        for product in products:

            if product["Product Id"] == product_id:

                current_quantity = int(product["Quantity"])
                price = float(product["Price"])

                if quantity > current_quantity:
                    print("Insufficient stock!")
                    print("Available stock:", current_quantity)
                    return

                product["Quantity"] = str(
                    current_quantity - quantity
                )

                with open(
                    self.product_file,
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

                self.saveTransaction(
                    product_id,
                    product["Product Name"],
                    "Sale",
                    quantity,
                    price
                )

                print("Sale completed successfully!")
                return

        print("Product not found!")


    # Save Transaction
    def saveTransaction(
        self,
        product_id,
        product_name,
        transaction_type,
        quantity,
        price
    ):

        headers = [
            "Transaction Id",
            "Product Id",
            "Product Name",
            "Transaction Type",
            "Quantity",
            "Price",
            "Total",
            "Date"
        ]

        file_exists = os.path.isfile(self.transaction_file)

        transaction_id = self.getTransactionId()

        total = quantity * price

        transaction = {
            "Transaction Id": transaction_id,
            "Product Id": product_id,
            "Product Name": product_name,
            "Transaction Type": transaction_type,
            "Quantity": quantity,
            "Price": price,
            "Total": total,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(
            self.transaction_file,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=headers
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow(transaction)


    # Generate Transaction ID
    def getTransactionId(self):

        if not os.path.exists(self.transaction_file):
            return "T001"

        with open(
            self.transaction_file,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as f:

            reader = csv.DictReader(f)
            transactions = list(reader)

        if not transactions:
            return "T001"

        last_id = transactions[-1]["Transaction Id"]

        number = int(last_id[1:])

        return f"T{number + 1:03d}"


    # View Transaction History
    def transactionHistory(self):

        if not os.path.exists(self.transaction_file):
            print("No transaction history found.")
            return

        with open(
            self.transaction_file,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as f:

            reader = csv.DictReader(f)
            transactions = list(reader)

        if not transactions:
            print("No transactions found.")
            return

        print("\n" + "=" * 120)
        print(" " * 45 + "TRANSACTION HISTORY")
        print("=" * 120)

        print(
            f"{'ID':<10}"
            f"{'Product':<20}"
            f"{'Type':<15}"
            f"{'Quantity':<12}"
            f"{'Price':<12}"
            f"{'Total':<12}"
            f"{'Date':<25}"
        )

        print("-" * 120)

        for transaction in transactions:

            print(
                f"{transaction['Transaction Id']:<10}"
                f"{transaction['Product Name']:<20}"
                f"{transaction['Transaction Type']:<15}"
                f"{transaction['Quantity']:<12}"
                f"{transaction['Price']:<12}"
                f"{transaction['Total']:<12}"
                f"{transaction['Date']:<25}"
            )

        print("=" * 120)