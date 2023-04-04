from wtforms import Form, StringField, IntegerField, EmailField, validators

class ProviderForm(Form):
    id = IntegerField('Id')
    business_name = StringField('Razón Social')
    contact_name = StringField('Nombre de contacto', [
        validators.DataRequired('Campo requerido')
    ])
    contact_email = EmailField('Email de contacto', [
        validators.DataRequired('Campo requerido')
    ])
    contact_phone = StringField('Telefono de contacto', [
        validators.DataRequired('Campo requerido'),
        validators.Email('Debes ingresar un email valido')
    ])
    address = StringField('Direccion', [
        validators.DataRequired('Campo requerido')
    ])