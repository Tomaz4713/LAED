#QUESTÃO 05

import random

def criar_mat(tam,lim_i,lim_s):
	matriz = [0] * tam
	for i in range(tam):
		matriz[i] = [0] * tam

	for i in range(tam):
		for j in range(tam):
			matriz[i][j] = random.randint(lim_i,lim_s)

	return matriz

def enc_linhas_iguais(tam, matriz):
	lin1 = []
	lin2 = []

	for i in range(tam):
		for j in range(i + 1, tam):
			sao_iguais = 1
			
			for k in range(tam):
				if matriz[i][k] != matriz[j][k]:
					sao_iguais = None
					break
					
			if sao_iguais != None:
				lin1.append(i + 1)
				lin2.append(j + 1)

	if not lin1:
		print("\nNão existem duas linhas exatamente iguais nesta matriz!")
	else:
		print("\nSim, existem linhas exatamente iguais na matriz M:")
		for i in range(len(lin1)):
			print(f"\nAs linhas {lin1[i]} e {lin2[i]} são exatamente iguais!")

tam = (int(input("Tamanho da matriz (n): ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

matriz = criar_mat(tam,lim_i,lim_s)
print("\nMatriz =")
for i in range(tam):
	print(matriz[i])

enc_linhas_iguais(tam, matriz)