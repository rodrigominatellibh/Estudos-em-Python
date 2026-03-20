# Forma de utilizar o comando break e continue.
while True:
    numero = int(input("Informe um número: "))

    if numero == 10: 
        break

    if numero % 2 == 0:
        continue
    print(numero)


