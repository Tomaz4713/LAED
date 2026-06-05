#QUESTÃO 04

import random

def criar_mat(tam,lim_i,lim_s):
	matriz = [0] * tam
	for i in range(tam):
		matriz[i] = [0] * tam

	for i in range(tam):
		for j in range(tam):
			matriz[i][j] = random.randint(lim_i,lim_s)

	return matriz

def enc_elementos_iguais(tam, matriz):
	num = []
	quant = []

	for i in range(tam):
		for j in range(tam):
			igual = None
			
			for k in range(len(num)):
				if matriz[i][j] == num[k]:
					igual = 1
					break
					
			if igual == None:
				temp = matriz[i][j]
				aparece = 0
				
				for l in range(tam):
					for c in range(tam):
						if matriz[l][c] == temp:
							aparece += 1
							
				if aparece > 1:
					num.append(temp)
					quant.append(aparece)

	if not num:
		print("\nNão existem elementos iguais nesta matriz!")
	else:
		print("\nSim, existem elementos iguais na matriz M:")
		for i in range(len(num)):
			print(f"\nO elemento '{num[i]}' aparece {quant[i]} vezes!")

tam = (int(input("Tamanho da matriz (n): ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

matriz = criar_mat(tam,lim_i,lim_s)
print("\nMatriz =")
for i in range(tam):
	print(matriz[i])

enc_elementos_iguais(tam, matriz)