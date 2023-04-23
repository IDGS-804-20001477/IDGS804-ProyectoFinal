from .provider import Provider
from .purchase_order_status import Buy_Order_Status


class Purchase_Order:
    id = 0,
    reference_number = ''
    total = 0,
    provider_id = Provider.id,
    purchase_order_details = []

    def __init__(self, id, reference_number, total, provider_id, purchase_order_details):
        self.id = id
        self.reference_number = reference_number
        self.total = total
        self.provider_id = provider_id
        self.purchase_order_details = purchase_order_details
