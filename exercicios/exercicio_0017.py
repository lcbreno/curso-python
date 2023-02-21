escala = input('Voce vai digitar a temperatura em qual escala (C/F)? ')

if escala == "F" or escala == "f":
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = 5 / 9 * (fahrenheit - 32)
    print('Temperatura equivalente em Celsius: {:.2f}' .format(celsius))
elif escala == "C" or escala == "c":
     celsius = float(input('Digite a temperatura em Celsius: '))
     fahrenheit = 9.0/5.0 * celsius + 32
     print('Temperatura equivalente em Fahrenheit: {:.2f}' .format(fahrenheit))
else:
    print('entrada invalida, digite apenas C ou F')

# Sempre que for usar um operador lógico, sempre usar a expressão/variável para dar certo
# Sempre que o usuário foi dar uma resposta ao input
# No if, elif e else, usar a resposta como STRING se for uma STRING a resposta dele