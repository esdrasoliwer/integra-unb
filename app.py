
from flask import Flask, render_template, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Integra UnB</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background: #f5f7f9;
            color: #253344;
        }
        header {
            background: #164c3b;
            color: white;
            padding: 24px;
        }
        main {
            max-width: 900px;
            margin: 32px auto;
            padding: 20px;
        }
        .card {
            background: white;
            border-radius: 10px;
            padding: 24px;
            margin-bottom: 16px;
        }
        a { color: #164c3b; }
    </style>
</head>
<body>
    <header>
        <h1>Integra UnB</h1>
        <p>Comissão de Integração e Eventos — DGP/UnB</p>
    </header>
    <main>
        <section class="card">
            <h2>Bem-vindo ao Integra UnB!</h2>
            <p>Conheça as iniciativas de integração, reconhecimento,
            desenvolvimento e bem-estar do DGP.</p>
            <a href="/programacao">Consultar programação</a>
        </section>
    </main>
</body>
</html>
"""


@app.route("/")
def inicio():
    return render_template_string(HTML)



@app.route("/programacao")
def programacao():
    return render_template("programacao.html")


@app.route("/detalhes")
def detalhes():
    return render_template("detalhes.html")


if __name__ == "__main__":
    app.run(debug=False)
