#QUESTÃO 02

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def enc_k_maior(tam,vetor,k):
	atual_maior = None

	for vez in range(k):
		prox_maior = None
		
		for i in range(tam):
			if atual_maior == None:
				if prox_maior == None or vetor[i] > prox_maior:
					prox_maior = vetor[i]
			elif vetor[i] < atual_maior:
				if prox_maior == None or vetor[i] > prox_maior:
					prox_maior = vetor[i]
					
		atual_maior = prox_maior
		if atual_maior == None:
			break

	if atual_maior == None:
		print(f"\nNão há elementos distintos suficientes para encontrar o {k}º maior elemento!")
	else:
		print(f"\nO {k}º maior elemento nesse vetor é: {atual_maior}")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))
k = (int(input("Valor de k: ")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
enc_k_maior(tam,vetor,k)