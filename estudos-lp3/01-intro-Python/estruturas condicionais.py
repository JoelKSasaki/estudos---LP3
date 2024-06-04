#if
idade = 18
if idade>=18:
    print('Maior de idade. Parabéns')

#if else

if(idade >=18):
    print('Maior de idade')
else:
    print('menor')

'''if/elif/else
crianca = 0 a 12 anos
adolescente = 12 a 17 anos
adulto = 18 a 59
idoso = 60+
'''

if idade<=12:
    print('criança')
elif idade <=17:
    print('Adolescente')
elif idade <=59:
    print('Adulto')
else:
    print('idoso')


email = "admin@email"
senha = '123'

if email == 'admin@email' and senha == '123':
    print('acesso permitido')
else:
    print('invalido')


'''entrada numero 
1 - Domingo
2 - Segunda
3 - terça
4 - Quarta
5 - Quinta
6 - Sexta
7 - Sábado
'''

dia = 4

dias = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sábado'
}

print(dias(dia))

#operador ternario

idade = 20

if idade>=18:
    status = 'Maior de idade'
else:
    status = 'Menor de idade'

status = 'Maior de idade' if idade>=18 else 'Menor de idade'

#match case

dia = 3

match dia:
    case 1:
        print('Segunda')
    case 2:
        print('Terça')
    case 3:
        print('Quartanumero2 = input()')
    case 4:
        print('Quinta')
    case 5:
        print('Sexta')

#imprimir
#1 e 7 - fim de semana
#2 a 6 - dia útil

match dia:
    case 1 | 7:
        print('Fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia útil')
    case _: 
        print('Dia inválido')
    
