# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo
print(11) # int
print(-11) # int
print(0) # int

# float -> Número com ponto flutuante
# O tipo de float representa qualquer número
# positivo ou negativo com ponto flutuante
# float sem sinal é considerado positivo
print(1.1, 10.11)
print(0.0, -1.5)
# Se tem casa decimal é float, se não tem casa decimal é int

# A função type mostra o tipo que o Python
# inferiu ao valor
print(type('teste'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))