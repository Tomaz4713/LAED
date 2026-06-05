#QUESTÃO 03

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def enc_prox_media(tam,vetor):
	soma = 0
	for i in range(tam):
		soma += vetor[i]

	media = soma / tam
	prox = None
	menor_dist = None

	for i in range(tam):
		dist = abs(vetor[i] - media)
		
		if menor_dist == None or dist < menor_dist:
			menor_dist = dist
			prox = vetor[i]

	print(f"\nMédia aritmética do vetor: {media:.2f}")
	print(f"\nO elemento mais próximo da média nesse vetor é: {prox}")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
enc_prox_media(tam,vetor)