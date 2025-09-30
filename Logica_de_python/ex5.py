'''Solicite três números ao usuário e mostre qual é o maior deles.'''

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
numero_3 = int(input("Digite mais um número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"O maior número digitado foi {numero_1}")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"O Maior número digitado foi {numero_2}")
else:
    print(f"O maior numero digitado foi {numero_3}")


#Outra forma de fazer

# if numero_1 > numero_2 and numero_1 > numero_3:
#     print(f"O maior número digitado foi {numero_1}")
# else:
#     if numero_2 > numero_1 and numero_2 > numero_3:
#         print(f"O maior número digitado foi {numero_2}")
#     else:
#         print(f"O maior número digitado foi {numero_3}")

