# Podemos pesquisar se um elemento está ou não em uma lista. Vejamos o exemplo:
# L = [15, 7, 27, 39]
# pesquisa = int(input("Digite o valor a pesquisar: "))
# x = 0
# while x < len(L):
# if L[x] == pesquisa:
# achou = True
# break
# else:
# achou = False
# x += 1
# if achou == True:
# print(f"{pesquisa} achado na posição {x}.")
# else:
# print(f"{pesquisa} não encontrado.")


# Modifique o exemplo anterior de forma a realizar a mesma tarefa,
# mas sem utilizar a variável achou. Dica: observe a condição de saída do while.

L = [15, 7, 27, 39]
pesquisa = int(input("Digite o valor a pesquisar: "))

x = 0
while x < len(L):
    if L[x] == pesquisa:
        break
    x += 1

if x < len(L):
    print(f"{pesquisa} achado na posição {x}.")
else:
    print(f"{pesquisa} não encontrado.")

