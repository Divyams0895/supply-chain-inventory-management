from models.products import Product
from services.supplier_service import SupplierService

class ProductService:

    def __init__(self,connection):
        self.connection = connection 

    # ADD NEW PRODUCT
    def addProduct(self):

        product_name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        reorder_level = int(input("Enter Reorder Level: "))
        supplier_service = SupplierService(self.connection)
        
        ids = supplier_service.getSupplierIds()
        print("Available supplier IDs: ",ids)
        supplier_id = input("Enter supplier id: ")

        query = """
            INSERT INTO products 
            (
                product_name,
                product_category,
                price,
                reorder_level,
                supplier_id
            )
            VALUES (%s,%s,%s,%s,%s)
        """

        cursor = self.connection.cursor()

        cursor.execute(
            query,
            (
                product_name,
                category,
                price,
                reorder_level,
                supplier_id
            )
        )

        self.connection.commit()

        cursor.close()

        print("Product added successfully")

    #LIST ALL PRODUCT
    def list_products(self):

        query = """
            SELECT *
            FROM products
            ORDER BY product_id
        """

        cursor = self.connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("No products found.")
            return
        
        print("\n" + "=" * 115)
        print(" "*50,"ALL PRODUCTS")
        print("=" * 115)

        print(
            f"{'ID':<8}"
            f"{'Product Name':<20}"
            f"{'Category':<18}"
            f"{'Price':<12}"
            f"{'Reorder Level':<20}"
            f"{'Supplier ID':<12}"
        )

        print("-" * 115)

        for row in rows:
            print(
                f"{str(row[0]):<8}"
                f"{str(row[1]):<20}"
                f"{str(row[2]):<18}"
                f"{str(row[3]):<12}"
                f"{str(row[4]):<20}"
                f"{str(row[5]):<12}"
            )

        print("=" * 115)   

        cursor.close()     

    # SEARCH FOR A PRODUCT
    def search_product(self):

        product_id = input("Enter a Product ID to search:")

        query = """
            SELECT
                product_id,
                product_name,
                product_category,
                price,
                reorder_level,
                supplier_id
            FROM products
            WHERE product_id = %s
        """

        cursor = self.connection.cursor()

        cursor.execute(
            query,
            (product_id,)
        )

        row = cursor.fetchone()

        if row is None:
            print("Product not found.")
            return

        product = Product(
            product_id=row[0],
            product_name=row[1],
            product_category=row[2],
            price=row[3],
            reorder_level=row[4],
            supplier_id=row[5]
        )

        print("\nProduct found!")
        print(product)


    # UPDATE PRODUCT
    def update_product(self):

        product_id = input("Enter Product ID to update: ")

        # Check whether product exists
        check_query = """
            SELECT product_id, product_name, product_category,
                price, reorder_level, supplier_id
            FROM products
            WHERE product_id = %s
        """

        cursor = self.connection.cursor()
        cursor.execute(check_query, (product_id,))

        row = cursor.fetchone()

        if row is None:
            print("Product not found.")
            cursor.close()
            return

        # Display current product
        print("\nCurrent Product Details")
        print("-" * 40)
        print(f"Product ID      : {row[0]}")
        print(f"Product Name    : {row[1]}")
        print(f"Category        : {row[2]}")
        print(f"Price           : {row[3]}")
        print(f"Reorder Level   : {row[4]}")
        print(f"Supplier ID     : {row[5]}")
        print("-" * 40)

        # Get new values
        product_name = input(f"Enter new product name [{row[1]}]: ")
        product_category = input(f"Enter new category [{row[2]}]: ")
        price = input(f"Enter new price [{row[3]}]: ")
        reorder_level = input(f"Enter new reorder level [{row[4]}]: ")
        supplier_id = input(f"Enter new supplier ID [{row[5]}]: ")

        # Keep old value if user presses Enter
        if product_name == "":
            product_name = row[1]

        if product_category == "":
            product_category = row[2]

        if price == "":
            price = row[3]

        if reorder_level == "":
            reorder_level = row[4]

        if supplier_id == "":
            supplier_id = row[5]

        update_query = """
            UPDATE products
            SET
                product_name = %s,
                product_category = %s,
                price = %s,
                reorder_level = %s,
                supplier_id = %s
            WHERE product_id = %s
        """

        cursor.execute(
            update_query,
            (
                product_name,
                product_category,
                price,
                reorder_level,
                supplier_id,
                product_id
            )
        )

        self.connection.commit()

        print("\nProduct updated successfully.")

        cursor.close()

    # DELETE A PRODUCT
    def delete_product(self):

        product_id = int(input("Enter Product ID to delete:"))

        query = """
            DELETE FROM products
            WHERE product_id = %s
        """

        cursor = self.connection.cursor()
        
        cursor.execute(
            query,
            (product_id,)
        )

        self.connection.commit()

        if cursor.rowcount == 0:
            print("Product not found.")
        else:
            print("Product deleted successfully!")