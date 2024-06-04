def media(nota):
    nota *= 0.10
    if(nota<=10 and nota>=9):
        print("A")
    elif(nota<=8.9 and nota>=8):
        print("B")
    elif(nota<=7.9 and nota>=7):
        print("C")
    elif(nota<=6.9 and nota>=6):
        print("D")
    else:
        print("F")
        print("reprovado")

M = int(input())
media(M)