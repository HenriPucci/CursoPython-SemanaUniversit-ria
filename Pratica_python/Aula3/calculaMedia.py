def calcula_media(lista):
    
    media = 0

    if type(lista) == list:

        for i in range(len(lista)):
            media += lista[i]
        
        media = media / len(lista)
        
        print("media :" , media, "!!")
    else:
        print("nao eh uma lista")

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


calcula_media(mega_sena)