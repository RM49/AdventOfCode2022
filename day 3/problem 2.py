# intersection code inspired by geekforgeeks
import string
import time
def intersect(l, l2, l3):
    return set(l).intersection(set(l2), set(l3))

data = open("data.txt", "r")

datas = []

intersects = []

for l in data:
    x = l.strip("\n")
    x = list(x)
    datas.append(x)

while datas != []:
    l = intersect(datas[0], datas[1], datas[2])
    p = list(l)
    intersects.append(p[0])
    datas.pop(0)
    datas.pop(0) # datas[1] becomes 0!
    datas.pop(0)

# list of lowercase and uppercase
a = list(string.ascii_lowercase)
b = list(string.ascii_uppercase)
c = a + b
total = 0

for x in intersects:
    total += c.index(x)+1

print(total)
