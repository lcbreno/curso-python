"""Problema "validacao_de_nota" 
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a 
média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao 
intervalo [0,10]). Cada nota deve ser validada separadamente. """

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

while nota1 <= 10 and nota2 <= 10:

    if nota1 > 0 and nota2 > 0:
        print('MEDIA =', media)
        break
    else:
        print('Valor invalido! Tente novamente.')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
