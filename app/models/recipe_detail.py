from .feedstock import Feedstock
from .recipe import Recipe


class Recipe_Detail:
    id = 0,
    quantity = 0.0,
    recipe_id = Recipe,
    feedstock_id = Feedstock.id

    def __init__(self, id, quantity, recipe_id, feedstock_id):
        self.id = id
        self.quantity = quantity
        self.recipe_id = recipe_id
        self.feedstock_id = feedstock_id
