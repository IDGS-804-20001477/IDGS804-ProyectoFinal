from .db import db


class Product:
    id = 0
    sku = ''
    name = ''
    description = ''
    price = 0.0
    size = ''
    min_value = 0.0
    max_value = 0.0
    quantity = 0.0
    photo = ''

    def __init__(self, id, sku, name, description, price, size, min_value, max_value, quantity, photo):
        self.id = id
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.size = size
        self.min_value = min_value
        self.max_value = max_value
        self.quantity = quantity
        self.photo = photo


class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer(), primary_key=True)
    sku = db.Column(db.String())
    name = db.Column(db.String())
    photo = db.Column(db.String())
    description = db.Column(db.String())
    price = db.Column(db.Double())
    status = db.Column(db.Integer())
    size = db.Column(db.String())
    min_value = db.Column(db.Integer())
    max_value = db.Column(db.Integer())
    details = db.relationship(
        'ProductDetail', backref='products')

    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_

    def get_quantity(self):
        total = 0
        for detail in self.details:
            total += detail.quantity
        return total

    def to_dict(self, size):
        return {
            'id': self.id,
            'quantity': 1,
            'size': size
        }


class ProductDetail(db.Model):
    __tablename__ = 'product_details'
    id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer())
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
    product_size_id = db.Column(
        db.Integer(), db.ForeignKey('product_sizes.id'))
    product_size = db.relationship(
        'ProductSize', backref='product_details', uselist=False)


class ProductSize(db.Model):
    __tablename__ = 'product_sizes'
    id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.Integer())
