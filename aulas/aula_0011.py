# A primeira coisa que vai ser executada em um 'comando' é os parenteses
# Se tem parenteses dentro de parenteses (())
# Sempre vai ser executado de dentro para fora
# A ordem a seguir representa o que vai ser executado primeiro

# 1. (n + n) #PARENTESES
# 2. ** #EXPONENCIAÇÃO
# 3. * / // % #Multiplicação/Divisão/DivisãoInteira/Módulo
# 4. + - #Adição/Subtração

conta_1 = (1 + 1) ** (5 + 5) 
print(conta_1)

# EXPONENCIAÇÃO -> ELEVAR UM NÚMERO
# EXPONENCIAÇÃO -> 2 elevado a 10 -> multiplicar 10x o número 2
# Exemplo: 2*2*2*2*2*2*2*2*2*2 = 1024