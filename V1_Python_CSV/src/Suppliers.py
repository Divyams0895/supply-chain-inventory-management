import csv
import os


class Supplier:

    def __init__(self):
        self.supplier = {}

    # Add Supplier
    def addSupplier(self):
        supplier_id = input("Enter Supplier ID: ")
        supplier_name = input("Enter Supplier Name: ")
        contact = input("Enter Contact Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        self.supplier = {
            "Supplier Id": supplier_id,
            "Supplier Name": supplier_name,
            "Contact": contact,
            "Email": email,
            "Address": address
        }

        headers = [
            "Supplier Id",
            "Supplier Name",
            "Contact",
            "Email",
            "Address"
        ]

        file = "data/supplierlist.csv"

        folder_path = os.path.dirname(file)
        if folder_path and not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_exists = os.path.isfile(file)

        with open(file, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)

            if not file_exists:
                writer.writeheader()

            writer.writerow(self.supplier)

        print("Supplier added successfully!")


    # View Suppliers
    def listSuppliers(self):
        file = "data/supplierlist.csv"

        if not os.path.exists(file):
            print("Supplier file does not exist.")
            return

        with open(file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            suppliers = list(reader)

        if not suppliers:
            print("No suppliers found.")
            return

        print("\n" + "=" * 100)
        print(" " * 35 + "SUPPLIER LIST")
        print("=" * 100)

        print(
            f"{'ID':<15}"
            f"{'Supplier Name':<25}"
            f"{'Contact':<18}"
            f"{'Email':<30}"
            f"{'Address':<20}"
        )

        print("-" * 100)

        for supplier in suppliers:
            print(
                f"{supplier['Supplier Id']:<15}"
                f"{supplier['Supplier Name']:<25}"
                f"{supplier['Contact']:<18}"
                f"{supplier['Email']:<30}"
                f"{supplier['Address']:<20}"
            )

        print("=" * 100)


    # Search Supplier
    def searchSupplier(self):
        supplier_id = input("Enter Supplier ID to search: ")

        file = "data/supplierlist.csv"

        if not os.path.exists(file):
            print("Supplier file does not exist.")
            return

        with open(file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            suppliers = list(reader)

        for supplier in suppliers:
            if supplier["Supplier Id"] == supplier_id:
                print("\nSupplier Found")
                print("=" * 30)
                print("Supplier ID:", supplier["Supplier Id"])
                print("Supplier Name:", supplier["Supplier Name"])
                print("Contact:", supplier["Contact"])
                print("Email:", supplier["Email"])
                print("Address:", supplier["Address"])
                print("=" * 30)
                return

        print("Supplier not found!")