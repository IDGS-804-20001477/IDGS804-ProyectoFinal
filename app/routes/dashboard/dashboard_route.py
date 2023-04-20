from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required
from flask_security.decorators import roles_required
from ...controllers.dashboard_controller import getLeadingProduct, getPurchasesPerMonth, getSalesPerMonth
from datetime import datetime
from ...models.product import ProductModel
from dateutil.relativedelta import relativedelta

dashboard = Blueprint('dashboard', __name__, url_prefix='/admin/dashboard')


@dashboard.route('/dashboard-index')
@login_required
@roles_required('admin')
def index():
    fecha_actual = datetime.now()
    months = []
    for i in range(12):
        mes_anterior = fecha_actual - relativedelta(months=i)
        months.append(mes_anterior.strftime('%Y-%m'))

    leading_products = getLeadingProduct(months[0])
    purchases_per_month = getPurchasesPerMonth(months[0])
    sales_per_month = getSalesPerMonth(months[0])
    products = ProductModel.query.all()
    return render_template('/admin/dashboard/index_admin.html', leading_products=leading_products, purchases_per_month=purchases_per_month, sales_per_month=sales_per_month, products=products, months=months)
