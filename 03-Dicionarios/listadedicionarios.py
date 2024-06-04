#aninhamento: armazenamento de múltiplos dicionários numa lista ou lista de itens como valor em um dicionário

time1 = {'nome': 'Corinthians', 'pais': 'Brasil', 'continente': 'América'}
time2 = {'nome': 'Liverpool', 'pais': 'Inglaterra', 'continente': 'Europa'}
time3 = {'nome': 'Al Hilal','pais': 'Arábia Saudita','continente': 'Ásia'}
time4 = {'nome': 'Inter Miami','pais': 'EUA','continente': 'América'}

times = [time1, time2, time3, time4]

for time in times:
    print(time)
print()
    
#adicionando um novo dicionário a uma lista
aliens = []

for alien_number in range(20):
    new_alien = {'color': 'red', 'points': '10', 'speed': 'slow'}
    aliens.append(new_alien)

    
#dicionário em uma lista
for alien in aliens[:3]:
    if alien['color'] == 'red':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '15'
        
for alien in aliens[:5]:
    print(alien)
    
print(f"número total de aliens: {len(aliens)}")
print()


#lista de itens em um dicionário
sanduiche = {
    'tamanho': 'grande',
    'ingredientes': ['queijo', 'frango', 'tomate']
}

print(f"Voce pediu um um sanduiche {sanduiche['tamanho']} com os ingredientes:")

for ingrediente in sanduiche['ingredientes']:
    print(f"\t{ingrediente}")
    

#quando mais de um valor é associado a uma única chave
    
alimento = {
    'frutas': ['maca', 'melancia', 'laranja'],
    'proteínas': ['peixe', 'frango', 'ovo'],
    'legumes': ['cenoura', 'batata', 'vagem'],
    'doces': ['bombom', 'sonho', 'mil folhas'],
}

for tiposdenutrientes, comidas in alimento.items():
    print(f"\nfazem parte das(os){tiposdenutrientes.title()}: ")
    for comida in comidas:
        print(f"\t{comida.title()}")
        
#dicionario em um dicionario
#se cada pessoa tiver um site com seu próprio nome de usuário, poderemos usar os nomes de usuário como chave em um dicionário

usuario = {
    'JKSSK': {
        'primeiroNome': 'Joel',
        'sobrenome': 'Sasaki',
        'pais_local': 'Brasil',
    },
    
    'LucMilho': {
        'primeiroNome': 'Lucas',
        'sobrenome': 'Milhomem',
        'pais_local': 'EUA',
    },
}
for username, user_info in usuario.items():
    print(f"\nUsername: {username}")
    nome_completo = f"{user_info['primeiroNome']} {user_info['sobrenome']}"
    localizacao = user_info['pais_local']
    
    print(f"\tNome Completo: {nome_completo.title()}")
    print(f"\tLocalização: {localizacao.title()}")


#cada chave é atribuida à variavel USERNAME e o dicionario associado a cada nome de usuário é atribuída à USER_INFO