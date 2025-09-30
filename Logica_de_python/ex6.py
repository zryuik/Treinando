'''Peça ao usuário uma idade e classifique em:

Criança (0–12)

Adolescente (13–17)

Adulto (18–64)

Idoso (65 ou mais)'''

idade = int(input("Digite sua idade: "))

if idade == 0:
    print("Idade inválida")

elif idade < 13:
    print("Voce é Criança")

elif idade < 18:
    print("Voce é Adolescente")

elif idade <65:
    print("Voce é Adulto")
    
else:
    print("Voce é Idoso")