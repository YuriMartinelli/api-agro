from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import NotFound

class BaseController(MethodView):
    def __init__(self, service_class):
        self.service_class = service_class()

    def handle_error(self, error):
        return jsonify({"error": str(error)}), 400

    def get(self, id=None):
        if id:
            return self.get_one(id)
        else:
            return self.get_all()

    def post(self):
        try:
            data = request.get_json()
            return self.create(data)
        except Exception as e:
            return self.handle_error(e)

    def put(self, id):
        try:
            data = request.get_json()
            return self.update(id, data)
        except Exception as e:
            return self.handle_error(e)

    def delete(self, id):
        try:
            return self.delete(id)
        except Exception as e:
            return self.handle_error(e)

    def get_all(self):
        try:
            items = self.service_class.get_all()
            return jsonify(items), 200
        except Exception as e:
            return self.handle_error(e)

    def get_one(self, id):
        try:
            item = self.service_class.get(id)
            if not item:
                raise NotFound(f"Item com ID {id} não encontrado.")
            return jsonify(item), 200
        except Exception as e:
            return self.handle_error(e)

    def create(self, data):
        try:
            item = self.service_class.create(data)
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
