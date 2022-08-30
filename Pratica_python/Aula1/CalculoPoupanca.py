dinheiroInicial = float(input("Digite o valor inicial: "))
meses = int(input("Digite quantos meses: "))

i = 0

while i < meses:
    dinheiroInicial = (dinheiroInicial * 0.005) + dinheiroInicial
    i = i + 1
    print("O valor do dinheiro depois de " , i , " meses é: " , "%.2f"%dinheiroInicial) 

