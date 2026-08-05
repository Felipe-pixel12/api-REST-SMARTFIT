from database import get_connection

class AlunoModel:

    @staticmethod
    def listar():
        conn = get_connection()

        alunos = conn.execute("SELECT * FROM aluno").fetchall()

        conn.close()

        return[dict(aluno) for aluno in alunos]
    

    @staticmethod
    def inserir(nome, cpf, idade):

        conn = get_connection()

        conn.execute(
            "UPTADE alunos SET nome=?, cpf=?, idade=?, WHERE id=?",
            (nome, cpf, idade, id)
        )

        conn.comit()

        conn.close()

    @staticmethod
    def excluir(id):

        conn = get_connection()

        conn.execute(
            "DELETE FROM alunos WHERE id=?",
            (id,)
        )

        conn.commit()

        conn.close()