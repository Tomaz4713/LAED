#QUESTÃO 05

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def dobro_do_outro(tam,vetor):
	num = []
	dobro = []

	for i in range(tam):
		igual = None
		
		for j in range(tam):
			for k in range(len(dobro)):
				if vetor[i] == dobro[k]:
					igual = 1
					break
		
			if igual != None:
				break
			
			else:
				if vetor[i] == 2 * vetor[j]:
					dobro.append(vetor[i])
					num.append(vetor[j])

	if not dobro:
		print("\nNão há nenhum número que seja o dobro do outro nesse vetor!")
	else:
		print("\nOs números que representam o dobro de outro número no mesmo vetor, são:")
		for i in range(len(dobro)):
			print(f"\n'{dobro[i]}' que é o dobro de '{num[i]}'")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
dobro_do_outro(tam,vetor)