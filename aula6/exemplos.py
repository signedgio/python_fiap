nomesAlunos = ["Gio", "Davi"]

for nome in nomesAlunos:
    print(nome)


#######################################################################################
## pesquisar se um nome existe dentro da lista e encontrar sua posição.

nomesAlunos = ["Gio", "Davi"]
pesquisa = input("Digite o nome do aluno: ").capitalize()

x = 0
for nome in nomesAlunos:
    if nome == pesquisa:
        print("Nome encontrado.")
        print(f"Encontrado na posição {x}.")
        break # colocamos o break para que o for acesse o else.
    x += 1 # aqui, o for pesquisa se, por exemplo, "Davi" está no zero. como não está,
    # o for pequisa denovo na lista e vê que eele está na posição 1.
else:
    print("Nome não encontrado.")

# tiramos o else de dentro do bloco do for para que imprima apenas uma mensagem.
#caso contrário, vai imprimir a mesma frase numa quantidade igual à quantidade de
# elementos na lista.

# .capitalize() serve pra independente do jeito que escrever (maiúsculo ou minúsculo),
# ele vai achar.

#######################################################################################

# usando range:

# for num in range(2,11,2) imprime apenas os múltiplos de 2 até 10.
listaASerGerada = []
for num in range(1,11):
    listaASerGerada.append(num)
print(listaASerGerada)

#######################################################################################

# percorrer uma lista e verificar o maior número

notas = [1, 7, 4, 8]
maiorNota = notas[0] # a maior nota está na posição zero teoricamente. deixamos assim
# e vai percorrer a lista toda procurando a maior.

for posicao, nota in enumerate(notas):
    if nota > maiorNota: # aqui coloca pro for percorrer TODAS as notas.
        maiorNota = nota
        i = posicao

print(maiorNota)
print(i)

# OU:

notas = [1, 7, 4, 8]
maiorNota = notas[0]
posicao = 0
contador = 0

for nota in notas:
    if nota > maiorNota:  # aqui coloca pro for percorrer TODAS as notas.
        maiorNota = nota
        posicao = contador
    contador += 1

print(maiorNota)
print(posicao)

