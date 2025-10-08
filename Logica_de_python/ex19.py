'''Crie um programa que pede dois números inteiros ao usuário: um numero e um divisor. O programa deve verificar e exibir duas iformações sobre o numero:'''
#Se o numero é múltiplo do divisor. Para ser múltiplo, a divisão deve ter resto.
#Se o numero é positivo, negativo ou zero.

numero = int(input("Digite um número: "))
divisor = int(input("Digite um divisor: "))

resultado = (numero / divisor)





if resultado % 2 == 0 and resultado > 0:
    print(f"{numero} é um número positivo e múltiplo de {divisor}")

elif resultado % 2 != 0 and resultado < 0:
    print(f"{numero} é um número negativo e n~eo é múltiplo de {divisor}")

else:
    print(f"{numero} é um múltiplo de  {divisor}")



