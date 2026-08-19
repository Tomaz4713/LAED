#QUESTÃO 05

#LETRA A
class No:
	def __init__(self, valor):
		self.valor = valor
		self.prox = None

def push(topo, valor):
	novo = No(valor)
	novo.prox = topo
	return novo

def pop(topo):
	if topo == None:
		return None, None
	removido = topo.valor
	topo = topo.prox
	return topo, removido

def verificar_delimitadores(expressao):
	topo = None
	
	for i in range(len(expressao)):
		c = expressao[i]
		
		if c == '(' or c == '[' or c == '{':
			topo = push(topo, c)
		elif c == ')' or c == ']' or c == '}':
			if topo == None:
				return False, i + 1, f"Fechador '{c}' sem abridor correspondente"
			
			topo, abridor = pop(topo)
			
			if c == ')' and abridor != '(':
				return False, i + 1, f"Fechador ')' incompatível com abridor '{abridor}'"
			elif c == ']' and abridor != '[':
				return False, i + 1, f"Fechador ']' incompatível com abridor '{abridor}'"
			elif c == '}' and abridor != '{':
				return False, i + 1, f"Fechador '}}' incompatível com abridor '{abridor}'"

	if topo != None:
		return False, len(expressao), "Existem delimitadores que não foram fechados"

	return True, None, "Expressão válida"

expressao = input("Digite a expressão com delimitadores: ")
valido, pos, msg = verificar_delimitadores(expressao)

if valido:
	print(f"\nResultado: Válida! ({msg})")
else:
	print(f"\nResultado: Inválida! Na posição {pos}: {msg}")

#LETRA B
#Tempo: O algoritmo percorre a cadeia de comprimento n caractere por caractere realizando em cada iteração operações de empilhamento ou desempilhamento que custam O(1). Portanto, a complexidade total de tempo é linear de O(n).
#Espaço: No pior cenário (quando a cadeia é formada exclusivamente por delimitadores de abertura), todos os n caracteres são armazenados na pilha encadeada, resultando em uma complexidade de espaço de O(n).

#LETRA C
#1. ({[]})
#   - Empilha '(', '{', '['.
#   - ']' desempilha e casa com '['; '}' desempilha e casa com '{'; ')' desempilha e casa com '('.
#   - Pilha finaliza vazia.
#   - Resultado: VÁLIDA.
#
#2. ({[)}]
#   - Empilha '(', '{', '['.
#   - Na posição 4, encontra-se o fechador ')' enquanto o topo da pilha possui o abridor '['.
#   - Resultado: INVÁLIDA (Posição 4: Fechador ')' incompatível com o abridor '[' do topo).
#
#3. ({[]}[()]{})
#   - O primeiro bloco ({[]}) fecha corretamente deixando a pilha vazia.
#   - O segundo bloco [()] fecha corretamente deixando a pilha vazia.
#   - O terceiro bloco {} fecha corretamente deixando a pilha vazia.
#   - Resultado: VÁLIDA.