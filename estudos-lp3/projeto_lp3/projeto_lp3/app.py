#importa a classe Flask do módulo flask
from flask import Flask
from validate_docbr import CPF, CNPJ

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
    return "<h1>Produtos </h1>"

#/gerar cpf (devolve um cpf aleatório)
#/gerar cnpj (devolve um cnpj aleatório)
#/servicos (devolve um título com "Nossos Serviços")

@app.route("/cpf")
def cpf():
    cpf = CPF()
    return f"<h1>Gerar CPF</h1>: {cpf.generate(mask=True)}"

@app.route("/cnpj")
def cnpj():
    cnpj = CNPJ()
    return f"<h1>Gerar CPF</h1>: {cnpj.generate(mask=True)}"

def cnpj():
    cnpj = cnpj.generate((True))
    return cnpj

@app.route("/serviços")
def servico():
    return "<h2>Nossos Serviços<h2>"


app.run()