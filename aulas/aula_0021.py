# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser VERDADEIRAS
# Se qualquer valor for considerado falso, a expressão inteira será avaliada como falsa
# São considerados falsy (que vc já viu) 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
print(entrada)
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if True

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curti circuito
# O operador and tem que ser respondido como true para avaliar a expreção inteira
# Se algum valor for falso, a expreção inteira passa a ser falsa
print(True and False and True)
print(True and 0.0 and True)