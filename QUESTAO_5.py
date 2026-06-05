#QUESTÃO 05

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def k_repeticoes(tam,vetor,k):
	num = []
	quant = []

	for i in range(tam):
		igual = None
		
		for j in range(len(num)):
			if vetor[i] == num[j]:
				igual = 1
				break
				
		if igual == None:
			temp = vetor[i]
			aparece = 0
			
			for i in range(tam):
				if vetor[i] == temp:
					aparece += 1
					
			if aparece >= k:
				num.append(temp)
				quant.append(aparece)

	if not num:
		print(f"\nNão há nenhum elemento que apareça ao menos {k} vezes nesse vetor!")
	else:
		print(f"\nOs elementos que aparecem ao menos {k} vezes nesse vetor, são:")
		for i in range(len(num)):
			print(f"\n'{num[i]}' que se repete {quant[i]} vezes!")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))
k = (int(input("Valor de k: ")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
k_repeticoes(tam,vetor,k)