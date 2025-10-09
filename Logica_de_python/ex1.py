'''Crie um programa que peça ao usuário seu nome e idade, e depois exiba a mensagem personalizada:
“Olá, [nome], você tem [idade] anos!”'''
###
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}, você tem {idade} anos")