palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("É um palindromo")
else:
    print("Não é um palindromo")