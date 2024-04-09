'''operadores aritméticos
+, -, *, /, **, %
'''

nota1 = 15.0
nota2 = 6.0
nota3 = 1.5

media = (nota1+nota2+nota3)/3

print(media)

#10 elevado
num = 10
elev_quadrado = num**3
print(elev_quadrado)

#operadores lógicos
#and, or, not

print('Maria')
print(2+3)
print(True and True)#True
print(True and False)#false
print(False and True)#false
print(False and False)#false

verdade = True and False

'''permite a entrada no sistema
usuário não é bloqueado E
usuário é um funcionário E
hora atual entre 8h e 18h
-----
caso for admin pode acessar de qualquer forma
'''

'''usuario_bloqueado = False
usuario_funcionario = True
hora_atual = 17
usuario_admin = False
'''

'''def dentro_horario_comercial(hora):
    return hora >=8 and hora<=18'''

'''
if (not usuario_bloqueado and usuario_funcionario and hora <= 18 and hora >= 8) or usuario_admin:
    print('Acesso liberado')
else:
    print('Acesso negado')
'''

#operadores de comparação
# ==, !=, >, <, >=, <=

nota4 = 3.0
nota5 = 9.0

if nota4>nota5:
    print('Aluno foi melhor na prova1')
else:
    print('Aluno foi melhor na prova2')

#operador is, is not
#operador de identidade
#comparar se objetos são os mesmos
#mesmo espaço de memória

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)

print(a is b)

c = b
print(c is b)

'''
operador in, not in
usado para verificar se um elemento existe em sequência
str, list, tupla
'''

opcoes = ('sim', 'nao', 'talvez')
opcao = input('Digite uma opcao')
opcao = opcao.lower().strip()

if opcao in opcoes:
    print('   Ok   ')
else:
    print('Invalido')