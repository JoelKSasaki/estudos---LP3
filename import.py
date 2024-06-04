from introPOO.POO import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza place', 'fast Food')
restaurante_japones = Restaurante('Chef Maeda', 'japonês')
restaurante_japones.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()