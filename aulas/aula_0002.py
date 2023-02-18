# \r\n - caractere que nao vejo mas existe no sistema operacional -> CRLF
# \n -> LF - para unix (linux)

print(12, 34, 1011, sep="-", end='\n##')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-')

# sep é separação, argumento sep para definir qual separador usar
# letras maiúsculas nao existe no python, ele diferencia as palavras
# end usar no final do print, depois do último argumento
# se der um erro no python tente ler o erro, a maioria dos erros são respondidos automaticamente