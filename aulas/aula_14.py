a = 'AAA'
b = 'BBB'
c = 1.1
string = 'b= {1} a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)

# Se colocar chaves e der um erro: out of range (fora de alcance)
# Pode-se usar número começando do 0, tudo que tem uma ordem, começa do 0
# Assim possibilita colocar várias vezes a variável na função format
# O exemplo acima está com duas variáveis, isso é um exemplo de que é possível criar isso
# Basicamente esssa função possibilita colocar várias variáveis dentro de uma variável
# Essa função é quase igual a da aula passada, mas tem alguns recursos a mais, como usar índice 
# Para colocar varias vezes a variável
# Quando uma função está dentro de um objeto, essa função é chamada de método

print(formato)