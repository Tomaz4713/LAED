#QUESTÃO 08

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def comuns_nas_duas(tam_u, vetor_u, tam_v, vetor_v):
	comuns = []

	for i in range(tam_u):
		achou = None
		
		for j in range(tam_v):
			if vetor_u[i] == vetor_v[j]:
				achou = 1
				break
				
		if achou != None:
			repetido = None
			
			for k in range(len(comuns)):
				if vetor_u[i] == comuns[k]:
					repetido = 1
					break
					
			if repetido == None:
				comuns.append(vetor_u[i])

	if not comuns:
		print("\nNão há nenhum número que apareça simultaneamente nas duas listas!")
	else:
		print("\nOs números que aparecem em ambas as listas são:")
		for i in range(len(comuns)):
			print(f"\nO número '{comuns[i]}' está presente nas duas listas!")

tam_u = (int(input("Tamanho do vetor U: ")))
tam_v = (int(input("Tamanho do vetor V: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor_u = criar_vet(tam_u,lim_i,lim_s)
vetor_v = criar_vet(tam_v,lim_i,lim_s)

print(f"\nVetor U = {vetor_u}")
print(f"\nVetor V = {vetor_v}")

comuns_nas_duas(tam_u, vetor_u, tam_v, vetor_v)