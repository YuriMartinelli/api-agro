# API Agro

## Descrição do Projeto

A API Agro é um sistema backend desenvolvido em Python utilizando o framework Flask, projetado para gerenciar dados relacionados à produção agrícola. Ela oferece funcionalidades para cadastro e consulta de produtores, bem como um dashboard para visualização de dados agregados. O projeto segue uma arquitetura modular, com controllers, models, services e rotas bem definidos, além de incluir testes e migrações de banco de dados.

## Funcionalidades

*   **Gerenciamento de Produtores:** Cadastro, consulta, atualização e exclusão de informações de produtores rurais.
*   **Dashboard de Dados:** Visualização de dados agregados sobre a produção agrícola.
*   **Estrutura Modular:** Organização clara do código em camadas para facilitar a manutenção e escalabilidade.
*   **Testes Automatizados:** Conjunto de testes para garantir a integridade e o funcionamento correto da API.
*   **Migrações de Banco de Dados:** Gerenciamento de alterações no esquema do banco de dados utilizando Alembic.

## Tecnologias Utilizadas

*   **Linguagem:** Python
*   **Framework Web:** Flask
*   **ORM:** SQLAlchemy
*   **Migrações de Banco de Dados:** Alembic
*   **Banco de Dados:** PostgreSQL (recomendado, configurável via variáveis de ambiente)
*   **Outras Bibliotecas:** Flask-RESTful, python-dotenv, requests, etc. (ver `requirements.txt`)

## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3.x e o `pip` instalados. É altamente recomendável usar um ambiente virtual.

### Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/YuriMartinelli/api-agro.git
    cd api-agro
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```
    DATABASE_URL=postgresql://user:password@host:port/database_name
    # Exemplo: DATABASE_URL=postgresql://postgres:postgres@localhost:5432/api_agro_db
    ```
    Substitua `user`, `password`, `host`, `port` e `database_name` pelas suas credenciais do PostgreSQL.

5.  **Execute as migrações do banco de dados:**
    ```bash
    flask db upgrade
    ```

### Executando a Aplicação

Para iniciar o servidor de desenvolvimento:

```bash
flask run
```

A API estará disponível em `http://127.0.0.1:5000`.

## Exemplos de Uso da API

### Produtores

*   **Listar todos os produtores:**
    ```bash
    curl -X GET http://127.0.0.1:5000/produtores
    ```

*   **Criar um novo produtor:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"nome": "João Silva", "cpf": "123.456.789-00", "fazenda": "Fazenda Esperança", "cidade": "São Paulo", "estado": "SP", "area_total_hectares": 1000, "area_agricultavel_hectares": 800, "area_vegetacao_hectares": 200}' http://127.0.0.1:5000/produtores
    ```

*   **Obter produtor por ID:**
    ```bash
    curl -X GET http://127.0.0.1:5000/produtores/<id_do_produtor>
    ```

*   **Atualizar produtor:**
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"nome": "João Silva Atualizado"}' http://127.0.0.1:5000/produtores/<id_do_produtor>
    ```

*   **Deletar produtor:**
    ```bash
    curl -X DELETE http://127.0.0.1:5000/produtores/<id_do_produtor>
    ```

### Dashboard

*   **Obter dados do dashboard:**
    ```bash
    curl -X GET http://127.0.0.1:5000/dashboard
    ```

## Executando os Testes

Para executar os testes automatizados do projeto:

```bash
pytest
```

## Status do Projeto

Este projeto está em desenvolvimento ativo. Novas funcionalidades e melhorias são adicionadas regularmente.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. (Assumindo licença MIT, caso contrário, ajuste conforme a licença real do projeto)

