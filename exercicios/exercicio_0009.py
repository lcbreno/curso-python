medida_a = float(input('Digite a medida A: '))
medida_b = float(input('Digite a medida B: '))
medida_c = float(input('Digite a medida C: '))

area_quadrado = medida_a ** 2
area_triangulo =  (medida_a * medida_b) / 2
area_trapezio = (medida_a + medida_b) * medida_c / 2

print('AREA DO QUADRADO = {:.4f}' .format(area_quadrado))
print('AREA DO TRIANGULO = {:.4f}' .format(area_triangulo))
print('AREA DO TRAPEZIO = {:.4f}' .format(area_trapezio))