# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar
# ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a
# seguir para obter o preço de cada produto:
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro
# código deve gerar a mensagem de erro “Código inválido”.

a_pagar = 0
while True:
    cod = int(input("Digite o código do produto: "))
    preco = 0
    if cod == 0:
        break
    elif cod == 1:
        preco = 0.50
    elif cod == 2:
        preco = 1.00
    elif cod == 4:
        preco = 4.00
    elif cod == 5:
        preco = 7.00
    elif cod == 9:
        preco = 8.00
    else:
        print("Código inválido! Por favor, insira novamente.")
    if preco != 0:
        quantidade = int(input("Quantos desse produto foram comprados? "))
        a_pagar = a_pagar + (preco*quantidade)
print(f"Você deve pagar R${a_pagar:.2f}")


# tem uma ordem correta pra ir colocando as coisas. eu tava colocando o código e a quantidade antes do true.
# não pode! tem que colocar de acordo com oq vamos fazendo.
