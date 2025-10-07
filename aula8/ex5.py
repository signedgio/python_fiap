# 5. Escreva um programa que leia duas strings e gere
# uma terceira apenas com os caracteres que aparecem
# em uma delas.
# 1ª string: CTA
# 2ª string: ABC
# A ordem dos caracteres da terceira string não é
# importante.

string1 = "CTA"
string2 = "ABC"
string3 = ""

for letrasDiferentes in string1:
    if letrasDiferentes not in string2 and letrasDiferentes not in string3:
        string3 = string3 + letrasDiferentes

for letrasDiferentes in string2:
    if letrasDiferentes not in string1 and letrasDiferentes not in string3:
        string3 = string3 + letrasDiferentes

print(f"String 3: {string3}")