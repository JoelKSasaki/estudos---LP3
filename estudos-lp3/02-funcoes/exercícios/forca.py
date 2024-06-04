def jogodaforca():
    import random
    palavra = "futebol"
    letras = []
    chances = 5
    ganhou = False
    perdeu = True
    
    while True:
        for letra in palavra:
            if letra in letras:
                print(letra, end = " ")
            else:
                print("_", end = " ")
        
        print(f"Você tem {chances} chances")
        tentativa = input("Escolha uma letra: ")
        letras.append(tentativa)
        if tentativa not in palavra:
            chances -= 1
        
        ganhou == True
        for letra in palavra:
            if letra not in palavra:
                ganhou == False
                
        if chances == 0 or ganhou:
            break
        
    if ganhou:
        print(f"Você ganhou. Palavra: {palavra}")
    elif perdeu:
        print(f"Você perdeu. A palavra era: {palavra}")
            
jogodaforca()