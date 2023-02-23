"""id  = identidade do objeto"""
# Algoritomo = solucionar problemas

teste_1 = 'a'
teste_2 = "b"

print(id(teste_1))
print(id(teste_1))

# A função ID serve para você ver qual o valor da memória
# No python, se o valor de duas variáveis forem iguais
# O valor ID pode ser que seja o mesmo, isso depende muito
# Iremos ver mais disso mais pra frente

"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')