'''Desenvolva um programa que peça ao usuário dois números e exiba:

A soma

A subtração

A multiplicação

A divisão'''

numero_1 = float(input("Digite um número: "))

numero_2 = float(input("Digite outro número: "))


operação = str(input("Qual operação você deseja? [+,-,x,/] "))

if operação == "+":
    print(f"O resultado da soma entre os números é: {numero_1+numero_2}")
elif operação == "-":
    print(f"O resultado da subtração ente os números é: {numero_1-numero_2}")
elif operação == "x":
    print(f"O resultado da multiplicação entre os números é {numero_1*numero_2}")
elif operação == "/":
    print(f"O resultado da divisão entre os números é {numero_1/numero_2}")
