#QUESTÃO 02

import random

def criar_vet(tam,lim_i,lim_s):
  vetor = [0] * tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i,lim_s)

  return vetor

def enc_seg_maior_impar(tam,vetor):
  maior = None
  seg_maior = None

  for i in range(tam):
    if vetor[i] % 2 != 0:
      if maior == None:
        maior = vetor[i]

      elif vetor[i] > maior:
        seg_maior = maior
        maior = vetor[i]

      elif vetor[i] != maior:
        if seg_maior == None:
          seg_maior = vetor[i]
        elif vetor[i] > seg_maior:
          seg_maior = vetor[i]

  if maior==None:
    print("\nNão há nenhum número ímpar nesse vetor!")

  elif seg_maior == None:
    print(f"\nMaior número ímpar nesse vetor: {maior}")
    print("\nNão há segundo maior número ímpar nesse vetor.")

  else:
    print(f"\nMaior número ímpar nesse vetor: {maior}")
    print(f"\nSegundo maior número ímpar nesse vetor: {seg_maior}")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
enc_seg_maior_impar(tam,vetor)