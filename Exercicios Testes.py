
from random import randint
num = randint(1,10)
chute = tent = 0
while chute != num:
    chute = int(input("Digite um numero: "))
    tent += 1
    if chute > num:
        print("Muito alto")
    elif chute < num:
        print("Muito baixo")
    elif chute == num:
        print("Acertou !!!")
print(f"Voçê tentou {tent} vezes ate acertar")