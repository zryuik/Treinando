#Criar dicionário de contatos
# Peça ao usuário para digitar o nome e o telefone de 3 pessoas e salve em um dicionário. Depois, mostre todos os contatos.


nome_contatos = {
    
}


for i in range(0,3):
    novo_nome = str(input("Digite o nome que deseja adicionar: "))
    novo_contato = str(input("Digite o contato que você deseja adicionar: "))
    nome_contatos[novo_nome] = novo_contato


for nome in nome_contatos:
    telefone = nome_contatos[nome]


    print(f"Nome: {nome} Telefone: {telefone}")