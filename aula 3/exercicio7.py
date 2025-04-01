quantidade_consumida = float(input( "Qual é a quantidade consumida de KwH?: "))
tipo_de_instalacao = (input( "Qual é o tipo de instalação? (residencial (R), comercial (C) ou industrial (I): "))
if "residencial" == 500:
    preco = 0.40
else:
    preco = 0.65
if "comercial" == 1000:
    preco = 0.55
else:
    preco = 0.60
if "industrial" == 5000:
    preco = 0.55
else:
    preco = 0.60

preco_total = (quantidade_consumida * preco)
print(f"O preço a pagar é de R${preco_total}")