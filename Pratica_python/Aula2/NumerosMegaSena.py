mega_sena = []
i = 0
while i < 6:
    numeroMega = int(input("Digite o numero: "))

    while numeroMega > 60 or numeroMega < 1:
        print("Numero invalido")
        numeroMega = int(input("Digite o numero novamente: "))
    
    mega_sena.append(numeroMega)
    i += 1

print(mega_sena)
tamanho = len(mega_sena)


