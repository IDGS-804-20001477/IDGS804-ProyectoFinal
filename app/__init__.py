from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore
from .models.db import db
from .models.auth import User, Role
from flask_wtf.csrf import CSRFProtect
import os

userDataStore = SQLAlchemySessionUserDatastore(db.session, User, Role)
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1/luminary_lane"
    app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
    app.config['SECURITY_PASSWORD_SALT'] = 'thisissecretsalt'

    csrf.init_app(app)
    db.init_app(app)

    @app.before_first_request
    def create_all():
        db.create_all()

    security = Security(app, userDataStore)

    from .routes.auth.auth_route import auth as auth_blueprint
    from .routes.feedstocks.feedstocks_route import feedstocks as feedstocks_blueprint
    from .routes.main.main_route import main as main_blueprint
    from .routes.products.products_route import products as products_blueprint
    from .routes.providers.providers_route import providers as providers_blueprint
    from .routes.purchase_orders.purchase_orders_route import purchase_orders as purchase_orders_blueprint
    from .routes.recipes.recipes_route import recipes as recipes_blueprint
    from .routes.sale_orders.sale_orders_route import sale_orders as sale_orders_blueprint
    from .routes.users.users_route import users as users_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(feedstocks_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(products_blueprint)
    app.register_blueprint(providers_blueprint)
    app.register_blueprint(purchase_orders_blueprint)
    app.register_blueprint(recipes_blueprint)
    app.register_blueprint(sale_orders_blueprint)
    app.register_blueprint(users_blueprint)

    return app
