""" 
“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă iubeşte …. Exemplu: Date de intrare: x=10 Date de ieşire: …
de loc. 
""" 
x=int(input("Numarul de petale")) 
if x%5==1: 
    print("ma iubeste un pic") 
elif x%5==2: 
    print("ma iubeste mult")
elif x%5==3: 
    print("ma iubeste cu pasiune") 
elif x%5==4: 
    print("ma iubeste la nebunie") 
else:
    print("ma iubeste de loc") 