## Vejamos um programa que lê números até que 0 (zero) seja
## digitado, depois o programa imprimirá na mesma ordem em
## que foram digitados:
L = []
while True:
    num = int(input("Digite um número (0 sai): "))
    if num == 0:
        break
    L.append(num)
    x = 0
    while x < len(L):
        print(L[x])
        x += 1

## Agora vamos ordenar a lista com os números digitados:
L = []
while True:
    num = int(input("Digite um número (0 sai): "))
    if num == 0:
        break
    L.append(num)
    x = 0
while x < len(L):
    print(L[x])
    x += 1
    print(L)
    L.sort() ## o método sort sem argumento ordena a lista em ordem ascendente
    print(L)
    L.sort(reverse=True) ## o método sort com argumento True ordena a lista em
    ## ordem descendente
    print(L)

## Outra maneira de adicionarmos elementos em uma lista é usando +
L = []
L = L + [1]
print(L)
L += [2]
print(L)
L += [3, 4, 5]
print(L)