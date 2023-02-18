import math

base_do_retangulo = float(input('Digite o valor da base do retângulo: '))
altura_do_retangulo = float(input('Digite o valor da altura do retângulo: '))

area = (base_do_retangulo * altura_do_retangulo)
perimetro = (base_do_retangulo + altura_do_retangulo) * 2
diagonal = math.sqrt(altura_do_retangulo ** 2 + base_do_retangulo ** 2)

print('Area do retângulo = {:.4f}' .format(area))
print('Perimetro do retângulo = {:.4f}' .format(perimetro))
print('Diagonal do retângulo = {:.4f}' .format(diagonal))