"""
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!

"""
numbers__ = [1,2,3,4,56,7,88,99,22,111]
def paros_e(numbers):
    for num in numbers:
        if num % 2 ==0:
            x = True
            break
        else: 
            x = False
    return x        

fugg_megold = paros_e(numbers__)
if fugg_megold == False:
    print('Nincs páros')
else: 
    print("van páros")