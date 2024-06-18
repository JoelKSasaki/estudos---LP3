#importa a classe Flask do módulo flask
from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

#instancia um objeto flask que representa a aplicação
app = Flask(__name__)

#função: função com retorno

#página home
@app.route("/")
def home():
    return render_template("home.html")

#página contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

#página produtos
@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome" : "Coca-cola", "descricao": "Mata a sede"},
        {"nome" : "Cheetos", "descricao": "Cheiro forte de queijo"},
        {"nome" : "Chocolate", "descricao": "Excelente"}
    ]

    return render_template("produtos.html", produtos = lista_produtos)

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