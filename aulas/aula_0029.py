# Se eu selecionar a variável e pressionar F2, automaticamente vai mudar todas variáveis juntas

"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

# try/except basicamente é igual if, elif e else
# Porém, serve para pular linhas que exibem um erro
# O Programa irá executar sem aparecer aquela linha que tem um erro
# Se existir um erro em try, automaticamente o programa pula para o except
# Sem exibir as linhas restante em try, porém, as que já foram executadas, apareceram