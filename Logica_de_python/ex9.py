'''Crie um programa que simule o jogo Pedra, Papel e Tesoura para dois jogadores'''

print("-" * 30 )

jogador_1 = str(input("Qual você escolhe? [Pedra,Papel,Tesoura]: "))
jogador_2 = str(input("Qual você escolhe? [Pedra,Papel,Tesoura]: "))

print("-" * 30 )

if jogador_1 == "Pedra" and jogador_2 == "Tesoura":
    print(f"O Jogador 1 Venceu {jogador_1} ganha de {jogador_2}")

elif jogador_1 == "Papel" and jogador_2 == "Pedra":
    print(f"O Jogador 1 Venceu {jogador_1} ganha de {jogador_2}")

elif jogador_1 == "Tesoura" and jogador_2 == "Papel":
    print(f"O Jogador 1 Venceu {jogador_1} ganha de {jogador_2}")

elif jogador_2 == "Pedra" and jogador_1 == "Tesoura":
    print(f"O Jogador 2 Venceu {jogador_2} ganha de {jogador_1}")

elif jogador_2 == "Papel" and jogador_1 == "Pedra":
    print(f"O Jogador 2 Venceu {jogador_2} ganha de {jogador_1}")

elif jogador_2 == "Tesoura" and jogador_1 == "Papel":
    print(f"O Jogador 2 Venceu {jogador_2} ganha de {jogador_1}")
else:
    print("Jogada inválida.")

print("-" * 30 )