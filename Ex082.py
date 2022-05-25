"""
numeros = []
impares = []
pares = []
while True:
    num = int(input("Digite um numero: "))
    numeros.append(num)
    resp = ' '
    while resp not in "NS":
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)
    if resp == "N":
        break
print(f"A lista completa é: {numeros}")
print(f"A lista dos numeros pares é: {pares}")
print(f"A lista dos numeros impares é: {impares}")
"""

num = []
impar = []
par = []

while True:
    num.append(int(input("Digite um numero: ")))
    resp = str(input("Quer continuar?[S/N]: ")).strip().upper()
    if resp == "N":
        break
for i, c in enumerate(num):
    if c % 2 == 0:
        par.append(c)
    elif c % 2 == 1:
        impar.append(c)

print(num)
print(par)
print(impar)
