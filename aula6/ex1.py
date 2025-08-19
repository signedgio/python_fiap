# 1. Altere o programa do exemplo anterior de formar a imprimir o menor elemento da lista.

## L = [1, 7, 2, 4]
## maximo = L[0]
## for e in L:
## if e > maximo:
## maximo = e
## print(maximo)

notas = [4, 5, 9, 8, 6, 2, 10]
menorNota = notas[0]

for nota in notas:
    if nota < menorNota:
        menorNota = nota
print(menorNota)

