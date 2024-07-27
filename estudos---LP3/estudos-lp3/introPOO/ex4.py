class ClienteBanco: 
    def __init__(this, nome, idade, endereco, cpf, profissao):
        this._nome = nome
        this._idade = idade
        this._endereco = endereco
        this._cpf = cpf
        this._profissao = profissao

cliente1 = ClienteBanco("Pedro", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Carlos", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Fabio", 40, "Rua C", "111.222.333-44", "Frontend")

print(cliente1)