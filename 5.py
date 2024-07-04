numero = int(input("Digite um número: "))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(fatorial)
