print('Digite as tres distancias: ')
distancia1 = float(input())
distancia2 = float(input())
distancia3 = float(input())

if distancia1 > distancia2 > distancia3:
    print('MAIOR DISTANCIA = ', distancia1)
elif distancia2 > distancia3:
    print('MAIOR DISTANCIA = ', distancia2)
else:
    print('MAIOR DISTANCIA = ', distancia3)

# Se no if a VARIÁVEL deu false, pode descartar essa variável