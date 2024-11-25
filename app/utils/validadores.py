import re

def validar_cpf(cpf):
    regex_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if re.match(regex_cpf, cpf):
        return True
    return False

def validar_cnpj(cnpj):
    regex_cnpj = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
    if re.match(regex_cnpj, cnpj):
        return True
    return False
