class Inventory:

    def __init__(
        self,
        inventory_id = 0,
        product_id  = 0,
        quantity = 0
    ):

        self.inventory_id = inventory_id
        self.product_id  = product_id
        self.quantity = quantity


    def __str__(self):
        return (
            f"Inventory ID: {self.inventory_id}\n"
            f"Product ID: {self.product_id}\n"
            f"Quantity: {self.quantity}\n"
        )