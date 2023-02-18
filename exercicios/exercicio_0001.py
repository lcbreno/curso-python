largura = input('Digite a largura do terreno: ')
comprimento = input('Digite o comprimento do terreno: ')
valor_do_metro = input('Digite o valor do metro quadrado: ')

area = float(largura) * float(comprimento)
preco = float(valor_do_metro) * float(area)

print('Area do terreno = {:.2f}'.format(area))
print('Preco do terreno = {:.2f}'.format(preco))
