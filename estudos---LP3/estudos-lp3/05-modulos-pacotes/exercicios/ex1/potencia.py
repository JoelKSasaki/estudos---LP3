from volume import volume as vol_aquario

temp_desejada = input("Digite a sua temperatura desejada: ")
temp_desejada = float(temp_desejada)
temp_atual = input("Digite a temperatura ambiente: ")
temp_atual = float(temp_atual)

potencia = vol_aquario* 0.05 * (temp_desejada - temp_atual)
print(f'potência necessária: {potencia}')