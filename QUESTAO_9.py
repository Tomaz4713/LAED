#QUESTÃO 09

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

def ordenar_lista_dupla(p):
	if p == None:
		return None

	i = p
	while i != None:
		j = i.prox
		while j != None:
			if i.valor > j.valor:
				aux = i.valor
				i.valor = j.valor
				j.valor = aux
			j = j.prox
		i = i.prox
	return p

def imprimir_lista_dupla(p):
	atual = p
	texto = ""
	while atual != None:
		texto += f"{atual.valor} <-> "
		atual = atual.prox
	texto += "None"
	print(texto)

def transformar_em_lista_de_listas(p, k):
	n = 0
	atual = p
	while atual != None:
		n += 1
		atual = atual.prox

	if n == 0 or k <= 0:
		return []

	L = [None] * k
	tam_base = n // k
	resto = n % k

	atual = p
	for i in range(k):
		if atual == None:
			break

		L[i] = atual
		tam_sub = tam_base
		if i < resto:
			tam_sub += 1

		for cont in range(tam_sub - 1):
			if atual != None:
				atual = atual.prox

		if atual != None:
			prox_sub = atual.prox
			atual.prox = None
			if prox_sub != None:
				prox_sub.ant = None
			atual = prox_sub

	return L

tam = (int(input("Tamanho da lista (n): ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))
k = (int(input("Quantidade de sublistas (k): ")))

p = criar_lista_dupla(tam,lim_i,lim_s)
p = ordenar_lista_dupla(p)
print("\nLista Duplamente Encadeada Ordenada =")
imprimir_lista_dupla(p)

L = transformar_em_lista_de_listas(p, k)
print("\nLista de Listas (L) =")
for i in range(len(L)):
	print(f"L[{i}] -> ", end="")
	imprimir_lista_dupla(L[i])

#LETRA B
#O algoritmo realiza duas etapas lineares: primeiro, percorre os n elementos da lista original para calcular o tamanho total n, consumindo tempo O(n). Em seguida, percorre novamente os nós dividindo-os em k blocos de tamanho aproximado n/k e desconectando os ponteiros entre as sublistas em tempo O(1) por quebra. Dessa forma, como cada nó é visitado um número constante de vezes, o tempo de execução total é linear de O(n).