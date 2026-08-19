#QUESTÃO 03

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

def inverter_lista(p):
	ant = None
	atual = p

	while atual != None:
		prox_no = atual.prox
		atual.prox = ant
		ant = atual
		atual = prox_no

	return ant

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista(tam,lim_i,lim_s)
print("\nLista Original =")
imprimir_lista(p)

p = inverter_lista(p)
print("\nLista Invertida =")
imprimir_lista(p)

#LETRA B
#O algoritmo realiza a inversão in-place utilizando três ponteiros auxiliares para redirecionar o encadeamento de cada nó para o seu nó antecessor. Como cada um dos n nós da lista é visitado exatamente uma vez e a manipulação de ponteiros em cada iteração leva tempo O(1), o tempo total de execução do algoritmo é linear de O(n), com custo adicional de memória O(1).