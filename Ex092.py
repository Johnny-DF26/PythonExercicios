from datetime import date
dados = dict()
dados['nome'] = str(input("Nome: "))
idade = int(input("Ano de nascimento: "))
dados['idade'] = date.today().year - idade
dados['ctps'] = int(input("Carteira de trabalho(0 nao tem): "))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input("Ano de Contratação: "))
    dados['salario'] = float(input("Salário R$: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - date.today().year)
print("-="*30)
for k, v in dados.items():
    print(f"- {k} tem o valor: {v}")
