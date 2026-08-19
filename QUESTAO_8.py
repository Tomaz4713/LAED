#QUESTÃO 08

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

def enc_mais_frequente(p):
	if p == None:
		print("\nA lista está vazia!")
		return

	mais_repetido = None
	max_ocorrencias = 0

	atual = p
	while atual != None:
		cont = 0
		aux = p
		
		while aux != None:
			if aux.valor == atual.valor:
				cont += 1
			aux = aux.prox

		if cont > max_ocorrencias:
			max_ocorrencias = cont
			mais_repetido = atual.valor

		atual = atual.prox

	print(f"\n{mais_repetido} é o elemento que aparece mais vezes, com {max_ocorrencias} ocorrências")

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista(tam,lim_i,lim_s)
print("\nLista =")
imprimir_lista(p)

enc_mais_frequente(p)

#LETRA B
#O algoritmo utiliza uma estrutura de dois laços encadeados sobre a lista encadeada. O laço externo percorre cada um dos n nós da lista e, para cada nó, o laço interno percorre novamente todos os n elementos da lista para contar a quantidade total de ocorrências do valor atual. Com isso, são realizadas n * n iterações no total, resultando em um tempo de execução quadrático de O(n^2).