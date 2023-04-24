from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from ...controllers.dashboard_controller import getLeadingProduct, getPurchasesPerMonth, getSalesPerMonth
from datetime import datetime
from sqlalchemy import extract
from ...models.product import ProductModel
from dateutil.relativedelta import relativedelta
from ...models.sale_order import SaleOrder
import logging

dashboard = Blueprint('dashboard', __name__, url_prefix='/admin/dashboard')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@dashboard.route('/dashboard-index')
@login_required
@roles_required('admin')
def index():
    fecha_actual = datetime.now()
    months = []
    earnings = []
    for i in range(12):
        mes_anterior = fecha_actual - relativedelta(months=i)
        sales = SaleOrder.query.filter(
            extract('month', SaleOrder.created_at) == extract('month', mes_anterior)).all()
        earnings = [len(sales), *earnings]
        months = [mes_anterior.strftime('%Y-%m'), *months]

    products = ProductModel.query.all()
    logger.info('Se muestra el dashboard: %s', current_user.name)
    return render_template('/admin/dashboard/index_admin.html', products=products, months=months, earnings=earnings)
