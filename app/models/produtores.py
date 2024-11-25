from app.database import db


class Produtor(db.Model):
    __tablename__ = 'produtores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf_cnpj = db.Column(db.String(18), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Produtor {self.nome}>"