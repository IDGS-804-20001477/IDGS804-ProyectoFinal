class Product:
    id = 0
    sku = ''
    name = ''
    description = ''
    price = 0.0
    size = '',
    min_value = 0.0,
    max_value = 0.0

    def __init__(self, id, sku, name, description, price, size, min_value, max_value):
        self.id = id
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.size = size
        self.min_value = min_value
        self.max_value = max_value
