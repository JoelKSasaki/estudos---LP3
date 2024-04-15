def palindromo(sentenca):
    
    if(inverso(sentenca) == sentenca):
        print("palindromo")
    else:
        print("não é palindromo")
        
def inverso(palavra):
    for e in palavra[::-1]:
        print(e)
    return palavra
        
word = input()
palindromo(word)
