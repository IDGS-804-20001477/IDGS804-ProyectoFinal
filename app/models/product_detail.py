from .product import Product


class Product_Detail:
    id = 0,
    quantity = 0.0
    product_id = Product

    def __init__(self, id, quantity, product_id):
        self.id = id
        self.quantity = quantity
        self.product_id = product_id
