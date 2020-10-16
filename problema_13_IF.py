""" 
La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul 
pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire : rosie. 
""" 
x=int(input("Locul ocupat de Ionel")) 
if x>100: 
    print("Nu primeste tricou") 
elif x%4==1: 
    print("alba") 
elif x%4==2: 
    print("rosie") 
elif x%4==3: 
    print("albastra") 
else: 
    print("neagra")