matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = somaTerc = maior = impares = 0
for b in range(0, 3):
    for c in range(0, 3):
        matriz[b][c] = int(input(f"Digite um valor para [{b}], [{c}]: "))
# max(matriz[1])
print("==" * 20)
for b in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[b][c]:^5}]", end='')
        if matriz[b][c] % 2 == 0:
            pares += matriz[b][c]
        if matriz[b][c] % 2 == 1:
            impares += 1
    print()
for c in matriz:
    somaTerc += c[2]
for c in matriz[1]:
    if c > maior:
        maior = c
# max(matriz[1])
print("==" * 20)
print(f"A soma dos numeros pares é: {pares}")
print(f"A soma dos numeros da terceira coluna é: {somaTerc}")
print(f"O maior numero da segunda linha é: {maior}")
print(f"A quantidade de numeros impares é: {impares}")
