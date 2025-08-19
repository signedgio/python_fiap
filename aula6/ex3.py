# 3. Faça um programa para selecionar os elementos de uma lista e copiá-los para outras.
# Copiar os valores pares para a lista P que estão na lista V = [9, 8, 7, 12, 0, 13, 21]
# e os ímpares para a lista I.

V = [9, 8, 7, 12, 0, 13, 21]
P = []
I = []

for valor in V:
    if valor % 2 == 0:
        P.append(valor)
    else:
        I.append(valor)

print(f"Os valores pares são: {P}.")
print(f"Os valores ímpares são: {I}.")