#ler arquivo
arquivo = open("dados.txt")

#read - lê o conteúdo do arquivo presente na memória
#chamar o read várias vezes não vai funcionar
conteudo = arquivo.read()

print(arquivo.read())
print(arquivo)
print(conteudo.lower)
arquivo.close()

with open("dados.txt") as arquivo2:
    print('1')
    print('2')
    print('3')

print('4')


with open("dados.txt") as arquivo2:
    arquivo2.read()

with open("dados.txt") as arquivo3:
    linhas = arquivo3.readlines()
    print(linhas)

with open("dados.txt") as arquivo4:
    linhas2 = []
    for linha in arquivo4:
        linhas.append(linha.strip())
    print(linhas)

with open("produtos.csv", "r") as arquivo_produtos:
    produtos = []
    for linha in arquivo_produtos:
        dados_produto = linha.strip().split(".")
        produto = {
            "nome": dados_produto[0],
            "descricao": dados_produto[1],
            "preço": float(dados_produto[2]),
            "imagem": dados_produto[3]
        }
        produtos.append(produto)

print(produtos)

def salvar_produto(nome, descricao, preço, imagem):
    #1: abrir o arquivo em modo append
    with open("produtos.csv", "a") as arquivo_produtos:
    #2: montar a string com os dados separados por .
        texto_produto = f"{nome},{descricao},{preço},{imagem}"
        #3: escrever no arquivo
        arquivo_produtos.write(texto_produto)

    