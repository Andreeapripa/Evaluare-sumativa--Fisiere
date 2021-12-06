with open('desktop/INPUT.txt', 'r') as f:
    lista1= f.readlines()
print('Nr. Numele Prenumele Nota1 Nota2 Nota3\n', *lista1)
with open ('desktop/REZERVA.txt', 'w') as f:
    for i in lista1:
        f.write(i)
for i in lista1:
    lista2=i.split()
    x=lista2[0]+' '+lista2[1]+' '+lista2[2]
    media=str(float(lista2[3])+float(lista2[4])+float(lista2[5]))
    y=x+' '+media+'\n'
with open('desktop/OUTPUT.txt', 'a') as f:
    f.write(y)
with open ('desktop/OUTPUT.txt', 'r') as f:
    lista3=f.readlines()
print('Nr. Numele Prenumele media\n' , *lista3)
