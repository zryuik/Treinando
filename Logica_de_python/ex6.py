'''Peça ao usuário uma idade e classifique em:

Criança (0–12)

Adolescente (13–17)

Adulto (18–64)

Idoso (65 ou mais)'''

idade = int(input("Digite sua idade: "))

if idade > 0 and idade < 13:
    print("Voce é criança")
elif idade < 18:
    print("Voce é adolescente")