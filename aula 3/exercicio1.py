velocidade = float(input("Digite o valor da velocidade em km: "))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print(f"Você ultrapassou o limite de velocidade. Sua multa é de R$ {multa: .2f}")
else:
    print("Você está no limite de velocidade.")
