from flask import Blueprint, jsonify, request
from app.controllers.produtores_controller import ProdutorController
from app.models.produtores import Produtor
from app.database import db
from app.utils.validadores import validar_cnpj, validar_cpf

bp = Blueprint('produtores', __name__, url_prefix='/produtores')

_produtorController = ProdutorController()

@bp.route('', methods=['POST'])
def cadastrar_produtor():
    return _produtorController.create(request.json)