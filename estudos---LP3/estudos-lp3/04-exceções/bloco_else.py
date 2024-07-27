'''As exceções podem prevenir falhas também, 
principalmente quando tem mais coisa pra executar depois do erro
'''

print("Entre 2 números e vou dividir eles")
print("aperte 'q' para sair")

while True:
    num1 = input("primeiro numero: ")
    if num1 == 'q':
        break
    num2 = input("segundo numero: ")
    if num2 == 'q':
        break
    try:
        answer = int(num1)/int(num2)
    except:
        print("Impossível dividir por 0")
    else:
        print(answer)
