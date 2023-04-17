class User:
    id = 0,
    email = '',
    password = '',
    type = 0,
    name = '',
    lastname = '',
    address = '',
    phone = ''
    
    def __init__(self, id, email, password, type, name, lastname, address, phone):
        self.id = id
        self.email = email
        self.password = password
        self.type = type
        self.name = name
        self.lastname = lastname
        self.address = address
        self.phone = phone