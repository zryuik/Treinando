'''Peça ao usuário sua idade em anos e converta para:

Meses

Dias

Horas'''

idade_anos = float(input("Digite sua idade: "))



idade_meses = idade_anos * 12 
idade_dias = idade_anos * 365
idade_horas = idade_dias * 24


print(f"Sua idade em meses é {idade_meses}")
print(f"Sua idade em dias é {idade_dias}")
print(f"Sua idade em {idade_horas}")