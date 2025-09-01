# Vejamos um exemplo em que a chave seria o produto e o valor seu preço:

tabela = {"alface": 0.45, "batata": 1.2, "tomate": 2.3, "feijão": 1.5}
print(tabela)

# Para obter o preço da alface, vamos digitar tabela[“alface”],tabela é o nome da
# variável do tipo dicionário, alface é a nossa chave e o valor retornado é 0.45.

########################################################################################
#Criando um dicionário com os RMs e os anos de nascimento:

dadosAlunos = {"Giovanna": ["563469", "2007"], "Allana": ["562227", "2004"]}
    ## colocamos os números entre aspas pq nn serão usados pra fazer contas. normal-
    ## mente, nn colocamos em aspas.
print(dadosAlunos["Giovanna"])

backUp_dadosAlunos = dadosAlunos.copy()
    ## esse .copy() é pra manter a lista inicial nessa variável de back up.
del dadosAlunos["Giovanna"]
    ## caso queira apagar alguém usamos "del".
print(dadosAlunos)
print(backUp_dadosAlunos)

dadosAlunos["Allana"][1] = "2003"
print(dadosAlunos)

print("Allana" in dadosAlunos)
print("Giovanna" in dadosAlunos)
    ## esse "in" serve pra procurar algo dentro da lista.
print(dadosAlunos.keys())
    ## esse .keys() é pra printar apenas as chaves. nesse caso, apenas "Allana" será
    ## printado pois "Giovanna" foi excluído da lista.
print(dadosAlunos.values())
    ## esse .values() é pra printar apenas os valores das chaves.

#######################################################################################

# Vejamos um programa que utiliza dicionários para exibir o preço de um produto:

tabela = {"alface": 0.45, "batata": 1.2, "tomate": 2.3, "feijão": 1.5}
while True:
    produto = input("Digite o nome do produto ou fim para terminar: ")
    if produto == "fim":
        break
    elif produto in tabela:
        print(f"Preço: R$ {tabela[produto]:.2f}")
    else:
        print("Produto não encontrado.")

######################################################################################

# Vamos modificar o código anterior agora:

rmsAlunos = {"Giovanna": "563469", "Allana": "562227", "Ian": "561435"}
while True:
    rms = input("Digite o nome do aluno (digite fim para finalizar): ")
    if rms == "fim":
        break
    elif rms in rmsAlunos:
        print(f"O RM do aluno é {rmsAlunos[rms]}")
    else:
        print("Aluno não encontrado.")

###################################################################################################################################

# Vamos modificar o código anterior mais uma vez, agora com cursos presenciais da FIAP:

cursosPresenciais = {"Data Science": ["R$2.285,00", "2 anos de duração"], "Mecatrônica": ["R$1.800,00", "5 anos de duração"]}
while True:
    cursos = input("Digite o nome do curso a pesquisar (digite fim para finalizar): ").title()
    ## esse .title() funciona como o captalize, mas como nesse caso temos cursos de duas palavras, o title é
    ## o mais incidicado. ex: se usarmos captalize e escrevermos Data science, com o S minúsculo, nn vai encontrar.
    if cursos == "fim":
        break
    elif cursos in cursosPresenciais:
        print(f"O valor da mensalidade do curso é de {cursosPresenciais[cursos][0]} e tem {cursosPresenciais[cursos][1]}.")
    else:
        print("Este curso não está disponível na modalidade presencial. ")

#################################################################################################################################





