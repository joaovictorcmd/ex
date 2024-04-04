from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)
app.run(debug=True)

frutas = []
registros = []


@app.route("/", methods=["GET", "POST"])
def principal():
    # frutas = ["Morango", "Uva", "Maça", "Laranja", "Mamao", "Pera", "Goiaba"]

    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))

    return render_template("index.html", frutas=frutas)


@app.route("/sobre", methods=["GET", "POST"])
def sobre():

    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append(
                {"aluno": request.form.get("aluno"), "nota": request.form.get("nota")}
            )

    return render_template("sobre.html", registros=registros)


@app.route("/filmes")
def filmes():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3d3ead3c05d27f6eb1d604befda8b752"
    resposta = urllib.request.urlopen(url)  # Request to server
    dados = resposta.read()  # Read the response given from server
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata["results"])


# Debug mode
if __name__ == "__main__":
    app.run(debug=True)

# http://127.0.0.1:5000/
