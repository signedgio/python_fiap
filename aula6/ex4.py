# 4. Faça um programa que lê e imprime uma lista de compras até que seja digitado fim.

listaDeCompras = []

while True:
    compras = input("Digite o que você comprou no mercado (um por vez) e digite fim ao terminar: ")
    if compras == "fim":
        break
    listaDeCompras.append(compras)

for todasAsCompras in listaDeCompras:
    print(todasAsCompras)


