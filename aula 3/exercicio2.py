a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
# maior
if a > b and a > c:
    print("O valor de a é o maior")
if b > a and b > c:
    print("O valor de b é o maior")
if c > a and c > b:
    print("O valor de c é o maior")
# menor
if a > b and c > b:
    print("O valor de b é o menor")
if a > c and b > c:
    print("O valor de c é o menor")
if b > a and c > a:
    print("O valor de a é o menor")
