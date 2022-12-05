data = open("data.txt", "r")
total = 0

for l in data:
    x = l.strip("\n")
    x = list(x)
    x.pop(1)

    # lose
    if x[1] == "X":
        if x[0] == "A":
            total += 3
        if x[0] == "B":
            total += 1
        if x[0] == "C":
            total += 2

    # draw
    if x[1] == "Y":
        if x[0] == "A":
            total += 4
        if x[0] == "B":
            total += 5
        if x[0] == "C":
            total += 6

    # win
    if x[1] == "Z":
        if x[0] == "A":
            total += 8
        if x[0] == "B":
            total += 9
        if x[0] == "C":
            total += 7
print(total)
        
