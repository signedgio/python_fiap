dias = int(input("Escreva quantos dias se passaram: "))
horas = int(input("Escreva quantas horas se passaram: "))
minutos = int(input("Escreva quantos minutos se passaram: "))
segundos = int(input("Escreva quantos segundos se passaram: "))

s1 = dias * 86400
s2 = horas * 3600
s3 = minutos * 60
s4 = segundos
soma = s1 + s2 + s3 + s4
print("A sua soma em segundos é", soma)
