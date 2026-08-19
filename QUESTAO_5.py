#QUESTÃO 05

#LETRA A
import random

class NoEsparso:
	def __init__(self, valor, pos):
		self.valor = valor
		self.pos = pos
		self.prox = None
		self.ant = None

def criar_vet(tam,lim_i,lim_s):
	vetor = [0] * tam
	for i in range(tam):
		if random.randint(1, 10) <= 3:
			vetor[i] = random.randint(lim_i,lim_s)
	return vetor

def imprimir_lista_esparsa(p):
	atual = p
	texto = ""
	while atual != None:
		texto += f"[{atual.valor} | {atual.pos}] <-> "
		atual = atual.prox
	texto += "None"
	print(texto)

def criar_vetor_esparso(tam, vetor):
	cabeca = None
	ultimo = None

	for i in range(tam):
		if vetor[i] != 0:
			novo = NoEsparso(vetor[i], i + 1)
			
			if cabeca == None:
				cabeca = novo
				ultimo = novo
			else:
				ultimo.prox = novo
				novo.ant = ultimo
				ultimo = novo

	return cabeca

tam = (int(input("Tamanho do vetor esparso (n): ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor V = {vetor}")

p = criar_vetor_esparso(tam, vetor)
print("\nLista Duplamente Encadeada (Vetor Esparso) =")
imprimir_lista_esparsa(p)

#LETRA B
#O algoritmo percorre uma única vez as n posições do vetor original V. A cada elemento diferente de zero identificado, um novo nó armazenando o valor e o seu respectivo índice é alocado e conectado ao final da lista duplamente encadeada com manipulação de ponteiros em tempo constante O(1). Como o laço executa exatamente n vezes, o tempo de execução total é linear de O(n).