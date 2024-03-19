#for, while, break, continue

#operador in: usado no forEach

for letra in 'Python':
    print(letra)

itens = ['banana', 'arroz', 'limao']
alunos = ['Sarah', 'Milho', 'Vini']

for item in itens:
    print(item)

for i in range(5):
    print(i)

for i in range(0, 11, 2):
    print(i)

#for
#list + rage

lista = list(range(101))
print(type(lista))

#while
contador = 0
while(contador<=5):
    print(contador)
    contador+=1

#break

numeros = [1, 3, 4, 7, 11, 8]

for numero in numeros:
    if numero %2 == 0:
        print(numero)
        break

#continue
nums = [-3, -2, -1, 0, 1, 2]
for num in nums:
    if num<=0:
        continue
    print(num)
    if num>0:
        print(num)

#compreensão de letras
#forma concisa de criar listas en Python

numeros2 = [3, 4, 5, 6, 7]
quadrados = []

for numero2 in numeros2:
    quadrados.append(numero2 ** 2)

quadrados = [numero2 ** 2 for numero2 in numeros2]

palavra = 'Ola mundo'
letras = [letra for letra in palavra]
letras = [letra.upper() for letra in palavra]