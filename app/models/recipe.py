from .product import Product


class Recipe:
    id = 0,
    product_id = Product.id
    description = ''
    recipe_details = []

    def __init__(self, id, product_id, description, recipe_details):
        self.id = id
        self.product_id = product_id
        self.description = description
        self.recipe_details = recipe_details
