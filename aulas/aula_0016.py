# if / elif      / else
# se / se não se / se não

# if pode "viver" sozinho (se a resposta do usuário for igual ao meu código)
# sempre que colocar if e elif, o else passa ser a obrigatório
# o usuário nem sempre vai responder a resposta certa de if ou elif
# por isso o else passa a ser "obrigatório"
# elif sempre é ao contrário de if

entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')
