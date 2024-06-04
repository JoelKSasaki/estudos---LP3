class Carro:
    def __init__(self, modelo = '', cor = '', ano = 0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        
carro1 = Carro(modelo='Fiat', cor='vermelho', ano=2000)

class Restaurante:
    def __init__(this, nome='', categoria='', ativo=False, local='', estrelas=''):
        this.nome = nome
        this.categoria = categoria
        this.ativo = ativo
        this.local = local
        this.estrelas = estrelas
    def __str__(this) -> str:
        return f'{this.nome} | {this.categoria}'
            
restaurante_exemplo = Restaurante(nome='Spolleto', categoria='Gourmet', ativo=True, local='Faria Lima', estrelas=4.5)
novo_restaurante = Restaurante(nome='Popeyes', categoria='Fast Food')
print(novo_restaurante)

class Cliente:
    def __init__(this, nome= '', idade= 0, cpf= '', telefone= ''):
        this.nome = nome
        this.idade = idade
        this.cpf = cpf
        this.telefone = telefone
    def __str__(this):
        return f'{this.nome} | {this.idade} | {this.telefone}'
        
cliente1 = Cliente(nome= 'Rafael', idade= 25, cpf= '32758934709', telefone= '924823895')
cliente2 = Cliente(nome= 'Gabriel Lula', idade= 40, cpf= '0385905092', telefone= '902387473')
cliente3 = Cliente(nome= 'Sarah', idade= 22, cpf= '12738855676', telefone= '957643386')

print(vars(cliente2))
print(cliente3)