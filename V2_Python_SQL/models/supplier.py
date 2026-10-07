class Supplier:

    def __init__(
        self,
        id = 0,
        supplier_id = None,
        supplier_name = None,
        contact_number = None,
        email = None,
        address = None
    ):
        self.id = id
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact_number = contact_number
        self.email = email 
        self.address = address 

    def __str__(self):
        return(
            f"Supplier ID: {self.supplier_id}\n"
            f"Supplier Name: {self.supplier_name}\n"
            f"Contact Number: {self.contact_number}\n"
            f"Email ID: {self.email}\n"
            f"Address: {self.address}\n"
        )
