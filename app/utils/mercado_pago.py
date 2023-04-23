import mercadopago
from ..config import config

sdk = mercadopago.SDK(config['MP_ACCESS_TOKEN'])


def get_preference_body(items):
    preference_data = {
        "items": [
            {
                "title": item['product']['name'],
                "quantity": item['quantity'],
                "unit_price": item['product']['price'],
                "currency_id": "MXN",
            } for item in items
        ],
        "payer": {
            "name": "Juan",
            "surname": "Lopez",
            "email": "user@email.com",
            "phone": {
                "area_code": "11",
                "number": "4444-4444"
            },
            "identification": {
                "type": "DNI",
                "number": "12345678"
            },
            "address": {
                "street_name": "Street",
                "street_number": 123,
                "zip_code": "5700"
            }
        },
        "back_urls": {
            "success": "https://www.success.com",
            "failure": "http://www.failure.com",
            "pending": "http://www.pending.com"
        },
        "notification_url": "https://www.your-site.com/ipn",
        "statement_descriptor": "Lumary Lane",
        "external_reference": "Reference_1234",
    }

    return preference_data
