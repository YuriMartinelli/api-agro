from flask import Blueprint
from app.controllers.base_controller import BaseController
from app.services.produtores_services import ProdutorService

# Criar o Blueprint do controlador
bp = Blueprint('produtor', __name__)

# Herança do controller base, passando o ProdutorService
class ProdutorController(BaseController):
    def __init__(self):
        super().__init__(ProdutorService)

# Registrar as rotas
produtor_view = ProdutorController.as_view('produtor')
bp.add_url_rule('/produtores/', view_func=produtor_view, methods=['GET', 'POST'])
bp.add_url_rule('/produtores/<int:id>/', view_func=produtor_view, methods=['GET', 'PUT', 'DELETE'])
