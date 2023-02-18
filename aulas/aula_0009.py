adicao = 10 + 10.2
print('Adição', adicao)
# Sempre que a adição for de um número int com um float
# O Resultado vai ser de um número float
# Adição pode ser float com int ou somente um

subtração = 10 - 5
print('Subtração', subtração)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)
# Sinal para multiplicação é asterisco *, somente um

divisao = 10 / 2.2 #float
print('Divisão', divisao)
# Divisão sempre vai ter o resultado com número float, independente se for int ou float

divisao_inteira = 10 // 2
print('Divisão inteira', divisao_inteira)
# Essa divisão sempre vai vir sem o resultado de número float
# Essa divisão ignora o float, depois da vírgula, o resultado é sempre 0

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)
# Muito cuidado com esse cálculo, o resultado pode travar a maquina
# Esse cálculo sempre vai ser composto por dois asterisco **
# Um asterisco * é MULTIPLICAÇÃO, dois asterisco ** é EXPONENCIAÇÃO

modulo = 25 % 5 # resto da divisão
print('Módulo', modulo)
# Esse cálculo vai dizer qual o resto da divisão
# Esse cálculo vai dizer se um número é divisível por outro
# Se for divisível o resultado é 0, se não for, vai haver resto