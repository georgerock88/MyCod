import random
import os  


print('============')
print('Bem vindo ao jogo PEDRA, PAPEL E TESOURA.')
print('============')
print()

jogardinovo = 0
venceu = ('VOCÊ VENCEU!')
perdeu = ('VOCE PERDEU!')
bot = [1, 2, 3]

while jogardinovo == int(0):
    jogador = int(input('Escolha seu palpite => 1 - Pedra | 2 - Papel | 3 - Tesoura: '))
    escolha_bot = random.choice(bot)

    if jogador == escolha_bot:
        print("Seu palpite foi " + str(jogador) + ' e o do BOT foi ' + str(escolha_bot) + ' então ' + perdeu)
        cont = input('Quer jogar dinovo? 0 - Sim | 1 - Não : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break
        os.system('cls')

    if jogador != escolha_bot:
        print('Seu palpite foi ' + str(jogador) + ' e o do BOT foi ' + str(escolha_bot) + ' então ' + venceu)
        cont = input('Quer jogar dinovo? 0 - Sim | 1 - Não : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break
        os.system('cls')

