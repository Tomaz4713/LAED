#QUESTÃO 06

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def verificar_permutacao(tam_u, vetor_u, tam_v, vetor_v):
	if tam_u != tam_v:
		print("\nNão! As listas U e V não são permutações uma da outra porque possuem tamanhos diferentes!")
		return

	conferidos = []
	eh_permutacao = 1

	for i in range(tam_u):
		ja_conferido = None
		
		for j in range(len(conferidos)):
			if vetor_u[i] == conferidos[j]:
				ja_conferido = 1
				break
				
		if ja_conferido == None:
			temp = vetor_u[i]
			conferidos.append(temp)
			
			quant_u = 0
			for j in range(tam_u):
				if vetor_u[j] == temp:
					quant_u += 1
					
			quant_v = 0
			for j in range(tam_v):
				if vetor_v[j] == temp:
					quant_v += 1
					
			if quant_u != quant_v:
				eh_permutacao = None
				break

	if eh_permutacao == None:
		print("\nNão! As listas U e V NÃO são permutações uma da outra.")
	else:
		print("\nSim! As listas U e V são permutações uma da outra.")

tam_u = (int(input("Tamanho do vetor U: ")))
tam_v = (int(input("Tamanho do vetor V: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor_u = criar_vet(tam_u,lim_i,lim_s)
vetor_v = criar_vet(tam_v,lim_i,lim_s)

print(f"\nVetor U = {vetor_u}")
print(f"\nVetor V = {vetor_v}")

verificar_permutacao(tam_u, vetor_u, tam_v, vetor_v)