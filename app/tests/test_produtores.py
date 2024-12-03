def test_create_produtor(client):
    response = client.post("/produtores", json={
        "nome": "Jorgao",
        "cpf_cnpj": "00.000.000/0001-04",
        "nome_fazenda": "querencia 3",
        "cidade": "Lages",
        "estado": "SC",
        "area_total": 13,
        "area_agricultavel": 7,
        "area_vegetacao": 4,
        "culturas": ["Banana", "Cenoura", "Cana de açucar"]
    })
    assert response.status_code == 201
    assert response.json["cpf_cnpj"] == "00.000.000/0001-04"

def test_create_produtor_invalid_area(client):
    response = client.post("/produtores", json={
        "cpf_cnpj": "98765432100",
        "nome": "Produtor Inválido",
        "nome_fazenda": "Fazenda Inválida",
        "cidade": "Cidade Inválida",
        "estado": "Estado Inválido",
        "area_total": 100.0,
        "area_agricultavel": 80.0,
        "area_vegetacao": 30.0,  
        "culturas": "Algodão"
    })
    assert response.status_code == 400
    assert "não pode ser maior que a área total" in response.json()["error"]