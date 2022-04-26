from time import sleep
import emoji
print('=========================================')
print('Contagem Regressiva:')
for c in range(10, 0, -1):
    sleep(0.5)
    print(c)
print(emoji.emojize('Buuuummm \033[31m:fireworks::sparkler:\033[m'))
