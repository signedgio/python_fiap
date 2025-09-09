# 1. Altere o exemplo anterior de forma a solicitar ao usuário o produto e a
# quantidade vendida. Verifique se o nome do produto digitado existe no
# dicionário e só então efetue a baixa no estoque.

estoque = {"tomate": [1000, 2.3],
           "alface": [500, 0.45],
           "batata": [2001, 1.2],
           "feijão": [100, 1.5]}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
totalVendidos = 0
while True:
    produto = input("Digite o produto (digite fim para sair): ")
    if produto == "fim":
        break
    elif produto in estoque:
        print(f"{produto} disponível no estoque")
        vendidos = int(input("Digite quantas unidades desse produto foram vendidas: "))
        totalInicial = estoque[produto][0]
        totalVendidos = totalInicial - vendidos
        print(f"Foram vendidas {vendidos} unidades de {produto}.")
    else:
        print("Produto não disponível no estoque.")

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto}: {quantidade} x {preco} = {custo}")
    estoque[produto][0] -= quantidade
    totalVendidos += custo
    print(f"Custo total: {totalVendidos}")



