# API Smart Fit

## Descrição

Esta API REST foi desenvolvida em Python utilizando o framework Flask com o objetivo de realizar o gerenciamento de alunos da Smart Fit. O sistema permite cadastrar, consultar, atualizar e excluir alunos por meio das operações CRUD. Cada aluno possui as seguintes informações: nome, CPF e idade.

## Tecnologias Utilizadas

* Python
* Flask
* SQLite

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

* **Routes:** responsáveis pelas rotas da aplicação.
* **Controllers:** responsáveis pela lógica de negócio.
* **Models:** responsáveis pela comunicação com o banco de dados.

## Instalação

1. Faça o download ou clone o projeto.
2. Acesse a pasta do projeto pelo terminal.
3. Instale as dependências utilizando o comando:

```bash
pip install -r requirements.txt
```

Caso não utilize o arquivo `requirements.txt`, instale o Flask com o comando:

```bash
pip install flask
```

## Como Executar

No terminal, execute o comando:

```bash
python app.py
```

Após iniciar a aplicação, a API ficará disponível no endereço:

```
http://localhost:5000
```

## Endpoints da API

### GET /alunos

Retorna a lista de todos os alunos cadastrados.

### POST /alunos

Realiza o cadastro de um novo aluno.

Exemplo de JSON:

```json
{
    "nome": "João Silva",
    "cpf": "11111111111",
    "idade": 22
}
```

### PUT /alunos/{id}

Atualiza os dados de um aluno existente por meio do seu ID.

### DELETE /alunos/{id}

Remove um aluno do banco de dados utilizando seu ID.

## Banco de Dados

A aplicação utiliza o banco de dados SQLite para armazenar as informações dos alunos. Para demonstrar o funcionamento da API, foram cadastrados no mínimo cinco alunos contendo nome, CPF e idade.

## Testes

Todos os endpoints da API foram testados utilizando o Postman, verificando o correto funcionamento das operações de cadastro (POST), consulta (GET), atualização (PUT) e exclusão (DELETE).

## Autor

Projeto desenvolvido como atividade acadêmica para a disciplina de Desenvolvimento Web utilizando Python e Flask.
