numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
numero3 = int(input('Terceiro valor: '))

if numero1 < numero2 < numero3:
    print('MENOR =', numero1)
elif numero2 < numero1 < numero3:
    print('MENOR =', numero2)
else:
    print('MENOR =', numero3)