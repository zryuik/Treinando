'''Desenvolva uma calculadora simples que receba dois números e uma operação (+, -, *, /) e mostre o resultado'''

numero_1 = float(input("Dgigite um número: "))
numero_2 = float(input("Digite outro número: "))

operação = str(input("Qual operação você escolhe? [+, -, x, /]: "))

if operação == "+":
    print(f"A soma entre os números é ({numero_1+numero_2})")

elif operação == "-":
    print(f"A ssubtração entre os números é ({numero_1-numero_2})")

elif operação == "x":
    print(f"A multiplicação entre os números é ({numero_1*numero_2})")

elif operação == "/":
    print(f"A divisão entre os números é ({numero_1/numero_2})")
else:
    print("Operação invalida")