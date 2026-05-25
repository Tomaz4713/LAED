#QUESTÃO 01

import random

def criar_vt(tam,lim_i,lim_s):
    vetor = [0] * tam

    for i in range(tam):
        vetor[i] = random.randint(lim_i, lim_s)

    return vetor

def enc_maior_impar(tam,vetor):
  maior = None

  for i in range(tam):
    if vetor[i] % 2 != 0:
      if maior == None:
        maior = vetor[i]
      elif vetor[i] > maior:
        maior = vetor[i]

  if maior == None:
    print("\nNão há números ímpares nesse vetor!")
  else:
    print(f"\nO maior número ímpar nesse vetor é: {maior}")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vt(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
enc_maior_impar(tam,vetor)