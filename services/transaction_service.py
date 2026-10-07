from datetime import datetime


class TransactionService:

    def __init__(self, connection):
        self.connection = connection


    # ==========================================
    # PURCHASE STOCK
    # ==========================================
    def purchaseStock(self):

        product_id = input("Enter Product ID: ")

        try:
            quantity = int(input("Enter purchase quantity: "))
        except ValueError:
            print("Invalid quantity.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        cursor = self.connection.cursor()

        try:

            # Get product details
            product_query = """
                SELECT
                    product_id,
                    product_name,
                    price
                FROM products
                WHERE product_id = %s
            """

            cursor.execute(product_query, (product_id,))
            product = cursor.fetchone()

            if product is None:
                print("Product not found.")
                return

            product_id = product[0]
            product_name = product[1]
            price = product[2]

            # Check inventory
            inventory_query = """
                SELECT quantity
                FROM inventory
                WHERE product_id = %s
            """

            cursor.execute(inventory_query, (product_id,))
            inventory = cursor.fetchone()

            if inventory is None:

                # Create inventory record
                insert_inventory = """
                    INSERT INTO inventory (product_id, quantity)
                    VALUES (%s, %s)
                """

                cursor.execute(
                    insert_inventory,
                    (product_id, quantity)
                )

            else:

                current_quantity = inventory[0]
                new_quantity = current_quantity + quantity

                update_inventory = """
                    UPDATE inventory
                    SET quantity = %s
                    WHERE product_id = %s
                """

                cursor.execute(
                    update_inventory,
                    (new_quantity, product_id)
                )

            # Calculate transaction total
            total = quantity * price

            # Save transaction
            transaction_query = """
                INSERT INTO transactions (
                    product_id,
                    transaction_type,
                    quantity,
                    price,
                    total,
                    transaction_date
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            cursor.execute(
                transaction_query,
                (
                    product_id,
                    "Purchase",
                    quantity,
                    price,
                    total,
                    datetime.now()
                )
            )

            self.connection.commit()

            print("\nPurchase completed successfully!")
            print("Product:", product_name)
            print("Quantity purchased:", quantity)
            print("Price:", price)
            print("Total:", total)

        except Exception as e:

            self.connection.rollback()
            print("Purchase failed:", e)

        finally:
            cursor.close()


    # ==========================================
    # SELL PRODUCT
    # ==========================================
    def sellProduct(self):

        product_id = input("Enter Product ID: ")

        try:
            quantity = int(input("Enter quantity to sell: "))
        except ValueError:
            print("Invalid quantity.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        cursor = self.connection.cursor()

        try:

            # Get product details
            product_query = """
                SELECT
                    product_id,
                    product_name,
                    price
                FROM products
                WHERE product_id = %s
            """

            cursor.execute(product_query, (product_id,))
            product = cursor.fetchone()

            if product is None:
                print("Product not found.")
                return

            product_id = product[0]
            product_name = product[1]
            price = product[2]

            # Get current inventory
            inventory_query = """
                SELECT quantity
                FROM inventory
                WHERE product_id = %s
            """

            cursor.execute(inventory_query, (product_id,))
            inventory = cursor.fetchone()

            if inventory is None:
                print("No inventory found for this product.")
                return

            current_quantity = inventory[0]

            # Check stock
            if quantity > current_quantity:
                print("Insufficient stock!")
                print("Available stock:", current_quantity)
                return

            new_quantity = current_quantity - quantity

            # Update inventory
            update_inventory = """
                UPDATE inventory
                SET quantity = %s
                WHERE product_id = %s
            """

            cursor.execute(
                update_inventory,
                (new_quantity, product_id)
            )

            # Calculate total
            total = quantity * price

            # Save transaction
            transaction_query = """
                INSERT INTO transactions (
                    product_id,
                    transaction_type,
                    quantity,
                    price,
                    total,
                    transaction_date
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            cursor.execute(
                transaction_query,
                (
                    product_id,
                    "Sale",
                    quantity,
                    price,
                    total,
                    datetime.now()
                )
            )

            self.connection.commit()

            print("\nSale completed successfully!")
            print("Product:", product_name)
            print("Quantity sold:", quantity)
            print("Price:", price)
            print("Total:", total)
            print("Remaining stock:", new_quantity)

        except Exception as e:

            self.connection.rollback()
            print("Sale failed:", e)

        finally:
            cursor.close()


    # ==========================================
    # TRANSACTION HISTORY
    # ==========================================
    def transactionHistory(self):

        query = """
            SELECT
                t.transaction_id,
                p.product_name,
                t.transaction_type,
                t.quantity,
                t.price,
                t.total,
                t.transaction_date
            FROM transactions t
            INNER JOIN products p
                ON t.product_id = p.product_id
            ORDER BY t.transaction_id
        """

        cursor = self.connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("No transactions found.")
            cursor.close()
            return

        print("\n" + "=" * 120)
        print(" " * 45 + "TRANSACTION HISTORY")
        print("=" * 120)

        print(
            f"{'ID':<10}"
            f"{'Product':<25}"
            f"{'Type':<15}"
            f"{'Quantity':<12}"
            f"{'Price':<15}"
            f"{'Total':<15}"
            f"{'Date':<25}"
        )

        print("-" * 120)

        for row in rows:

            print(
                f"{str(row[0]):<10}"
                f"{str(row[1]):<25}"
                f"{str(row[2]):<15}"
                f"{str(row[3]):<12}"
                f"{str(row[4]):<15}"
                f"{str(row[5]):<15}"
                f"{str(row[6]):<25}"
            )

        print("=" * 120)

        cursor.close()