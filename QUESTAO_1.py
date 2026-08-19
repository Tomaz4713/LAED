#QUESTÃO 01

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

def enc_elemento_central(p):
	if p == None:
		print("\nA lista está vazia!")
		return

	lento = p
	rapido = p

	while rapido.prox != None and rapido.prox.prox != None:
		lento = lento.prox
		rapido = rapido.prox.prox

	print(f"\nO elemento central da lista é: {lento.valor}")

tam = (int(input("Tamanho da lista: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

p = criar_lista_dupla(tam,lim_i,lim_s)
print("\nLista =")
imprimir_lista_dupla(p)

enc_elemento_central(p)

#LETRA B
#O algoritmo utiliza a técnica de dois ponteiros que avançam em velocidades diferentes: o ponteiro lento anda uma posição por vez, enquanto o ponteiro rápido anda duas posições por vez. Quando o ponteiro rápido atinge o final da lista, o ponteiro lento estará posicionado exatamente no elemento central (ou no último elemento da primeira metade caso o tamanho seja par). Como a lista de tamanho n é percorrida em n/2 iterações, o tempo de execução total é linear de O(n), gastando apenas O(1) de memória adicional.