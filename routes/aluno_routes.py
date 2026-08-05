from flask import Blueprint
from controllers.aluno_controller import AlunoController

aluno_bp = Blueprint("alunos", __name__)

aluno_bp.route("/alunos", methods=["GET"])(AlunoController.listar)

aluno_bp.route("/alunos", methods=["POST"])(AlunoController.cadastrar)

aluno_bp.route("/alunos/<int:id>", methods=["PUT"])(AlunoController.atualizar)

aluno_bp.route("/alunos/<int:id>", methods=["DELETE"])(AlunoController.excluir)