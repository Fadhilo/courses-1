from decimal import *

getcontext().prec = 4

file = input("Path: ")

with open(file) as f:
    content = f.read()

content_list = content.split('\n')

content_list.pop()

D={}

for i in range(len(content_list)):
    if content_list[i][0] == '#':
        continue
    D[content_list[i].split('=')[0]]=content_list[i].split('=')[1]

safwen=Decimal(0)
fadhel=Decimal(0)
total_commun=Decimal(0)

for key in D:
    if key[0] == 'S':
        safwen = safwen + Decimal(D[key])
    else :
        if key[0] == 'F':
            fadhel = fadhel + Decimal(D[key])
        else:
            if key[0] == 'C':
                total_commun = total_commun + Decimal(D[key])
            else:
                print("Frais est attribué à un inconnu.")
                print("Vérifie la première lettre de la ligne contenant: ", D[key])

print("safwen: %.2f" % safwen)
print("fadhel: %.2f" % fadhel)
print("commun: %.2f" % total_commun)
print("total: %.2f" % (safwen + fadhel + total_commun))
print("total safwen: %.2f" % (safwen + total_commun/Decimal(2)))
print("total fadhel: %.2f" % (fadhel + total_commun/Decimal(2)))