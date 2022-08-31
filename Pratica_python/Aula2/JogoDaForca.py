palavra_secreta = input("Digite a palavra secreta: ")
letras_digitadas = []
chances = 3

while True:
    letra = str(input("Digite uma letra: "))

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue

    letras_digitadas.append(letra)

    letra_secreta_temporaria = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            letra_secreta_temporaria += letra_secreta
        else:
            letra_secreta_temporaria += "*"

    if letra_secreta_temporaria == palavra_secreta:
        print("Você ganhou!")
        break
    else:
        print("A palavra secreta está assim: {}".format(letra_secreta_temporaria))

    if letra not in palavra_secreta:
        chances -= 1
        print("Você errou! Ainda tem {} chances".format(chances))
    if chances == 0:
        print("Você perdeu!")
        break

