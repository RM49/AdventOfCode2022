datafile = open("data.txt", "r")
data = datafile.readlines()
total = 0
for l in data:
    d = l.strip("\n")
    d = d.strip(" ")
    e = d.split(",")
    e[0] = e[0].split("-")
    e[1] = e[1].split("-")
    
    for l in e:
        count = 0
        for n in l:
            l[count] = int(n)
            count += 1
    # create a set for each range
    list1 = []
    list2 = []
    for i in range(e[0][0], e[0][1]+1, 1):
        list1.append(i)
    for i in range(e[1][0], e[1][1]+1, 1):
        list2.append(i)

    set1 = set(list1)
    set2 = set(list2)

    intersect = set1.intersection(set2) # returns the overlap of the two sets
    if intersect: # not empty set returns true
        total += 1

print(total)

