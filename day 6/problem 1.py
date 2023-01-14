file = open("data.txt", "r")
data = file.readline()
d = list(data)

prev = []
count = 3

for i in range(3):
    prev.append(d[0])
    d.pop(0)

for l in d:
    count += 1
    prev.append(d[0])
    prev_tup = tuple(prev)
    ordered = sorted(prev_tup)
    duplicate = False
    for i in range(3):
        if ordered[i] == ordered[i+1]:
            duplicate = True
    
    if duplicate == False:
        break
    else:
        prev.pop(0)
    d.pop(0)
print(count)
print(prev)
    
