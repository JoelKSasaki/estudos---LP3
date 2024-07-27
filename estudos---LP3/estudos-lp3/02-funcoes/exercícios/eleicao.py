def eleicao():
    cand1 = input()
    cand2 = input()
    cand3 = input()
    P1 = 0
    P2 = 0
    P3 = 0
    v = 0
    while True:
        from random import randint
        num = randint(1, 3)
        if(num == 1):
            P1 += 1
        elif(num == 2):
            P2 += 1
        elif(num == 3):
            P3 += 1
        v += 1
        if(v == 7):
            break
        
    print("candidato 1: ", P1)
    print("candidato 2: ", P2)
    print("candidato 3: ", P3)
    
    if(P1>P2 and P1>P3):
        print("vitoria de: ", cand1)
    if(P2>P1 and P2>P3):
        print("vitoria de: ", cand2)
    if(P3>P1 and P3>P2):
        print("vitoria de: ", cand3)
    
eleicao()