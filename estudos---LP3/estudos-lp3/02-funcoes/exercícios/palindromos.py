def palindromo(sentenca):
    letras = 0
    for i in sentenca:
        letras += 1
    
    if(letras%2 != 0 and inverso(sentenca) == sentenca):
        print("palindromo")
    else:
        print("não é palindromo")
        
def inverso(palavra):
    for e in palavra[::-1]:
        print(e)
    return palavra
        
word = input()
palindromo(word)