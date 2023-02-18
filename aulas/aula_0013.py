nome = 'João Santos'
altura = 1.72
peso = 83
imc = peso / (altura * altura)

# F-Strings (formatação de strings)
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
# Existe a possibilidade de colocar variáveis dentro de variáveis 
# Com a F-Strings
# Existe a possibilidade de alterar as casas decimais dos números 
# Existe a possibilidade de colocar vírgula nos números por meio de F-Strings

print(linha_1)
print(linha_2)
print(linha_3)

# João Santos tem 1.72 de altura,
# pesa 83 quilos e seu IMC é
# 28.055705786911847