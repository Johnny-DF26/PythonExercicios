time = list()
jogador = dict()
partidas = list()
while True:
    print("=-"*30)
    partidas.clear()
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    qtd = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0,qtd):
        partidas.append(int(input(f"Quantos gols na partida {c+1}: ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
        if resp in 'SN':
            break
        print("ERRO ! Digite S ou N")
    if resp in 'N':
        break
print("=-"*30)
print("cod.",end='')
for i in jogador.keys():
    print(f"{i:>12}", end='')
print()
print("--"*30)
for k, v in enumerate(time):
    print(f" {k+1}: ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("--"*30)
while True:
    busca = int(input("Mostrar dados de qual jogador: "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com o código {busca}")
    else:
        print("--" * 30)
        print(f"-- LEVANTAMENTO DO JOGADOR {time[busca]['nome']} --")
        for k, v in enumerate(time[busca]['gols']):
            print(f" No jogo {k+1} fez {v} gols")
        print("--"*30)
print("FIM")
