#com um loop: 
comida = {
    'fruta': 'maca',
    'proteína': 'peixe',
    'legume': 'cenoura',
    'doce': 'bombom',
}

#Para percorrer o dicionário com um FOR, é preciso armazenar as chaves e os seus respectivos valores em cada par chave-valor em variáveis
for key, value in comida.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print()
    
favorite_languages = {
    'Sarah': 'python',
    'Pedro': 'java',
    'Júlio': 'HTML',
    'Jossana': 'JS',
    'Emanuel': 'C'
}

for name, language in favorite_languages.items():
    print(f"A linguagem favorida do(a){name.title()} eh {language.title()}")
print()

#percorrendo e extraindo todas as chaves do dicionário

friends = ['Júlio', 'Sarah', 'Pedro']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, vejo que você gosta de {language}")
        
if 'Rony' not in favorite_languages.keys():
    print("Rony, te convido a fazer uma pesquisa")
    print()

#o método keys() retorna uma sequência de todas as chaves, não sendo usado apenas em loops

#percorrendo e extraindo todos os valores do dicionário

print("As linguagens mencionadas foram:")
for language in favorite_languages.values():
    print(language.title())