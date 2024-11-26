from flask import Blueprint
from app.controllers.base_controller import BaseController
from app.services.produtores_services import ProdutorService

bp = Blueprint('produtor', __name__)

class ProdutorController(BaseController):
    def __init__(self):
        super().__init__(ProdutorService)
