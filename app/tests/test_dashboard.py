
def test_dashboard(client):
    client.post("/produtores", json={
        "cpf_cnpj": "12.123.123/0001-00",
        "nome": "Produtor A",
        "nome_fazenda": "Fazenda A",
        "cidade": "Cidade A",
        "estado": "SP",
        "area_total": 150.0,
        "area_agricultavel": 80.0,
        "area_vegetacao": 70.0,
        "culturas": "Soja"
    })
    client.post("/produtores", json={
        "cpf_cnpj": "12.124.124/0001-00",
        "nome": "Produtor B",
        "nome_fazenda": "Fazenda B",
        "cidade": "Cidade B",
        "estado": "MG",
        "area_total": 200.0,
        "area_agricultavel": 100.0,
        "area_vegetacao": 100.0,
        "culturas": "Milho"
    })

    response = client.get("/dashboard")
    assert response.status_code == 200
    assert response.json["total_fazendas"] == 2
    assert response.json["total_hectares"] == 350.0