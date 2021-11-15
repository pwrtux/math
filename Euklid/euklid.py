import itertools as it


def euklid(a,b):
    counter = it.count()
    while b != 0 and True:
        a,b = b, a % b # % = a mod b
    return a
    print(next(counter))

#print(euklid(121,83))


y = 12
z = 4
sumXy = z + y

division = y / z
intDivision = y // z
remainder = y % z 

print("Berechnung: " + (str(sumXy)))
print("Berechnung: " + (str(division)))
print("Berechnung: " + (str(intDivision)))
print("Berechnung: " + (str(remainder)))
