#QUESTÃO 02

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

def atualizar_elemento(p, x, y):
	atual = p
	achou = None

	while atual != None:
		if atual.valor == x:
			achou = 1
			break
		atual = atual.prox

	if achou == None:
		print(f"\nO elemento '{x}' não foi encontrado na lista!")
		return p

	atual.valor = y

	if atual.ant != None:
		atual.ant.prox = atual.prox
	else:
		p = atual.prox

	if atual.prox != None:
		atual.prox.ant = atual.ant

	atual.ant = None
	atual.prox = None

	if p == None:
		return atual

	if y <= p.valor:
		atual.prox = p
		p.ant = atual
		p = atual
		return p

	aux = p
	while aux.prox != None and aux.prox.valor < y:
		aux = aux.prox

	atual.prox = aux.prox
	atual.ant = aux
	if aux.prox != None:
		aux.prox.ant = atual
	aux.prox = atual

	return p

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista_dupla(tam,lim_i,lim_s)
p = ordenar_lista_dupla(p)
print("\nLista Ordenada =")
imprimir_lista_dupla(p)

x = (int(input("Elemento a ser modificado (x): ")))
y = (int(input("Novo valor (y): ")))

p = atualizar_elemento(p, x, y)
print("\nLista após atualização =")
imprimir_lista_dupla(p)

#LETRA B
#O algoritmo executa três etapas sequenciais: primeiro, realiza a busca linear para localizar o nó de valor x na lista de tamanho n, consumindo tempo O(n). Em seguida, desconecta o nó de sua posição original alterando ponteiros em tempo O(1). Por fim, percorre a lista ordenada para encontrar a nova posição correta de inserção do valor y em tempo O(n), reconectando os ponteiros em tempo constante O(1). Dessa forma, o tempo de execução total da operação de atualização é linear de O(n).