from .purchase_order import Buy_Order
from .feedstock import Feedstock


class Buy_Order_Detail:
    id = 0,
    quantity = 0.0,
    price = 0.0,
    feedstock_id = Feedstock.id
    buy_order_id = Buy_Order

    def __init__(self, id, quantity, price, feedstock_id, buy_order_id):
        self.id = id
        self.quantity = quantity
        self.price = price
        self.feedstock_id = feedstock_id
        self.buy_order_id = buy_order_id
