import os

print('============')
print('CALCULADORA')
print('============')
print()

continuar = 0
while continuar == int(0):
    operacao = input('Qual operação deseja fazer (+,-,/,*)?: ')
    num1 = float(input('Informe o primeiro numero: '))
    num2 = float(input('Informe o segundo numero: '))
                            
    if operacao == '+': 
        print('O resultado de {} + {}'.format(num1, num2))
        print('é = '+ str(num1+num2))
        cont = input('Gostaria de continuar? 0 - Continuar | 1 - Parar : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break
        os.system('cls')         
   
    if operacao == '-': 
        print('O resultado de {} + {}'.format(num1, num2))
        print('é = '+ str(num1-num2))
        cont = input('Gostaria de continuar? 0 - Continuar | 1 - Parar : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break 
        os.system('cls') 
    
    if operacao == '*': 
        print('O resultado de {} + {}'.format(num1, num2))
        print('é = '+ str(num1*num2))
        cont = input('Gostaria de continuar? 0 - Continuar | 1 - Parar : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break 
        os.system('cls') 
    
    if operacao == '/': 
        print('O resultado é {} + {}'.format(num1, num2))
        print('é = '+ str(num1/num2))
        cont = input('Gostaria de continuar? 0 - Continuar | 1 - Parar : ')
        if cont == '1':
            print("Obrigado e volte sempre!")
            break 
        os.system('cls') 
    









    

        






    

