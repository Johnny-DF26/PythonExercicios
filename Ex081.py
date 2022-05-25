numeros = []
while True:
    numeros.append(int(input("Digite um numero: ")))
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Deseja continuar?[S/N]: ")).upper().strip()
    if resp == 'N':
        break
print("=="*20)
print(f"Voce digitou {len(numeros)} elementos")
numeros.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {numeros}")
if 5 in numeros:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista !")
