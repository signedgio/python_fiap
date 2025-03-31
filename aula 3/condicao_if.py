## se a condição for verdadeira, faça isso (if)
## caso não (else)
media_final = float(input("Digite sua média final de 0 a 10:"))
if media_final >= 6:
    print("Aprovado! :)")
else:
    print("Reprovado! :(")

## testanto todas as condições:
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
if a > b:
    print("O primeiro valor é maior!")
if a < b:
    print ("O segundo valor é maior!")