from .provider import Provider
from .purchase_order_status import Buy_Order_Status


class Buy_Order:
    id = 0,
    total = 0,
    provider_id = Provider.id,
    buy_order_status_id = Buy_Order_Status.id

    def __init__(self, id, total, provider_id, buy_order_status_id):
        self.id = id
        self.total = total
        self.provider_id = provider_id
        self. buy_order_status_id = buy_order_status_id
