"""
Fatiamento de cordas
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str |
"""
variavel = 'Olá mundo'
print(variavel[::-1])

# o P significa PASSO, basicamente é quantas caracteres você quer que ele vá PASSANDO (PASSO)
# Também aprendi sobre a função len, ela serve para contar caracteres de uma expressão

testando = str(1555) + 'teste'

print(len(testando))

# A função len não funciona para números int e float
# Mas podemos usar a coerção de dados para usar a função len

teste_fatiamento = 'testando'
print(teste_fatiamento[1:6:1])

# O exemplo acima é sobre fatiamento, bem simples de entender