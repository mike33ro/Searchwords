# Returns words that are present in a dictionary from letters submitted by user
# Works only for romanian words

import re


dictionar = open('lista-ro.txt')
dictionar_r = dictionar.read()

while True :

    Nr_litere=int(input('Number of letters (max 10) : '))
    if Nr_litere > 10:
        print ('Too many words ! Take another shot !')
    else :
        print(' Number of letters is : {} '.format( Nr_litere))
        break

# print (Nr_litere)
#introduceti litere
Litere =[]
for nr in range(Nr_litere):
    litera = input('Letter : {}'.format(nr+1))
    #trebuie verificat ca este litera !!!!
    Litere.append(litera)
    print (Litere)
#print (Litere)
r=len(Litere)
print(r)
#faceti combinatii de fiecare litera
l=0
n=0
lista_cuvinte=[]
def permute(dictionar_r,Litere,lista_cuvinte, l, r):
    a=Litere[:]

    if l==r:
        cuv_cautat=''.join(a)
        lungine=len(cuv_cautat)
        # linii=dictionar.read()
        # print(re.match('acasa',dictionar))

        if re.search('\s'+cuv_cautat+'\s', dictionar_r):
            print(cuv_cautat)
            lista_cuvinte.append(cuv_cautat)



    else:
        for i in range(l,r):
            a[l], a[i] = a[i], a[l]
            permute(dictionar_r,a,lista_cuvinte, l+1, r)
            a[l], a[i] = a[i], a[l]
    return lista_cuvinte
permute(dictionar_r,Litere,lista_cuvinte,l,r)
print (lista_cuvinte)
