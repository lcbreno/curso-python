# nome = input('Qual o seu nome? ')
# Essa função faz que o usuário interaja com você
# A resposta do usuário sempre vai voltar como uma string
# Para transformar a resposta em outro tipo, utilizamos a coerção de dados

# print(f'O seu nome é {nome=}')
# Se colocarmos = na frente da variável, vamos ter o valor acoplado a variável

numero_1 = (input('Digite um número: '))
numero_2 = (input('Digite outro número: '))

# print(f'A soma dos números é: {numero_1 + numero_2}')

# A soma desses dois números vai ser 15, no caso foi somado uma str
# Para isso fazemos a coerção para int 
# O primeiro exemplo acima está com a coerção na mesma linha, isso pode matar o programa
# Se o usuário digitar uma str por exemplo

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

# Aqui temos um exemplo de como fazer a coerção tendo a resposta do usuário sem matar o programa
# Mas se a resposta for uma strings vai continuar com erro 
# Porque a coerção foi feita para int