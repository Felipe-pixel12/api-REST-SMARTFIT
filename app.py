from flask import Flask
from database import criar_tabela
from routes.aluno_routes import aluno_bp

app = Flask(__name__)

criar_tabela()

app.register_blueprint(aluno_bp)

if __name__ == "__main__":
    app.run(debug=True)