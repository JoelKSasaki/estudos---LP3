print("Calculo do IMC")

kg = input("peso: ")
kg = float(kg)

altura = input('altura: ')
altura = float(altura)

IMC = kg/(pow(altura, 2))

print(f'seu IMC: {IMC:.2f}')

if IMC < 18.5:
    print("Baixo peso")
elif IMC >= 18.5 and IMC < 25.0:
    print("Peso normal")
elif IMC >= 25.0 and IMC < 30.0:
    print("Excesso de peso")
elif IMC >= 30.0 and IMC < 35.0:
    print("Obesidade de Classe 1")
elif IMC >= 35.0 and IMC < 40.0:
    print("Obesidade de Classe 2")
else:
    print("Obesidade de Classe 3")

if IMC > 24.9:
    perda_de_peso = IMC - 24.9
    print(f'Para chegar ao peso normal, você deve perder {perda_de_peso:.2f} quilogramas')
if IMC < 18.5:
    ganho_de_peso = 18.5 - IMC
    print(f'Para chegar ao peso normal, você deve ganhar {ganho_de_peso:.2f} quilogramas')