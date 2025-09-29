# 2. Escreva um programa que gere um dicionário, em que cada chave seja um
# caractere e seu valor seja um número desse caractere encontrado em uma frase lida.
# Exemplo: O rato -> {“O”:1, “r”:1, “a”:1, “t”:1, “o”:1}

frase = input("Digite uma frase: ")
dicionario = {}

for letra in frase:
    if letra in dicionario:
        dicionario[letra] = dicionario[letra] + 1
    else:
        dicionario[letra] = 1

print(dicionario)

## oq aconteceu aqui: o loop for passa por todos os caracteres da frase, adicionando uma por uma ao
## dicionário. como o dicionário está vazio, fica 'O': 1 e não somando 1.