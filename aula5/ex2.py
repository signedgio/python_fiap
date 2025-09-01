# O método extend adiciona os elementos de uma lista a outra e o
#  método append adionada a lista dentro de outra lista.
# L =[]
# L.extend(["a", "b"])
# print(L)
# L.append(["c", "d"])
# print(L)
# print(len(L))
# print(L[0])
# print(L[1])
# print(L[2])


## Faça um programa que leia duas listas e que gere uma terceira com os elementos
## das duas primeiras.

lista1 = [1, 2, 3 ,4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = lista1 + lista2
print(lista3)

# outro jeito:

lista = ["Gio", "Ian", "Davi", "Pedro"]
listaNovosAlunos = []

while True:
    novosNomes = input("Qual é o seu nome? (digite fim para sair) ")
    if novosNomes == "fim":
        break
    listaNovosAlunos.append(novosNomes)

listaNova = []
listaNova = lista + listaNovosAlunos
# listaNova.extend(lista + listaNovosAlunos)
print(listaNova)