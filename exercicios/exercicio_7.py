nome = input('Nome: ')
valor_hora = float(input('Valor por hora: '))
horas_trabalhadas = int(input('Horas trabalhadas: '))

pagamento = valor_hora * horas_trabalhadas
pagamento = f'{pagamento:.2f}'

print('O pagamento para', nome, 'deve ser', pagamento)