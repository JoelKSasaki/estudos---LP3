#função

#Declaração
'''def_nomedafunção(parametro1, parametro2)
        return valor'''


#função sem retorno
#final da função feita pela identação
#parametro: referência definida na assinatura da função porque é possível acessar a variável dentro da função
def imprimir_nome():
    print(f'Nome: (nome)')


#função com retorno sem parametros
def saudacao():
    return "bom dia"

#Chamada
print('ola')
'''
funcao()
funcao()
funcao()
'''

#função com retorno e com parâmetros

def gerar_saudacao(nome):
    print(f'Boa tarde, (nome)')

#argumento: valor(literal) ou referência enviada a um parâmetro
imprimir_nome('Joelinton')
imprimir_nome('Pedro')

nome = 'Milhomenos'
imprimir_nome(nome)

saudacao = saudacao()
print(saudacao)

print(gerar_saudacao())

#funções
#return    parametros
#   0          0
#   0          1
#   1          0
#   1          1      (melhor caso)

'''
imprimir a saudação
'''
def imprimir_saudacao(nome):
    print(f'Bom dia (nome)')
    

#função pura - sem efeito colateral e sem acesso à estado global
def gerar_saudacao(nome):
    return f'Boa tarde, (nome)'

#argumentos nomeados
def nova_saudacao(nome, saudacao):
    return f'(saudacao) (nome)'

print(nova_saudacao('Luska', 'Bom dia'))
print(nova_saudacao('Pantufa', 'Boa tarde'))
print(nova_saudacao('Gabriel', 'Boa noite'))

print(nova_saudacao(nome='Luska', saudacao='Bom dia'))
print(nova_saudacao(saudacao='Bom dia', nome='Débora'))

#valores padrão de parâmetros
def obter_saudacao(nome, saudacao='Boa tarde'):
    return f'(saudacao) (nome)'

print(obter_saudacao('Sarah'))
print(obter_saudacao('Sarah', 'Boa tarde'))

print("ola", "Mundo", sep=", ")

#args (non-keyward-arguments)
def media(notas):
    return sum(notas)/len(notas)

media(9.0, 7.0, 6.0)
media(5.0, 9.0, 7.0, 6.0)

def calcular_media2(*notas):
    return sum(notas)/len(notas)

media(5.0, 9.0, 7.0, 6.0)

#cálculo de média de notas de vários alunos
#calcular_media - lista de notas - media
#calcular_medias - lista de lista de notas - lista de médias

notas_alunos [
    [5.0, 6.0]
    [10.0, 7.0]
    [7.0, 7.0]
]

def calcular_media(notas):
    return sum(notas)/len(notas)

def calcular_medias(notas_alunos):
    medias = []
    for notas in notas_alunos:
        medias.append(calcular_media(notas))
    return medias
    #return [calcular_media(notas) for notas in notas_alunos]

print(calcular_medias(notas_alunos))