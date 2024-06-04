def palindromo(sentenca):

    if(inverso(sentenca) == sentenca):
        print("palindromo")
    else:
        print("não é palindromo")
        
def inverso(palavra):
    palInversa = ""
    for e in palavra[::-1]:
        palInversa = palInversa+ e
    return palInversa.lower()
        
word = input()
word = word.lower()
palindromo(word)