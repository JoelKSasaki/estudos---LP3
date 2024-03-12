# variavel

nome1 = "Joelinton"
idade = 17

# nao existe constante em Python
# docstring
# documentar códigos de funções

def somar(num1, num2):
    return num1 + num2
somar(15.0, 3.0)

#comentário de uma linha

'''
comentário
de múltiplas
linhas
'''

'''
tipos de dados
    1 - numerico: int, float, complex
    2 - boolean
    3 - Strings
    4 - listas
    5 - tupla
'''
#int
idade2 = 30
temperatura = -2

#float
peso = 55.23
altura = 1.00

#boolean
verdade = True
mentira = False

#Sequencia de caracteres
nome2 = 'Milhomenos'
nome3 = "Luska"

#multilinha
frase = """ skooaoskii
BOm dia
skfksja
"""

#interpolação de string
# f strings
nome4 = "Sarah Sabongi"
idade3 = 16
frase2 = f"Olá {nome3}. Você tem {idade2} anos"
print(frase2)

#char
letra = 'w'
letra2 = "u"
nome5 = 'Rony rustico'
print(nome5[0])
print(nome5[-1])
print(nome4.capitalize())
print(nome4.upper())

#strings são objetos
#método

habilidades2 = ['python', 'Js', 'java', 'c']
print(habilidades2) 
#final da lista
habilidades2.append('c#') #python, Js, java, c, c#

#inserir um item em uma posição X

habilidades2.insert(2, 'css')
print(habilidades2)

#habilidades.clear
#print(habilidades)

for habilidade in habilidades2:
    print(habilidades2)

#5: lista de valores QUE NAO PODE SE2R ALTERADA

opcoes = ('sim', 'nao', 'talvez')

print(opcoes[0])

for opcao in opcoes: 
    print(opcoes)

#set: conjunto de valores que não permite elementos duplicados. Não é indexado
habilidades3 = ['futebol', 'basquete', 'volei', 'natação']
print(habilidades3)
#habilidades[i] não vai funcionar

#6: dicionários
# palavra que contém uma definição

def somar(num1, num2):
    return num1 + num2
somar(15.0, 3.0)

#comentário de uma linha
# chave -> valor
# conjunto chave valor

nome6 = 'Julio Nagaita'
idade = 17
habilidades2 = ['python', 'Js', 'java', 'c']
empregado = True

candidato = {
    'nome': 'Julio Nagaita',
    'idade': 17,
    'empregado': True
}

print(candidato['nome'])
print(candidato.keys())
print(candidato.values())

#7: none
nome = None