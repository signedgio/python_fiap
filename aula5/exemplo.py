## conteúdo: listas.

## nomesAlunos = [] (podemos criar listas vazias e ir enviando pra ela)
## print(nomesAlunos)
nomesAlunos = ["Gio", "Ian", "João", "Lana", "Davi"]
print(nomesAlunos)
print(len(nomesAlunos))
nomesAlunos[0] = "Giovanna" ## isso aqui é pra mudar algo dentro da lista
print(nomesAlunos)
nomesAlunos[3] = "Allana"
print(nomesAlunos[3]) ## esse [3] faz com que imprima apenas o quarto

nomesAlunosBackUp = nomesAlunos[:] ## colocamos [:] pra ele salvar oq estava
## originalmente na lista
print(nomesAlunosBackUp)

nomesAlunos[0] = "Giovanna Carmona"
print(nomesAlunos)
print(nomesAlunosBackUp) ## como "fechamos" oq entra na lista lá em cima, não vai
## imprimir essa última modificação na variante do back up

## Vejamos um exemplo em que um aluno tem cinco notas e
## desejamos calcular a média aritmética:
## notas = [6, 7, 5, 8, 9]
## soma = 0
## x = 0
## while x < 5:
## soma += notas[x]
## x += 1
## print(f"Média = {(soma/x):.2f}")


## Vejamos uma modificação desse exemplo, vamos ler as notas uma a uma:
## notas = [0, 0, 0, 0, 0]
## soma = 0
## x = 0
## while x < 5:
   ## notas[x] = float(input(f"Nota {x+1} = "))
   ## soma += notas[x]
   ## x += 1
## print(f"Média = {(soma/x):.2f}")
