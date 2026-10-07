class Transaction:

    def __init__(
        self,
        transaction_id = 0,
        product_id = 0,
        transaction_type = None,
        quantity = 0,
        price = 0.0,
        total = 0.0,
        transaction_date = None
    ):
        self.transaction_id  = transaction_id
        self.product_id  = product_id
        self.transaction_type = transaction_type
        self.quantity = quantity
        self.price = price 
        self.total = total 
        self.transaction_date = transaction_date


    def __str__(self):
        return(
            f"Transaction ID: {self.transaction_id}"
            f"Product ID: {self.product_id}"
            f"Transaction Type: {self.transaction_type}"
            f"Quantity: {self.quantity}"
            f"Price: {self.price}"
            f"Total Amount: {self.total}"
            f"Transaction Date: {self.transaction_date}"
        )