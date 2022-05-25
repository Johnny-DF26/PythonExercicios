valores = list()
for c in range(0,5):  # faz uma contagem de 0 a 5
    num = int(input("Digite um valor: ")) # recebe um numero inteiro
    if c == 0 or num > valores[-1]:  # condiciona se c for = 0 ou num é menor que os valores da lista
        valores.append(num)   # adiciona o numero na ultima posicao da lista
        print("Adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(valores):  # enquanto pos for menor que os nuemro da lista
            if num <= valores[pos]:  # verifica se num é menor que os valores da lista
                valores.insert(pos,num) # se true, adiciona o numero na posicao
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1


print(valores)
