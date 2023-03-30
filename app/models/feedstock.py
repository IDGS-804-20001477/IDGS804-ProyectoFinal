from .measurement_unit import Measurement_Unit
from .provider import Provider


class Feedstock:
    id = 0,
    name = '',
    description = '',
    price = 0.0,
    min_value = 0.0,
    max_value = 0.0,
    status = 0,
    measurement_unit_id = Measurement_Unit.id
    provider_id = Provider.id

    def __init__(self, id, name, description, price, status, min_value, max_value, measurement_unit_id, provider_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.min_value = min_value
        self.max_value = max_value
        self.status = status
        self.measurement_unit_id = measurement_unit_id
        self.provider_id = provider_id
