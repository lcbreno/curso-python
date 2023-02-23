nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print('Seu nome é', nome)
    print('Seu nome invertido é', nome[::-1])
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÂO contém espaços')
    print('Seu nome contém', len(nome), 'caracteres')
    print('A primeira letra do seu nome é', nome[0])
    print('A última letra do seu nome é', nome[-1])
else:
    print('Desculpe, você deixou campos vazios.')
    
# Podemos colocar if, elif e else dentro de outros if... 
# Como o exemplo acima mostra
# Para mostrar somente a primeira caractere ou a última, não precisamos fazer igual o fatiamento
# Somente colocar colchetes com o índice que você quer que mostre