#uma classe é o que abrange as características de um objeto
#Atributos: características do objeto

'''__init__: irá gerar um método construtor. É chamado automaticamente quando uma nova instância de classe é criada
método construtor: sempre chamado quando criamos uma instância de um objeto e espera uma informação
Quando definirmos um objeto, todas as suas informações devem ser do objeto original
this: se trata do objeto referenciado naquele momento
'''

#é possível adicionar, criar e retirar atributos dentro de uma classe

#para criar um novo objeto a partir da sua classe, é necessário instanciá-lo
#Objeto: instância de uma classe

#método para os objetos da classe

#__nome da classe__: método especial que toda classe Python possui
#dir: exibe todos os atributos que o objeto possui
'''vars: exibe o objeto em forma de dicionário
Sem isso, o Python tenta exibir em forma de texto (String)
__str__: mostra o objeto em formato de texto
'''
#A informação que ele exibe, de momento, é um objeto da classe Restaurante. Ele mostra apenas o local da memória onde está armazenado aquele objeto.
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    #o _ antes do atrbuto mostra que ele está PROTEGIDO para informar que o atributo não deve ser modificado
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    #método exclusivo da classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    #property: pega o atributo e muda a forma como ele será lido
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

Restaurante.listar_restaurantes()

#pycache: forma mais simples de importar o modo que importamos. Diretório que armazena os arquivos em Hash code.