#Receba um número n e calcule a soma de todos os números de 1 até n.
n = int(input("Digite um numero:\n "))
soma = 0
contador = 1

while contador != n:
    soma += contador
    contador += 1

print(f"A soma dos numeros de 1 ate {n} é {soma}")
