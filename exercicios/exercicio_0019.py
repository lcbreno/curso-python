salario = float(input('Digite o salario da pessoa: '))
vinte_porcento = ((salario / 100) * 20) + salario
quinze_porcento = ((salario / 100) * 15) + salario
dez_porcento = ((salario / 100) * 10) + salario
cinco_porcento = ((salario / 100)  * 5) + salario

if salario <= 1000.00:
    print(f'Novo salario = R$ {vinte_porcento:.2f}')
    print(f'Aumento = R$ {vinte_porcento - salario:.2f}')
    print('Porcentagem =', '20%')
elif salario <= 3000.00:
    print(f'Novo salario = R$ {quinze_porcento:.2f}')
    print(f'Aumento = R$ {quinze_porcento - salario:.2f}')
    print('Porcentagem =', '15%')
elif salario <= 8000.00:
    print(f'Novo salario = R$ {dez_porcento:.2f}')
    print(f'Aumento = R$ {dez_porcento - salario:.2f}')
    print('Porcentagem =', '10%')
elif salario > 8000.00:
    print(f'Novo salario = R$ {cinco_porcento:.2f}')
    print(f'Aumento = R$ {cinco_porcento - salario:.2f}')
    print('Porcentagem =', '5%')
    