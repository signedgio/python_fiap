# 2. A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
# T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura,
# assim como a temperatura média.


temperatura = [-10, -8, 0, 1, 2, 5, -2, -4]
menorTemp = temperatura[0]
maiorTemp = temperatura[0]
soma = 0

for quente in temperatura:
    if quente > maiorTemp:
        maiorTemp = quente
    soma += quente # aqui vai somar todos os valores da lista!
print(f"A maior temperatura foi de {maiorTemp}°C.")

for frio in temperatura:
    if frio < menorTemp:
        menorTemp = frio
print(f"A menor temperatura foi de {menorTemp}°C.")

media = soma/len(temperatura)
print(f"A média de temperatura é de {media}°C")