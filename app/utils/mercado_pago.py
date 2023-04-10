import mercadopago
from ..config import config

print(config)
sdk = mercadopago.SDK(config['MP_ACCESS_TOKEN'])
