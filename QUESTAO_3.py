#QUESTÃO 03

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def enc_mediana_o_logn(tam, vetor_u, vetor_v):
	ini = 0
	fim = tam
	mediana = None

	while ini <= fim:
		i = (ini + fim) // 2
		j = tam - i

		if i > 0:
			esq1 = vetor_u[i - 1]
		else:
			esq1 = None

		if i < tam:
			dir1 = vetor_u[i]
		else:
			dir1 = None

		if j > 0:
			esq2 = vetor_v[j - 1]
		else:
			esq2 = None

		if j < tam:
			dir2 = vetor_v[j]
		else:
			dir2 = None

		if (esq1 == None or dir2 == None or esq1 <= dir2) and (esq2 == None or dir1 == None or esq2 <= dir1):
			if esq1 == None:
				mediana = esq2
			elif esq2 == None:
				mediana = esq1
			elif esq1 > esq2:
				mediana = esq1
			else:
				mediana = esq2
			break
		elif esq1 != None and dir2 != None and esq1 > dir2:
			fim = i - 1
		else:
			ini = i + 1

	print(f"\nA mediana do conjunto unificado U e V é: {mediana}")

tam = (int(input("Tamanho dos vetores (n): ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor_u = criar_vet(tam,lim_i,lim_s)
vetor_v = criar_vet(tam,lim_i,lim_s)

vetor_u.sort()
vetor_v.sort()

print(f"\nVetor U Ordenado = {vetor_u}")
print(f"\nVetor V = {vetor_v}")

enc_mediana_o_logn(tam, vetor_u, vetor_v)