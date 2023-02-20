minutos_utilizados = int(input('Digite a quantidade de minutos: '))
adicional = minutos_utilizados - 100
taxa = (adicional * 2)  + 50

if minutos_utilizados <= 100:
    print('Valor a pagar: R$: 50.00')
elif taxa:
    print('Valor a pagar: R$: {:.2f}' .format(taxa))