from .product import Product


class Recipe:
    id = 0,
    description = ''
    product_id = Product.id

    def __init__(self, id, description, product_id):
        self.id = id
        self.description = description
        self.product_id = product_id
