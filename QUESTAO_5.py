#QUESTÃO 05

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

def ordenar_lista(p):
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

def imprimir_lista(p):
	atual = p
	texto = ""
	while atual != None:
		texto += f"{atual.valor} -> "
		atual = atual.prox
	texto += "None"
	print(texto)

def intercalar_listas(p1, p2):
	if p1 == None:
		return p2
	if p2 == None:
		return p1

	cabeca = None
	fim = None

	while p1 != None and p2 != None:
		if p1.valor <= p2.valor:
			escolhido = p1
			p1 = p1.prox
		else:
			escolhido = p2
			p2 = p2.prox

		escolhido.prox = None

		if cabeca == None:
			cabeca = escolhido
			fim = escolhido
		else:
			fim.prox = escolhido
			fim = escolhido

	if p1 != None:
		fim.prox = p1
	elif p2 != None:
		fim.prox = p2

	return cabeca

tam_u = (int(input("Tamanho da lista p1: ")))
tam_v = (int(input("Tamanho da lista p2: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p1 = criar_lista(tam_u,lim_i,lim_s)
p2 = criar_lista(tam_v,lim_i,lim_s)

p1 = ordenar_lista(p1)
p2 = ordenar_lista(p2)

print("\nLista p1 Ordenada =")
imprimir_lista(p1)
print("\nLista p2 Ordenada =")
imprimir_lista(p2)

p = intercalar_listas(p1, p2)
print("\nLista Unificada e Ordenada (p) =")
imprimir_lista(p)

#LETRA B
#O algoritmo compara iterativamente os nós da frente das listas p1 e p2, que possuem tamanhos n e m respectivamente. Em cada comparação, o menor elemento é desconectado e ligado ao final da nova lista ordenada em tempo O(1). Ao esgotar uma das listas, o restante da outra é conectado diretamente também em tempo O(1). Como cada nó é processado uma única vez, o tempo total de execução é de O(n + m).