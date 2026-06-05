#QUESTÃO 01

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def enc_terc_maior(tam,vetor):
	maior = None
	seg_maior = None
	terc_maior = None

	for i in range(tam):
		if maior == None:
			maior = vetor[i]
			
		elif vetor[i] > maior:
			terc_maior = seg_maior
			seg_maior = maior
			maior = vetor[i]
			
		elif vetor[i] != maior:
			if seg_maior == None:
				seg_maior = vetor[i]
			elif vetor[i] > seg_maior:
				terc_maior = seg_maior
				seg_maior = vetor[i]
			elif vetor[i] != seg_maior:
				if terc_maior == None:
					terc_maior = vetor[i]
				elif vetor[i] > terc_maior:
					terc_maior = vetor[i]

	if maior == None:
		print("\nO vetor está vazio!")
		
	elif seg_maior == None:
		print(f"\nMaior elemento: {maior}")
		print("\nNão há elementos distintos suficientes para encontrar o terceiro maior!")
		
	elif terc_maior == None:
		print(f"\nMaior elemento: {maior}")
		print(f"\nSegundo maior elemento: {seg_maior}")
		print("\nNão há um terceiro maior elemento distinto nesse vetor!")
		
	else:
		print(f"\nMaior elemento: {maior}")
		print(f"\nSegundo maior elemento: {seg_maior}")
		print(f"\nO terceiro maior elemento nesse vetor é: {terc_maior}")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
enc_terc_maior(tam,vetor)