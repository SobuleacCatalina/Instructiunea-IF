""" 
Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În ce clasa va fi repartizat (A, B, C, D sau E)?. 
Exemplu : date de intrare : x=73 date de ieşire : C 
""" 
x=int(input("Radu e pe locul")) 
if x//25==0: 
    print("A") 
elif x//25==1: 
    print("B") 
elif x//25==2: 
    print("C") 
elif x//25==3: 
    print("D") 
else: 
    print("E")