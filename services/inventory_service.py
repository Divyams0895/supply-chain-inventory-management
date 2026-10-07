class InventoryService:

    def __init__(self, connection):
        self.connection = connection


    # ==========================================
    # ADD STOCK
    # ==========================================
    def addStock(self):

        product_id = input("Enter Product ID: ")

        try:
            quantity = int(input("Enter quantity to add: "))
        except ValueError:
            print("Invalid quantity.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        cursor = self.connection.cursor()

        # Check whether product exists
        product_query = """
            SELECT product_id
            FROM products
            WHERE product_id = %s
        """

        cursor.execute(product_query, (product_id,))
        product = cursor.fetchone()

        if product is None:
            print("Product not found.")
            cursor.close()
            return

        # Check current inventory
        inventory_query = """
            SELECT quantity
            FROM inventory
            WHERE product_id = %s
        """

        cursor.execute(inventory_query, (product_id,))
        inventory = cursor.fetchone()

        if inventory is None:

            # No inventory record yet
            insert_query = """
                INSERT INTO inventory (product_id, quantity)
                VALUES (%s, %s)
            """

            cursor.execute(
                insert_query,
                (product_id, quantity)
            )

            new_quantity = quantity

        else:

            current_quantity = inventory[0]
            new_quantity = current_quantity + quantity

            update_query = """
                UPDATE inventory
                SET quantity = %s
                WHERE product_id = %s
            """

            cursor.execute(
                update_query,
                (new_quantity, product_id)
            )

        self.connection.commit()
        cursor.close()

        print("Stock added successfully!")
        print("New Stock:", new_quantity)


    # ==========================================
    # REMOVE STOCK
    # ==========================================
    def removeStock(self):

        product_id = input("Enter Product ID: ")

        try:
            quantity = int(input("Enter quantity to remove: "))
        except ValueError:
            print("Invalid quantity.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        cursor = self.connection.cursor()

        query = """
            SELECT quantity
            FROM inventory
            WHERE product_id = %s
        """

        cursor.execute(query, (product_id,))
        row = cursor.fetchone()

        if row is None:
            print("No inventory record found for this product.")
            cursor.close()
            return

        current_quantity = row[0]

        if quantity > current_quantity:
            print("Insufficient stock!")
            print("Available stock:", current_quantity)
            cursor.close()
            return

        new_quantity = current_quantity - quantity

        update_query = """
            UPDATE inventory
            SET quantity = %s
            WHERE product_id = %s
        """

        cursor.execute(
            update_query,
            (new_quantity, product_id)
        )

        self.connection.commit()
        cursor.close()

        print("Stock removed successfully!")
        print("Remaining Stock:", new_quantity)


    # ==========================================
    # CHECK STOCK
    # ==========================================
    def checkStock(self):

        product_id = input("Enter Product ID: ")

        query = """
            SELECT
                p.product_id,
                p.product_name,
                i.quantity
            FROM products p
            INNER JOIN inventory i
                ON p.product_id = i.product_id
            WHERE p.product_id = %s
        """

        cursor = self.connection.cursor()
        cursor.execute(query, (product_id,))

        row = cursor.fetchone()

        if row is None:
            print("Product or inventory record not found.")
            cursor.close()
            return

        print("\nProduct:", row[1])
        print("Current Stock:", row[2])

        cursor.close()


    # ==========================================
    # LOW STOCK ALERT
    # ==========================================
    def lowStockAlert(self):

        query = """
            SELECT
                p.product_id,
                p.product_name,
                i.quantity,
                p.reorder_level
            FROM products p
            INNER JOIN inventory i
                ON p.product_id = i.product_id
            WHERE i.quantity <= p.reorder_level
            ORDER BY p.product_id
        """

        cursor = self.connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("\nNo low-stock products.")
            cursor.close()
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

        for row in rows:

            print(
                f"{str(row[0]):<10}"
                f"{str(row[1]):<25}"
                f"{str(row[2]):<15}"
                f"{str(row[3]):<15}"
            )

        print("=" * 70)

        cursor.close()


    # ==========================================
    # CALCULATE INVENTORY VALUE
    # ==========================================
    def inventoryValue(self):

        query = """
            SELECT
                SUM(p.price * i.quantity)
            FROM products p
            INNER JOIN inventory i
                ON p.product_id = i.product_id
        """

        cursor = self.connection.cursor()
        cursor.execute(query)

        row = cursor.fetchone()

        total_value = row[0]

        if total_value is None:
            total_value = 0

        print("\nTotal Inventory Value:", total_value)

        cursor.close()