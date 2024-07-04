from random import randint

numero = randint(1, 100)
palpite = 0
vezes = 0

while palpite != numero:
    palpite = int(input("Aposta: "))
    vezes = vezes + 1

print("Você precisou de",vezes,"tentativas para acertar meu número!")
