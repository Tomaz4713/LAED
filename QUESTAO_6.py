#QUESTÃO 06

#LETRA A
class NoEsparso:
	def __init__(self, valor, pos):
		self.valor = valor
		self.pos = pos
		self.prox = None
		self.ant = None

def imprimir_lista_esparsa(p):
	atual = p
	texto = ""
	while atual != None:
		texto += f"[{atual.valor} | {atual.pos}] <-> "
		atual = atual.prox
	texto += "None"
	print(texto)

#a1) Busca por índice
def busca_por_indice(p, k):
	atual = p
	while atual != None:
		if atual.pos == k:
			return atual.valor
		elif atual.pos > k:
			break
		atual = atual.prox
	return 0

#a2) Busca por valor
def busca_por_valor(p, x):
	atual = p
	while atual != None:
		if atual.valor == x:
			return atual.pos
		atual = atual.prox
	return -1

#a3) Atualização
def atualizacao(p, x, k):
	atual = p
	achou = None

	while atual != None:
		if atual.pos == k:
			achou = 1
			break
		elif atual.pos > k:
			break
		atual = atual.prox

	if achou != None:
		if x != 0:
			atual.valor = x
		else:
			if atual.ant != None:
				atual.ant.prox = atual.prox
			else:
				p = atual.prox

			if atual.prox != None:
				atual.prox.ant = atual.ant
	else:
		if x != 0:
			novo = NoEsparso(x, k)
			if p == None:
				p = novo
			elif k < p.pos:
				novo.prox = p
				p.ant = novo
				p = novo
			else:
				aux = p
				while aux.prox != None and aux.prox.pos < k:
					aux = aux.prox

				novo.prox = aux.prox
				novo.ant = aux
				if aux.prox != None:
					aux.prox.ant = novo
				aux.prox = novo

	return p

valores = [4, 5, 10, 1, 9]
posicoes = [3, 7, 9, 12, 17]

p = None
ultimo = None
for i in range(len(valores)):
	novo = NoEsparso(valores[i], posicoes[i])
	if p == None:
		p = novo
		ultimo = novo
	else:
		ultimo.prox = novo
		novo.ant = ultimo
		ultimo = novo

print("\nVetor Esparso Inicial =")
imprimir_lista_esparsa(p)

k_busca = (int(input("\nBuscar índice (k): ")))
val_k = busca_por_indice(p, k_busca)
print(f"Valor no índice {k_busca}: {val_k}")

x_busca = (int(input("\nBuscar valor (x): ")))
pos_x = busca_por_valor(p, x_busca)
print(f"Posição do valor {x_busca}: {pos_x}")

k_up = (int(input("\nAtualizar índice (k): ")))
x_up = (int(input("Novo valor (x): ")))
p = atualizacao(p, x_up, k_up)

print("\nVetor Esparso Atualizado =")
imprimir_lista_esparsa(p)

#LETRA B
#Considerando que a lista contém m elementos não-nulos (onde m <= n):
#1) Busca-por-índice: Percorre no pior caso todos os m nós da lista até encontrar a posição k ou ultrapassá-la, gastando tempo linear O(m).
#2) Busca-por-valor: Realiza uma varredura linear inspecionando o campo de valor de no máximo m nós, consumindo tempo linear O(m).
#3) Atualização: Localiza a posição de inserção, remoção ou modificação em tempo O(m) e ajusta os ponteiros em tempo constante O(1), resultando em tempo de execução total de O(m).