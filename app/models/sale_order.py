from .sale_order_status import Sale_Order_Status
from .auth import User


class Sale_Order:
    id = 0,
    reference_number = '',
    total = 0.0,
    sale_order_status_id = Sale_Order_Status.id
    client_id = User.id

    def __init__(self, id, reference_number, total, sale_order_status_id, client_id):
        self.id = id
        self.reference_number = reference_number
        self.total = total
        self.sale_order_status_id = sale_order_status_id
        self.client_id = client_id
