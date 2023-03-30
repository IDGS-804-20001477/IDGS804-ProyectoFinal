class Provider:
    id = 0
    business_name = ''
    contact_name = ''
    contact_email = ''
    contact_phone = ''
    address = ''

    def __init__(self, id, business_name, contact_name, contact_email, contact_phone, address):
        self.id = id
        self.business_name = business_name
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.address = address
