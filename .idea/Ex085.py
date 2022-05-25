numeros = [[],[]]
num = 0
for c in range(0,7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f"Os numeros pares são:{numeros[0]}")
print(f"Os numeros impares são: {numeros[1]}")
