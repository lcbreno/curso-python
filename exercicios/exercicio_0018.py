cod_produto = int(input('Codigo do produto comprado: '))
quantidade = float(input('Quantidade comprada: '))

produto1 = 5.00 * quantidade
produto2 = 3.50 * quantidade
produto3 = 4.80 * quantidade
produto4 = 8.90 * quantidade
produto5 = 7.32 * quantidade


if cod_produto == 1:
    print(f'Valor a pagar: R$: {produto1:.2f}')
elif cod_produto == 2:
    print(f'Valor a pagar: R$: {produto2:.2f}')
elif cod_produto == 3:
    print(f'Valor a pagar: R$: {produto3:.2f}')
elif cod_produto == 4:
    print(f'Valor a pagar: R$: {produto4:.2f}')
elif cod_produto == 5:
    print(f'Valor a pagar: R$: {produto5:.2f}')
else:
    print('Você digitou o código do produto incorreto.')
