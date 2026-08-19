#QUESTÃO 02

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

def separar_pares_impares(p):
	p1 = None
	fim1 = None
	p2 = None
	fim2 = None

	atual = p
	while atual != None:
		prox_no = atual.prox
		atual.prox = None

		if atual.valor % 2 != 0:
			if p1 == None:
				p1 = atual
				fim1 = atual
			else:
				fim1.prox = atual
				fim1 = atual
		else:
			if p2 == None:
				p2 = atual
				fim2 = atual
			else:
				fim2.prox = atual
				fim2 = atual

		atual = prox_no

	return p1, p2

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista(tam,lim_i,lim_s)
print("\nLista Original (p) =")
imprimir_lista(p)

p1, p2 = separar_pares_impares(p)
print("\nLista Ímpares (p1) =")
imprimir_lista(p1)
print("\nLista Pares (p2) =")
imprimir_lista(p2)

#LETRA B
#O algoritmo percorre cada um dos n nós da lista encadeada original uma única vez. A verificação da paridade e o ajuste dos ponteiros para anexar o nó ao final da lista de ímpares (p1) ou da lista de pares (p2) são executados em tempo constante O(1) para cada elemento, utilizando referências para o final de cada sublista. Portanto, o tempo de execução total é linear de O(n).