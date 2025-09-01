## Escreva um programa para ler 7 notas e calcular a média aritmética

notas = [3, 4, 5, 9, 6, 6, 9]
soma = 0
totalNumerosMediaAritimetica = 0

while soma < len(notas):
    soma += notas[totalNumerosMediaAritimetica]
    totalNumerosMediaAritimetica += 1
print(f"Média = {(soma/totalNumerosMediaAritimetica):.1f}")