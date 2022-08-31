mega_sena[6] = []
i = 0
while i < 6:
    mega_sena[i] = int(input("Digite o numero: "))

    while mega_sena[i] > 60 or mega_sena[i] < 1:
        print("Numero invalido")
        mega_sena[i] = int(input("Digite o numero novamente: "))

    i += 1

print(mega_sena) 
