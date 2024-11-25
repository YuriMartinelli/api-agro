from flask import Blueprint, jsonify, request
from app.models.produtores import Produtor
from app.database import db
from app.utils.validadores import validar_cnpj, validar_cpf

bp = Blueprint('produtores', __name__, url_prefix='/produtores')

@bp.route('', methods=['POST'])
def cadastrar_produtor():
    dados = request.json
    cpf_cnpj = dados.get('cpf_cnpj')

    if not cpf_cnpj:
        return jsonify({"error": "CPF ou CNPJ é obrigatório!"}), 400

    # Validação de CPF ou CNPJ usando regex
    if len(cpf_cnpj) == 11 and not validar_cpf(cpf_cnpj):
        return jsonify({"error": "CPF inválido!"}), 400
    elif len(cpf_cnpj) == 14 and not validar_cnpj(cpf_cnpj):
        return jsonify({"error": "CNPJ inválido!"}), 400

    produtor = Produtor(nome=dados['nome'], cpf_cnpj=cpf_cnpj)
    db.session.add(produtor)
    db.session.commit()

    return jsonify({"message": "Produtor cadastrado com sucesso!"}), 201