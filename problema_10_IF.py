""" 
La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot fi împărţite vor fi primite de curcanul Clapon. Să se spună 
cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, 
iar dupa aceea numărul de boabe de porumb. Exemplu: Date de intrare 100 4050 Date de ieşire: Curcanul mai mult cu 10 boabe. 
""" 
ng=int(input("Numarul de gaini")) 
nb=int(input("Numarul total de boabe")) 
nbg=nb//ng 
nbc=nb-(ng*nbg) 
if nbg>nbc: 
    print("Gaina primeste mai mult cu",nbg-nbc,"boabe") 
elif nbc>nbg: 
    print("Curcanul primeste mai mult cu",nbc-nbg,"boabe") 
else: 
    print("Primesc acelasi numar de boabe")