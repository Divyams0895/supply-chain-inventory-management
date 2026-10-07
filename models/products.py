class Product:

    def __init__(
            self,
            product_id = 0,
            product_name = None,
            product_category = None,
            price = 0.0,
            reorder_level = 0,
            supplier_id = None            
    ):

        self.product_id = product_id
        self.product_name = product_name
        self.product_category = product_category
        self.price = price
        self.reorder_level = reorder_level
        self.supplier_id = supplier_id

    def __str__(self):
        return (
            f"Product ID: {self.product_id}\n"
            f"Product Name: {self.product_name}\n"
            f"Category: {self.product_category}\n"
            f"Price: {self.price}\n"
            f"Reorder Level: {self.reorder_level}\n"
            f"Supplier ID: {self.supplier_id}"
        )









        