#QUESTÃO 09

#LETRA A
import random

class No:
	def __init__(self, valor):
		self.valor = valor
		self.prox = None

def criar_lista(tam,lim_i,lim_s):
	if tam == 0:
		return None

	primeiro = No(random.randint(lim_i,lim_s))
	atual = primeiro
	
	for i in range(tam - 1):
		atual.prox = No(random.randint(lim_i,lim_s))
		atual = atual.prox

	return primeiro

def imprimir_lista(p):
	atual = p
	texto = ""
	while atual != None:
		texto += f"{atual.valor} -> "
		atual = atual.prox
	texto += "None"
	print(texto)

def enc_repetido(p):
	achou = None
	
	atual = p
	while atual != None:
		verif = atual.prox
		
		while verif != None:
			if atual.valor == verif.valor:
				achou = 1
				break
			verif = verif.prox

		if achou != None:
			break
			
		atual = atual.prox

	if achou != None:
		print("\nSim")
	else:
		print("\nNão")

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista(tam,lim_i,lim_s)
print("\nLista =")
imprimir_lista(p)

enc_repetido(p)

#LETRA B
#No melhor caso, os dois primeiros elementos da lista são iguais, o que encerra a busca imediatamente na primeira iteração consumindo tempo constante O(1). No pior caso, não há elementos repetidos na lista (ou a duplicata está nas últimas posições), exigindo que cada elemento seja comparado com todos os elementos seguintes. Isso gera uma soma de comparações da ordem de (n * (n - 1)) / 2, resultando em um tempo de execução de pior caso quadrático de O(n^2).