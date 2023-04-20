from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from ...controllers.dashboard_controller import getLeadingProduct, getPurchasesPerMonth, getSalesPerMonth
from datetime import datetime
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
    month = str(datetime.now().month)
    leading_products = getLeadingProduct(month)
    purchases_per_month = getPurchasesPerMonth(month)
    sales_per_month = getSalesPerMonth(month)
    logger.info('Se muestra el dashboard: %s', current_user.name)
    return render_template('/admin/dashboard/index_admin.html', leading_products=leading_products, purchases_per_month=purchases_per_month, sales_per_month=sales_per_month)
