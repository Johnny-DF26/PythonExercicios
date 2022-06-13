def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos o voto é Negado'
    elif 16 <= idade <= 18 or idade > 65:
        return f'Com {idade} anos o voto é Opcional'
    else:
        return f'Com {idade} anos seu voto é Obrigatório'


#   programa principal
print('-- ' * 30)
nascimento = int(input('Em que ano você nasceu: '))
print(voto(nascimento))
