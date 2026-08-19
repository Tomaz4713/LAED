#QUESTÃO 06

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

def particionar_lista(p, k):
	menor_ini = None
	menor_fim = None
	maior_ini = None
	maior_fim = None

	atual = p
	while atual != None:
		prox_no = atual.prox
		atual.prox = None

		if atual.valor <= k:
			if menor_ini == None:
				menor_ini = atual
				menor_fim = atual
			else:
				menor_fim.prox = atual
				menor_fim = atual
		else:
			if maior_ini == None:
				maior_ini = atual
				maior_fim = atual
			else:
				maior_fim.prox = atual
				maior_fim = atual

		atual = prox_no

	if menor_ini == None:
		return maior_ini

	menor_fim.prox = maior_ini
	return menor_ini

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))
k = (int(input("Valor do pivô (k): ")))

p = criar_lista(tam,lim_i,lim_s)
print("\nLista Original =")
imprimir_lista(p)

p = particionar_lista(p, k)
print(f"\nLista Particionada em torno de k={k} =")
imprimir_lista(p)

#LETRA B
#O algoritmo realiza uma única varredura pela lista encadeada original contendo n elementos. Cada nó é avaliado e encadeado ao final da sublista de elementos menores ou iguais a k ou da sublista de elementos maiores que k em tempo O(1). Ao final, a junção das duas sublistas ocorre em tempo constante O(1) ligando o fim da primeira ao início da segunda. Portanto, o tempo total de execução é linear de O(n).