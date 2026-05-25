#QUESTÃO 03

import random

def criar_vet(tam,lim_i,lim_s):
  vetor = [0] * tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i,lim_s)

  return vetor

def enc_k_aprox(tam,vetor,k):
  presente = None
  posicao = None
  posicao1 = None
  proximo = None
  outro_proximo = None

  for i in range(tam):
    temp = k - vetor[i]

    if temp == 0:   #ACHEI "k"
      presente = 1
      posicao = i + 1
      break

    elif proximo == None:   #COMO NÃO ACHEI "k", ESSE É O MAIS PRÓXIMO TEMPORARIAMENTE
      proximo = vetor[i]
      posicao = i + 1

    elif temp < (k - proximo) and proximo < k or temp > (k - proximo) and proximo > k:    #ESSE É MAIS PRÓXIMO DE "k" DO QUE O ANTERIOR?
      proximo = vetor[i]
      posicao = i + 1

  if presente == None:    #"k" NÃO ESTANDO PRESENTE, VAMOS CONFERIR SE HÁ UM SEGUNDO NÚMERO MAIS PRÓXIMO DE "k"
    for i in range(tam):
      temp = k - vetor[i]

      if temp * -1 == k - proximo:
        outro_proximo = vetor[i]
        posicao1 = i + 1

  if presente != None:
    print(f"\nO número '{k}' está presente nesse vetor na {posicao}º posição!")

  elif outro_proximo == None:
    print(f"\nFoi mal chefia, seu número '{k}' não está presente em nenhuma posição do vetor, porém, o mais próximo de '{k}' é o '{proximo}' que está na {posicao}º posição!")

  else:
    print(f"\nFoi mal chefia, seu número '{k}' não está presente em nenhuma posição do vetor, porém, achei outros dois números igualmente próximos de '{k}', são eles:\n\nO número '{proximo}' que está na {posicao}º posição!\n\nE o número '{outro_proximo}' que está na {posicao1}º posição!")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))
k = (int(input("Número a se encontrar: ")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
enc_k_aprox(tam,vetor,k)