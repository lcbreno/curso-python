"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_int = int(input('Digite um número inteiro: '))

if type(numero_int) != int:
    print('Este número não é inteiro')

if (numero_int) % 2:
    print('Este número é ímpar')
elif (numero_int):
   print('Este número é par')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = (input('Qual o horário? '))

#if horario <= 11:
   # print('Bom dia')
#elif horario <= 17:
    #print('Boa tarde')
#elif horario <= 23:
    #print('Boa noite')

try:

    entrada = int(horario)

    if entrada >= 0 and entrada <= 11:
        print('Bom dia')
    elif entrada >= 12 and entrada<= 17:
        print('Boa tarde')
    elif entrada >= 18 and entrada<= 23:
        print('Boa noite')
    else:
        print('Você digitou o horário errado')
except:
    print('Por favor, digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual seu nome? ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
   print('Seu nome é muito grande')