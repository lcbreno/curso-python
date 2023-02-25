"""Problema "senha_fixa" (adaptado de URI 1114)
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de 
senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha 
for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo 
encerrado. Considere que a senha correta é o valor 2002. """


while True:
    senha = "2002"
    digite_a_senha = input('Digite a senha: ')

    if senha == digite_a_senha:
        print('Acesso permitido! ')
        break
    elif digite_a_senha != senha:
        print('Senha Invalida! Tente novamente: ')
        continue
    