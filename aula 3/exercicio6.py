casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu salário: "))
anos = float(input("Digite em quantos anos a casa será paga: "))
meses = anos * 12
prestacao_mensal = casa / meses
limite_prestacao = 0.30 * salario
print(f"Este é o limite por prestação: {limite_prestacao}")

if prestacao_mensal <= limite_prestacao:
    print("Seu empréstimo foi aprovado!")
    print(f"O valor da sua parcela esse mês é de R${prestacao_mensal: .2f}")
else:
    print("Seu empréstimo foi recusado.")
    print(f"O valor de sua prestação foi de R${prestacao_mensal: .2f}, excedendo o limite de 30%")
