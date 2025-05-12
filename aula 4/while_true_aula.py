# enquanto verdadeiro (true), execute esse bloco...
# saímos do bloco true colocando break
# nesse caso, se o número for igual a zero, entra no if. caso não seja, vai para o print.
soma = 0
while True:
 num = int(input("Digite um número a somar ou 0 para sair: "))
 if num == 0:
  break
 soma += num
print(soma)