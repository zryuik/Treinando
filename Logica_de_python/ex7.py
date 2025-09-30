'''Desenvolva um programa que calcule o IMC e exiba a classificação:

Abaixo do peso (<18.5)

Peso normal (18.5–24.9)

Sobrepeso (25–29.9)

Obesidade (≥30)'''

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu imc é {imc:.2f}")

if imc < 18.5:
    print("Voce esta abaixo do peso")

elif imc < 25:
    print("Voce esta no peso normal")

elif imc < 30:
    print("Voce esta sobrepeso")

else:
    print("Você esta obeso")


