texto = input("Informe um texto: ")
vogais = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print() 
print("executa no final do laço.")


# Exemplo utilizando a função bult-in-range
for numero in range(0, 51, 5):
    print(numero, end= " ")




         

