import os
import datetime

from flask import Flask, jsonify
from flask_mongoengine import MongoEngine


app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": os.getenv("DATABASE_NAME", "atletica"),
    "host": os.getenv("DATABASE_HOST", "mongodb-atletica"),
    "username": os.getenv("DATABASE_USER", "admin"),
    "password": os.getenv("DATABASE_PASSWORD", "admin"),
    'authentication_source': 'admin'
}

db = MongoEngine()


class EventoAtletica(db.Document):
    nome = db.StringField(required=True)
    descricao = db.StringField()
    organizadores = db.ListField()
    participantes = db.ListField()
    localizacao = db.DictField()
    data = db.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.nome

db.init_app(app)

@app.route("/")
def index():
    return jsonify(EventoAtletica.objects.all())

@app.route("/<nome>")
def nome(nome):
    return "Deu certo, {}".format(nome)


if __name__ == "__main__":
    app.run(host="0.0.0.0")