from flask import Blueprint

from app.controllers.dashboard_controller import DashboardController

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

_dashboardController = DashboardController()

@bp.route('', methods=['GET'])
def get_dashboard():
    return _dashboardController.get_dashboard_data()
