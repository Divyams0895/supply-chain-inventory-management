from database.connection import get_connection
from services.product_service import ProductService
from services.supplier_service import SupplierService
from services.inventory_service import InventoryService
from services.transaction_service import TransactionService

connection = get_connection()
product_service = ProductService(connection)
supplier_service = SupplierService(connection)
inventory_service = InventoryService(connection)
transaction_service = TransactionService(connection)

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
            product_service.addProduct()

        elif choice == "2":
            product_service.list_products()

        elif choice == "3":
            product_service.search_product()

        elif choice == "4":
            product_service.update_product()

        elif choice == "5":
            product_service.delete_product()

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
            supplier_service.addSupplier()

        elif choice == "2":
            supplier_service.listSuppliers()

        # elif choice == "3":
        #     supplier_service.searchSupplier()

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
            inventory_service.addStock()

        elif choice == "2":
            inventory_service.removeStock()

        elif choice == "3":
            inventory_service.checkStock()

        elif choice == "4":
            inventory_service.lowStockAlert()

        elif choice == "5":
            inventory_service.inventoryValue()

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
            transaction_service.purchaseStock()

        elif choice == "2":
            transaction_service.sellProduct()

        elif choice == "3":
            transaction_service.transactionHistory()

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
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

