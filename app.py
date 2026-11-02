from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/programacao")
def programacao():
    return render_template("programacao.html")

@app.route("/detalhes")
def detalhes():
    return render_template("detalhes.html")

@app.route("/realizadas")
def realizadas():
    return render_template("realizadas.html")

@app.route("/documentos")
def documentos():
    return render_template("documentos.html")

if __name__ == "__main__":
    app.run(debug=False)
