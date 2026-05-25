#QUESTÃO 04

import random

def criar_vet(tam,lim_i,lim_s):
  vetor = [0] * tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i,lim_s)

  return vetor

def impar_impar(tam,vetor):
  quant = []
  num = []

  for i in range(tam):
    igual = None
    if vetor[i] % 2 != 0:   #É ÍMPAR?

      for j in range(len(num)):   #É IGUAL A QUALQUER ELEMENTO DE "num"?
        if vetor[i] == num[j]:
          igual = 1
          break

      if igual == None:
        temp = vetor[i]
        aparece = 0

        for i in range(tam):    #QUANTAS VEZES APARECE?
          if vetor[i] == temp:
            aparece += 1

        if aparece % 2 != 0:    #É ÍMPAR E APARECE ÍMPAR VEZES, ANOTA OS VALORES EM DOIS VETORES
          num.append(temp)
          quant.append(aparece)

  if not num:
    print("\nNão há números ímpares que se repitam uma quantidade ímpar de vezes nesse vetor!")
  else:
    print("\nOs números ímpares que se repetem uma quantidade ímpar de vezes nesse vetor, são:")
    for i in range(len(num)):
      print(f"\n'{num[i]}' que se repete {quant[i]} vezes!")

tam = (int(input("Tamanho do vetor: ")))
lim_i = (int(input("Randomizar de:")))
lim_s = (int(input("Até:")))

vetor = criar_vet(tam,lim_i,lim_s)
print(f"\nVetor = {vetor}")
impar_impar(tam,vetor)