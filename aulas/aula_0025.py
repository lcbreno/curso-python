"""
Interpolação básica de strings
s - cadeia de caracteres
d e i - int
f - flutuador
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000,95897643
variavel = '%s, o preço é R$%.2f' %  (nome, preco)
print (variavel)
print('O hexadecimal de %d é %08X' %  (1500, 1500))

# Podemos escolher entre F-Strings, formart ou interpolação para usar
# Escolher uma dessas três tipos e praticar é uma boa tática