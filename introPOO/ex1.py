#Crie uma classe chamada Musica com os atributos NOME, ARTISTA E DURAÇÃO e crie 3 objetos definindo cada atributo..

class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1= Musica()
musica1.nome = 'Ticket to Ride'
musica1.artista = 'Beatles'
musica1.duracao = 3

musica2 = Musica()
musica2.nome = 'Billie Jean'
musica2.artista = 'Michael Jackson'
musica2.duracao = 3

musica3 = Musica()
musica3.nome = 'Mil razões'
musica3.artista = 'Tiago Iorc'
musica3.duracao = 3

print(f'Musica: {musica2.nome}, Artista: {musica2.artista}')