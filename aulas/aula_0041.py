""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')

# Else no while só vai ser executado se não houver um break sendo ativado dentro do while
# Em qualquer situação o else é executado, porém, se haver um break ele não vai ser
# Esse é um recurso que não é muito usado, mas podemos usar como o exemplo acima