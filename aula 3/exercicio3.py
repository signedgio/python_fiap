salario = int(input("Digite o valor do seu salário em reais: "))
if salario > 1250:
    print(f"Seu aumento é de R$ {(salario * 0.10)} e seu salário total é de R$ {(salario + salario * 0.10)}")
else:
    print(f"Seu aumento é de R$ {(salario * 0.15)} e seu salário total é de R$ {(salario + salario * 0.15)}")