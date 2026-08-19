#QUESTÃO 07

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

def remover_todas_copias(p, k):
	while p != None and p.valor == k:
		p = p.prox

	if p == None:
		return None

	atual = p
	while atual.prox != None:
		if atual.prox.valor == k:
			atual.prox = atual.prox.prox
		else:
			atual = atual.prox

	return p

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))
k = (int(input("Elemento a ser removido (k): ")))

p = criar_lista(tam,lim_i,lim_s)
print("\nLista Original =")
imprimir_lista(p)

p = remover_todas_copias(p, k)
print(f"\nLista após remover todas as cópias de '{k}' =")
imprimir_lista(p)

#LETRA B
#O algoritmo faz um tratamento inicial na cabeça da lista para ignorar valores iguais a k e, em seguida, percorre o restante da lista com um único laço de repetição. A cada nó com valor igual a k identificado, a exclusão é feita ajustando o ponteiro do nó anterior diretamente para o nó seguinte em tempo O(1). Como todos os n nós são inspecionados uma única vez, o tempo total de execução é linear de O(n).