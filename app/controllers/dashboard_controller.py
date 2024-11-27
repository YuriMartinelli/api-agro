from app.controllers.base_controller import BaseController
from app.services.dashboard_service import DashboardService
from flask import jsonify


class DashboardController:
    def __init__(self):
        self.service = DashboardService()

    def get_dashboard_data(self):
        try:
            data = self.service.get_dashboard_data()
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
