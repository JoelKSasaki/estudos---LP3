def conVC():
    frase = input()
    v = 0
    c = 0
    i = 0
    for i in frase:
        if(i == 'a' or i == 'e' or i == 'i'or i == 'o' or i == 'u'):
            v += 1
        elif(i == ' '):
            v += 0
            c += 0
        else:
            c += 1
    return v, c
            
print(conVC())