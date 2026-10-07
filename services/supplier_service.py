from models.supplier import Supplier

class SupplierService:

    def __init__(self,connection):
        self.connection = connection

    #ADD NEW SUPPLIER
    def addSupplier(self):

        supplier_name = input("Enter supplier name: ")
        contact = input("Enter contact number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        query = """
            INSERT INTO suppliers(
                supplier_id,
                supplier_name,
                contact,
                email,
                address
            )
            VALUES (%s,%s,%s,%s,%s)
        """

        cursor = self.connection.cursor()

        cursor.execute(
            query,
            (
                "temp",
                supplier_name,
                contact,
                email,
                address
            )
        )

        generated_id = cursor.lastrowid
        
        # Convert 100 -> s100
        supplier_id = f"s{generated_id}"

        cursor.execute(
            "UPDATE suppliers SET supplier_id = %s,supplier_name =%s,contact=%s,email=%s,address=%s WHERE id = %s",
            (supplier_id,supplier_name,contact,email,address,generated_id)
        )

        self.connection.commit()

        cursor.close()

        print("Supplier added successfully!")


    # LIST ALL SUPPLIERS
    def listSuppliers(self):

        query ="""
            SELECT * FROM suppliers
        """

        cursor = self.connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("No suppliers found")
            return 

        for row in rows:

            supplier = Supplier(
                supplier_id=row[1],
                supplier_name=row[2],
                contact_number=row[3],
                email=row[4],
                address=row[5],
            )

            print(supplier)
            print("-" * 90)

    # GET ALL SUPPLIER IDs
    def getSupplierIds(self):

        query ="""
            SELECT supplier_id FROM suppliers
        """

        cursor = self.connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("No suppliers found")
            return 

        supplier_ids = [row[0] for row in rows]

        return supplier_ids
        

        

    

        
                    

        

