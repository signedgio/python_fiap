deposito = float(input("Valor do depósito inicial: R$"))
taxa = float(input("Valor da taxa de juros da poupança em porcentagem:
"))
investimento = float(input("Investimento mensal: R$"))
mes = 1
while mes <= 24:
deposito = deposito + (deposito * (taxa / 100)) + investimento
print(f"Saldo do mês {mes} é de R${deposito:.2f}.")
mes += 1
print(f"O ganho obtido com os juros foi de R${deposito:.2f}.")

# esse eu TAMBÉM tinha feito e não salvou