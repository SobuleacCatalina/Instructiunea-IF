""" 
La ora de matematică Gigel este scos la tablă. Profesoara îi dictează trei numere şi îi cere să verifice dacă cele trei numere pot fi laturile unui triunghi. Ajutaţi-l pe Gigel 
să afle rezultatul. Scrieţi un program care primeşte numerele lui Gigel, care sunt mai mici ca 32000, şi returnează DA sau NU. Observaţie: Trei numere pot fi laturile unui triunghi 
numai dacă fiecare este mai mic ca suma celorlalte două. Exemple: Date de intrare 3 5 7 Date de ieşire Da Date de intrare 2 5 9 Date de ieşire Nu. 
""" 
a=int(input("primului numar")) 
b=int(input("al doilea numar")) 
c=int(input("al treilea numar")) 
if ((a<a+b)and(b<c+a)and(c<a+b)): 
    print("Da") 
else: 
    print("Nu")