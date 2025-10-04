'''Remova o par chave-valor correspondente ao shopping "Plaza" do dicionário emails_gerentes utilizando o método .pop(). Imprima o dicionário emails_gerentes após a remoção.

Saída Esperada (Exemplo): {'Iguatemi': 'iguatemi@gmail.com', 'Barra': 'barra@gmail.com'}'''


emails_gerentes = {

    "Iguatemi": "iguatemi@gmail.com",

    "Plaza": "plaza@gmail.com",

    "Barra": "barra@gmail.com",

    }



emails_gerentes.pop("Plaza")

print(emails_gerentes)