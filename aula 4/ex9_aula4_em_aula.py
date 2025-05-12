# Altere o programa anterior de forma a perguntar
# também o valor depositado mensalmente. Esse valor
# será depositado no início de cada mês e você deve
# considerá-lo para o cálculo de juros do mês seguinte.

di = float(input("Depósito inicial: "))
dm = float(input("Depósito mensal: "))
j = float(input("Juros sem porcentagem: "))
mes = 1
while mes <= 24:
    di = di + (di*j)
    print(f"Valor do mês {mes} é de: R${di:.2f}")
    mes = mes + 1
print(f"Seu valor total é de R${di:.2f}")