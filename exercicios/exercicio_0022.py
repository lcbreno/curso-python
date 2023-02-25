"""Problema "quadrante" 
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no 
sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O 
algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem 
escrever mensagem alguma). """

# O While só é interrompido quando a CONDIÇÃO que estiver dentro dele for FALSE
# Enquanto a condição que estiver do lado do while for TRUE, o While vai continuar rodando
# Quando a condição que estava do lado do while passa a ser FALSE, ele é interrompido automaticamente
# Condição = variável + um cálculo, por exemplo.

print('Digite os valores das coordenadas X e Y: ')
coordenada_x = int(input())
coordenada_y = int(input())

while coordenada_x != 0 or coordenada_y != 0:

    if coordenada_x > 0 and coordenada_y > 0:
            print('QUADRANTE Q1')
    elif coordenada_x < 0 and coordenada_y > 0:
            print('QUADRANTE Q2')
    elif coordenada_x < 0 and coordenada_y < 0:
            print('QUADRANTE Q3')
    elif coordenada_x > 0 and coordenada_y < 0:
            print('QUADRANTE Q4')

    print('Digite os valores das coordenadas X e Y: ')
    coordenada_x = int(input())
    coordenada_y = int(input())