# done after a while without trees
file = open("data.txt", "r")
data = file.readlines()

# all directories in a list. Index 1 of each list is the name of the directory, each list is a directory.
system = ["/"]

data.pop(0) # get rid of cd /
d = []
for l in data:
    d.append(l.strip("\n").split(" "))
    
# d is the list of commands / data

path = [] # route of where the stuff being handled is. Each will point to a directory in each sub list.

for l in d:

    # pointing to current directory list
    current = system
    for n in path:
        current = current[n]


    if l[0] == "$":
        if l[1] == "ls":
            continue
        if l[1] == "cd":
            if l[2] == "..":
                if path != []:
                    path.pop()
            else: # cd </a>, finds which index the directory is at then adds to path
                for directories in current:
                    if type(directories) == list:
                        if directories[0] == l[2]:
                            path.append(current.index(directories))
    elif l[0] == "dir":
        current.append([l[1]])
    else:
        current.append([int(l[0]), l[1]])
totals = []
def count(directory):
    total = 0
    for d in directory:     
        if type(d[0]) == int:
            total += d[0]
        elif type(d[0]) == str and d[0] != "/":
            print(d)
            d.pop(0) # stops infinite loop on directory name
            temp = count(d)
            print(temp)
            total += temp
            totals.append(temp)
    return total

print(system) 
print(count(system))
total_under_100k = 0
for n in totals:
    if n < 100000:
        total_under_100k += n
print(total_under_100k)

