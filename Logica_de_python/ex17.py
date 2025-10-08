'''Desenvolva um programa que calcula o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve pedir o peso (em quilogramas) e a altura (em metros),
calcular o IMC e, em seguida classificar o resultado em uima das categorias abaixo.'''

#a fórmula para o cálculo do IMC é: IMC = Peso/altura²

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso/altura**2

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Classificação: Abaixo do peso.") 

elif imc <24.9:
    print(f"Seu IMC é {imc:.2f}. Classificação: Peso normal.")

elif imc <29.9:
    print(f"Seu IMC é {imc:.2f}. Classificação: Sobrepeso.")
    
else:
    print(f"Seu IMC é {imc:.2f}. Classificação: Obesidade.")



