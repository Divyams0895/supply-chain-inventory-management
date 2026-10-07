import csv
import os

class Product:

    def __init__(self):
        self.products = {}
        file = 'data/productlist.csv'

    # Add product
    def addProduct(self):
        id = int(input("Enter Product ID: "))
        prodName = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        reorder_level = int(input("Enter Reorder Level: "))
        supplier_id = input("Enter Supplier ID:")

        self.products["Product Id"] = id
        self.products["Product Name"] = prodName
        self.products["Product Category"] = category
        self.products["Price"] = price 
        self.products["Quantity"] = quantity
        self.products["Reorder Level"] = reorder_level
        self.products["Supplier Id"] = supplier_id

        headers = ["Product Id", "Product Name", "Product Category", "Price", "Quantity", "Reorder Level", "Supplier Id"]

        file = 'data/productlist.csv'

        folder_path = os.path.dirname(file )
        if folder_path and not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_exists = os.path.isfile(file )

        with open(file ,mode='a',newline='',encoding='utf-8') as f:
            writer = csv.DictWriter(f,fieldnames=headers)

            if not file_exists:
                writer.writeheader()

            writer.writerow(self.products)

        print("New product added successfully!")

    # Update product
    def updateProduct(self):
        product_id = input("Enter Product ID to update: ")

        file = 'data/productlist.csv'

        if not os.path.exists(file ):
            print("Product file does not exist.")
            return

        with open(file , mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            products = list(reader)

        found = False

        for product in products:
            if product["Product Id"] == product_id:
                found = True

                print("\nCurrent Product Details:")
                print("Product Name:", product["Product Name"])
                print("Category:", product["Product Category"])
                print("Price:", product["Price"])
                print("Quantity:", product["Quantity"])
                print("Reorder Level:", product["Reorder Level"])
                print("Supplier ID:", product["Supplier Id"])

                print("\nEnter New Details")

                product["Product Name"] = input("Enter Product Name: ")
                product["Product Category"] = input("Enter Category: ")
                product["Price"] = input("Enter Price: ")
                product["Quantity"] = input("Enter Quantity: ")
                product["Reorder Level"] = input("Enter Reorder Level: ")
                product["Supplier Id"] = input("Enter Supplier ID: ")

                break

        if not found:
            print("Product not found!")
            return

        headers = [
            "Product Id",
            "Product Name",
            "Product Category",
            "Price",
            "Quantity",
            "Reorder Level",
            "Supplier Id"
        ]

        with open(file , mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(products)

        print("Product updated successfully!")
        

        
    # Delete product
    def deleteProduct(self):
        product_id = input("Enter Product Id to delete: ")

        file = 'data/productlist.csv'
        if not os.path.exists(file ):
            print("File not found")
            return 

        with open(file , mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            products = list(reader)
        
        found = False
        
        for product in products:
            if product["Product Id"] == product_id:
                print("\nProduct found")

                confirm = input("Are you sure you want to delete this product? (y/n)")
                if confirm.lower()=="y":
                    products.remove(product)
                    found = True
                else: 
                    print("Delete cancelled")
                    return
                break

        if not found:
            print("Product not found!")
            return
        
        headers = [
            "Product Id",
            "Product Name",
            "Product Category",
            "Price",
            "Quantity",
            "Reorder Level",
            "Supplier Id"
        ]

        with open(file , mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(products)

        print("Product deleted successfully!") 

    # Search product
    def searchProduct(self):
        product_id = input("Enter Product ID to search: ")
        
        file = 'data/productlist.csv'
        
        if not os.path.exists(file ):
            print("Product file does not exist.")
            return
        
        with open(file , mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            products = list(reader)
        
        found = False
        
        for product in products:
            if product["Product Id"] == product_id:
                found = True
        
                print("\nProduct Details:")
                print("="*25)
                print("Product Name:", product["Product Name"])
                print("Category:", product["Product Category"])
                print("Price:", product["Price"])
                print("Quantity:", product["Quantity"])
                print("Reorder Level:", product["Reorder Level"])
                print("Supplier ID:", product["Supplier Id"])

        if not found:
            print("Product not available!")

        
    # View products
    def listProducts(self):
        file = 'data/productlist.csv'
        
        if not os.path.exists(file ):
            print("Product file does not exist.")
            return
        
        with open(file , mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            products = list(reader)


        if not products:
            print("No prodcts found!!")
            return
        
        print("\n" + "=" * 115)
        print(" "*50,"ALL PRODUCTS")
        print("=" * 115)

        print(
            f"{'ID':<8}"
            f"{'Product Name':<20}"
            f"{'Category':<18}"
            f"{'Price':<12}"
            f"{'Quantity':<12}"
            f"{'Reorder Level':<20}"
            f"{'Supplier ID':<12}"
        )

        print("-" * 115)

        for product in products:
            print(
                f"{product['Product Id']:<8}"
                f"{product['Product Name']:<20}"
                f"{product['Product Category']:<18}"
                f"{product['Price']:<12}"
                f"{product['Quantity']:<12}"
                f"{product['Reorder Level']:<20}"
                f"{product['Supplier Id']:<12}"
            )

        print("=" * 115)      
        
