# 3. Considere um dicionário com 5 nomes de alunos e
# suas notas. Escreva um programa que calcule a média
# dessas notas.

nomesAlunos = {"Giovanna": 10, "Davi": 8, "Allana": 10, "Ian": 9, "João": 7}
total = 0
for nota in nomesAlunos.values():
    total += nota

media = total/len(nomesAlunos)
print(f"Média = {media}")

## oq aconteceu aqui: na linha 8, graças ao nomesAlunos.values(), serão percorridos todos os valores
## das notas, somando 1 de cada vez. então digamos que as notas sejam 9.0, 10.0 e 5.0:
## 	1.	No começo:
## total = 0
## 	2.	Primeira volta do for:
##  nota = 9.0
##  total = total + nota
## total = 0 + 9.0 = 9.0
## 	3.	Segunda volta:
##  nota = 10.0
##  total = total + nota
##   total = 9.0 + 10.0 = 19.0
## 	4.	Terceira volta:
## nota = 5.0
## total = total + nota
## total = 19.0 + 5.0 = 24.0
