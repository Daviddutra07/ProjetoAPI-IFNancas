# ProjetoAPI-IFNancas

Esse projeto acadêmico é um **mini sistema web de controle financeiro** , para gerenciar as finanças pessoais.
O sistema permite o **cadastro, listagem, edição, remoção e filtragem** de entradas e saídas financeiras, sem uso de banco de dados, utilizando um arquivo JSON como armazenamento.

- **Backend:** API REST em Flask  
- **Frontend:** Interface web consumindo a API via `fetch`  
- **Persistência:** Arquivo JSON (`items.json`)  

---

## Tecnologias Utilizadas

- Python 3  
- Flask  
- Flask-CORS  
- HTML  
- CSS (TailwindCSS)  
- JavaScript (Fetch API)  

> Aviso: O projeto **não utiliza React**, pois a proposta permite outras soluções front-end.

---

## Como rodar o Backend

### 1. Abra um terminal
- PowerShell ou CMD

### 2. Navegue até a pasta do backend (Após Clonar o Repositório)

```bash
cd backend

# Criar e Ativar o Ambiente Virtual
python -m venv .venv
.venv\Scripts\activate

#Baixar as dependências
pip install -r requirements.txt

#Executar o código
flask run
```

---

O backend estará rodando em: http://127.0.0.1:5000

## Como rodar o FrontEnd

### Abra outro Terminal

### 2. Navegue até a pasta do frontend

```bash
cd frontend

# Crie um servidor web simples
python -m http.server 8000

```
Acesse no navegador http://localhost:8000

## Funcionamento da API

A API possui os seguintes endpoints:

- `GET /items` → Lista todos os itens
- `GET /items?id` → Retorna um item específico
- `POST /items` → Cria um novo item
- `PUT /items/<id>` → Atualiza um item
- `DELETE /items/<id>` → Remove um item
- `PATCH /items/<id>/status` → Altera apenas o status do item

---

## Regras de Validação

As validações são realizadas **no backend**, garantindo a integridade dos dados enviados para a API.

### Título
- Obrigatório  
- Deve conter **no mínimo 3 caracteres**

### Valor
- Deve ser numérico  
- Deve ser **maior ou igual a zero**

### Tipo
Valores permitidos:
- `entrada`
- `saida`

### Status
Valores permitidos:
- `ativo`
- `concluido`
- `arquivado`

> Em caso de erro de validação, a API retorna **HTTP 400** com uma mensagem clara em **JSON**, e o frontend exibe um **feedback visual**.

## API Endpoints
Os endpoints da API necessários na proposta do projeto 

---

### GET /items
```bash
GET /items - Lista todos os itens cadastrados.
```
#### Query Params 
- `tipo` → filtra por tipo (`entrada` ou `saida`)
- `status` → filtra por status (`ativo`, `concluido`, `arquivado`)

#### Exemplo de Request
- GET /items
- GET /items?tipo=entrada
- GET /items?status=ativo
- GET /items?tipo=saida&status=concluido


#### Exemplo de Response — 200 OK
```json
[
  {
    "id": 1,
    "titulo": "Salário",
    "tipo": "entrada",
    "status": "ativo",
    "valor": 30000,
    "data": "2026-01-30"
  },
  {
    "id": 2,
    "titulo": "Conta de Luz",
    "tipo": "saida",
    "status": "ativo",
    "valor": 1200,
    "data": "2026-02-04"
  }
]
```
---

### GET /items/:id
```bash
GET /items/:id - Retorna um item específico pelo ID.
```

#### Exemplo de Request
 - GET /items/1
#### Exemplo de Response — 200 OK
```json
    {
    "id": 1,
    "titulo": "Salário",
    "tipo": "entrada",
    "status": "ativo",
    "valor": 30000,
    "data": "2026-01-30"
    }
```

#### Erro — 404 Not Found
```json
{
  "error": "Item não encontrado"
}
```
---

### POST /items
```bash
POST /items - Cria um novo item.
```

#### Exemplo de Request

```json
{
  "titulo": "Internet",
  "tipo": "saida",
  "status": "ativo",
  "valor": 99.90,
  "data": "2026-02-01"
}
```

#### Exemplo de Response — 201 Created
```json
{
  "id": 3,
  "titulo": "Internet",
  "tipo": "saida",
  "status": "ativo",
  "valor": 99.9,
  "data": "2026-02-01"
}
```

#### Erro de Validação — 400 Bad Request

```json
{
  "error": "Titulo é obrigatório e deve ter no mínimo 3 caracteres"
}
```

---

### PUT /items/:id
```bash
PUT /items/:id - Edita completamente um item existente.
```

#### Exemplo de Request
```json
{
  "titulo": "Internet Fibra",
  "tipo": "saida",
  "status": "concluido",
  "valor": 109.90,
  "data": "2026-02-01"
}
```

#### Exemplo de Response — 200 OK

```json
{
  "id": 3,
  "titulo": "Internet Fibra",
  "tipo": "saida",
  "status": "concluido",
  "valor": 109.9,
  "data": "2026-02-01"
}
```

---

### PATCH /items/:id/status
```bash
PATCH /items/:id/status - Atualiza apenas o status de um item.
```

#### Exemplo de Request
```json
{
  "status": "arquivado"
}
```
#### Exemplo de Response — 200 OK
```json
{
  "id": 3,
  "titulo": "Internet Fibra",
  "tipo": "saida",
  "status": "arquivado",
  "valor": 109.9,
  "data": "2026-02-01"
}
```

---

### DELETE /items/:id
```bash
DELETE /items/:id - Remove um item pelo ID.
```

#### Exemplo de Request
- DELETE /items/3

#### Exemplo de Response — 200 OK

```json
{
  "message": "Item removido"
}
```

## Sistema Funcionando

![Sistema funcionando](gif/if-nancas.gif)