# if / elif      / else
# se / se não se / se não
# não pode-se ter elif ou else sozinhos, os dois dependem do if

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')

# Pode-se usar outra condição para checar sem problemas, portanto, pular uma linha

if 10 == 10:
    print('Outro if')


print('Fora do if')