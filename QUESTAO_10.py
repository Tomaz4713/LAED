#QUESTÃO 10

#LETRA A
class No:
	def __init__(self, valor):
		self.valor = valor
		self.prox = None
		self.ant = None

def imprimir_lista_dupla(p):
	atual = p
	texto = ""
	while atual != None:
		texto += f"{atual.valor} <-> "
		atual = atual.prox
	texto += "None"
	print(texto)

#Busca(L, x)
def busca(L, x):
	if not L:
		return None

	sub_escolhida = None
	for i in range(len(L)):
		if L[i] != None and L[i].valor <= x:
			sub_escolhida = i
		elif L[i] != None and L[i].valor > x:
			break

	if sub_escolhida == None:
		sub_escolhida = 0

	atual = L[sub_escolhida]
	while atual != None:
		if atual.valor == x:
			return sub_escolhida, atual
		elif atual.valor > x:
			break
		atual = atual.prox

	return None

#Inserção(L, x)
def insercao(L, x):
	novo = No(x)
	if not L:
		return

	idx = 0
	for i in range(len(L)):
		if L[i] != None and L[i].valor <= x:
			idx = i
		elif L[i] != None and L[i].valor > x:
			break

	p = L[idx]
	if p == None:
		L[idx] = novo
		return

	if x < p.valor:
		novo.prox = p
		p.ant = novo
		L[idx] = novo
		return

	atual = p
	while atual.prox != None and atual.prox.valor < x:
		atual = atual.prox

	novo.prox = atual.prox
	novo.ant = atual
	if atual.prox != None:
		atual.prox.ant = novo
	atual.prox = novo

#Remoção(L, x)
def remocao(L, x):
	res = busca(L, x)
	if res == None:
		print(f"\nO elemento '{x}' não foi encontrado para remoção!")
		return

	idx, no_alvo = res

	if no_alvo.ant != None:
		no_alvo.ant.prox = no_alvo.prox
	else:
		L[idx] = no_alvo.prox

	if no_alvo.prox != None:
		no_alvo.prox.ant = no_alvo.ant

	print(f"\nO elemento '{x}' foi removido da sublista L[{idx}] com sucesso!")

#Criando a Lista de Listas do exemplo
sub1 = No(2)
sub1.prox = No(9); sub1.prox.ant = sub1

sub2 = No(15)
sub2.prox = No(19); sub2.prox.ant = sub2

sub3 = No(31)
sub3.prox = No(49); sub3.prox.ant = sub3

L = [sub1, sub2, sub3]

print("\nLista de Listas (L) Inicial =")
for i in range(len(L)):
	print(f"L[{i}] -> ", end="")
	imprimir_lista_dupla(L[i])

x_busca = (int(input("\nValor para buscar (x): ")))
resultado = busca(L, x_busca)
if resultado != None:
	print(f"\nElemento '{x_busca}' encontrado na sublista L[{resultado[0]}]!")
else:
	print(f"\nElemento '{x_busca}' não encontrado na lista de listas!")

x_ins = (int(input("\nValor para inserir (x): ")))
insercao(L, x_ins)

print("\nLista de Listas após inserção =")
for i in range(len(L)):
	print(f"L[{i}] -> ", end="")
	imprimir_lista_dupla(L[i])

x_rem = (int(input("\nValor para remover (x): ")))
remocao(L, x_rem)

print("\nLista de Listas após remoção =")
for i in range(len(L)):
	print(f"L[{i}] -> ", end="")
	imprimir_lista_dupla(L[i])

#LETRA B
#Considerando um conjunto de n elementos particionado em k sublistas balanceadas de tamanho aproximado n/k:
#1) Busca(L, x): Identifica a sublista candidata no vetor de ponteiros L em tempo O(k) e percorre a sublista selecionada em tempo O(n/k), totalizando tempo de execução de O(k + n/k).
#2) Inserção(L, x): Localiza a sublista apropriada em tempo O(k) e insere o nó na ordem correta dentro da sublista em tempo O(n/k), totalizando tempo de execução de O(k + n/k).
#3) Remoção(L, x): Realiza a busca em tempo O(k + n/k) e atualiza os ponteiros do nó em tempo O(1), totalizando tempo de execução de O(k + n/k).
#Ao dimensionar o número de sublistas como k = sqrt(n), o tempo de execução de todas as três operações atinge a complexidade assintótica ótima de O(sqrt(n)).