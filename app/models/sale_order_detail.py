from .product import Product
from .sale_order import Sale_Order


class Sale_Order_Detail:
    id = 0,
    quantity = 0.0
    price = 0.0
    product_id = Product.id
    sale_order_id = Sale_Order.id

    def __init__(self, id, quantity, price, product_id, sale_order_id):
        self.id = id
        self.quantity = quantity
        self.price = price
        self.product_id = product_id
        self.sale_order_id = sale_order_id
