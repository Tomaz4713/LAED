#QUESTÃO 07

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def enc_repetidos_proximos(tam, vetor, k):
	num = []
	pos1 = []
	pos2 = []

	for i in range(tam):
		for j in range(i + 1, tam):
			if vetor[i] == vetor[j]:
				distancia = j - i
				
				if distancia <= k:
					repetido = None
					
					for m in range(len(num)):
						if num[m] == vetor[i]:
							repetido = 1
							break
							
					if repetido == None:
						num.append(vetor[i])
						pos1.append(i + 1)
						pos2.append(j + 1)

	if not num:
		print(f"\nNão existem elementos repetidos a uma distância de no máximo {k} um do outro!")
	else:
		print(f"\nSim! Foram encontrados elementos repetidos dentro da distância máxima de {k}:")
		for i in range(len(num)):
			print(f"\nO número '{num[i]}' (nas posições {pos1[i]}º e {pos2[i]}º)")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))
k = (int(input("Distância máxima (k): ")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
enc_repetidos_proximos(tam, vetor, k)