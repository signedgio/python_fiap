num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
operacao = (input("Qual operação você deseja realizar? (soma, subtração, multiplicação ou divisão): " ))
if operacao == "soma":
    resultado = num1 + num2
    print(f"A sua soma vale {resultado}")
elif operacao == "subtração":
    resultado = num1 - num2
    print(f"A sua subtração vale {resultado}")
elif operacao == "multiplicação":
    resultado = num1 * num2
    print(f"A sua multiplicação vale {resultado}")
elif operacao == "divisão":
    resultado = num1 / num2
    print(f"A sua divisão vale {resultado}")
## para realizarmos esse exercício, colocamos o resultado em cada uma das possibilidades if,
## assim evitando que o programa imprima todas as respostas.