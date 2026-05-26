#QUESTÃO 07

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def quantas_inversoes(tam,vetor):
	inversoes = 0
	for i in range(tam-1):
		for j in range(i+1,tam,1):
			if vetor[j] < vetor[i]:
				inversoes += 1
				
	if inversoes == 0:
		print("\nNão há inversões nesse vetor!")
	else:
		print(f"\nO número de inversões nesse vetor é: '{inversoes}'")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
quantas_inversoes(tam,vetor)