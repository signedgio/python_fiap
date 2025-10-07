
frase = "Hello world!"
print(len(frase))
print(frase[0])

###################################################################################

a = "Hello"
b = "World"
print(a, b)
print(a + " " + b)
c = "!"
print(a, b + c)
print(a + " " + b + c)
print(a, b + c *3)

###################################################################################

frase = "Hello World!"
print(frase[6:11])
## aqui ele conta desde o W até o d. precisamos colocar um número acima da
# ## posição, então por isso 11.
print(frase[6:-1])
## funciona assim também.
print(frase[6:])
## vai até o final. saída: "World!"

####################################################################################

nome = "Gio"
idade = 18
altura = 1.60
print(f"A {nome} tem {idade} anos e {altura} de altura.")

# cep = input("Digite seu CEP: ")
# print(f"{cep[:5]}-{cep[5:]}")

####################################################################################

frase1 = "Hello World!"
# frase1[11] = "!!!" tentar modificar uma string por posição NÃO FUNCIONA!!!!!
frase2 = list("Hello world!")
print(frase2)
frase2[11] = "!!!"
print(frase2)
frase2 = "".join(frase2)
print(frase2)
frase2 = " ".join(frase2)
print(frase2)

## esse "".join funciona pra tornar uma lista em string.
## a escolha de ter um espaço entre as aspas no join modifica o jeito que a string
## vai ser printada.

#####################################################################################

## verificação do início (start) e do fim (end) de uma string & uso do in.

fRaSe = "Oi mundo!"
print(fRaSe.startswith("Oi"))
print(fRaSe.endswith("mundo!"))
## saída = True
verdade = "txtForthGenLeaders"
print(verdade.startswith("t"))
## saída = True. como está tudo junto, qualquer letra do começo vai funcionar.
print("Oi" in fRaSe)
## saída = True
print("oi" in fRaSe)
## saída = False

####################################################################################

fraseeeeee = "Oi mundoooooo!"
print(fraseeeeee.count("o"))
# saída = 6. contou quantas letra "o" existem na string.

####################################################################################

## perguntar se o que está sendo buscado existe ou não na string. se sim, sáida = 0.
## se não, sáida = -1.

string = "Oi mundo!"
print(string.find("Oi"))
print(string.find("oi"))

####################################################################################

## centralizar, mexer pra direita e pra esquerda.

titulo = "Oi mundo!"
print(titulo.center(30, "*"))
## saída: **********Oi mundo!***********
print(titulo.ljust(50, "!"))
## saída: Oi mundo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

####################################################################################

## separar e modificar momentaneamente uma string.

frase4 = "TXT líderes da quarta geração."
print(frase4.split())
frase5 = "TXT, o grupo conhecido como os maiores de sua geração."
print(frase5.split(","))
print(frase5)
print(frase5.replace("como os maiores", "por ser o maior"))

## lembrando que, ao usarmos o replace, ele não vai mudar a string realmente.
## estará diferente apnas no momento em que foi usado. quando colocarmos pra
## printar novamente, vai imprimir o original.

## pra mudar, fazemos assim:

frase5 = "TXT, o grupo conhecido como os maiores de sua geração."
frase6 = frase5.replace("como os maiores", "por ser o maior")
print(frase6)

###################################################################################

# sep=’separador‘ – Especifica como as strings serão
# separadas, se houver mais do que uma. O padrão é um
# espaço em branco.
# end=’caractere‘ – Especifica o caractere que é impresso no
# final da linha. O padrão é \n, uma quebra de linha.

print("Hello", "world")
print('Hello', "world", sep=" ")
print('Hello', "world", sep=", ")
print("Hello", "world")
print('Hello', "world", end="\n")
print('Hello', "world", end="\n\n")
print('Hello', "world", sep=", ", end="!")
