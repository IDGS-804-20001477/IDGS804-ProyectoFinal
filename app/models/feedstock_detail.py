from .feedstock import Feedstock


class Feedstock_Detail:
    id = 0,
    quantity = 0.0,
    feedstock_id = Feedstock

    def __init__(self, id, quantity, feedstock_id):
        self.id = id
        self.quantity = quantity
        self.feedstock_id = feedstock_id
