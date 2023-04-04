from wtforms import Form, StringField, IntegerField, EmailField, validators, DecimalField, SelectField, TextAreaField

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
    
class ProductForm(Form):
    id = IntegerField('Id')
    sku = StringField('Sku')
    name = StringField('Nombre', [
        validators.DataRequired('Campo requerido')
    ])
    price = DecimalField('Precio', places=2, validators=[
        validators.DataRequired('Campo requerido'),
        validators.number_range(min=0, max=3000, message='No puede exceder el precio estipulado por la empresa')
    ])
    size = SelectField('Talla', [
        validators.DataRequired('Campo requerido')
    ], choices=[
        (1, 'XXCH'),
        (2, 'XCH'),
        (3, 'CH'),
        (4, 'M'),
        (5, 'G'),
        (6, 'XG'),
        (7, 'XXG'),
        (8, 'XXXG')
    ])
    min_value = IntegerField('Minimo en inventario', [
        validators.DataRequired('Campo requerido')
    ])
    max_value = IntegerField('Maximo en inventario', [
        validators.DataRequired('Campo requerido')
    ])
    quantity = IntegerField('Cantidad', [
        validators.DataRequired('Campo requerido')
    ])
    description = TextAreaField('Descripcion')