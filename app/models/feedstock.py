from .unit_of_measurement import Unit_Of_Measurement
from .provider import Provider


class Feedstock:
    id = 0,
    sku = '',
    name = '',
    description = '',
    price = 0.0,
    min_value = 0.0,
    max_value = 0.0,
    status = 0,
    unit_of_measurement_id = Unit_Of_Measurement.id
    provider_id = Provider.id

    def __init__(self, id, sku, name, description, price, status, min_value, max_value, unit_of_measurement_id, provider_id):
        self.id = id
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.min_value = min_value
        self.max_value = max_value
        self.status = status
        self.unit_of_measurement_id = unit_of_measurement_id
        self.provider_id = provider_id
