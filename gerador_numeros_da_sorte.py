import random
import os


print('============================')
print()
print('GERADOR DE NÚMEROS DA SORTE')
print()
print('============================')
print()



qtd_numeros = {'megasena': 6, 'quina': 5, 'lotomania': 50, 'lotofacil': 15, 'jogobicho': 1}
limite_inf = {'megasena': 1, 'quina': 1, 'lotomania': 0, 'lotofacil': 1, 'jogobicho': 0}
limite_sup = {'megasena': 60, 'quina': 80, 'lotomania': 99, 'lotofacil': 25, 'jogobicho': 9999}

continuar = 0

while continuar == int(0):
    listajogos = input('Escolha o jogo => 1 - Mega Sena | 2 - Quina | 3 - Loto Mania | 4 - Loto Fácil | 5 - Jogo do Bicho: ')
    num_aleatorios_ms = random.sample(range(limite_inf['megasena'], limite_sup['megasena']+1), qtd_numeros['megasena'])
    num_aleatorios_q = random.sample(range(limite_inf['quina'], limite_sup['quina']+1), qtd_numeros['quina'])
    num_aleatorios_lm = random.sample(range(limite_inf['lotomania'], limite_sup['lotomania']+1), qtd_numeros['lotomania'])
    num_aleatorios_lf = random.sample(range(limite_inf['lotofacil'], limite_sup['lotofacil']+1), qtd_numeros['lotofacil'])
    num_aleatorios_jb = random.sample(range(limite_inf['jogobicho'], limite_sup['jogobicho']+1), qtd_numeros['jogobicho'])

    if listajogos == '1':
        print('Seus numeros da sorte na Mega Sena são: ' + str(sorted(num_aleatorios_ms)))
        cont = input('Gostaria de gerar outros numeros? 0 - Sim | 1 - Não : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break
        os.system('cls')

    if listajogos == '2':
        print('Seus numeros da sorte na Quina são: ' + str(sorted(num_aleatorios_q)))
        cont = input('Gostaria de gerar outros numeros? 0 - Sim | 1 - Não : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break
        os.system('cls')

    if listajogos == '3':
        print('Seus numeros da sorte na Loto Mania são: ' + str(sorted(num_aleatorios_lm)))
        cont = input('Gostaria de gerar outros numeros? 0 - Sim | 1 - Não : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break
        os.system('cls')

    if listajogos == '4':
        print('Seus numeros da sorte na Loto Fácil são: ' + str(sorted(num_aleatorios_lf)))
        cont = input('Gostaria de gerar outros numeros? 0 - Sim | 1 - Não : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break
        os.system('cls')

    if listajogos == '5':
        print('Seus numeros da sorte no Jogo do Bicho são: ' + str(num_aleatorios_jb))
        cont = input('Gostaria de gerar outros numeros? 0 - Sim | 1 - Não : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break
        os.system('cls')




