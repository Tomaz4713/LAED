#QUESTÃO 06

import random

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam

	for i in range(tam):
		vetor[i] = random.randint(lim_i,lim_s)

	return vetor

def dois_mais_proximos(tam, vetor):
	num1 = None
	num2 = None
	diferenca = None

	for i in range(tam):
		for j in range(tam):
			if vetor[i] - vetor[j] != 0:
				if diferenca == None:
					diferenca = abs(vetor[i] - vetor[j])
					num1 = vetor[i]
					num2 = vetor[j]
				elif abs(vetor[i] - vetor[j]) < diferenca:
					diferenca = abs(vetor[i] - vetor[j])
					num1 = vetor[i]
					num2 = vetor [j]
	
	if not diferenca:
		print("\nNão há dois números distintos nesse vetor para que possa ser medida a diferença entre eles!")
	else:
		print(f"\nOs dois números distintos com a menor diferença entre si nesse vetor, são: '{num1}' e '{num2}'")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
dois_mais_proximos(tam, vetor)