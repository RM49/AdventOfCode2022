file = open("data.txt", "r")
data = file.readline()
d = list(data)

prev = []
count = 13
print(len(d))
for i in range(13):
    prev.append(d[0])
    d.pop(0)


while True: # for some reason "for l in d" would stop at 2054, eventhough len d is 4095. while true solved this. However for l in d still iterates 4095 in other test????
    count += 1
    prev.append(d[0])
    prev_tup = tuple(prev)
    ordered = sorted(prev_tup)
    duplicate = False
    for i in range(13):
        if ordered[i] == ordered[i+1]:
            duplicate = True
    if duplicate == False:
        break
    else:
        prev.pop(0)
        d.pop(0)
print(prev)
print(count)
# this works, issues prompted for using for l in d when popping values of d throughout the loop
##for l in d: # for some reason "for l in d" would stop at 2054, eventhough len d is 4095. while true solved this. However for l in d still iterates 4095 in other test????
##    count += 1
##    prev.append(l)
##    prev_tup = tuple(prev)
##    ordered = sorted(prev_tup)
##    duplicate = False
##    for i in range(13):
##        if ordered[i] == ordered[i+1]:
##            duplicate = True
##    if duplicate == False:
##        break
##    else:
##        prev.pop(0)
##        
