from .product import Product


class Recipe:
    id = 0,
    product_id = Product.id
    description = ''
    recipe_details = []
    product_size_id = 0

    def __init__(self, id, product_id, description, recipe_details, product_size_id):
        self.id = id
        self.product_id = product_id
        self.description = description
        self.recipe_details = recipe_details
        self.product_size_id = product_size_id
