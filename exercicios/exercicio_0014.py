preco_unitario = float(input('Preço unitário do produto: '))
quantidade_comprada = int(input('Quantidade comprada: '))
dinheiro_recebido = float(input('Dinheiro recebido: '))

troco = dinheiro_recebido - (preco_unitario * quantidade_comprada)
faltante = (preco_unitario * quantidade_comprada) - dinheiro_recebido

if troco > 0:
    print('TROCO = {:.2f}' .format(troco))
else:
    print('DINHEIRO INSUFICIENTE. FALTAM {:.2f}' .format(faltante),'REAIS')