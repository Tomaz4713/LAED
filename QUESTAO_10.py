#QUESTÃO 10

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

def intersec_listas(p1, p2):
	p3 = None
	fim3 = None

	atual1 = p1
	while atual1 != None:
		achou = None
		atual2 = p2
		
		while atual2 != None:
			if atual1.valor == atual2.valor:
				achou = 1
				break
			atual2 = atual2.prox

		if achou != None:
			repetido = None
			atual3 = p3
			
			while atual3 != None:
				if atual3.valor == atual1.valor:
					repetido = 1
					break
				atual3 = atual3.prox

			if repetido == None:
				novo = No(atual1.valor)
				if p3 == None:
					p3 = novo
					fim3 = novo
				else:
					fim3.prox = novo
					fim3 = novo

		atual1 = atual1.prox

	return p3

tam_u = (int(input("Tamanho da lista p1: ")))
tam_v = (int(input("Tamanho da lista p2: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p1 = criar_lista(tam_u,lim_i,lim_s)
p2 = criar_lista(tam_v,lim_i,lim_s)

print("\nLista p1 =")
imprimir_lista(p1)
print("\nLista p2 =")
imprimir_lista(p2)

p3 = intersec_listas(p1, p2)
print("\nLista Interseção (p) =")
imprimir_lista(p3)

#LETRA B
#Para cada um dos n elementos da primeira lista (p1), o algoritmo varre a segunda lista (p2) de tamanho m para checar se o elemento está presente, consumindo O(m) comparações por nó. Em seguida, para os elementos encontrados, é feita uma checagem na lista resultante p3 para evitar inserções duplicadas, gastando no máximo O(min(n, m)). Dessa forma, o tempo de execução total do algoritmo é dominado pelo cruzamento das duas listas, resultando em O(n * m).