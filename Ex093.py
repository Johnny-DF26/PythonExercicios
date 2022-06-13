jogador = dict()
Todosgols = list()
total = 0
jogador['nome'] = str(input("Nome do jogador: "))
part = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
jogador['gols'] = Todosgols
for c in range(0,part):
    partidas = int(input(f"Quantos gols na partida {c + 1}: "))
    total = total + partidas
    Todosgols.append(partidas)
# jogador['gols'] = sum(partidas)
jogador['total'] = total
print("=-"*30)
print(jogador)
print("=-"*30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("=-" * 30)
print(f"O jogador {jogador['nome']} jogou {part} partidas.")
for k, v in enumerate(jogador['gols']):
    print(f"  => Na partida {k}, fez {v} gols.")
