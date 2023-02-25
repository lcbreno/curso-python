"""Problema "crescente"
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma 
mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O 
programa deve finalizar quando forem digitados dois valores iguais. """

while True:
        
        print('Digite dois números: ')
        numero1 = int(input())
        numero2 = int(input())

        if numero1 == numero2:
            break

        if numero1 > numero2:
            print('DECRESCENTE!')
        elif numero1 < numero2:
            print('CRESCENTE!')
            
        

    