#peça 3 numeros e informe qual e maior entre os 3
numeros = []
for _ in range(0,3):
    numero = int(input(f"Digite o {_+1}º numero: "))
    numeros.append(numero)
##
print(f"Os números digitados foram: {numeros}")
print(f"O maior numero digitado foi {max(numeros)}")