from flask import request, jsonify
from models.aluno_model import AlunoModel

class AlunoController:
    @staticmethod
    def listar():
        
        alunos = AlunoModel.listar()
        return jsonify(alunos)
    
    @staticmethod
    def cadastrar():
        
        dados = request.get_json()

        nome = dados ["nome"]
        cpf = dados ["cpf"]
        cpf = dados ["idade"]

        AlunoModel.inserir(nome, cpf, idade)

        return jsonify({"mensagem": "Aluno cadastrado com sucesso!"})
    
    @staticmethod
    def atualizar(id):
        dados = request.get_json()
        nome = dados["nome"]
        cpf = dados["cpf"]
        idade = dados["idade"]

        AlunoModel.atualizar(id, nome, cpf, idade)

        return jsonify({"mensagem": "Aluno atualizado com sucesso!"})


    @staticmethod
    def excluir(id):

        AlunoModel.excluir(id)

        return jsonify({"mensagem": "Aluno removido com sucesso!"})