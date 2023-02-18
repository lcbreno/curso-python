preco_unitario = float(input('Preço unitário do produto: '))
quantidade_comprada = int(input('Quantidade comprada: '))
dinheiro_recebido = float(input('Dinheiro recebido: '))

valor_total = preco_unitario * quantidade_comprada
troco = dinheiro_recebido - valor_total

print('TROCO = {:.2f}' .format(troco))