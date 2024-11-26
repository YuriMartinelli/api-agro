from app.models.produtores import Produtor
from app.services.base_service import BaseService
from werkzeug.exceptions import BadRequest

class ProdutorService(BaseService):
    def __init__(self):
        super().__init__(Produtor)

    def validate(self, data):
        """Sobrescreve o método de validação para incluir regras específicas de produtor."""
        if not self.validar_cpf_cnpj(data['cpf_cnpj']):
            raise BadRequest("CPF ou CNPJ inválido.")
        
        if data['area_agricultavel'] + data['area_vegetacao'] > data['area_total']:
            raise BadRequest("A soma da área agricultável e da vegetação não pode ser maior que a área total.")

    def criar_produtor(self, data):
        """Método para criar um novo produtor e realizar validações"""
        self.validate(data)
        return self.create(data)
    
    def atualizar_produtor(self, id, data):
        """Método para atualizar um produtor e realizar validações"""
        self.validate(data)
        return self.update(id, data)
