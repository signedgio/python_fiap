# um programa que calcule a soma de 10 números

n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o número: "))
    soma = soma + x
    n = n + 1
print(f"Soma = {soma}")