""" 
Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. Exemple : Date de intrare 23 45 Date de ieşire nu exista numar par ; Date de intrare 28 14 Date
de ieşire 28 ; Date de intrare 77 4 Date de ieşire 4. 
""" 
a=int(input("primului numar")) 
b=int(input("al doilea numar")) 
if((a%2==0)and(b%2==0)): 
    if a>b: 
        print(a) 
    else: 
        print(b) 
elif ((a%2==0)and(b%2!=0)): 
    print(a) 
elif((a%2!=0)and(b%2==0)): 
    print(b) 
else: 
    print("Nici unul dintre numere nu e par")