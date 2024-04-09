valor = float(input('Digite o valor da compra'))
#valor = float(valor)
desconto = float()

if(valor>=0.01 and valor<=9.99):
    print('desconto de 0%')

if(valor>=10.00 and valor<=99.99):
    desconto = valor * 0.05
    print('desconto de 5%')

elif(valor>=100.00 and valor<=499.99):
    desconto = valor * 0.1
    print('desconto de 10%')

else:
    desconto = valor * 0.15
    print('desconto de 15%')

valorTotal = valor - desconto

print(valorTotal)
