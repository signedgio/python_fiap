nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = nota1 + nota2 / 2
print(f"A sua média é de {media}")
if media >= 6:
    print("Aprovado! ;)")
else:
    print("Reprovado. :(")