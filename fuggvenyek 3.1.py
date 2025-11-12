"""
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!

"""
numbers = [1,2,3,4,5,6,77,88,99,100,1780,200]
def harommal_oszthatok(numbers):
    db = 0
    for num in numbers:
        if num % 3 == 0:
            db += 1
            
    return db
megold = harommal_oszthatok(numbers)
print(megold)