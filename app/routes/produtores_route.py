from flask import Blueprint, request
from app.controllers.produtores_controller import ProdutorController

bp = Blueprint('produtores', __name__, url_prefix='/produtores')

_produtorController = ProdutorController()

@bp.route('', methods=['POST'])
def cadastrar_produtor():
    return _produtorController.create(request.json)

@bp.route('', methods=['GET'])
def listar_produtores():
    return _produtorController.get_all()

@bp.route('/<int:id>', methods=['GET'])
def buscar_produtor(id):
    return _produtorController.get_by_id(id)

@bp.route('/<int:id>', methods=['PUT'])
def atualizar_produtor(id):
    return _produtorController.update(id, request.json)

@bp.route('/<int:id>', methods=['DELETE'])
def deletar_produtor(id):
    return _produtorController.delete(id)