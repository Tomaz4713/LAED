#QUESTÃO 04

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def enc_elem_isolado(tam, vetor):
	isolados = []

	for i in range(tam):
		tem_menos_um = None
		tem_mais_um = None
		
		for j in range(tam):
			if vetor[j] == vetor[i] - 1:
				tem_menos_um = 1
			if vetor[j] == vetor[i] + 1:
				tem_mais_um = 1
				
		if tem_menos_um == None and tem_mais_um == None:
			repetido = None
			
			for k in range(len(isolados)):
				if vetor[i] == isolados[k]:
					repetido = 1
					break
					
			if repetido == None:
				isolados.append(vetor[i])

	if not isolados:
		print("\nNão há nenhum elemento isolado nesse vetor!")
	else:
		print("\nOs elementos isolados encontrados nesse vetor, são:")
		for i in range(len(isolados)):
			print(f"\nO número '{isolados[i]}' está isolado!")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
enc_elem_isolado(tam, vetor)