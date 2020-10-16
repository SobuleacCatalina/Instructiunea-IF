""" 
Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau IMPAR. Exemplu : Date de intrare : 45 3 24 Date de ieşire : 
45 impar 3 impar 24 par. 
""" 
a=int(input("primului numar")) 
b=int(input("al doilea numar")) 
c=int(input("al treilea numar")) 
if ((a%2==0)and(b%2==0)and(c%2==0)): 
    print(a,"PAR") 
    print(b,"PAR") 
    print(c,"PAR") 
elif ((a%2==0)and(b%2==0)and(c%2!=0)): 
    print(a,"PAR") 
    print(b,"PAR") 
    print(c,"IMPAR") 
elif ((a%2==0)and(b%2!=0)and(c%2==0)): 
    print(a,"PAR") 
    print(b,"IMPAR") 
    print(c,"PAR") 
elif ((a%2!=0)and(b%2==0)and(c%2==0)): 
    print(a,"IMPAR") 
    print(b,"PAR") 
    print(c,"PAR") 
elif ((a%2!=0)and(b%2!=0)and(c%2==0)): 
    print(a,"IMPAR") 
    print(b,"IMPAR") 
    print(c,"PAR") 
elif ((a%2!=0)and(b%2==0)and(c%2!=0)): 
    print(a,"IMPAR") 
    print(b,"PAR") 
    print(c,"IMPAR") 
elif ((a%2==0)and(b%2!=0)and(c%2!=0)): 
    print(a,"PAR") 
    print(b,"IMPAR") 
    print(c,"IMPAR")
else: 
    print(a,"IMPAR") 
    print(b,"IMPAR") 
    print(c,"IMPAR")