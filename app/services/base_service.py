from app import db
from werkzeug.exceptions import BadRequest

class BaseService:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return [item.as_dict() for item in self.model.query.all()]

    def get(self, id):
        return self.model.query.filter_by(id=id).first().as_dict()

    def create(self, data):
        item = self.model(**data)
        db.session.add(item)
        db.session.commit()
        return item.as_dict()

    def update(self, id, data):
        item = self.model.query.filter_by(id=id).first()
        if not item:
            raise BadRequest(f"Item com ID {id} não encontrado.")

        for key, value in data.items():
            setattr(item, key, value)

        db.session.commit()
        return item.as_dict()

    def delete(self, id):
        item = self.model.query.filter_by(id=id).first()
        if not item:
            raise BadRequest(f"Item com ID {id} não encontrado.")

        db.session.delete(item)
        db.session.commit()

    def validate(self, data):
        pass
