#QUESTÃO 03

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

def trocar_nos(p, q, r):
	ant_q = q.ant
	prox_r = r.prox

	if ant_q != None:
		ant_q.prox = r
	else:
		p = r

	r.ant = ant_q
	r.prox = q
	q.ant = r
	q.prox = prox_r

	if prox_r != None:
		prox_r.ant = q

	return p

def varredura(p):
	q = p
	while q != None and q.prox != None:
		if q.valor > q.prox.valor:
			p = trocar_nos(p, q, q.prox)
		else:
			q = q.prox
	return p

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista_dupla(tam,lim_i,lim_s)
print("\nLista Original =")
imprimir_lista_dupla(p)

p = varredura(p)
print("\nLista após uma varredura =")
imprimir_lista_dupla(p)

#LETRA B
#A operação de varredura percorre a lista da esquerda para a direita uma única vez, realizando n - 1 comparações entre elementos adjacentes. Quando uma inversão é detectada, a função de troca rearranja exclusivamente os ponteiros dos nós envolvidos em tempo constante O(1). Logo, uma passada completa de varredura possui tempo de execução linear de O(n). (Se a varredura for repetida sucessivamente n vezes até a ordenação completa de todos os elementos, o tempo total resultante será quadrático de O(n^2)).