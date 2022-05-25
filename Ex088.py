from random import randint
lista = list()
jogos = list()
print("=="*20)
qtd = int(input("Quantos jogos sortear: "))
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1,25)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 15:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("=="*20)
for i, l in enumerate(jogos):
    print(f"Jogo {i+1:^1}: {l}")
print("=="*20)