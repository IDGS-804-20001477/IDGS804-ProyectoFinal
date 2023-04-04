from .product import Product


class Recipe:
    id = 0,
    description = ''
    product_id = Product.id
    recipe_details = []

    def __init__(self, id, description, product_id, recipe_details):
        self.id = id
        self.description = description
        self.product_id = product_id
        self.recipe_details = recipe_details
