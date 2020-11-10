from flask import Flask

app = Flask("Exemplo")


@app.route("/")
def index():
    return "Deu certoooo"

@app.route("/teste")
def teste():
    return "Este também deu certo"


if __name__ == "__main__":
    app.run(host="0.0.0.0")