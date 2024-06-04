#as exceções gerenciam erros durante a execução de um programa.
#Quando ocorre um erro, o Python fica em dúvida sobre qual seria sua próxima ação
#o programa seguirá sendo executado caso uma exceção seja abordada

'''o erro no traceback é um objeto de exceção, ou seja, 
uma resposta para uma situação na qual o Python não consegue fazer o que foi solicitado. 
Essas informações são muito usadas para tratar essa exceção'''

#try except

amigo1 = input()
amigo2 = input()
amigo3 = input()
amigo4 = input()

try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1: 
        print(amigo1)
    elif opcao_escolhida == 2: 
        print(amigo2)
    elif opcao_escolhida == 3: 
        print(amigo3)
    else: 
        print(amigo4)
except:
    print("opcao invalida")
    print("escolha um número de 1 a 4")
