nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota_final = nota1 + nota2

if nota_final > 60.0:
    print('NOTA FINAL =', nota_final)
elif nota_final < 60.0:
    print('NOTA FINAL =', nota_final)
    print('REPROVADO')