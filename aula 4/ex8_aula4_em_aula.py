# Escreva um programa que pergunte o depósito inicial
# e a taxa de juros de uma poupança. Exiba os valores
# mês a mês para os 24 primeiros meses. Escreva o total
# do ganho com juros no período.

di = float(input("Depósito inicial: "))
j = float(input("Juros em porcentagem: "))
mes = 1
while mes <= 24:
    di = di + (di*j) + dm
    print(f"Valor do mês {mes} é de: R${di:.2f}")
    mes = mes + 1
print(f"Seu valor total é de {di:.2f}")