from Products import Product
from Inventory import Inventory
from Suppliers import Supplier 
from Transactions import Transaction

# Objects
product = Product()
inventory = Inventory()
supplier = Supplier()
transaction = Transaction()

def productMenu():
    while True:
        print("\n")
        print("=" * 40)
        print("          PRODUCT MANAGEMENT")
        print("=" * 40)
        print("1. Add Product")
        print("2. List Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            product.addProduct()

        elif choice == "2":
            product.listProducts()

        elif choice == "3":
            product.searchProduct()

        elif choice == "4":
            product.updateProduct()

        elif choice == "5":
            product.deleteProduct()

        elif choice == "6":
            break

        else:
            print("Invalid choice! Please try again.")

def supplierMenu():
    while True:
        print("\n")
        print("=" * 40)
        print("          SUPPLIER MANAGEMENT")
        print("=" * 40)
        print("1. Add Supplier")
        print("2. List Suppliers")
        print("3. Search Supplier")
        print("4. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            supplier.addSupplier()

        elif choice == "2":
            supplier.listSuppliers()

        elif choice == "3":
            supplier.searchSupplier()

        elif choice == "4":
            break

        else:
            print("Invalid choice! Please try again.")

def inventoryMenu():
    while True:
        print("\n")
        print("=" * 40)
        print("          INVENTORY MANAGEMENT")
        print("=" * 40)
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Check Stock")
        print("4. Low Stock")
        print("5. Calculate Inventory")
        print("6. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.addStock()

        elif choice == "2":
            inventory.removeStock()

        elif choice == "3":
            inventory.checkStock()

        elif choice == "4":
            inventory.lowStockAlert()

        elif choice == "5":
            inventory.inventoryValue()

        elif choice == "6":
            break

        else:
            print("Invalid choice! Please try again.")

def transactionMenu():
    while True:
        print("\n")
        print("=" * 40)
        print("          TRANSACTION MANAGEMENT")
        print("=" * 40)
        print("1. Purchase Stock")
        print("2. Sell Product")
        print("3. Transaction History")
        print("4. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            transaction.purchaseStock()

        elif choice == "2":
            transaction.sellProduct()

        elif choice == "3":
            transaction.transactionHistory()

        elif choice == "4":
            break

        else:
            print("Invalid choice! Please try again.")


def main():
    while True:
        print("=" * 50)
        print("SUPPLY CHAIN & INVENTORY SYSTEM")
        print("=" * 50)
        # print("Application started successfully!")

        print("Select a choice")
        print("-"*50)
        print("1. PRODUCT MANAGEMENT")
        print("2. SUPPLIER MANAGEMENT")
        print("3. INVENTORY MANAGEMENT")
        print("4. TRANSACTION MANAGEMENT")
        print("5. EXIT")


        choice = input("Enter your choice: ")

        if choice == "1":
            productMenu()

        elif choice == "2":
            supplierMenu()

        elif choice == "3":
            inventoryMenu()

        elif choice == "4":
            transactionMenu()

        elif choice == "5":
            print("\nThank you for using the system!")
            print("Program closed.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()