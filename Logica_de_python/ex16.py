''' Para ser considerado bissexto, um ano precisa seguir uma lógica complexa de três regras. O programa só deve retornar True (Sim) se TODAS as condições necessárias forem atendidas:

O ano é divisível por 4.

E, o ano NÃO é divisível por 100.

OU, o ano é divisível por 400.

'''

ano = int(input("Digite um ano para descobrir se ele é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O {ano} é bissexto...")
else:
    print(f"O {ano} não é bissexto...")


