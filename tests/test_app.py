
import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_pagina_inicial(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert "Integra UnB" in resposta.get_data(as_text=True)


def test_programacao(client):
    resposta = client.get("/programacao")

    assert resposta.status_code == 200
    assert "2º Encontro dos Gestores" in resposta.get_data(
        as_text=True
    )


def test_detalhes(client):
    resposta = client.get("/detalhes")

    assert resposta.status_code == 200
    assert "Em planejamento" in resposta.get_data(
        as_text=True
    )


def test_pagina_inexistente(client):
    resposta = client.get("/pagina-inexistente")

    assert resposta.status_code == 404
