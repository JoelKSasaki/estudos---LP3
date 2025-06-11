'''dicionarios associam as informações relacionadas a uma variável 
Ele é uma coleção de pares chaves-valor. 
Cada chave está vinculada a um valor 
'''
livro = {'color': 'blue', 'pages': '83'}

#Dicionario simples:
alien = {'color': 'green'}
#color é a chave do dicionário, enquanto o seu valor associado é GREEN
#Um dicionário pode armazenar infinitos pares chave-valor


#acessando valor de uma chave
print(livro['color'])

pagina = livro['pages']
print(f"o livro possui {pagina} paginas")


#adicionando novas pares chave-valor
livro['tema'] = 'suspense'
alien['vida'] = 5
alien['x'] = 0
alien['y'] = 25
alien['velocidade'] = 'média'

print(livro)
print(alien)


#modificado valores num dicionário
print(f"o livro original possui {livro['pages']}")

livro['pages'] = 100
print(f"A nova versao possui {livro['pages']} paginas")


#deslocameno do alien
print(f"posicao original do alien: {alien['x']}, {alien['y']}")

if alien['velocidade'] == 'devagar':
    x_increment = 1
elif alien['velocidade'] == 'média':
    x_increment = 2
else:
    x_increment = 4

alien['x'] = alien['x'] + x_increment
print(f"Nova posicao: {alien['x']}")
    
#removendo pares chave-valor
del alien['color']
print(alien)

#dicionário de objetos parecidos

favorite_languages = {
    'Milho': 'python',
    'Pedro': 'java',
    'Júlio': 'HTML',
}

language = favorite_languages['Milho'].title()
print(f"Milhomem gosta da linguagem {language}")

#acesso de valores com get

pontos = alien.get('points', 'sem valor definido')
print(pontos)
