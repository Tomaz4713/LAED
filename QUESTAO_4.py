#QUESTÃO 04

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

def duplicar_impares(p):
	atual = p

	while atual != None:
		if atual.valor % 2 != 0:
			novo = No(atual.valor)
			novo.prox = atual.prox
			atual.prox = novo
			atual = novo.prox
		else:
			atual = atual.prox

	return p

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista(tam,lim_i,lim_s)
print("\nLista Original =")
imprimir_lista(p)

p = duplicar_impares(p)
print("\nLista com Ímpares Duplicados =")
imprimir_lista(p)

#LETRA B
#O algoritmo faz uma única passagem pela lista encadeada original. Ao encontrar um elemento ímpar, ele aloca um novo nó com o mesmo valor e o insere logo após o elemento atual através de operações de ponteiro que custam O(1). Em seguida, o ponteiro avança para o próximo elemento original. Como cada um dos n nós da lista original é verificado uma só vez, o tempo total de execução é linear de O(n).