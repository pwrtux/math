from math import sqrt

def cantor(x, y):
    return int((x + y) * (x + y +1)/2 + y)


def cantinv(index: int):
    first = int((sqrt(8 * index + 1) - 1) / 2)
    second = int((first ** 2 + first) / 2)
    index2 = index - second
    index1 = first - index2
    return [index1, index2]


print(cantor(1,2))
print(cantor(3,4))
print(cantor(5,2))
print(cantinv(8))
print(cantinv(32))
print(cantinv(30))