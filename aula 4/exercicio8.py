deposito = float(input("Valor do depósito inicial: R$"))
taxa = float(input("Valor da taxa de juros da poupança em porcentagem:
"))
mes = 1
while mes <= 24:
deposito = deposito + (deposito * (taxa / 100))
print(f"Saldo do mês {mes} é de R${deposito:.2f}.")
mes += 1
print(f"O ganho obtido com os juros foi de R${deposito:.2f}.")

# esse eu tinha feito, mas não salvou por algum motivo.