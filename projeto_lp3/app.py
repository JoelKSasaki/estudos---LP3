#importa a classe Flask do módulo flask
from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

lista_produtos = [
        {"nome" : "Coca-cola", "descricao": "Mata a sede"},
        {"nome" : "Cheetos", "descricao": "Cheiro forte de queijo"},
        {"nome" : "Chocolate", "descricao": "Excelente"}
    ]

#instancia um objeto flask que representa a aplicação
app = Flask(__name__)

# função: função com retorno

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
    

    return render_template("produtos.html", produtos = lista_produtos)

#/gerar cpf (devolve um cpf aleatório)
#/gerar cnpj (devolve um cnpj aleatório)
#/servicos (devolve um título com "Nossos Serviços")

@app.route("/cpf")
def cpf():
    cpf = CPF()
    return render_template("cpf.html", cpf = cpf.generate(True))

@app.route("/cnpj")
def cnpj():
    cnpj = CNPJ()
    return render_template("cnpj.html", cnpj = cnpj.generate(True))

@app.route("/serviços")
def servico():
    return "<h2>Nossos Serviços<h2>"

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos", method=['POST'])
def salvar_produtos():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = {"nome": nome, "descricao": descricao}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos=lista_produtos)

if __name__ == "__main__":
    app.run(port=5001)

'''<h1>Gerar CNPJ</h1>: {cnpj.generate(mask=True)}'''