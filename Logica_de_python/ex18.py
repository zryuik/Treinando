'''Crie um programa que calcula a média final de um aluno com base em quatro avaliações com pesos distintos. O programa deve pedir as notas, calcular a média ponderada e, em seguida, determinar e exibir a situação do aluno: Aprovado, Prova Final ou Reprovado.'''

#O programa deve solicitar a entrada de quatro notas:
    #Notas do Teste 1 e da Oriva 1: pesos 2 e 8 respectivamente
    #Notas do Teste 2 e da Prova 2: pesos 2 e 8 respectivamente
#A média final deve ser calculada com usandfo a fórmula da média ponderada:


teste1 = float(input("Digite a nota do Teste 1: "))
prova1 = float(input("Digite a nota da Prova 1: "))
teste2 = float(input("Digite a nota do Teste 2: "))
prova2 = float(input("Digite a nota da Prova 2: "))


media = (teste1 * 2 + teste2 * 2 + prova1 * 8 + prova2 * 8) / 20

if media >= 7:
    print(f"Média Final: {media:.2f}")
    print("Situação: Aprovado")
elif media >= 4:
    print(f"Média Final: {media:.2f}")
    print("Situação: Prova Final")
else:
    print(f"Média Final: {media:.2f}")
    print("Situação: Prova Final")