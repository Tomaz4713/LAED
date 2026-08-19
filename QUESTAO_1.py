#QUESTÃO 01

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

def mover_maior_fim(p):
	if p == None or p.prox == None:
		return p

	maior = p.valor
	no_maior = p
	ant_maior = None
	
	ant = p
	atual = p.prox
	
	while atual != None:
		if atual.valor > maior:
			maior = atual.valor
			no_maior = atual
			ant_maior = ant
		ant = atual
		atual = atual.prox

	ultimo = ant

	if no_maior == ultimo:
		return p

	if no_maior == p:
		p = p.prox
	else:
		ant_maior.prox = no_maior.prox

	ultimo.prox = no_maior
	no_maior.prox = None

	return p

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista(tam,lim_i,lim_s)
print("\nLista Original =")
imprimir_lista(p)

p = mover_maior_fim(p)
print("\nLista com o maior elemento no fim =")
imprimir_lista(p)

#LETRA B
#O algoritmo realiza uma única varredura linear pela lista encadeada de tamanho n para encontrar o nó com o maior valor, o seu nó anterior e o último nó da lista, o que consome tempo O(n). Em seguida, o rearranjo dos ponteiros para desconectar o maior nó de sua posição original e anexá-lo ao final da lista é feito em tempo constante O(1). Portanto, o tempo de execução total do algoritmo é linear de O(n).