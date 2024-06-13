#importa a classe Flask do módulo flask
from flask import Flask

#instancia um objeto flask que representa a aplicação
app = Flask("minha aplicação")

#função: função com retorno

#página home
@app.route("/")
def home():
    return "<h1>Home page </h1>"

#página contato
@app.route("/contato")
def contato():
    return "<h1>Contato </h1>"

#página produtos
@app.route("/produtos")
def produtos():
    return "<h1>Produtos</h1>"