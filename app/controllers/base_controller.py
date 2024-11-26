from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import NotFound

class BaseController(MethodView):
    def __init__(self, service_class):
        self.service_class = service_class()

    def handle_error(self, error):
        return jsonify({"error": str(error)}), 400

    def create(self, data):
        try:
            item = self.service_class.criar_produtor(data)
            return jsonify(item), 201
        except Exception as e:
            return self.handle_error(e)

    def update(self, id, data):
        try:
            item = self.service_class.update(id, data)
            return jsonify(item), 200
        except Exception as e:
            return self.handle_error(e)

    def delete(self, id):
        try:
            self.service_class.delete(id)
            return '', 204
        except Exception as e:
            return self.handle_error(e)
