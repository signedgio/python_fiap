# 6. Escreva um programa que leia uma string e imprima
# quantas vezes cada caractere aparece nessa string.
# String: TTAAC
# Resultado:
# T: 2x
# A: 2x
# C: 1x

string = "TTAAC"
T = string.count("T")
A = string.count("A")
C = string.count("C")

print(f"T: {T}x")
print(f"A: {A}x")
print(f"C: {C}x")

