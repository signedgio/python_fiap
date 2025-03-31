distancia = float(input("Distância a ser percorrida em km: "))
if distancia <= 200:
    print(f"O valor da sua passagem é de R$ {distancia * 0.50}")
else:
    print(f"O valor da sua passagem é de R$ {distancia * 0.45}")