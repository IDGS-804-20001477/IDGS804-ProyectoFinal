from .sale_order_status import Sale_Order_Status
from .auth import User
from .db import db


class Sale_Order:
    id = 0,
    reference_number = '',
    total = 0.0,
    sale_order_status_id = Sale_Order_Status.id
    client_id = User.id
    sale_order_details = []

    def __init__(self, id, reference_number, total, sale_order_status_id, client_id, sale_order_details):
        self.id = id
        self.reference_number = reference_number
        self.total = total
        self.sale_order_status_id = sale_order_status_id
        self.client_id = client_id
        self.sale_order_details = sale_order_details


class SaleOrder(db.Model):
    __tablename__ = 'sale_orders'
    id = db.Column(db.Integer(), primary_key=True)
    reference_number = db.Column(db.String())
    total = db.Column(db.Double())
    client_id = db.Column(db.Integer())
    sale_orders_status_id = db.Column(
        db.Integer(), db.ForeignKey('sale_orders_status.id'))
    created_at = db.Column(db.DateTime())
    sale_order_details = db.relationship(
        'SaleOrdeDetail', backref='sale_orders')
    status = db.relationship(
        'SaleOrderStatus', backref=db.backref("sale_orders_status", uselist=False))


class SaleOrdeDetail(db.Model):
    __tablename__ = 'sale_orders_details'
    id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer())
    price = db.Column(db.Double())
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
    sale_orders_id = db.Column(db.Integer(), db.ForeignKey('sale_orders.id'))
    product_size = db.Column(
        db.String(), db.ForeignKey('product_sizes.size'))
    product = db.relationship(
        'ProductModel', backref=db.backref("products", uselist=False))


class SaleOrderStatus(db.Model):
    __tablename__ = 'sale_orders_status'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
