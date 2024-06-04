def sortear():
    from random import randint
    num = randint(1, 100)
    
    while True:
        palpite = int(input('Adivinhe o número '))
        int()
        if (palpite > num):
            print('palpite alto')
        elif (palpite < num):
            print('palpite baixo')
        else:
            print('parabéns')
            break
        
sortear()



