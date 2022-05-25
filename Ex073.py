brasileirao = ('Corinthias','Bragantino','Atletico-MG','Coritiba','São Paulo','Santos','Cuiabá','Internacional','Avaí',
               'America-MG','Palmeiras','Flamengo','Botafogo','Fluminense','Ceará','Athletico-PR','Atlético-GO','Goiás',
               'Juventude','Fortaleza')
print('=='*50)
print(brasileirao)
print('=='*50)
print(f'Os 5 primeiros sao: {brasileirao[:5]}')
print('=='*50)
print(f'Os 4 ultimos sao: {brasileirao[16:]}')  # [-4:]
print('=='*50)
print(f'Times em ordem alfabética:,{sorted(brasileirao)}')
print(f'O Flamengo está na {brasileirao.index("Flamengo")+1}ª posição')
