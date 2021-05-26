from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Deu certoooo"

@app.route("/teste")
def teste():
    return "Este também deu certo"

@app.route("/<nome>")
def nome(nome):
    return "Deu certo, {}".format(nome)


if __name__ == "__main__":
    app.run(host="0.0.0.0")