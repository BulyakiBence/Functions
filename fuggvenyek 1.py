"""
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!
"""

numbers = [1,2,3,4,5,6,7,8,22,88, 1.22, 1.78]
def osszegzo(numbers):
    osszeg = 0
    for num in numbers:
        if not isinstance(num, float):
            osszeg += num
    return osszeg
print(osszegzo(numbers))
