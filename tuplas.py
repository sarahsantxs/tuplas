
import random
lista = []

for i in range (1,51) :
    tam = input ("Digite o Tamanho: ")
    while tam != 'p' and tam != 'P' and tam != 'g' and tam != 'G' and tam != 'm' and tam != 'M' : print ("Valor inválido, não corresponde a um tamnho.")
    cor = int (input ("Digite a cor escolhida (1-Branco, 2-Preto , 3-Azul): "))
    while cor != 1 and cor  !=2 and  cor !=3 : print ("Valor inválido, não corresponde a uma cor.")
    lista.append((tam,cor))

    if cor ==1 : tupla = (tam, "Branco")
    elif cor ==2 : tupla = (tam, "Preto")
    else: tupla = (tam, "Azul")

    lista.append (tupla)

contp=0
contm=0
contg=0

for i in lista :
    if i[0]=='p' or i[0] =='P' : contp = contp + 1
    elif i[0]=='m' or i[0] =='M' : contm = contm + 1
    else: contg = contg + 1

maior=0
if contg > maior : maior = contg
elif maior < contp : maior = contp
else: maior = contm
