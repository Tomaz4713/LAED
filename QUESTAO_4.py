#QUESTÃO 04

#LETRA A
import random

class No:
	def __init__(self, valor):
		self.valor = valor
		self.prox = None
		self.ant = None

def criar_lista_dupla(tam,lim_i,lim_s):
	if tam == 0:
		return None

	primeiro = No(random.randint(lim_i,lim_s))
	atual = primeiro

	for i in range(tam - 1):
		novo = No(random.randint(lim_i,lim_s))
		atual.prox = novo
		novo.ant = atual
		atual = novo

	return primeiro

def imprimir_lista_dupla(p):
	atual = p
	texto = ""
	while atual != None:
		texto += f"{atual.valor} <-> "
		atual = atual.prox
	texto += "None"
	print(texto)

def particionar_dupla(p, k):
	if p == None:
		return p

	q = p
	r = p
	while r.prox != None:
		r = r.prox

	while q != None and r != None and q != r and q.ant != r:
		while q != None and q != r and q.ant != r and q.valor <= k:
			q = q.prox

		while r != None and q != r and q.ant != r and r.valor > k:
			r = r.ant

		if q != None and r != None and q != r and q.ant != r:
			aux = q.valor
			q.valor = r.valor
			r.valor = aux
			q = q.prox
			r = r.ant

	return p

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))
k = (int(input("Valor do pivô (k): ")))

p = criar_lista_dupla(tam,lim_i,lim_s)
print("\nLista Original =")
imprimir_lista_dupla(p)

p = particionar_dupla(p, k)
print(f"\nLista Particionada em torno de k={k} =")
imprimir_lista_dupla(p)

#LETRA B
#O algoritmo inicialmente percorre a lista para posicionar o ponteiro r no último elemento em tempo O(n). Durante o particionamento, os ponteiros q (avançando para a direita) e r (recuando para a esquerda) se movimentam em direções opostas em direção ao centro da lista, inspecionando cada um dos n nós no máximo uma vez. Cada troca de elementos é realizada em tempo O(1). Portanto, o tempo total de execução do algoritmo é linear de O(n).