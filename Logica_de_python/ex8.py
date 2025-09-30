'''Faça um programa que calcule o vértice da parábola da função:
f(x) = x² – 5x + 6'''

a = 1
b = -5
c = 6



xv = -b / (2 * a)
xy = a * (xv ** 2) + b * xv + c

print(f"O vértice da parábola é: ({xv},{xy})")

